import os, copy, sys, csv, string
import nltk
import json

# FUNCTION
#   Load dataset from dataset_path;
# INPUT
#   dataset_path: a string for dataset dir
# OUTPUT
#   dataset: [(e1, rel, e2, label), ...]
def load_conceptnet_only_keep_IsA_relation_single_file(dataset_path=None):
    cnt_rel_isA = 0
    with open(dataset_path, encoding='utf_8') as f:
        f = f.read().splitlines()
        dataset = []
        for id_line, line in enumerate(f):
            rel, e1, e2, label = line.split("\t")
            # filter data instances whose label is not positive
            if label == "0":
                continue
            rel = rel.strip()
            # lower case and without punctuation
            e1 = e1.strip().lower().translate(str.maketrans('','',string.punctuation))
            e2 = e2.strip().lower().translate(str.maketrans('','',string.punctuation))
            # only keep data whose rel is "IsA"
            if rel != 'IsA':
                continue
            dataset.append((e1, rel, e2, label))
            cnt_rel_isA += 1
        # print some samples
        print("load_conceptnet_pure, dataset[-3:]: ", dataset[-3:])
    print("cnt_rel_isA: ", cnt_rel_isA)
    return dataset


# FUNCTION
#   load dataset from dataset_root_path;
#   When there're many data files in dataset_root_path, load them seperately and concat them all
# INPUT
#   dataset_root_path: a string for dataset root dir
#   Each file in dataset_root_path should be a ConceptNet dataset file
# OUTPUT
#   dataset_collection: [(e1, rel, e2, label), ...]
def load_conceptnet_only_keep_IsA_relation(dataset_root_path):
    data_files = os.listdir(dataset_root_path)
    data_files_full_path = [os.path.join(dataset_root_path, f) for f in data_files]

    dataset_collection = []
    for cur_data_full_path in data_files_full_path:
        assert cur_data_full_path.endswith('txt')
        dataset = load_conceptnet_only_keep_IsA_relation_single_file(cur_data_full_path)
        dataset_collection += dataset

    print("len(dataset_collection): ", len(dataset_collection))
    return dataset_collection


# FUNCTION
#   load full conceptnet from dataset_root_path, and only keep tuples with IsA relation;
# INPUT
#   dataset_root_path: a string for dataset root dir, where file conceptnet-assertions-5.7.0.csv is in
# OUTPUT
#   dataset_collection: [(e1, rel, e2, label), ...]
def load_full_conceptnet_only_keep_IsA_relation(dataset_root_path):
    all_relations = []
    dataset_collection = []
    print("Loading from conceptnet-assertions-5.7.0.csv...")
    with open(os.path.join(dataset_root_path, 'conceptnet-assertions-5.7.0.csv'), 'r') as f:
        csvFile = csv.reader(f)
        for id, lines in enumerate(csvFile):
            rel = lines[0]
            # Add rel to all_relations if it hasn't; and break control (since data in csvFile are sorted in terms of their relation, we break 'for' loop when it completes loading 'IsA' tuples)
            if rel not in all_relations:
                if len(all_relations) > 0:
                    if 'IsA' in all_relations[-1]:
                        break
                # print(rel)
                all_relations.append(rel)
            # Only keep lines with 'IsA' relation and with other conditions
            if 'IsA' in rel:
                # condition 0: the relation is 'IsA'
                rel_no_noise = rel.replace('/a/[/r/', '').strip().split('/')[0]
                assert rel_no_noise == 'IsA'
                # condition 1: e1 and e2 are written in English
                e1 = lines[1]
                e2 = lines[2]
                if e1.startswith('/c/en/') and e2.startswith('/c/en/'):
                    # lower case and without punctuation
                    e1 = e1.replace('/c/en', '').split('/')[1].replace('_', ' ').lower().translate(str.maketrans('','',string.punctuation))
                    e2 = e2.replace('/c/en', '').split('/')[1].replace('_', ' ').lower().translate(str.maketrans('','',string.punctuation))
                    if '/' in e1 or '/' in e2:
                        print("e1: {}; e2: {}".format(lines[1], lines[2]))
                        raise Exception
                    dataset_collection.append((e1, rel_no_noise, e2, None))
    print("Loaded 'IsA' tuples from conceptnet-assertions-5.7.0.csv.")
    return dataset_collection




