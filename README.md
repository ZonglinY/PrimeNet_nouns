# PrimeNet_nouns

## Brief intro of current code
Build PrimeNet from 100k ConceptNet tuple. One example of ConceptNet tuple is (necklace, IsA, jewelrey).

For current version, only when 

1. the second item of the tuple == "IsA"
 
2. the first and the third item of the tuple are both single noun word
 
do we count it in PrimeNet.

Created PrimeNet is saved in ./Data/PrimeNet.json

## Statistics
Number of keys in PrimeNet: 908

Number of included ConceptNet tuples: 3171

Average length of value for each key in PrimeNet: 3.49

## To run the code 
python main.py or sbatch main
