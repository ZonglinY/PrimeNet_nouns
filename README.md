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

Average number of values for each key in PrimeNet: 5.24

## Examples of current PrimeNet
PrimeNet['food'] = ['abgoosht', 'affogato', 'afikoman', 'agnolotti', 'ajika', 'ajvar', 'akutaq', 'amok', 'andouille', 'anellini', 'animals', 'antidoron', 'antipasto', 'arepa', 'babka', 'bagel', 'baguette', 'baklava', 'bakso', 'bamiyeh', 'banana', 'banchan', 'banku', 'bannock', 'bavette', 'bbq', 'beef', 'beignet', 'berliner', 'beverage', 'bhajji', 'bigoli', 'bigos', 'biryani', 'biscotti', 'biscuit', 'bisque', 'blancmange', 'blintz', 'blt', 'blueberries', 'bobotie', 'bockwurst', 'borani', 'borscht', 'bosintang', 'bosna', 'botargo', 'bouillabaisse', 'boule', 'bratwurst', 'braunschweiger', 'bread', 'breadstick', 'brioche', 'brittle', 'brunost', 'bruschetta', 'bucatini', 'buldak', 'burger', 'burrito', 'butter', 'cajun', 'cake', 'candy', 'cannelloni', 'cannoli', 'capellini', 'capirotada', 'caramel', 'carbonara', 'carpaccio', 'carrots', 'cassoulet', 'castella', 'cavatelli', 'cendol', 'cepelinai', 'cereal', 'chaat', 'challah', 'chapati', 'charlotte', 'cheese', 'cheeseburger', 'cheesecake', 'chicken', 'chips', 'chistorra', 'chocolate', 'chorizo', 'churro', 'chutney', 'chyme', 'ciabatta', 'cobbler', 'coconut', 'coleslaw', 'comfit', 'commissariat', 'compote', 'conchiglie', 'congee', 'cookie', 'corn', 'cornbread', 'cracker', 'cretons', 'crispbread', 'croissant', 'croquembouche', 'croquette', 'crêpe', 'cupcake', 'curry', 'currywurst', 'custard', 'dacquoise', 'damper', 'dango', 'dashi', 'daube', 'debrecener', 'dessert', 'dhokla', 'dolma', 'dosa', 'doughnut', 'douhua', 'dushbara', 'egg', 'eggs', 'empanada', 'enchilada', 'fajita', 'falafel', 'fare', 'farfalle', 'feed', 'feijoada', 'fettuccine', 'financier', 'fish', 'flatbread', 'focaccia', 'foodstuff', 'frangipane', 'freekeh', 'fregula', 'frikadeller', 'fritter', 'fruitcake', 'frumenty', 'fudge', 'fufu', 'fusilli', 'fårikål', 'galette', 'gazpacho', 'gingerbread', 'gnocchi', 'gochujang', 'gougère', 'goulash', 'granita', 'gravlax', 'grit', 'gruel', 'guacamole', 'gugelhupf', 'gyro', 'haggis', 'halva', 'ham', 'hamburger', 'hardtack', 'hasenpfeffer', 'hoe', 'honey', 'hummus', 'idli', 'injera', 'jalebi', 'japchae', 'jeon', 'jiaozi', 'johnnycake', 'kalakukko', 'kanafeh', 'kaymak', 'kebab', 'kefir', 'ketchup', 'khachapuri', 'kheer', 'khinkali', 'kho', 'kissel', 'koeksister', 'kokoretsi', 'kroppkaka', 'krupuk', 'kulcha', 'kumis', 'ladyfinger', 'laksa', 'lamington', 'lasagne', 'lassi', 'lavash', 'leblebi', 'lefse', 'leftovers', 'lekvar', 'lettuce', 'linguine', 'liptauer', 'liquorice', 'loaf', 'lobster', 'lollipop', 'macaron', 'macaroni', 'madeleine', 'mafaldine', 'magiritsa', 'malabar', 'malidzano', 'mandu', 'manna', 'manti', 'margarine', 'mars', 'marshmallow', 'marzipan', 'matzo', 'meat', 'meringue', 'meze', 'micronutrient', 'migas', 'milkshake', 'minestrone', 'mititei', 'mofongo', 'momo', 'mooncake', 'moussaka', 'mousse', 'mozartkugel', 'muffin', 'muffuletta', 'musakhan', 'naan', 'nachos', 'naengmyeon', 'nikujaga', 'nonpareils', 'noodle', 'nougat', 'nutella', 'nutriment', 'oden', 'okonomiyaki', 'okroshka', 'oliebol', 'omelette', 'orange', 'orecchiette', 'pabulum', 'paella', 'pajeon', 'pancake', 'pancetta', 'panettone', 'pannekoek', 'papadum', 'pappardelle', 'paratha', 'parfait', 'parmigiana', 'paska', 'pasta', 'pastiera', 'pastilla', 'pastry', 'pasty', 'pears', 'peas', 'pepernoot', 'pepperoni', 'pho', 'pickle', 'pierogi', 'pilaf', 'pirog', 'pistou', 'pita', 'pizza', 'poffertjes', 'polenta', 'porridge', 'potato', 'potatoes', 'potoato', 'poutine', 'pozole', 'praline', 'pretzel', 'pringles', 'prinzregententorte', 'produce', 'products', 'pumpernickel', 'pupusa', 'pâté', 'quesadilla', 'quiche', 'ragout', 'ramen', 'ratatouille', 'ravioli', 'religieuse', 'rigatoni', 'risotto', 'rojak', 'romesco', 'rotelle', 'rösti', 'sachertorte', 'salad', 'salmon', 'salsa', 'sambar', 'samosa', 'sandwich', 'sandwitch', 'satay', 'sauerbraten', 'sausage', 'scone', 'seafood', 'sfogliatella', 'shashlik', 'shchi', 'shortbread', 'sikhye', 'simit', 'sinseollo', 'sisig', 'skilandis', 'slatko', 'slop', 'slug', 'slush', 'soba', 'sobrassada', 'solyanka', 'sopaipilla', 'sorbet', 'soufflé', 'soup', 'soupd', 'sourdough', 'spaghetti', 'spam', 'speculoos', 'sprinkles', 'ssamjang', 'steak', 'stoemp', 'stollen', 'streuselkuchen', 'stroopwafel', 'strudel', 'sukiyaki', 'sundae', 'supplì', 'tabbouleh', 'taco', 'tagliatelle', 'tahini', 'taiyaki', 'tajine', 'takoyaki', 'tamagoyaki', 'tangyuan', 'tapas', 'tapenade', 'tarator', 'teacake', 'thukpa', 'timbits', 'tiramisu', 'toast', 'toffee', 'tomatoes', 'torte', 'tortellini', 'tortelloni', 'tortilla', 'trenette', 'trifle', 'tteok', 'tulumba', 'turkey', 'turrón', 'twinkie', 'tzatziki', 'udon', 'uttapam', 'varenye', 'vatrushka', 'vegetable', 'vegetables', 'vermicelli', 'vetkoek', 'vinaigrette', 'vla', 'waffle', 'water', 'waterzooi', 'wine', 'wonton', 'xiaolongbao', 'yassa', 'yogurt', 'yolk', 'youtiao', 'zabaione', 'zakuski', 'zeppole', 'zongzi', 'zrazy', 'éclair']

