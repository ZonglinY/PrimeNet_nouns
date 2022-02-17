import json
from utils import load_conceptnet_only_keep_IsA_relation, build_primenet




def main():
    ## hyper-parameters
    dataset_dir = "./Data/ConceptNet/"
    data_save_dir = "./Data/PrimeNet.json"

    ## load dataset
    # dataset: [(e1, rel, e2, label), ...]
    dataset = load_conceptnet_only_keep_IsA_relation(dataset_dir)

    ## build PrimeNet
    PrimeNet = build_primenet(dataset)

    ## save PrimeNet
    with open(data_save_dir, 'w') as f:
        json.dump(PrimeNet, f)





if __name__ == "__main__":
    main()