# FUNCTION
#   get values of the cur_node and values that correspond to all sub-nodes of cur_node
# INPUT
#   PrimeNet: PrimeNet
#   cur_node: a key in PrimeNet
#   remained_depth: max depth for the recursion (it seems there's circle in PrimeNet so there's unlimited depth for this recursion; hence we use remained_depth to avoid this problem)
#   root_node: the root node that begins get_all_values_in_and_below_this_node
#   max_remained_depth: the remained_depth that begins get_all_values_in_and_below_this_node
# OUTPUT
#   all_values_in_and_below_this_node: a list of string entities
def get_all_values_in_and_below_this_node(PrimeNet, cur_node, remained_depth, root_node, max_remained_depth):
    assert cur_node in PrimeNet

    # to avoid loop count
    if (cur_node in PrimeNet[root_node] or cur_node == root_node) and remained_depth != max_remained_depth:
        return [cur_node]

    ## all_values_in_this_node: a list
    all_values_in_this_node = PrimeNet[cur_node]

    # check if this is the end node
    if_end_node = True
    for concept in all_values_in_this_node:
        if concept in PrimeNet:
            if_end_node = False
    if remained_depth == 0:
        if_end_node = True
    if if_end_node:
        return all_values_in_this_node
    else:
        remained_depth -= 1
        all_values_below_this_node_prev = [get_all_values_in_and_below_this_node(PrimeNet, sub_node, remained_depth, root_node, max_remained_depth) for sub_node in PrimeNet[cur_node] if sub_node in PrimeNet]
        all_values_below_this_node = []
        for value_list in all_values_below_this_node_prev:
            all_values_below_this_node += value_list
        return all_values_below_this_node + all_values_in_this_node


