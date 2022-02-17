# PrimeNet_nouns

## Brief intro of current code
Build PrimeNet from 100k ConceptNet tuples. One example of ConceptNet tuple is (necklace, IsA, jewelrey).

For current version, only when 

1. the second item of the tuple == "IsA"
 
2. the first and the third item of the tuple are both single noun word
 
do we count it in PrimeNet.

Created PrimeNet (a dictionary) is saved in ./Data/PrimeNet.json

## Statistics
Number of keys in PrimeNet: 908

Number of included ConceptNet tuples: 3171

Average length of value for each key in PrimeNet: 3.49

## Examples of current PrimeNet
PrimeNet['food'] = ['apple', 'bacon', 'beef', 'biscket', 'cherry', 'chopstick', 'coconut', 'coffee', 'cookie', 'cornbread', 'cracker', 'dessert', 'drink', 'fruit', 'gnocchi', 'ham', 'hotdog', 'lasagna', 'leftover', 'lobster', 'makisushi', 'meat', 'oatmeal', 'pear', 'pepsi', 'pickle', 'pineapple', 'pizza', 'potato', 'salmon', 'sausage', 'snack', 'soupd', 'spaghetti', 'stew', 'tiramisu', 'tomato', 'turkey', 'water', 'bagel', 'bread', 'hamburger', 'steak', 'butter', 'cheese', 'chicken', 'chocolate', 'corn', 'egg', 'rice', 'salad', 'soup', 'sushi', 'vegetable']

PrimeNet['coffee'] = ['brewedcoffee', 'cappuccino', 'cappuchino', 'latte']

PrimeNet['dessert'] = ['cake', 'cupcake', 'sorbet']

PrimeNet['bread'] = ['roll', 'toast', 'bagel']

PrimeNet['cheese'] = ['brie', 'cheddar', 'cheshire', 'emmental', 'gouda', 'lancashire', "pont-l'eveque", 'savoyard', 'stilton', 'tilsit']

PrimeNet['vegetable'] = ['artichoke', 'asparagus', 'beet', 'burdock', 'cabbage', 'carrot', 'cauliflower', 'chicory', 'cress', 'eggplant', 'honey', 'onion', 'radish', 'sweetcorn', 'turnip', 'vegemite', 'watermelon', 'yam', 'zucchini', 'celery', 'spinach', 'bean', 'corn', 'cucumber', 'lettuce', 'pea', 'potato', 'tomato']

## To run the code 
python main.py or sbatch main
