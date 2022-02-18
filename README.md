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

Average number of values for each key in PrimeNet: 3.09

## Examples of current PrimeNet
PrimeNet['food'] = ['bacon', 'beef', 'biscket', 'chopstick', 'coconut', 'cookie', 'cornbread', 'cracker', 'dessert', 'drink', 'fruit', 'gnocchi', 'hotdog', 'lasagna', 'leftover', 'lobster', 'makisushi', 'meat', 'oatmeal', 'pizza', 'salmon', 'sausage', 'snack', 'soupd', 'spaghetti', 'stew', 'tiramisu', 'turkey', 'bread', 'butter', 'cheese', 'egg', 'rice', 'salad', 'soup', 'sushi', 'vegetable']

PrimeNet['drink'] = ['beverage', 'lemonade', 'screwdriver']

PrimeNet['beverage'] = ['beer', 'coffee', 'juice', 'milk', 'soda', 'tea', 'vodca', 'water', 'wine']

PrimeNet['coffee'] = ['brewedcoffee', 'cappuccino', 'cappuchino', 'latte']

PrimeNet['bread'] = ['roll', 'toast', 'bagel']

PrimeNet['dessert'] = ['cake', 'sorbet']

PrimeNet['meat'] = ['ham', 'hamburger', 'lamb', 'muscle', 'pork', 'steak', 'venison', 'chicken']

PrimeNet['pasta'] = ['gnocchi', 'macaroni', 'spaghetti']

## To run the code 
python main.py or sbatch main