# FUNCTION
#   Build PrimeNet from dataset
#   Only when e1 and e2 are (both single word but not phrase) and (both noun) and (not equal) do we count it in PrimeNet
# INPUT
#   dataset: [(e1, rel, e2, label), ...]
#   max_recursion_depth: max depth for recursion during building hierachical PrimeNet (it seems there's circle in PrimeNet so there's unlimited depth for this recursion; hence we use max_recursion_depth to avoid this problem)
# OUTPUT
#   PrimeNet: {}
def build_primenet(dataset, max_recursion_depth):
    print("\nlen(dataset): ", len(dataset))

    # sys.setrecursionlimit(10000)
    # print("sys.getrecursionlimit(): ", sys.getrecursionlimit())
    ## for nltk PoS tagging
    nltk.download('averaged_perceptron_tagger')

    ### Build PrimeNet (not hierachical)
    PrimeNet = {}
    cnt_used_conceptnet_instance = 0
    print("\nBuilding raw (non-hierachical) PrimeNet...")
    for (e1, rel, e2, label) in dataset:
        assert rel == "IsA"
        # e1 and e2 should both be single word but not phrase
        if len(e1.split()) > 1 or len(e2.split()) > 1:
            # print("e1: {}, e2: {}".format(e1, e2))
            continue
        # e1 should not equal to e2 (if so, it's hard to build a hierachical PrimeNet)
        if e1 == e2:
            continue
        # check if e1 and e2 are both NOUN
        posTag_e1 = nltk.pos_tag([e1])
        posTag_e2 = nltk.pos_tag([e2])
        # only keep data when e1 and e2 are both NOUN
        if not ((posTag_e1[0][1] == 'NN' or posTag_e1[0][1] == 'NNS' or posTag_e1[0][1] == 'NNPS' or posTag_e1[0][1] == 'NNP') and (posTag_e2[0][1] == 'NN' or posTag_e2[0][1] == 'NNS' or posTag_e2[0][1] == 'NNPS' or posTag_e2[0][1] == 'NNP')):
            # print("posTag_e1: {}, posTag_e2: {}".format(posTag_e1, posTag_e2))
            continue
        # build PrimeNet
        if e2 not in PrimeNet:
            PrimeNet[e2] = [e1]
            cnt_used_conceptnet_instance += 1
        elif e1 not in PrimeNet[e2]:
            PrimeNet[e2].append(e1)
            cnt_used_conceptnet_instance += 1

    # statistics
    print("Statistics for NOT hierachical PrimeNet:")
    print("cnt_used_conceptnet_instance: ", cnt_used_conceptnet_instance)
    print("len(PrimeNet): ", len(PrimeNet))
    len_collection_for_each_key = [len(PrimeNet[key]) for key in PrimeNet]
    print('average length of collection for each key in PrimeNet: ', sum(len_collection_for_each_key)/len(len_collection_for_each_key))


    ### Build hierachical PrimeNet
    #   remove the concept from PrimeNet[key] if concept in PrimeNet[subkey] and subkey in PrimeNet[key] (here depth is 1, and we can set max_recursion_depth for this depth) (here subkey != this concept)
    print("\nBuilding hierachical PrimeNet...")
    # dict_noter: dict_noter[concept_as_key] = all_values_in_and_below_this_node; to recuce repetitive computations
    dict_noter = {}
    for key in PrimeNet:
        concept_list = PrimeNet[key]
        ## Get temp_dict_key_removedConcept and temp_dict_key_num_removedConcept
        # temp_dict_key_removedConcept: note which concept_as_key can remove which concept_as_value
        temp_dict_key_removedConcept = {}
        #  temp_dict_key_num_removedConcept: note which concept_as_key can remove how many concept_as_value
        temp_dict_key_num_removedConcept = {}
        for concept_as_key in concept_list:
            temp_dict_key_removedConcept[concept_as_key] = []
            temp_dict_key_num_removedConcept[concept_as_key] = 0
            if concept_as_key in PrimeNet:
                # to be more hierachical, we remove certain repetitive concepts
                if concept_as_key not in dict_noter:
                    all_values_in_and_below_this_node = get_all_values_in_and_below_this_node(PrimeNet, concept_as_key, remained_depth=max_recursion_depth, root_node=concept_as_key, max_remained_depth=max_recursion_depth)
                    dict_noter[concept_as_key] = all_values_in_and_below_this_node
                else:
                    all_values_in_and_below_this_node = dict_noter[concept_as_key]
                for concept_as_value in concept_list:
                    # (subkey != this concept)
                    if concept_as_value != concept_as_key:
                        if concept_as_value in all_values_in_and_below_this_node:
                            if concept_as_value not in temp_dict_key_removedConcept[concept_as_key]:
                                temp_dict_key_removedConcept[concept_as_key].append(concept_as_value)
                                temp_dict_key_num_removedConcept[concept_as_key] += 1
        ## Use temp_dict_key_removedConcept and temp_dict_key_num_removedConcept to decide why concept in hierachical_concept_list to remove
        # use a greedy method that each time select a concept with most temp_removed_concepts, util all concepts are covered.
        covered_keys = []
        hierachical_concept_list = []
        most_influential_key = sorted(temp_dict_key_num_removedConcept, key=temp_dict_key_num_removedConcept.__getitem__, reverse=True)
        # add influential keys to hierachical_concept_list
        for id_influ_key, influ_key in enumerate(most_influential_key):
            # many temp_dict_key_removedConcept[influ_key] is [], and we do not want to add influ_key in this circumstance
            if len(temp_dict_key_removedConcept[influ_key]) > 0 and influ_key not in covered_keys:
                covered_keys += temp_dict_key_removedConcept[influ_key]
                covered_keys += [influ_key]
                covered_keys = list(set(covered_keys))
                hierachical_concept_list.append(influ_key)
            assert len(covered_keys) <= len(concept_list)
            if len(covered_keys) == len(concept_list):
                break
        if not len(covered_keys) == len(concept_list):
            # add non-influential keys to hierachical_concept_list
            for id_tmp_key, tmp_key in enumerate(concept_list):
                if tmp_key not in covered_keys:
                    hierachical_concept_list.append(tmp_key)
                    covered_keys.append(tmp_key)
                if len(covered_keys) == len(concept_list):
                    break
        assert len(covered_keys) == len(concept_list)
        PrimeNet[key] = sorted(list(set(hierachical_concept_list)))

    # statistics
    print("Statistics for hierachical PrimeNet:")
    print("cnt_used_conceptnet_instance: ", cnt_used_conceptnet_instance)
    print("len(PrimeNet): ", len(PrimeNet))
    len_collection_for_each_key = [len(PrimeNet[key]) for key in PrimeNet]
    print('average length of collection for each key in PrimeNet: ', sum(len_collection_for_each_key)/len(len_collection_for_each_key))
    return PrimeNet