PrimeNet['beverage'] = ['absinthe', 'alcohol', 'aquafina', 'arak', 'ararat', 'ayahuasca', 'beer', 'borjomi', 'burn', 'buttermilk', 'campari', 'cappuccino', 'chartreuse', 'cider', 'cocoa', 'coffee', 'cognac', 'cointreau', 'coke', 'cooler', 'corona', 'crush', 'curaçao', 'dasani', 'eggnog', 'fanta', 'fizz', 'frappuccino', 'glenfiddich', 'guinness', 'hydromel', 'juice', 'jägermeister', 'latte', 'lemonade', 'mate', 'milk', 'milkshake', 'mirinda', 'mixer', 'oenomel', 'orangina', 'ovaltine', 'pepsi', 'pinolillo', 'potion', 'pulque', 'refresher', 'skol', 'smirnoff', 'smoothie', 'soda', 'sprite', 'tea', 'water', 'wine', 'zamzam', 'zima']

PrimeNet['coffee'] = ['americano', 'breve', 'cappuccino', 'espresso', 'latte', 'mocha', 'starbucks']

PrimeNet['bread'] = ['bagel', 'bap', 'barmbrack', 'biscuit', 'breadstick', 'bun', 'challah', 'ciabatta', 'cracker', 'crouton', 'flatbread', 'host', 'matzo', 'nan', 'roll', 'shortbread', 'simnel', 'toast', 'wafer', 'zwieback']

PrimeNet['dessert'] = ['ambrosia', 'banana', 'blancmange', 'brownie', 'cake', 'charlotte', 'chocolate', 'compote', 'cookie', 'custard', 'flan', 'junket', 'mould', 'mousse', 'pastry', 'pavlova', 'sorbet', 'syllabub', 'tiramisu', 'whip', 'zabaglione']

PrimeNet['meat'] = ['beef', 'bird', 'carbonado', 'chicken', 'crabmeat', 'cut', 'duck', 'eel', 'escargot', 'fillet', 'fish', 'game', 'goose', 'halal', 'hamburgers', 'horsemeat', 'jerky', 'lamb', 'mouton', 'muscle']

PrimeNet['pasta'] = ['cannelloni', 'fedelline', 'fettuccine', 'fettucini', 'gnocchi', 'lasagna', 'linguine', 'macaroni', 'manicotti', 'mostaccioli', 'noodle']

## To run the code 
Step 1: Download full ConceptNet data (https://s3.amazonaws.com/conceptnet/downloads/2019/edges/conceptnet-assertions-5.7.0.csv.gz) to ./Data/ConceptNet/ and unzip it as csv file.

Step 2: python main.py or sbatch main
