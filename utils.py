import os
import nltk

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
            e1 = e1.strip()
            e2 = e2.strip()
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
#   Build PrimeNet from dataset
#   Only when e1 and e2 are (both single word but not phrase) and (both noun) do we count it in PrimeNet
# INPUT
#   dataset: [(e1, rel, e2, label), ...]
# OUTPUT
#   PrimeNet: {}
def build_primenet(dataset):
    print("len(dataset): ", len(dataset))
    ## for nltk PoS tagging
    nltk.download('averaged_perceptron_tagger')

    PrimeNet = {}
    cnt_used_conceptnet_instance = 0
    for (e1, rel, e2, label) in dataset:
        assert rel == "IsA"
        # e1 and e2 should both be single word but not phrase
        if len(e1.split()) > 1 or len(e2.split()) > 1:
            # print("e1: {}, e2: {}".format(e1, e2))
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
    print("cnt_used_conceptnet_instance: ", cnt_used_conceptnet_instance)
    print("len(PrimeNet): ", len(PrimeNet))
    print('average length of collection for each key in PrimeNet: ', cnt_used_conceptnet_instance/len(PrimeNet))

    return PrimeNet
