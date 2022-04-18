# PrimeNet_nouns

## Brief intro of current code
Build hierachical PrimeNet from full ConceptNet tuples. One example of ConceptNet tuple is (necklace, IsA, jewelrey).

For current version, only when 

1. the relation of the tuple == "IsA"
 
2. the first item != the third item

3. the first and the third item of the tuple are both single noun word
 
do we count it in PrimeNet.

Created hierachical PrimeNet (a dictionary) is saved in ./Data/PrimeNet_full_ConceptNet.json

## Statistics
Number of keys in PrimeNet: 9534

Number of included ConceptNet tuples: 57936

Average number of values for each key in PrimeNet: 5.72

## Examples of current PrimeNet
PrimeNet['food'] = ['abgoosht', 'affogato', 'afikoman', 'agnolotti', 'ajika', 'ajvar', 'akutaq', 'amok', 'andouille', 'anellini', 'animals', 'antidoron', 'antipasto', 'babka', 'baguette', 'bakso', 'bamiyeh', 'banchan', 'banku', 'bavette', 'bbq', 'beignet', 'berliner', 'beverage', 'bhajji', 'bigoli', 'bigos', 'biryani', 'biscotti', 'biscuit', 'blueberries', 'bobotie', 'bockwurst', 'borani', 'borscht', 'bosintang', 'bosna', 'botargo', 'bouillabaisse', 'boule', 'bratwurst', 'braunschweiger', 'bread', 'brioche', 'brunost', 'bruschetta', 'bucatini', 'buldak', 'burger', 'burrito', 'butter', 'cajun', 'cake', 'candy', 'cannoli', 'capellini', 'capirotada', 'carbonara', 'carpaccio', 'carrots', 'cassoulet', 'castella', 'cavatelli', 'cendol', 'cepelinai', 'cereal', 'chaat', 'cheese', 'chips', 'chistorra', 'churro', 'chutney', 'chyme', 'cobbler', 'coconut', 'comfit', 'commissariat', 'conchiglie', 'cookie', 'cornbread', 'cracker', 'cretons', 'crispbread', 'croissant', 'croquembouche', 'croquette', 'crêpe', 'curry', 'currywurst', 'dacquoise', 'damper', 'dango', 'dashi', 'daube', 'debrecener', 'dessert', 'dhokla', 'dolma', 'dosa', 'doughnut', 'douhua', 'dushbara', 'eggs', 'empanada', 'enchilada', 'fajita', 'falafel', 'fare', 'farfalle', 'feed', 'feijoada', 'financier', 'fish', 'flatbread', 'foodstuff', 'freekeh', 'fregula', 'frikadeller', 'fritter', 'frumenty', 'fufu', 'fusilli', 'fårikål', 'gochujang', 'gougère', 'goulash', 'granita', 'gravlax', 'grit', 'gruel', 'guacamole', 'gugelhupf', 'haggis', 'halva', 'ham', 'hamburger', 'hasenpfeffer', 'hoe', 'honey', 'hummus', 'jalebi', 'japchae', 'jeon', 'jiaozi', 'kalakukko', 'kanafeh', 'kaymak', 'kebab', 'kefir', 'ketchup', 'khachapuri', 'kheer', 'khinkali', 'kho', 'kissel', 'koeksister', 'kokoretsi', 'kroppkaka', 'krupuk', 'kulcha', 'kumis', 'laksa', 'lamington', 'lasagne', 'lassi', 'leblebi', 'leftovers', 'lekvar', 'liptauer', 'liquorice', 'loaf', 'lobster', 'macaron', 'madeleine', 'mafaldine', 'magiritsa', 'malabar', 'malidzano', 'mandu', 'manna', 'manti', 'margarine', 'mars', 'meat', 'meringue', 'meze', 'micronutrient', 'migas', 'minestrone', 'mititei', 'mofongo', 'momo', 'mooncake', 'moussaka', 'mozartkugel', 'muffuletta', 'musakhan', 'nachos', 'naengmyeon', 'nikujaga', 'nonpareils', 'noodle', 'nutella', 'nutriment', 'oden', 'okonomiyaki', 'okroshka', 'oliebol', 'omelette', 'orange', 'orecchiette', 'pabulum', 'paella', 'pajeon', 'pancake', 'pancetta', 'panettone', 'pannekoek', 'papadum', 'pappardelle', 'paratha', 'parfait', 'parmigiana', 'paska', 'pasta', 'pastiera', 'pastilla', 'pastry', 'pasty', 'pears', 'pepernoot', 'pierogi', 'pilaf', 'pirog', 'pistou', 'pizza', 'poffertjes', 'polenta', 'porridge', 'potoato', 'poutine', 'pozole', 'pringles', 'prinzregententorte', 'produce', 'products', 'pumpernickel', 'pupusa', 'pâté', 'quiche', 'ragout', 'ratatouille', 'religieuse', 'risotto', 'rojak', 'romesco', 'rotelle', 'rösti', 'sachertorte', 'salad', 'salsa', 'sambar', 'samosa', 'sandwich', 'sandwitch', 'satay', 'sauerbraten', 'sausage', 'scone', 'seafood', 'sfogliatella', 'shashlik', 'shchi', 'shortbread', 'sikhye', 'simit', 'sinseollo', 'sisig', 'skilandis', 'slatko', 'slug', 'soba', 'sobrassada', 'solyanka', 'sopaipilla', 'soufflé', 'soup', 'soupd', 'sourdough', 'spam', 'speculoos', 'sprinkles', 'ssamjang', 'stoemp', 'stollen', 'streuselkuchen', 'stroopwafel', 'sukiyaki', 'sundae', 'supplì', 'taco', 'tahini', 'taiyaki', 'tajine', 'takoyaki', 'tamagoyaki', 'tangyuan', 'tapas', 'tapenade', 'tarator', 'thukpa', 'timbits', 'toffee', 'tortelloni', 'trenette', 'trifle', 'tteok', 'tulumba', 'turkey', 'turrón', 'twinkie', 'tzatziki', 'udon', 'uttapam', 'varenye', 'vatrushka', 'vegetable', 'vegetables', 'vetkoek', 'vinaigrette', 'vla', 'water', 'waterzooi', 'wonton', 'xiaolongbao', 'yassa', 'yogurt', 'yolk', 'youtiao', 'zabaione', 'zakuski', 'zeppole', 'zongzi', 'zrazy', 'éclair']

