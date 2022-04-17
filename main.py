import json
from utils import load_conceptnet_only_keep_IsA_relation, load_full_conceptnet_only_keep_IsA_relation, build_primenet




def main():
    ## hyper-parameters
    max_recursion_depth = 5
    # if_full_conceptnet: when False, use the 100k tuples version of conceptnet
    if_full_conceptnet = True
    if if_full_conceptnet:
        dataset_dir = "./Data/ConceptNet/"
        # dataset_dir = "/home/v-zonyang/Data/"
        data_save_dir = "./Data/PrimeNet_full_ConceptNet.json"
    else:
        dataset_dir = "./Data/ConceptNet/"
        data_save_dir = "./Data/PrimeNet.json"

    ## load dataset
    # dataset: [(e1, rel, e2, label), ...]
    if if_full_conceptnet:
        dataset = load_full_conceptnet_only_keep_IsA_relation(dataset_dir)
    else:
        dataset = load_conceptnet_only_keep_IsA_relation(dataset_dir)

    ## build PrimeNet
    PrimeNet = build_primenet(dataset, max_recursion_depth)

    ## save PrimeNet
    with open(data_save_dir, 'w') as f:
        json.dump(PrimeNet, f)





if __name__ == "__main__":
    main()
