# PrimeNet_nouns

## Brief intro of current code
Build hierachical PrimeNet from 100k ConceptNet tuples. One example of ConceptNet tuple is (necklace, IsA, jewelrey).

For current version, only when 

1. the second item of the tuple == "IsA"
 
2. the first and the third item of the tuple are both single noun word

3. the first item != the third item
 
do we count it in PrimeNet.

Created hierachical PrimeNet (a dictionary) is saved in ./Data/PrimeNet.json

## Statistics
Number of keys in PrimeNet: 905

Number of included ConceptNet tuples: 3161

Average length of value for each key in PrimeNet: 3.09

## Examples of current PrimeNet
PrimeNet['food'] = ['bacon', 'beef', 'biscket', 'chopstick', 'coconut', 'cookie', 'cornbread', 'cracker', 'dessert', 'drink', 'fruit', 'gnocchi', 'hotdog', 'lasagna', 'leftover', 'lobster', 'makisushi', 'meat', 'oatmeal', 'pizza', 'salmon', 'sausage', 'snack', 'soupd', 'spaghetti', 'stew', 'tiramisu', 'turkey', 'bread', 'butter', 'cheese', 'egg', 'rice', 'salad', 'soup', 'sushi', 'vegetable']

PrimeNet['coffee'] = ['brewedcoffee', 'cappuccino', 'cappuchino', 'latte']

PrimeNet['dessert'] = ['cake', 'sorbet']

PrimeNet['bread'] = ['roll', 'toast', 'bagel']

PrimeNet['cheese'] = ['brie', 'cheddar', 'cheshire', 'emmental', 'gouda', 'lancashire', "pont-l'eveque", 'savoyard', 'stilton', 'tilsit']

PrimeNet['vegetable'] = ['artichoke', 'asparagus', 'beet', 'burdock', 'cabbage', 'carrot', 'cauliflower', 'chicory', 'cress', 'eggplant', 'honey', 'onion', 'radish', 'sweetcorn', 'turnip', 'vegemite', 'watermelon', 'yam', 'zucchini', 'celery', 'spinach', 'bean', 'corn', 'cucumber', 'lettuce', 'pea', 'potato', 'tomato']

## To run the code 
python main.py or sbatch main