PrimeNet['beverage'] = ['absinthe', 'alcohol', 'aquafina', 'arak', 'ararat', 'ayahuasca', 'beer', 'borjomi', 'burn', 'campari', 'chartreuse', 'cider', 'cocoa', 'coffee', 'cognac', 'cointreau', 'cooler', 'corona', 'crush', 'curaçao', 'eggnog', 'fanta', 'fizz', 'frappuccino', 'glenfiddich', 'hydromel', 'juice', 'jägermeister', 'lemonade', 'mate', 'milk', 'milkshake', 'mirinda', 'mixer', 'oenomel', 'orangina', 'ovaltine', 'pinolillo', 'potion', 'refresher', 'skol', 'smirnoff', 'smoothie', 'soda', 'tea', 'water', 'zamzam', 'zima']

PrimeNet['coffee'] = ['americano', 'breve', 'cappuccino', 'espresso', 'latte', 'mocha', 'starbucks']

PrimeNet['bread'] = ['bap', 'barmbrack', 'biscuit', 'breadstick', 'bun', 'challah', 'ciabatta', 'crouton', 'flatbread', 'host', 'matzo', 'roll', 'shortbread', 'simnel', 'toast', 'wafer']

PrimeNet['dessert'] = ['ambrosia', 'banana', 'blancmange', 'cake', 'charlotte', 'chocolate', 'compote', 'cookie', 'custard', 'flan', 'junket', 'mould', 'mousse', 'pastry', 'pavlova', 'sorbet', 'syllabub', 'whip', 'zabaglione']

PrimeNet['meat'] = ['beef', 'bird', 'carbonado', 'crabmeat', 'cut', 'eel', 'escargot', 'fillet', 'fish', 'game', 'halal', 'hamburgers', 'horsemeat', 'jerky', 'mouton', 'muscle', 'mutton', 'pork', 'poultry', 'rodent', 'sausage', 'seafood', 'snail']

PrimeNet['pasta'] = ['cannelloni', 'fedelline', 'fettuccine', 'fettucini', 'gnocchi', 'lasagna', 'linguine', 'manicotti', 'mostaccioli', 'noodle', 'orzo', 'penne', 'ravioli', 'rice', 'rigatoni', 'spagetti', 'spaghetti', 'spaghettini', 'tagliatelle', 'tortellini', 'vermicelli', 'ziti']

## To run the code 
Step 1: Download full ConceptNet data (https://s3.amazonaws.com/conceptnet/downloads/2019/edges/conceptnet-assertions-5.7.0.csv.gz) to ./Data/ConceptNet/ and unzip it as csv file.

Step 2: python main.py or sbatch main
