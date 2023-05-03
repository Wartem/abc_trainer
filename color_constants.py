from collections import namedtuple, OrderedDict


class ColorConst:
    
    
    colors_gpt = {
    'black': '#000000',
    'darkslategray': '#2f4f4f',
    'dimgray': '#696969',
    'slategray': '#708090',
    'gray': '#808080',
    'lightslategray': '#778899',
    'darkgray': '#a9a9a9',
    'silver': '#c0c0c0',
    'lightgray': '#d3d3d3',
    'gainsboro': '#dcdcdc',
    'whitesmoke': '#f5f5f5',
    'white': '#ffffff',
    'maroon': '#800000',
    'darkred': '#8b0000',
    'brown': '#a52a2a',
    'firebrick': '#b22222',
    'crimson': '#dc143c',
    'red': '#ff0000',
    'tomato': '#ff6347',
    'coral': '#ff7f50',
    'indianred': '#cd5c5c',
    'lightcoral': '#f08080',
    'darksalmon': '#e9967a',
    'salmon': '#fa8072',
    'lightsalmon': '#ffa07a',
    'orange': '#ffa500',
    'darkorange': '#ff8c00',
    'gold': '#ffd700',
    'yellow': '#ffff00',
    'khaki': '#f0e68c',
    'palegoldenrod': '#eee8aa',
    'moccasin': '#ffe4b5',
    'navajowhite': '#ffdead',
    'peachpuff': '#ffdab9',
    'wheat': '#f5deb3',
    'burlywood': '#deb887',
    'tan': '#d2b48c',
    'rosybrown': '#bc8f8f',
    'sandybrown': '#f4a460',
    'goldenrod': '#daa520',
    'darkgoldenrod': '#b8860b',
    'peru': '#cd853f',
    'chocolate': '#d2691e',
    'saddlebrown': '#8b4513',
    'sienna': '#a0522d',
    'brown': '#a52a2a',
    'maroon': '#800000',
    'darkolivegreen': '#556b2f',
    'olive': '#808000',
    'olivedrab': '#6b8e23',
    'yellowgreen': '#9acd32',
    'limegreen': '#32cd32',
    'lime': '#00ff00',
    'lawngreen': '#7cfc00',
    'chartreuse': '#7fff00',
    'greenyellow': '#adff2f',
    'springgreen': '#00ff7f',
    'mediumspringgreen': '#00fa9a',
    'lightgreen': '#90ee90',
    'palegreen': '#98fb98',
    'darkseagreen': '#8fbc8f',
    'mediumaquamarine': '#66cdaa',
    'mediumseagreen': '#3cb371',
    'seagreen': '#2e8b57',
    'forestgreen': '#228b22',
    'green': '#008000',
    'darkgreen': '#006400',
    'aqua': '#00ffff',
    'cyan': '#00ffff',
     'lightcyan': '#e0ffff',
    'paleturquoise': '#afeeee',
    'aquamarine': '#7fffd4',
    'turquoise': '#40e0d0',
    'mediumturquoise': '#48d1cc',
    'darkturquoise': '#00ced1',
    'cadetblue': '#5f9ea0',
    'steelblue': '#4682b4',
    'lightsteelblue': '#b0c4de',
    'powderblue': '#b0e0e6',
    'lightblue': '#add8e6',
    'skyblue': '#87ceeb',
    'lightskyblue': '#87cefa',
    'deepskyblue': '#00bfff',
    'dodgerblue': '#1e90ff',
    'cornflowerblue': '#6495ed',
    'royalblue': '#4169e1',
    'blue': '#0000ff',
    'mediumblue': '#0000cd',
    'darkblue': '#00008b',
    'navy': '#000080',
    'midnightblue': '#191970',
    'purple': '#800080',
    'indigo': '#4b0082',
    'blueviolet': '#8a2be2',
    'darkviolet': '#9400d3',
    'darkorchid': '#9932cc',
    'mediumorchid': '#ba55d3',
    'orchid': '#da70d6',
    'violet': '#ee82ee',
    'plum': '#dda0dd',
    'thistle': '#d8bfd8',
    'lavender': '#e6e6fa',
    'ghostwhite': '#f8f8ff',
    'aliceblue': '#f0f8ff',
    'mintcream': '#f5fffa',
    'honeydew': '#f0fff0',
    'lightgoldenrodyellow': '#fafad2',
    'lemonchiffon': '#fffacd',
    'cornsilk': '#fff8dc',
    'beige': '#f5f5dc',
    'oldlace': '#fdf5e6',
    'ivory': '#fffff0',
    'lightyellow': '#ffffe0',
    'lavenderblush': '#fff0f5',
    'mistyrose': '#ffe4e1',
}
    
    main_colors = {
"#4c4f56": "Abbey",
"#0048ba": "Absolute Zero",
"#1b1404": "Acadia",
"#7cb0a1": "Acapulco",
"#b0bf1a": "Acid Green",
"#7cb9e8": "Aero",
"#c9ffe5": "Aero Blue",
"#714693": "Affair",
"#b284be": "African Violet",
"#00308f": "Air Force Blue",
"#72a0c1": "Air Superiority Blue",
"#d4c4a8": "Akaroa",
"#af002a": "Alabama Crimson",
"#fafafa": "Alabaster",
"#f5e9d3": "Albescent White",
"#93dfb8": "Algae Green",
"#f0f8ff": "Alice Blue",
"#84de02": "Alien Armpit",
"#e32636": "Alizarin Crimson",
"#c46210": "Alloy Orange",
"#0076a3": "Allports",
"#efdecd": "Almond",
"#907b71": "Almond Frost",
"#af8f2c": "Alpine",
"#dbdbdb": "Alto",
"#a9acb6": "Aluminium",
"#e52b50": "Amaranth",
"#f19cbb": "Amaranth Pink",
"#ab274f": "Amaranth Purple",
"#d3212d": "Amaranth Red",
"#3b7a57": "Amazon",
"#ffbf00": "Amber",
"#ff033e": "American Rose",
"#87756e": "Americano",
"#9966cc": "Amethyst",
"#a397b4": "Amethyst Smoke",
"#f9eaf3": "Amour",
"#7b9f80": "Amulet",
"#9de5ff": "Anakiwa",
"#a4c639": "Android Green",
"#f2f3f4": "Anti Flash White",
"#cd9575": "Antique Brass",
"#665d1e": "Antique Bronze",
"#915c83": "Antique Fuchsia",
"#841b2d": "Antique Ruby",
"#faebd7": "Antique White",
"#e0b646": "Anzac",
"#008000": "Ao",
"#dfbe6f": "Apache",
"#4fa83d": "Apple",
"#af4d43": "Apple Blossom",
"#8db600": "Apple Green",
"#fbceb1": "Apricot",
"#fffeec": "Apricot White",
"#014b43": "Aqua Deep",
"#5fa777": "Aqua Forest",
"#edf5f5": "Aqua Haze",
"#a1dad7": "Aqua Island",
"#eaf9f5": "Aqua Spring",
"#e8f5f2": "Aqua Squeeze",
"#7fffd4": "Aquamarine",
"#71d9e2": "Aquamarine Blue",
"#110c6c": "Arapawa",
"#d0ff14": "Arctic Lime",
"#433e37": "Armadillo",
"#4b5320": "Army Green",
"#948771": "Arrowtown",
"#3b444b": "Arsenic",
"#8f9779": "Artichoke",
"#e9d66b": "Arylide Yellow",
"#c6c3b5": "Ash",
"#b2beb5": "Ash Grey",
"#87a96b": "Asparagus",
"#130a06": "Asphalt",
"#faeab9": "Astra",
"#327da0": "Astral",
"#283a77": "Astronaut",
"#013e62": "Astronaut Blue",
"#eef0f3": "Athens Gray",
"#ecebce": "Aths Special",
"#97cd2d": "Atlantis",
"#0a6f75": "Atoll",
"#97605d": "Au Chico",
"#3b0910": "Aubergine",
"#a52a2a": "Auburn",
"#fdee00": "Aureolin",
"#6e7f80": "Auro Metal Saurus",
"#f5ffbe": "Australian Mint",
"#568203": "Avocado",
"#4e6649": "Axolotl",
"#f7c8da": "Azalea",
"#0d1c19": "Aztec",
"#c39953": "Aztec Gold",
"#007fff": "Azure",
"#f0ffff": "Azure Mist",
"#dbe9f4": "Azureish White",
"#89cff0": "Baby Blue",
"#a1caf1": "Baby Blue Eyes",
"#fefefa": "Baby Powder",
"#026395": "Bahama Blue",
"#a5cb0c": "Bahia",
"#fff8d1": "Baja White",
"#ff91af": "Baker Miller Pink",
"#859faf": "Bali Hai",
"#21abcd": "Ball Blue",
"#2a2630": "Baltic Sea",
"#da6304": "Bamboo",
"#fae7b5": "Banana Mania",
"#ffe135": "Banana Yellow",
"#858470": "Bandicoot",
"#ded717": "Barberry",
"#e0218a": "Barbie Pink",
"#a68b5b": "Barley Corn",
"#fff4ce": "Barley White",
"#7c0a02": "Barn Red",
"#44012d": "Barossa",
"#292130": "Bastille",
"#828f72": "Battleship Gray",
"#7da98d": "Bay Leaf",
"#273a81": "Bay of Many",
"#98777b": "Bazaar",
"#2e5894": "Bdazzled Blue",
"#bcd4e6": "Beau Blue",
"#eec1be": "Beauty Bush",
"#9f8170": "Beaver",
"#fef2c7": "Beeswax",
"#f5f5dc": "Beige",
"#add8ff": "Belgion",
"#7dd8c6": "Bermuda",
"#6b8ba2": "Bermuda Gray",
"#dee5c0": "Beryl Green",
"#fcfbf3": "Bianca",
"#9c2542": "Big Dip Oruby",
"#e88e5a": "Big Foot Feet",
"#162a40": "Big Stone",
"#327c14": "Bilbao",
"#b2a1ea": "Biloba Flower",
"#373021": "Birch",
"#d4cd16": "Bird Flower",
"#1b3162": "Biscay",
"#497183": "Bismark",
"#c1b7a4": "Bison Hide",
"#ffe4c4": "Bisque",
"#3d2b1f": "Bistre",
"#868974": "Bitter",
"#cae00d": "Bitter Lemon",
"#fe6f5e": "Bittersweet",
"#bf4f51": "Bittersweet Shimmer",
"#eededa": "Bizarre",
"#000000": "Black",
"#3d0c02": "Black Bean",
"#54626f": "Black Coral",
"#0b1304": "Black Forest",
"#f6f7f7": "Black Haze",
"#253529": "Black Leather Jacket",
"#3e2c1c": "Black Marlin",
"#3b3c36": "Black Olive",
"#041322": "Black Pearl",
"#0d0332": "Black Rock",
"#67032d": "Black Rose",
"#0a001c": "Black Russian",
"#bfafb2": "Black Shadows",
"#f2fafa": "Black Squeeze",
"#fffef6": "Black White",
"#4d0135": "Blackberry",
"#32293a": "Blackcurrant",
"#ffebcd": "Blanched Almond",
"#a57164": "Blast Off Bronze",
"#ff6700": "Blaze Orange",
"#fef3d8": "Bleach White",
"#2c2133": "Bleached Cedar",
"#318ce7": "Bleu De France",
"#a3e3ed": "Blizzard Blue",
"#faf0be": "Blond",
"#dcb4bc": "Blossom",
"#0000ff": "Blue",
"#496679": "Blue Bayoux",
"#a2a2d0": "Blue Bell",
"#f1e9ff": "Blue Chalk",
"#010d1a": "Blue Charcoal",
"#0c8990": "Blue Chill",
"#380474": "Blue Diamond",
"#204852": "Blue Dianne",
"#2c0e8c": "Blue Gem",
"#6699cc": "Blue Gray",
"#0d98ba": "Blue Green",
"#bfbed8": "Blue Haze",
"#5dadec": "Blue Jeans",
"#ace5ee": "Blue Lagoon",
"#553592": "Blue Magenta Violet",
"#7666c6": "Blue Marguerite",
"#0066ff": "Blue Ribbon",
"#d2f6de": "Blue Romance",
"#126180": "Blue Sapphire",
"#748881": "Blue Smoke",
"#016162": "Blue Stone",
"#8a2be2": "Blue Violet",
"#042e4c": "Blue Whale",
"#5072a7": "Blue Yonder",
"#13264d": "Blue Zodiac",
"#4f86f7": "Blueberry",
"#1c1cf0": "Bluebonnet",
"#18587a": "Blumine",
"#de5d83": "Blush",
"#79443b": "Bole",
"#afb1b8": "Bombay",
"#e5e0e1": "Bon Jour",
"#0095b6": "Bondi Blue",
"#e3dac9": "Bone",
"#dde26a": "Booger Buster",
"#5c0120": "Bordeaux",
"#4e2a5a": "Bossanova",
"#3b91b4": "Boston Blue",
"#cc0000": "Boston University Red",
"#c7dde5": "Botticelli",
"#006a4e": "Bottle Green",
"#7a7a7a": "Boulder",
"#ae809e": "Bouquet",
"#ba6f1e": "Bourbon",
"#873260": "Boysenberry",
"#4a2a04": "Bracken",
"#0070ff": "Brandeis Blue",
"#dec196": "Brandy",
"#cd8429": "Brandy Punch",
"#bb8983": "Brandy Rose",
"#b5a642": "Brass",
"#5da19f": "Breaker Bay",
"#cb4154": "Brick Red",
"#fffaf4": "Bridal Heath",
"#fef0ec": "Bridesmaid",
"#1dacd6": "Bright Cerulean",
"#3c4151": "Bright Gray",
"#66ff00": "Bright Green",
"#bf94e4": "Bright Lavender",
"#d891ef": "Bright Lilac",
"#c32148": "Bright Maroon",
"#1974d2": "Bright Navy Blue",
"#b10000": "Bright Red",
"#fed33c": "Bright Sun",
"#08e8de": "Bright Turquoise",
"#d19fe8": "Bright Ube",
"#ffaa1d": "Bright Yellow",
"#3399ff": "Brilliant Azure",
"#f4bbff": "Brilliant Lavender",
"#ff55a3": "Brilliant Rose",
"#fb607f": "Brink Pink",
"#004225": "British Racing Green",
"#aba196": "Bronco",
"#cd7f32": "Bronze",
"#4e420c": "Bronze Olive",
"#737000": "Bronze Yellow",
"#4d400f": "Bronzetone",
"#ffec13": "Broom",
"#964b00": "Brown",
"#592804": "Brown Bramble",
"#492615": "Brown Derby",
"#401801": "Brown Pod",
"#af593e": "Brown Rust",
"#af6e4d": "Brown Sugar",
"#37290e": "Brown Tumbleweed",
"#cc9966": "Brown Yellow",
"#1b4d3e": "Brunswick Green",
"#ffc1cc": "Bubble Gum",
"#e7feff": "Bubbles",
"#622f30": "Buccaneer",
"#a8ae9c": "Bud",
"#7bb661": "Bud Green",
"#c1a004": "Buddha Gold",
"#f0dc82": "Buff",
"#480607": "Bulgarian Rose",
"#864d1e": "Bull Shot",
"#0d1117": "Bunker",
"#151f4c": "Bunting",
"#800020": "Burgundy",
"#deb887": "Burlywood",
"#002e20": "Burnham",
"#ff7034": "Burning Orange",
"#d99376": "Burning Sand",
"#a17a74": "Burnished Brown",
"#420303": "Burnt Maroon",
"#cc5500": "Burnt Orange",
"#e97451": "Burnt Sienna",
"#8a3324": "Burnt Umber",
"#0d2e1c": "Bush",
"#f3ad16": "Buttercup",
"#a1750d": "Buttered Rum",
"#624e9a": "Butterfly Bush",
"#fff1b5": "Buttermilk",
"#fffcea": "Buttery White",
"#bd33a4": "Byzantine",
"#702963": "Byzantium",
"#007aa5": "CG Blue",
"#e03c31": "CG Red",
"#4d0a18": "Cab Sav",
"#d94972": "Cabaret",
"#3f4c3a": "Cabbage Pont",
"#587156": "Cactus",
"#536872": "Cadet",
"#5f9ea0": "Cadet Blue",
"#91a3b0": "Cadet Grey",
"#b04c6a": "Cadillac",
"#006b3c": "Cadmium Green",
"#ed872d": "Cadmium Orange",
"#e30022": "Cadmium Red",
"#fff600": "Cadmium Yellow",
"#4b3621": "Cafe Noir",
"#6f440c": "Cafe Royale",
"#1e4d2b": "Cal Poly Green",
"#e0c095": "Calico",
"#fe9d04": "California",
"#31728d": "Calypso",
"#00581a": "Camarone",
"#a3c1ad": "Cambridge Blue",
"#893456": "Camelot",
"#d9b99b": "Cameo",
"#efbbcc": "Cameo Pink",
"#3c3910": "Camouflage",
"#78866b": "Camouflage Green",
"#d591a4": "Can Can",
"#f3fb62": "Canary",
"#ffef00": "Canary Yellow",
"#fcd917": "Candlelight",
"#ff0800": "Candy Apple Red",
"#251706": "Cannon Black",
"#894367": "Cannon Pink",
"#3c4443": "Cape Cod",
"#fee5ac": "Cape Honey",
"#a26645": "Cape Palliser",
"#dcedb4": "Caper",
"#00bfff": "Capri",
"#592720": "Caput Mortuum",
"#ffddaf": "Caramel",
"#eeeee8": "Cararra",
"#01361c": "Cardin Green",
"#c41e3a": "Cardinal",
"#8c055e": "Cardinal Pink",
"#d29eaa": "Careys Pink",
"#00cc99": "Caribbean Green",
"#ea88a8": "Carissma",
"#f3ffd8": "Carla",
"#960018": "Carmine",
"#eb4c42": "Carmine Pink",
"#ff0038": "Carmine Red",
"#5c2e01": "Carnaby Tan",
"#f95a61": "Carnation",
"#ffa6c9": "Carnation Pink",
"#b31b1b": "Carnelian",
"#56a0d3": "Carolina Blue",
"#f9e0ed": "Carousel Pink",
"#ed9121": "Carrot Orange",
"#f8b853": "Casablanca",
"#2f6168": "Casal",
"#8ba9a5": "Cascade",
"#e6bea5": "Cashmere",
"#adbed1": "Casper",
"#00563b": "Castleton Green",
"#52001f": "Castro",
"#062a78": "Catalina Blue",
"#703642": "Catawba",
"#eef6f7": "Catskill White",
"#e3bebe": "Cavern Pink",
"#3e1c14": "Cedar",
"#c95a49": "Cedar Chest",
"#711a00": "Cedar Wood Finish",
"#92a1cf": "Ceil",
"#ace1af": "Celadon",
"#2f847c": "Celadon Green",
"#b8c25d": "Celery",
"#b2ffff": "Celeste",
"#4997d0": "Celestial Blue",
"#1e385b": "Cello",
"#163222": "Celtic",
"#8d7662": "Cement",
"#fcfff9": "Ceramic",
"#de3163": "Cerise",
"#ec3b83": "Cerise Pink",
"#007ba7": "Cerulean",
"#2a52be": "Cerulean Blue",
"#6d9bc3": "Cerulean Frost",
"#fff4f3": "Chablis",
"#516e3d": "Chalet Green",
"#eed794": "Chalky",
"#354e8c": "Chambray",
"#eddcb1": "Chamois",
"#a0785a": "Chamoisee",
"#f7e7ce": "Champagne",
"#f8c3df": "Chantilly",
"#292937": "Charade",
"#36454f": "Charcoal",
"#fff3f1": "Chardon",
"#ffcd8c": "Chardonnay",
"#232b2b": "Charleston Green",
"#baeef9": "Charlotte",
"#d47494": "Charm",
"#e68fac": "Charm Pink",
"#dfff00": "Chartreuse",
"#40a860": "Chateau Green",
"#bdb3c7": "Chatelle",
"#175579": "Chathams Blue",
"#83aa5d": "Chelsea Cucumber",
"#9e5302": "Chelsea Gem",
"#dfcd6f": "Chenin",
"#fcda98": "Cherokee",
"#ffb7c5": "Cherry Blossom Pink",
"#2a0359": "Cherry Pie",
"#651a14": "Cherrywood",
"#f8d9e9": "Cherub",
"#954535": "Chestnut",
"#8581d9": "Chetwode Blue",
"#5d5c58": "Chicago",
"#f1ffc8": "Chiffon",
"#f77703": "Chilean Fire",
"#fffde6": "Chilean Heath",
"#fcffe7": "China Ivory",
"#a8516e": "China Rose",
"#aa381e": "Chinese Red",
"#856088": "Chinese Violet",
"#cec7a7": "Chino",
"#a8e3bd": "Chinook",
"#4aff00": "Chlorophyll Green",
"#7b3f00": "Chocolate",
"#33036b": "Christalle",
"#67a712": "Christi",
"#e7730a": "Christine",
"#e8f1d4": "Chrome White",
"#ffa700": "Chrome Yellow",
"#0e0e18": "Cinder",
"#fde1dc": "Cinderella",
"#98817b": "Cinereous",
"#e34234": "Cinnabar",
"#cd607e": "Cinnamon Satin",
"#55280c": "Cioccolato",
"#e4d00a": "Citrine",
"#faf7d6": "Citrine White",
"#9fa91f": "Citron",
"#a1c50a": "Citrus",
"#480656": "Clairvoyant",
"#d4b6af": "Clam Shell",
"#7f1734": "Claret",
"#fbcce7": "Classic Rose",
"#bdc8b3": "Clay Ash",
"#8a8360": "Clay Creek",
"#e9fffd": "Clear Day",
"#e96e00": "Clementine",
"#371d09": "Clinker",
"#c7c4bf": "Cloud",
"#202e54": "Cloud Burst",
"#aca59f": "Cloudy",
"#384910": "Clover",
"#0047ab": "Cobalt Blue",
"#481c1c": "Cocoa Bean",
"#d2691e": "Cocoa Brown",
"#965a3e": "Coconut",
"#f8f7dc": "Coconut Cream",
"#0b0b0b": "Cod Gray",
"#6f4e37": "Coffee",
"#2a140e": "Coffee Bean",
"#9f381d": "Cognac",
"#3f2500": "Cola",
"#aba0d9": "Cold Purple",
"#cebaba": "Cold Turkey",
"#ffedbc": "Colonial White",
"#c4d8e2": "Columbia Blue",
"#5c5d75": "Comet",
"#517c66": "Como",
"#c9d9d2": "Conch",
"#7c7b7a": "Concord",
"#f2f2f2": "Concrete",
"#e9d75a": "Confetti",
"#593737": "Congo Brown",
"#f88379": "Congo Pink",
"#02478e": "Congress Blue",
"#acdd4d": "Conifer",
"#c6726b": "Contessa",
"#002e63": "Cool Black",
"#8c92ac": "Cool Grey",
"#b87333": "Copper",
"#7e3a15": "Copper Canyon",
"#ad6f69": "Copper Penny",
"#cb6d51": "Copper Red",
"#996666": "Copper Rose",
"#944747": "Copper Rust",
"#ff3800": "Coquelicot",
"#ff7f50": "Coral",
"#ff4040": "Coral Red",
"#c7bca2": "Coral Reef",
"#a86b6b": "Coral Tree",
"#893f45": "Cordovan",
"#606e68": "Corduroy",
"#c4d0b0": "Coriander",
"#40291d": "Cork",
"#e7bf05": "Corn",
"#f8facd": "Corn Field",
"#8b6b0b": "Corn Harvest",
"#6495ed": "Cornflower Blue",
"#ffb0ac": "Cornflower Lilac",
"#fff8dc": "Cornsilk",
"#fad3a2": "Corvette",
"#76395d": "Cosmic",
"#2e2d88": "Cosmic Cobalt",
"#fff8e7": "Cosmic Latte",
"#ffd8d9": "Cosmos",
"#615d30": "Costa Del Sol",
"#ffbcd9": "Cotton Candy",
"#c2bdb6": "Cotton Seed",
"#01371a": "County Green",
"#4d282d": "Cowboy",
"#81613e": "Coyote Brown",
"#b95140": "Crail",
"#db5079": "Cranberry",
"#462425": "Crater Brown",
"#1f75fe": "Crayola Blue",
"#1cac78": "Crayola Green",
"#ff7538": "Crayola Orange",
"#ee204d": "Crayola Red",
"#fce883": "Crayola Yellow",
"#fffdd0": "Cream",
"#ffe5a0": "Cream Brulee",
"#f5c85c": "Cream Can",
"#1e0f04": "Creole",
"#737829": "Crete",
"#dc143c": "Crimson",
"#be0032": "Crimson Glory",
"#990000": "Crimson Red",
"#736d58": "Crocodile",
"#771f1f": "Crown of Thorns",
"#1c1208": "Crowshead",
"#b5ecdf": "Cruise",
"#004816": "Crusoe",
"#fd7b33": "Crusta",
"#924321": "Cumin",
"#fdffd5": "Cumulus",
"#fbbeda": "Cupid",
"#2596d1": "Curious Blue",
"#507672": "Cutty Sark",
"#00ffff": "Cyan",
"#4e82b4": "Cyan Azure",
"#4682bf": "Cyan Blue Azure",
"#28589c": "Cyan Cobalt Blue",
"#188bc2": "Cyan Cornflower Blue",
"#58427c": "Cyber Grape",
"#ffd300": "Cyber Yellow",
"#f56fa1": "Cyclamen",
"#003e40": "Cyprus",
"#ffff31": "Daffodil",
"#012731": "Daintree",
"#f9e4bc": "Dairy Cream",
"#4f2398": "Daisy Bush",
"#6e4b26": "Dallas",
"#f0e130": "Dandelion",
"#6093d1": "Danube",
"#00008b": "Dark Blue",
"#666699": "Dark Blue Gray",
"#654321": "Dark Brown",
"#88654e": "Dark Brown Tangelo",
"#770f05": "Dark Burgundy",
"#5d3954": "Dark Byzantium",
"#a40000": "Dark Candy Apple Red",
"#08457e": "Dark Cerulean",
"#986960": "Dark Chestnut",
"#cd5b45": "Dark Coral",
"#008b8b": "Dark Cyan",
"#3c2005": "Dark Ebony",
"#0a480d": "Dark Fern",
"#b8860b": "Dark Goldenrod",
"#013220": "Dark Green",
"#1f262a": "Dark Gunmetal",
"#6e6ef9": "Dark Imperial Blue",
"#1a2421": "Dark Jungle Green",
"#bdb76b": "Dark Khaki",
"#734f96": "Dark Lavender",
"#534b4f": "Dark Liver",
"#8b008b": "Dark Magenta",
"#a9a9a9": "Dark Medium Gray",
"#003366": "Dark Midnight Blue",
"#4a5d23": "Dark Moss Green",
"#556b2f": "Dark Olive Green",
"#ff8c00": "Dark Orange",
"#9932cc": "Dark Orchid",
"#779ecb": "Dark Pastel Blue",
"#03c03c": "Dark Pastel Green",
"#966fd6": "Dark Pastel Purple",
"#c23b22": "Dark Pastel Red",
"#e75480": "Dark Pink",
"#4f3a3c": "Dark Puce",
"#301934": "Dark Purple",
"#872657": "Dark Raspberry",
"#8b0000": "Dark Red",
"#e9967a": "Dark Salmon",
"#560319": "Dark Scarlet",
"#8fbc8f": "Dark Sea Green",
"#3c1414": "Dark Sienna",
"#8cbed6": "Dark Sky Blue",
"#483d8b": "Dark Slate Blue",
"#2f4f4f": "Dark Slate Gray",
"#177245": "Dark Spring Green",
"#918151": "Dark Tan",
"#ffa812": "Dark Tangerine",
"#cc4e5c": "Dark Terra Cotta",
"#00ced1": "Dark Turquoise",
"#d1bea8": "Dark Vanilla",
"#9400d3": "Dark Violet",
"#9b870c": "Dark Yellow",
"#00703c": "Dartmouth Green",
"#555555": "Davys Grey",
"#a6a29a": "Dawn",
"#f3e9e5": "Dawn Pink",
"#7ac488": "De York",
"#d70a53": "Debian Red",
"#d2da97": "Deco",
"#220878": "Deep Blue",
"#e47698": "Deep Blush",
"#4a3004": "Deep Bronze",
"#a9203e": "Deep Carmine",
"#ef3038": "Deep Carmine Pink",
"#e9692c": "Deep Carrot Orange",
"#da3287": "Deep Cerise",
"#b94e48": "Deep Chestnut",
"#051040": "Deep Cove",
"#002900": "Deep Fir",
"#182d09": "Deep Forest Green",
"#c154c1": "Deep Fuchsia",
"#056608": "Deep Green",
"#0e7c61": "Deep Green Cyan Turquoise",
"#004b49": "Deep Jungle Green",
"#333366": "Deep Koamaru",
"#f5c71a": "Deep Lemon",
"#9955bb": "Deep Lilac",
"#cc00cc": "Deep Magenta",
"#820000": "Deep Maroon",
"#412010": "Deep Oak",
"#ff1493": "Deep Pink",
"#a95c68": "Deep Puce",
"#850101": "Deep Red",
"#843f5b": "Deep Ruby",
"#ff9933": "Deep Saffron",
"#082567": "Deep Sapphire",
"#01826b": "Deep Sea",
"#095859": "Deep Sea Green",
"#4a646c": "Deep Space Sparkle",
"#7e5e60": "Deep Taupe",
"#003532": "Deep Teal",
"#66424d": "Deep Tuscan Red",
"#330066": "Deep Violet",
"#ba8759": "Deer",
"#b09a95": "Del Rio",
"#396413": "Dell",
"#a4a49d": "Delta",
"#7563a8": "Deluge",
"#1560bd": "Denim",
"#2243b6": "Denim Blue",
"#ffeed8": "Derby",
"#669999": "Desaturated Cyan",
"#ae6020": "Desert",
"#edc9af": "Desert Sand",
"#f8f8f7": "Desert Storm",
"#ea3c53": "Desire",
"#eafffe": "Dew",
"#db995e": "Di Serria",
"#b9f2ff": "Diamond",
"#130000": "Diesel",
"#696969": "Dim Gray",
"#5d7747": "Dingley",
"#c53151": "Dingy Dungeon",
"#9b7653": "Dirt",
"#871550": "Disco",
"#e29418": "Dixie",
"#1e90ff": "Dodger Blue",
"#b86d29": "Dogs",
"#d71868": "Dogwood Rose",
"#85bb65": "Dollar Bill",
"#f9ff8b": "Dolly",
"#646077": "Dolphin",
"#8e775e": "Domino",
"#5d4c51": "Don Juan",
"#664c28": "Donkey Brown",
"#6b5755": "Dorado",
"#eee3ad": "Double Colonial White",
"#fcf4d0": "Double Pearl Lusta",
"#e6d7b9": "Double Spanish White",
"#6d6c6c": "Dove Gray",
"#092256": "Downriver",
"#6fd0c5": "Downy",
"#af8751": "Driftwood",
"#fdf7ad": "Drover",
"#00009c": "Duke Blue",
"#a899e6": "Dull Lavender",
"#383533": "Dune",
"#e5ccc9": "Dust Storm",
"#a8989b": "Dusty Gray",
"#efdfbb": "Dutch White",
"#b6baa4": "Eagle",
"#004953": "Eagle Green",
"#c9b93b": "Earls Green",
"#fff9e6": "Early Dawn",
"#e1a95f": "Earth Yellow",
"#414c7d": "East Bay",
"#ac91ce": "East Side",
"#1e9ab0": "Eastern Blue",
"#e9e3e3": "Ebb",
"#555d50": "Ebony",
"#26283b": "Ebony Clay",
"#311c17": "Eclipse",
"#c2b280": "Ecru",
"#f5f3e5": "Ecru White",
"#fa7814": "Ecstasy",
"#105852": "Eden",
"#c8e3d7": "Edgewater",
"#a2aeab": "Edward",
"#1b1b1b": "Eerie Black",
"#fff4dd": "Egg Sour",
"#ffefc1": "Egg White",
"#614051": "Eggplant",
"#f0ead6": "Eggshell",
"#1034a6": "Egyptian Blue",
"#1e1708": "El Paso",
"#8f3e33": "El Salva",
"#7df9ff": "Electric Blue",
"#ff003f": "Electric Crimson",
"#6f00ff": "Electric Indigo",
"#ccff00": "Electric Lime",
"#bf00ff": "Electric Purple",
"#8b00ff": "Electric Violet",
"#ffff33": "Electric Yellow",
"#123447": "Elephant",
"#088370": "Elf Green",
"#1c7c7d": "Elm",
"#50c878": "Emerald",
"#6c3082": "Eminence",
"#514649": "Emperor",
"#817377": "Empress",
"#0056a7": "Endeavour",
"#f8dd5c": "Energy Yellow",
"#ba160c": "Engineering International Orange",
"#022d15": "English Holly",
"#b48395": "English Lavender",
"#ab4b52": "English Red",
"#cc474b": "English Vermillion",
"#3e2b23": "English Walnut",
"#8ba690": "Envy",
"#e1bc64": "Equator",
"#612718": "Espresso",
"#211a0e": "Eternity",
"#96c8a2": "Eton Blue",
"#44d7a8": "Eucalyptus",
"#cfa39d": "Eunry",
"#024e46": "Evening Sea",
"#1c402e": "Everglade",
"#010b13": "FOGRA29 Rich Black",
"#010203": "FOGRA39 Rich Black",
"#427977": "Faded Jade",
"#ffefec": "Fair Pink",
"#7f626d": "Falcon",
"#c19a6b": "Fallow",
"#801818": "Falu Red",
"#b53389": "Fandango",
"#de5285": "Fandango Pink",
"#faf3f0": "Fantasy",
"#f400a1": "Fashion Fuchsia",
"#e5aa70": "Fawn",
"#796a78": "Fedora",
"#9fdd8c": "Feijoa",
"#4d5d53": "Feldgrau",
"#63b76c": "Fern",
"#657220": "Fern Frond",
"#4f7942": "Fern Green",
"#704f50": "Ferra",
"#ff2800": "Ferrari Red",
"#fbe96c": "Festival",
"#f0fcea": "Feta",
"#6c541e": "Field Drab",
"#b35213": "Fiery Orange",
"#ff5470": "Fiery Rose",
"#626649": "Finch",
"#556d56": "Finlandia",
"#692d54": "Finn",
"#405169": "Fiord",
"#aa4203": "Fire",
"#e89928": "Fire Bush",
"#ce2029": "Fire Engine Red",
"#b22222": "Firebrick",
"#0e2a30": "Firefly",
"#e25822": "Flame",
"#da5b38": "Flame Pea",
"#ff7d07": "Flamenco",
"#f2552a": "Flamingo",
"#fc8eac": "Flamingo Pink",
"#f7e98e": "Flavescent",
"#eedc82": "Flax",
"#7b8265": "Flax Smoke",
"#6f6a61": "Flint",
"#a2006d": "Flirt",
"#fffaf0": "Floral White",
"#ca3435": "Flush Mahogany",
"#d8fcfa": "Foam",
"#d7d0ff": "Fog",
"#cbcab6": "Foggy Gray",
"#ff004f": "Folly",
"#228b22": "Forest Green",
"#fff1ee": "Forget Me Not",
"#56b4be": "Fountain Blue",
"#ffdeb3": "Frangipani",
"#856d4d": "French Bistre",
"#0072bb": "French Blue",
"#fd3f92": "French Fuchsia",
"#bdbdc6": "French Gray",
"#86608e": "French Lilac",
"#9efd38": "French Lime",
"#d473d4": "French Mauve",
"#bdedfd": "French Pass",
"#fd6c9e": "French Pink",
"#811453": "French Plum",
"#4e1609": "French Puce",
"#c72c48": "French Raspberry",
"#f64a8a": "French Rose",
"#77b5fe": "French Sky Blue",
"#8806ce": "French Violet",
"#ac1e44": "French Wine",
"#a6e7ff": "Fresh Air",
"#990066": "Fresh Eggplant",
"#807e79": "Friar Gray",
"#b1e2c1": "Fringy Flower",
"#f57584": "Froly",
"#edf5dd": "Frost",
"#e936a7": "Frostbite",
"#dbfff8": "Frosted Mint",
"#e4f6e7": "Frostee",
"#4f9d5d": "Fruit Salad",
"#ff00ff": "Fuchsia",
"#7a58c1": "Fuchsia Blue",
"#ff77ff": "Fuchsia Pink",
"#cc397b": "Fuchsia Purple",
"#c74375": "Fuchsia Rose",
"#bede0d": "Fuego",
"#eca927": "Fuel Yellow",
"#e48400": "Fulvous",
"#1959a8": "Fun Blue",
"#016d39": "Fun Green",
"#54534d": "Fuscous Gray",
"#cc6666": "Fuzzy Wuzzy",
"#c45655": "Fuzzy Wuzzy Brown",
"#00ab66": "GO Green",
"#163531": "Gable Green",
"#dcdcdc": "Gainsboro",
"#efefef": "Gallery",
"#dcb20c": "Galliano",
"#e49b0f": "Gamboge",
"#996600": "Gamboge Orange",
"#ffdf46": "Gargoyle Gas",
"#d18f1b": "Geebung",
"#007f66": "Generic Viridian",
"#15736b": "Genoa",
"#fb8989": "Geraldine",
"#d4dfe2": "Geyser",
"#c7c9d5": "Ghost",
"#f8f8ff": "Ghost White",
"#b05c52": "Giants Club",
"#fe5a1d": "Giants Orange",
"#523c94": "Gigas",
"#b8b56a": "Gimblet",
"#e8f2eb": "Gin",
"#fff9e2": "Gin Fizz",
"#b06500": "Ginger",
"#f8e4bf": "Givry",
"#80b3c4": "Glacier",
"#61845f": "Glade Green",
"#6082b6": "Glaucous",
"#e6e8fa": "Glitter",
"#ab92b3": "Glossy Grape",
"#726d4e": "Go Ben",
"#3d7d52": "Goblin",
"#f18200": "Gold Drop",
"#85754e": "Gold Fusion",
"#deba13": "Gold Tips",
"#ffd700": "Golden",
"#e28913": "Golden Bell",
"#996515": "Golden Brown",
"#f0d52d": "Golden Dream",
"#f5fb3d": "Golden Fizz",
"#c0362c": "Golden Gate Bridge",
"#fde295": "Golden Glow",
"#fcc200": "Golden Poppy",
"#f0db7d": "Golden Sand",
"#ffcc5c": "Golden Tainoi",
"#ffdf00": "Golden Yellow",
"#daa520": "Goldenrod",
"#261414": "Gondola",
"#0b1107": "Gordons Green",
"#fff14f": "Gorse",
"#069b81": "Gossamer",
"#d2f8b0": "Gossip",
"#6d92a1": "Gothic",
"#2f3cb3": "Governor Bay",
"#e4d5b7": "Grain Brown",
"#ffd38c": "Grandis",
"#676767": "Granite Gray",
"#8d8974": "Granite Green",
"#d5f6e3": "Granny Apple",
"#84a0a0": "Granny Smith",
"#a8e4a0": "Granny Smith Apple",
"#6f2da8": "Grape",
"#251607": "Graphite",
"#4a444b": "Gravel",
"#808080": "Gray",
"#465945": "Gray Asparagus",
"#a2aab3": "Gray Chateau",
"#c3c3bd": "Gray Nickel",
"#e7ece6": "Gray Nurse",
"#a9a491": "Gray Olive",
"#c1becd": "Gray Suit",
"#00ff00": "Green",
"#1164b4": "Green Blue",
"#009966": "Green Cyan",
"#01a368": "Green Haze",
"#24500f": "Green House",
"#25311c": "Green Kelp",
"#436a0d": "Green Leaf",
"#a7f432": "Green Lizard",
"#cbd3b0": "Green Mist",
"#1d6142": "Green Pea",
"#6eaea1": "Green Sheen",
"#a4af6e": "Green Smoke",
"#b8c1b1": "Green Spring",
"#032b52": "Green Vogue",
"#101405": "Green Waterloo",
"#e8ebe0": "Green White",
"#adff2f": "Green Yellow",
"#d54600": "Grenadier",
"#885818": "Grizzly",
"#a99a86": "Grullo",
"#ba0101": "Guardsman Red",
"#051657": "Gulf Blue",
"#80b3ae": "Gulf Stream",
"#9dacb7": "Gull Gray",
"#b6d3bf": "Gum Leaf",
"#7ca1a6": "Gumbo",
"#414257": "Gun Powder",
"#2a3439": "Gunmetal",
"#828685": "Gunsmoke",
"#9a9577": "Gurkha",
"#98811b": "Hacienda",
"#6b2a14": "Hairy Heath",
"#1b1035": "Haiti",
"#663854": "Halayà Úbe",
"#85c4cc": "Half Baked",
"#fdf6d3": "Half Colonial White",
"#fef7de": "Half Dutch White",
"#fef4db": "Half Spanish White",
"#fffee1": "Half and Half",
"#e5d8af": "Hampton",
"#446ccf": "Han Blue",
"#5218fa": "Han Purple",
"#3fff00": "Harlequin",
"#46cb18": "Harlequin Green",
"#e6f2ea": "Harp",
"#c90016": "Harvard Crimson",
"#da9100": "Harvest Gold",
"#5590d9": "Havelock Blue",
"#9d5616": "Hawaiian Tan",
"#d4e2fc": "Hawkes Blue",
"#ff7a00": "Heat Wave",
"#541012": "Heath",
"#b7c3d0": "Heather",
"#b6b095": "Heathered Gray",
"#2b3228": "Heavy Metal",
"#df73ff": "Heliotrope",
"#aa98a9": "Heliotrope Gray",
"#aa00bb": "Heliotrope Magenta",
"#5e5d3b": "Hemlock",
"#907874": "Hemp",
"#b6316c": "Hibiscus",
"#6f8e63": "Highland",
"#aca586": "Hillary",
"#6a5d1b": "Himalaya",
"#e6ffe9": "Hint of Green",
"#fbf9f9": "Hint of Red",
"#fafde4": "Hint of Yellow",
"#589aaf": "Hippie Blue",
"#53824b": "Hippie Green",
"#ae4560": "Hippie Pink",
"#a1adb5": "Hit Gray",
"#ffab81": "Hit Pink",
"#c8a528": "Hokey Pokey",
"#65869f": "Hoki",
"#011d13": "Holly",
"#4f1c70": "Honey Flower",
"#f0fff0": "Honeydew",
"#edfc84": "Honeysuckle",
"#006db0": "Honolulu Blue",
"#49796b": "Hookers Green",
"#d06da1": "Hopbush",
"#5a87a0": "Horizon",
"#543d37": "Horses",
"#604913": "Horses Neck",
"#ff1dce": "Hot Magenta",
"#ff69b4": "Hot Pink",
"#b38007": "Hot Toddy",
"#cff9f3": "Humming Bird",
"#355e3b": "Hunter Green",
"#877c7b": "Hurricane",
"#b7a458": "Husk",
"#b1f4e7": "Ice Cold",
"#71a6d2": "Iceberg",
"#fcf75e": "Icterine",
"#319177": "Illuminating Emerald",
"#f6a4c9": "Illusion",
"#602f6b": "Imperial",
"#002395": "Imperial Blue",
"#ed2939": "Imperial Red",
"#b0e313": "Inch Worm",
"#b2ec5d": "Inchworm",
"#4c516d": "Independence",
"#138808": "India Green",
"#cd5c5c": "Indian Red",
"#4d1e01": "Indian Tan",
"#e3a857": "Indian Yellow",
"#4b0082": "Indigo",
"#091f92": "Indigo Dye",
"#c26b03": "Indochine",
"#002fa7": "International Klein Blue",
"#ff4f00": "International Orange",
"#5a4fcf": "Iris",
"#5f3d26": "Irish Coffee",
"#433120": "Iroko",
"#d4d7d9": "Iron",
"#676662": "Ironside Gray",
"#86483c": "Ironstone",
"#b3446c": "Irresistible",
"#f4f0ec": "Isabelline",
"#009000": "Islamic Green",
"#fffcee": "Island Spice",
"#fffff0": "Ivory",
"#2e0329": "Jacaranda",
"#3a2a6a": "Jacarta",
"#2e1905": "Jacko Bean",
"#20208d": "Jacksons Purple",
"#00a86b": "Jade",
"#ef863f": "Jaffa",
"#c2e8e5": "Jagged Ice",
"#350e57": "Jagger",
"#080110": "Jaguar",
"#5b3013": "Jambalaya",
"#f4ebd3": "Janna",
"#9d2933": "Japanese Carmine",
"#264348": "Japanese Indigo",
"#0a6906": "Japanese Laurel",
"#780109": "Japanese Maple",
"#5b3256": "Japanese Violet",
"#d87c63": "Japonica",
"#f8de7e": "Jasmine",
"#d73b3e": "Jasper",
"#1fc2c2": "Java",
"#a50b5e": "Jazzberry Jam",
"#da614e": "Jelly Bean",
"#343434": "Jet",
"#b5d2ce": "Jet Stream",
"#126b40": "Jewel",
"#3b1f1f": "Jon",
"#f4ca16": "Jonquil",
"#8ab9f1": "Jordy Blue",
"#544333": "Judge Gray",
"#7c7b82": "Jumbo",
"#bdda57": "June Bud",
"#29ab87": "Jungle Green",
"#b4cfd3": "Jungle Mist",
"#6d9292": "Juniper",
"#eccdb9": "Just Right",
"#e8000d": "KU Crimson",
"#5e483e": "Kabul",
"#004620": "Kaitoke Green",
"#c6c8bd": "Kangaroo",
"#1e1609": "Karaka",
"#ffead4": "Karry",
"#507096": "Kashmir Blue",
"#4cbb17": "Kelly Green",
"#454936": "Kelp",
"#7c1c05": "Kenyan Copper",
"#3ab09e": "Keppel",
"#e8f48c": "Key Lime",
"#bfc921": "Key Lime Pie",
"#c3b091": "Khaki",
"#e1ead4": "Kidnapper",
"#240c02": "Kilamanjaro",
"#3a6a47": "Killarney",
"#736c9f": "Kimberly",
"#3e0480": "Kingfisher Daisy",
"#e79fc4": "Kobi",
"#6b4423": "Kobicha",
"#6e6d57": "Kokoda",
"#354230": "Kombu Green",
"#8f4b0e": "Korma",
"#ffbd5f": "Koromiko",
"#ffe772": "Kournikova",
"#886221": "Kumera",
"#368716": "La Palma",
"#b3c110": "La Rioja",
"#087830": "La Salle Green",
"#d6cadd": "Languid Lavender",
"#26619c": "Lapis Lazuli",
"#c6e610": "Las Palmas",
"#c8b568": "Laser",
"#749378": "Laurel",
"#a9ba9d": "Laurel Green",
"#cf1020": "Lava",
"#b57edc": "Lavender",
"#fff0f5": "Lavender Blush",
"#c4c3d0": "Lavender Gray",
"#9457eb": "Lavender Indigo",
"#ee82ee": "Lavender Magenta",
"#e6e6fa": "Lavender Mist",
"#fbaed2": "Lavender Pink",
"#967bb6": "Lavender Purple",
"#fba0e3": "Lavender Rose",
"#7cfc00": "Lawn Green",
"#967059": "Leather",
"#fff700": "Lemon",
"#fffacd": "Lemon Chiffon",
"#cca01d": "Lemon Curry",
"#ac9e22": "Lemon Ginger",
"#fdff00": "Lemon Glacier",
"#9b9e8f": "Lemon Grass",
"#e3ff00": "Lemon Lime",
"#f6eabe": "Lemon Meringue",
"#fff44f": "Lemon Yellow",
"#ba93d8": "Lenurple",
"#545aa7": "Liberty",
"#1a1110": "Licorice",
"#fdd5b1": "Light Apricot",
"#add8e6": "Light Blue",
"#fe2e2e": "Light Brilliant Red",
"#b5651d": "Light Brown",
"#e66771": "Light Carmine Pink",
"#88ace0": "Light Cobalt Blue",
"#f08080": "Light Coral",
"#93ccea": "Light Cornflower Blue",
"#f56991": "Light Crimson",
"#e0ffff": "Light Cyan",
"#ff5ccd": "Light Deep Pink",
"#c8ad7f": "Light French Beige",
"#f984ef": "Light Fuchsia Pink",
"#fafad2": "Light Goldenrod Yellow",
"#d3d3d3": "Light Gray",
"#cc99cc": "Light Grayish Magenta",
"#90ee90": "Light Green",
"#ffb3de": "Light Hot Pink",
"#f0e68c": "Light Khaki",
"#d39bcb": "Light Medium Orchid",
"#addfad": "Light Moss Green",
"#e6a8d7": "Light Orchid",
"#b19cd9": "Light Pastel Purple",
"#ffb6c1": "Light Pink",
"#ffa07a": "Light Salmon",
"#ff9999": "Light Salmon Pink",
"#20b2aa": "Light Sea Green",
"#87cefa": "Light Sky Blue",
"#778899": "Light Slate Gray",
"#b0c4de": "Light Steel Blue",
"#b38b6d": "Light Taupe",
"#afeeee": "Light Turquoise",
"#ffffe0": "Light Yellow",
"#fcc01e": "Lightning Yellow",
"#c8a2c8": "Lilac",
"#9874d3": "Lilac Bush",
"#ae98aa": "Lilac Luster",
"#c8aabf": "Lily",
"#e7f8ff": "Lily White",
"#76bd17": "Lima",
"#bfff00": "Lime",
"#32cd32": "Lime Green",
"#6f9d02": "Limeade",
"#747d63": "Limed Ash",
"#ac8a56": "Limed Oak",
"#394851": "Limed Spruce",
"#9dc209": "Limerick",
"#195905": "Lincoln Green",
"#faf0e6": "Linen",
"#d9e4f5": "Link Water",
"#ab0563": "Lipstick",
"#423921": "Lisbon Brown",
"#6ca0dc": "Little Boy Blue",
"#674c47": "Liver",
"#987456": "Liver Chestnut",
"#4d282e": "Livid Brown",
"#eef4de": "Loafer",
"#bdc9ce": "Loblolly",
"#2c8c84": "Lochinvar",
"#007ec7": "Lochmara",
"#a8af8e": "Locust",
"#242a1d": "Log Cabin",
"#aaa9cd": "Logan",
"#dfcfdb": "Lola",
"#bea6c3": "London Hue",
"#6d0101": "Lonestar",
"#863c3c": "Lotus",
"#460b41": "Loulou",
"#af9f1c": "Lucky",
"#1a1a68": "Lucky Point",
"#ffe4cd": "Lumber",
"#3c493a": "Lunar Green",
"#e62020": "Lust",
"#a7882c": "Luxor Gold",
"#697e9a": "Lynch",
"#18453b": "MSU Green",
"#d9f7ff": "Mabel",
"#ffbd88": "Macaroni And Cheese",
"#ffb97b": "Macaroni and Cheese",
"#b7f0be": "Madang",
"#09255d": "Madison",
"#3f3002": "Madras",
"#ca1f7b": "Magenta",
"#9f4576": "Magenta Haze",
"#cc338b": "Magenta Pink",
"#aaf0d1": "Magic Mint",
"#ff4466": "Magic Potion",
"#f8f4ff": "Magnolia",
"#c04000": "Mahogany",
"#b06608": "Mai Tai",
"#fbec5d": "Maize",
"#6050dc": "Majorelle Blue",
"#897d6d": "Makara",
"#444954": "Mako",
"#0bda51": "Malachite",
"#7dc8f7": "Malibu",
"#233418": "Mallard",
"#bdb2a1": "Malta",
"#8e8190": "Mamba",
"#979aaa": "Manatee",
"#ad781b": "Mandalay",
"#f37a48": "Mandarin",
"#e25465": "Mandy",
"#f2c3b2": "Mandys Pink",
"#ff8243": "Mango Tango",
"#f5c999": "Manhattan",
"#74c365": "Mantis",
"#8b9c90": "Mantle",
"#eeef78": "Manz",
"#880085": "Mardi Gras",
"#eaa221": "Marigold",
"#fbe870": "Marigold Yellow",
"#286acd": "Mariner",
"#800000": "Maroon",
"#520c17": "Maroon Oak",
"#0b0f08": "Marshland",
"#afa09e": "Martini",
"#363050": "Martinique",
"#f8db9d": "Marzipan",
"#403b38": "Masala",
"#1b659d": "Matisse",
"#b05d54": "Matrix",
"#4e3b41": "Matterhorn",
"#e0b0ff": "Mauve",
"#915f6d": "Mauve Taupe",
"#ef98aa": "Mauvelous",
"#d8c2d5": "Maverick",
"#47abcc": "Maximum Blue",
"#fafa37": "Maximum Yellow",
"#4c9141": "May Green",
"#73c2fb": "Maya Blue",
"#e5b73b": "Meat Brown",
"#66ddaa": "Medium Aquamarine",
"#0000cd": "Medium Blue",
"#e2062c": "Medium Candy Apple Red",
"#035096": "Medium Electric Blue",
"#1c352d": "Medium Jungle Green",
"#ba55d3": "Medium Orchid",
"#9370db": "Medium Purple",
"#bb3385": "Medium Red Violet",
"#aa4069": "Medium Ruby",
"#3cb371": "Medium Sea Green",
"#80daeb": "Medium Sky Blue",
"#7b68ee": "Medium Slate Blue",
"#c9dc87": "Medium Spring Bud",
"#00fa9a": "Medium Spring Green",
"#48d1cc": "Medium Turquoise",
"#d9603b": "Medium Vermilion",
"#e4c2d5": "Melanie",
"#300529": "Melanzane",
"#f8b878": "Mellow Apricot",
"#fdbcb4": "Melon",
"#c7c1ff": "Melrose",
"#e5e5e5": "Mercury",
"#f6f0e6": "Merino",
"#413c37": "Merlin",
"#831923": "Merlot",
"#ff00fd": "Metal Pink",
"#49371b": "Metallic Bronze",
"#71291d": "Metallic Copper",
"#d4af37": "Metallic Gold",
"#0a7e8c": "Metallic Seaweed",
"#9c7c38": "Metallic Sunburst",
"#d07d12": "Meteor",
"#3c1f76": "Meteorite",
"#e4007c": "Mexican Pink",
"#a72525": "Mexican Red",
"#5f5f6e": "Mid Gray",
"#702670": "Midnight",
"#191970": "Midnight Blue",
"#041004": "Midnight Moss",
"#2d2510": "Mikado",
"#ffc40c": "Mikado Yellow",
"#faffa4": "Milan",
"#b81104": "Milano Red",
"#fff6d4": "Milk Punch",
"#594433": "Millbrook",
"#f8fdd3": "Mimosa",
"#e3f988": "Mindaro",
"#323232": "Mine Shaft",
"#3f5d53": "Mineral Green",
"#36747d": "Ming",
"#f5e050": "Minion Yellow",
"#3f307f": "Minsk",
"#3eb489": "Mint",
"#f5fffa": "Mint Cream",
"#98ff98": "Mint Green",
"#f1eec1": "Mint Julep",
"#c4f4eb": "Mint Tulip",
"#161928": "Mirage",
"#d1d2dd": "Mischka",
"#c4c4bc": "Mist Gray",
"#bbb477": "Misty Moss",
"#ffe4e1": "Misty Rose",
"#7f7589": "Mobster",
"#6e1d14": "Moccaccino",
"#ffe4b5": "Moccasin",
"#782d19": "Mocha",
"#c04737": "Mojo",
"#ffa194": "Mona Lisa",
"#8b0723": "Monarch",
"#4a3c30": "Mondo",
"#b5a27f": "Mongoose",
"#8a8389": "Monsoon",
"#83d0c6": "Monte Carlo",
"#c7031e": "Monza",
"#7f76d3": "Moody Blue",
"#fcfeda": "Moon Glow",
"#dcddcc": "Moon Mist",
"#d6cef6": "Moon Raker",
"#73a9c2": "Moonstone Blue",
"#ae0c00": "Mordant Red",
"#9edee0": "Morning Glory",
"#441d00": "Morocco Brown",
"#504351": "Mortar",
"#036a6e": "Mosque",
"#8a9a5b": "Moss Green",
"#30ba8f": "Mountain Meadow",
"#959396": "Mountain Mist",
"#997a8d": "Mountbatten Pink",
"#b78e5c": "Muddy Waters",
"#aa8b5b": "Muesli",
"#306030": "Mughal Green",
"#c54b8c": "Mulberry",
"#5c0536": "Mulberry Wood",
"#8c472f": "Mule Fawn",
"#4e4562": "Mulled Wine",
"#828e84": "Mummys Tomb",
"#0093af": "Munsell Blue",
"#00a877": "Munsell Green",
"#9f00c5": "Munsell Purple",
"#f2003c": "Munsell Red",
"#efcc00": "Munsell Yellow",
"#ffdb58": "Mustard",
"#d69188": "My Pink",
"#ffb31f": "My Sin",
"#317873": "Myrtle Green",
"#d65282": "Mystic",
"#ad4379": "Mystic Maroon",
"#0087bd": "NCS Blue",
"#009f6b": "NCS Green",
"#c40233": "NCS Red",
"#f6adc6": "Nadeshiko Pink",
"#4b5d52": "Nandor",
"#aca494": "Napa",
"#2a8000": "Napier Green",
"#fada5e": "Naples Yellow",
"#edf9f1": "Narvik",
"#8b8680": "Natural Gray",
"#ffdead": "Navajo White",
"#000080": "Navy",
"#cbdbd6": "Nebula",
"#ffe2c5": "Negroni",
"#ffa343": "Neon Carrot",
"#fe4164": "Neon Fuchsia",
"#39ff14": "Neon Green",
"#8eabc1": "Nepal",
"#7cb7bb": "Neptune",
"#140600": "Nero",
"#646e75": "Nevada",
"#214fc6": "New Car",
"#f3d69d": "New Orleans",
"#d7837f": "New York Pink",
"#06a189": "Niagara",
"#727472": "Nickel",
"#1f120f": "Night Rider",
"#aa375a": "Night Shadz",
"#193751": "Nile Blue",
"#b7b1b1": "Nobel",
"#bab1a2": "Nomad",
"#a4dded": "Non Photo Blue",
"#059033": "North Texas Green",
"#a8bd9f": "Norway",
"#c59922": "Nugget",
"#81422c": "Nutmeg",
"#683600": "Nutmeg Wood Finish",
"#e9ffdb": "Nyanza",
"#feefce": "Oasis",
"#02866f": "Observatory",
"#4f42b5": "Ocean Blue",
"#0077be": "Ocean Boat Blue",
"#48bf91": "Ocean Green",
"#cc7722": "Ochre",
"#e6f8f3": "Off Green",
"#fef9e3": "Off Yellow",
"#fd5240": "Ogre Odor",
"#281e15": "Oil",
"#901e1e": "Old Brick",
"#43302e": "Old Burgundy",
"#724a2f": "Old Copper",
"#cfb53b": "Old Gold",
"#563c5c": "Old Heliotrope",
"#fdf5e6": "Old Lace",
"#796878": "Old Lavender",
"#867e36": "Old Moss Green",
"#c08081": "Old Rose",
"#848482": "Old Silver",
"#808000": "Olive",
"#6b8e23": "Olive Drab",
"#3c341f": "Olive Drab Seven",
"#b5b35c": "Olive Green",
"#8b8470": "Olive Haze",
"#716e10": "Olivetone",
"#9ab973": "Olivine",
"#cdf4ff": "Onahau",
"#2f270e": "Onion",
"#353839": "Onyx",
"#a9c6c2": "Opal",
"#b784a7": "Opera Mauve",
"#8e6f70": "Opium",
"#377475": "Oracle",
"#ff7f00": "Orange",
"#ff9f00": "Orange Peel",
"#ff4500": "Orange Red",
"#c45719": "Orange Roughy",
"#fa5b3d": "Orange Soda",
"#fefced": "Orange White",
"#f8d568": "Orange Yellow",
"#da70d6": "Orchid",
"#f2bdcd": "Orchid Pink",
"#fffdf3": "Orchid White",
"#9b4703": "Oregon",
"#6c2e1f": "Organ",
"#015e85": "Orient",
"#c69191": "Oriental Pink",
"#f3fbd4": "Orinoco",
"#fb4f14": "Orioles Orange",
"#878d91": "Oslo Gray",
"#e9f8ed": "Ottoman",
"#414a4c": "Outer Space",
"#ff6e4a": "Outrageous Orange",
"#002147": "Oxford Blue",
"#779e86": "Oxley",
"#dafaff": "Oyster Bay",
"#e9cecd": "Oyster Pink",
"#a65529": "Paarl",
"#776f61": "Pablo",
"#1ca9c9": "Pacific Blue",
"#778120": "Pacifika",
"#411f10": "Paco",
"#ade6c4": "Padua",
"#006600": "Pakistan Green",
"#273be2": "Palatinate Blue",
"#682860": "Palatinate Purple",
"#987654": "Pale Brown",
"#ffff99": "Pale Canary",
"#af4035": "Pale Carmine",
"#9bc4e2": "Pale Cerulean",
"#ddadaf": "Pale Chestnut",
"#da8a67": "Pale Copper",
"#abcdef": "Pale Cornflower Blue",
"#87d3f8": "Pale Cyan",
"#e6be8a": "Pale Gold",
"#eee8aa": "Pale Goldenrod",
"#98fb98": "Pale Green",
"#dcd0ff": "Pale Lavender",
"#c0d3b9": "Pale Leaf",
"#f984e5": "Pale Magenta",
"#ff99cc": "Pale Magenta Pink",
"#988d77": "Pale Oyster",
"#fadadd": "Pale Pink",
"#dda0dd": "Pale Plum",
"#fdfeb8": "Pale Prim",
"#db7093": "Pale Red Violet",
"#96ded1": "Pale Robin Egg Blue",
"#ffe1f2": "Pale Rose",
"#c9c0bb": "Pale Silver",
"#6e7783": "Pale Sky",
"#c3bfc1": "Pale Slate",
"#ecebbd": "Pale Spring Bud",
"#bc987e": "Pale Taupe",
"#cc99ff": "Pale Violet",
"#09230f": "Palm Green",
"#19330e": "Palm Leaf",
"#f4f2ee": "Pampas",
"#eaf6ee": "Panache",
"#edcdab": "Pancho",
"#78184a": "Pansy Purple",
"#0018a8": "Pantone Blue",
"#00ad43": "Pantone Green",
"#d0417e": "Pantone Magenta",
"#ff5800": "Pantone Orange",
"#d74894": "Pantone Pink",
"#fedf00": "Pantone Yellow",
"#009b7d": "Paolo Veronese Green",
"#ffefd5": "Papaya Whip",
"#8d0226": "Paprika",
"#e63e62": "Paradise Pink",
"#317d82": "Paradiso",
"#f1e9d2": "Parchment",
"#fff46e": "Paris Daisy",
"#26056a": "Paris M",
"#cadcd4": "Paris White",
"#134f19": "Parsley",
"#aec6cf": "Pastel Blue",
"#836953": "Pastel Brown",
"#cfcfc4": "Pastel Gray",
"#77dd77": "Pastel Green",
"#f49ac2": "Pastel Magenta",
"#ffb347": "Pastel Orange",
"#dea5a4": "Pastel Pink",
"#b39eb5": "Pastel Purple",
"#ff6961": "Pastel Red",
"#cb99c9": "Pastel Violet",
"#fdfd96": "Pastel Yellow",
"#639a8f": "Patina",
"#def5ff": "Pattens Blue",
"#260368": "Paua",
"#d7c498": "Pavlova",
"#536878": "Paynes Grey",
"#ffcba4": "Peach",
"#fff0db": "Peach Cream",
"#ffcc99": "Peach Orange",
"#ffdab9": "Peach Puff",
"#ffdcd6": "Peach Schnapps",
"#fadfad": "Peach Yellow",
"#782f16": "Peanut",
"#d1e231": "Pear",
"#eae0c8": "Pearl",
"#88d8c0": "Pearl Aqua",
"#e8e0d5": "Pearl Bush",
"#fcf4dc": "Pearl Lusta",
"#32c6a6": "Pearl Mystic Turquoise",
"#b768a2": "Pearly Purple",
"#716b56": "Peat",
"#3eabbf": "Pelorous",
"#e3f5e1": "Peppermint",
"#a9bef2": "Perano",
"#d0bef8": "Perfume",
"#e6e200": "Peridot",
"#e1e6d6": "Periglacial Blue",
"#ccccff": "Periwinkle",
"#c3cde6": "Periwinkle Gray",
"#e12c2c": "Permanent Geranium Lake",
"#1c39bb": "Persian Blue",
"#00a693": "Persian Green",
"#32127a": "Persian Indigo",
"#d99058": "Persian Orange",
"#f77fbe": "Persian Pink",
"#701c1c": "Persian Plum",
"#cc3333": "Persian Red",
"#fe28a2": "Persian Rose",
"#ec5800": "Persimmon",
"#cd853f": "Peru",
"#7f3a02": "Peru Tan",
"#7c7631": "Pesto",
"#db9690": "Petite Orchid",
"#96a8a1": "Pewter",
"#8ba8b7": "Pewter Blue",
"#a3807b": "Pharlap",
"#000f89": "Phthalo Blue",
"#123524": "Phthalo Green",
"#fff39d": "Picasso",
"#6e4826": "Pickled Bean",
"#314459": "Pickled Bluewood",
"#45b1e8": "Picton Blue",
"#c30b4e": "Pictorial Carmine",
"#fdd7e4": "Pig Pink",
"#afbdd9": "Pigeon Post",
"#fddde6": "Piggy Pink",
"#333399": "Pigment Blue",
"#00a550": "Pigment Green",
"#ed1c24": "Pigment Red",
"#6d5e54": "Pine Cone",
"#c7cd90": "Pine Glade",
"#01796f": "Pine Green",
"#171f04": "Pine Tree",
"#ffc0cb": "Pink",
"#fc74fd": "Pink Flamingo",
"#e1c0c8": "Pink Flare",
"#ffddf4": "Pink Lace",
"#fff1d8": "Pink Lady",
"#d8b2d1": "Pink Lavender",
"#ff9966": "Pink Orange",
"#e7accf": "Pink Pearl",
"#980036": "Pink Raspberry",
"#f78fa7": "Pink Sherbet",
"#beb5b7": "Pink Swan",
"#c96323": "Piper",
"#fef4cc": "Pipi",
"#ffe1df": "Pippin",
"#ba7f03": "Pirate Gold",
"#93c572": "Pistachio",
"#c0d8b6": "Pixie Green",
"#391285": "Pixie Powder",
"#ff9000": "Pizazz",
"#c99415": "Pizza",
"#27504b": "Plantation",
"#e5e4e2": "Platinum",
"#8e4585": "Plum",
"#5946b2": "Plump Purple",
"#8f021c": "Pohutukawa",
"#e5f9f6": "Polar",
"#5da493": "Polished Pine",
"#8da8cc": "Polo Blue",
"#f34723": "Pomegranate",
"#660045": "Pompadour",
"#be4f62": "Popstar",
"#eff2f3": "Porcelain",
"#eaae69": "Porsche",
"#251f4f": "Port Gore",
"#ffffb4": "Portafino",
"#8b9fee": "Portage",
"#f9e663": "Portica",
"#ff5a36": "Portland Orange",
"#f5e7e2": "Pot Pourri",
"#8c5738": "Potters Clay",
"#bcc9c2": "Powder Ash",
"#b0e0e6": "Powder Blue",
"#9a3820": "Prairie Sand",
"#d0c0e5": "Prelude",
"#f0e2ec": "Prim",
"#edea99": "Primrose",
"#ff85cf": "Princess Perfume",
"#f58025": "Princeton Orange",
"#00b7eb": "Process Cyan",
"#ff0090": "Process Magenta",
"#fef5f1": "Provincial Pink",
"#003153": "Prussian Blue",
"#df00ff": "Psychedelic Purple",
"#cc8899": "Puce",
"#7d2c14": "Pueblo",
"#3fc1aa": "Puerto Rico",
"#644117": "Pullman Brown",
"#3b331c": "Pullman Green",
"#c2cac4": "Pumice",
"#ff7518": "Pumpkin",
"#b1610b": "Pumpkin Skin",
"#dc4333": "Punch",
"#4d3d14": "Punga",
"#800080": "Purple",
"#69359c": "Purple Heart",
"#9678b6": "Purple Mountain Majesty",
"#4e5180": "Purple Navy",
"#fe4eda": "Purple Pizzazz",
"#9c51b6": "Purple Plum",
"#50404d": "Purple Taupe",
"#9a4eae": "Purpureus",
"#e7cd8c": "Putty",
"#fffdf4": "Quarter Pearl Lusta",
"#f7f2e1": "Quarter Spanish White",
"#51484f": "Quartz",
"#436b95": "Queen Blue",
"#e8ccd7": "Queen Pink",
"#a6a6a6": "Quick Silver",
"#bd978e": "Quicksand",
"#d6d6d1": "Quill Gray",
"#8e3a59": "Quinacridone Magenta",
"#623f2d": "Quincy",
"#0247fe": "RYB Blue",
"#66b032": "RYB Green",
"#fb9902": "RYB Orange",
"#fe2712": "RYB Red",
"#8601af": "RYB Violet",
"#fefe33": "RYB Yellow",
"#0c1911": "Racing Green",
"#ff355e": "Radical Red",
"#eadab8": "Raffia",
"#b9c8ac": "Rainee",
"#242124": "Raisin Black",
"#fbab60": "Rajah",
"#2e3222": "Rangitoto",
"#1c1e13": "Rangoon Green",
"#e30b5d": "Raspberry",
"#e25098": "Raspberry Pink",
"#727b89": "Raven",
"#d68a59": "Raw Sienna",
"#826644": "Raw Umber",
"#ff33cc": "Razzle Dazzle Rose",
"#e3256b": "Razzmatazz",
"#8d4e85": "Razzmic Berry",
"#663399": "Rebecca Purple",
"#3c1206": "Rebel",
"#ff0000": "Red",
"#7b3801": "Red Beech",
"#8e0000": "Red Berry",
"#da6a41": "Red Damask",
"#860111": "Red Devil",
"#ff5349": "Red Orange",
"#6e0902": "Red Oxide",
"#e40078": "Red Purple",
"#ed0a3f": "Red Ribbon",
"#80341f": "Red Robin",
"#fd3a4a": "Red Salsa",
"#d05f04": "Red Stage",
"#c71585": "Red Violet",
"#a45a52": "Redwood",
"#c9ffa2": "Reef",
"#9f821c": "Reef Gold",
"#013f6a": "Regal Blue",
"#522d80": "Regalia",
"#86949f": "Regent Gray",
"#aad6e6": "Regent St Blue",
"#feebf3": "Remy",
"#a86515": "Reno Sand",
"#002387": "Resolution Blue",
"#2c1632": "Revolver",
"#2e3f62": "Rhino",
"#777696": "Rhythm",
"#fffef0": "Rice Cake",
"#eeffe2": "Rice Flower",
"#004040": "Rich Black",
"#f1a7fe": "Rich Brilliant Lavender",
"#d70040": "Rich Carmine",
"#0892d0": "Rich Electric Blue",
"#a85307": "Rich Gold",
"#a76bcf": "Rich Lavender",
"#b666d2": "Rich Lilac",
"#b03060": "Rich Maroon",
"#444c38": "Rifle Green",
"#bbd009": "Rio Grande",
"#f4d81c": "Ripe Lemon",
"#410056": "Ripe Plum",
"#8be6d8": "Riptide",
"#434c59": "River Bed",
"#704241": "Roast Coffee",
"#eac674": "Rob Roy",
"#00cccc": "Robin Egg Blue",
"#4d3833": "Rock",
"#9eb1cd": "Rock Blue",
"#ba450c": "Rock Spray",
"#8a7f80": "Rocket Metallic",
"#c9b29b": "Rodeo Dust",
"#747d83": "Rolling Stone",
"#de6360": "Roman",
"#795d4c": "Roman Coffee",
"#838996": "Roman Silver",
"#fffefd": "Romance",
"#ffd2b7": "Romantic",
"#ecc54e": "Ronchi",
"#a62f20": "Roof Terracotta",
"#8e4d1e": "Rope",
"#ff007f": "Rose",
"#f9429e": "Rose Bonbon",
"#fbb2a3": "Rose Bud",
"#800b47": "Rose Bud Cherry",
"#9e5e6f": "Rose Dust",
"#674846": "Rose Ebony",
"#e7bcb4": "Rose Fog",
"#b76e79": "Rose Gold",
"#ff66cc": "Rose Pink",
"#c21e56": "Rose Red",
"#905d5d": "Rose Taupe",
"#ab4e52": "Rose Vale",
"#fff6f5": "Rose White",
"#bf5500": "Rose of Sharon",
"#65000b": "Rosewood",
"#d40000": "Rosso Corsa",
"#bc8f8f": "Rosy Brown",
"#c6a84b": "Roti",
"#a23b6c": "Rouge",
"#5d8aa8": "Royal Air Force Blue",
"#0038a8": "Royal Azure",
"#4169e1": "Royal Blue",
"#ca2c92": "Royal Fuchsia",
"#ab3472": "Royal Heath",
"#7851a9": "Royal Purple",
"#ce4676": "Ruber",
"#d10056": "Rubine Red",
"#e0115f": "Ruby",
"#9b111e": "Ruby Red",
"#ff0028": "Ruddy",
"#bb6528": "Ruddy Brown",
"#e18e96": "Ruddy Pink",
"#a81c07": "Rufous",
"#796989": "Rum",
"#f9f8e4": "Rum Swizzle",
"#80461b": "Russet",
"#755a57": "Russett",
"#679267": "Russian Green",
"#32174d": "Russian Violet",
"#b7410e": "Rust",
"#480404": "Rustic Red",
"#86560a": "Rusty Nail",
"#da2c43": "Rusty Red",
"#ff7e00": "SAE ECE Amber",
"#043927": "Sacramento State Green",
"#4c3024": "Saddle",
"#8b4513": "Saddle Brown",
"#ff7800": "Safety Orange",
"#eed202": "Safety Yellow",
"#f4c430": "Saffron",
"#f9bf58": "Saffron Mango",
"#bcb88a": "Sage",
"#b7a214": "Sahara",
"#f1e788": "Sahara Sand",
"#b8e0f9": "Sail",
"#097f4b": "Salem",
"#fa8072": "Salmon",
"#ff91a4": "Salmon Pink",
"#fedb8d": "Salomie",
"#685e6e": "Salt Box",
"#f1f7f2": "Saltpan",
"#3a2010": "Sambuca",
"#0b6207": "San Felix",
"#304b6a": "San Juan",
"#456cac": "San Marino",
"#967117": "Sand Dune",
"#aa8d6f": "Sandal",
"#ab917a": "Sandrift",
"#796d62": "Sandstone",
"#ecd540": "Sandstorm",
"#f5e7a2": "Sandwisp",
"#ffeac8": "Sandy Beach",
"#f4a460": "Sandy Brown",
"#92000a": "Sangria",
"#8d3d38": "Sanguine Brown",
"#b16d52": "Santa Fe",
"#9fa0b1": "Santas Gray",
"#507d2a": "Sap Green",
"#ded4a4": "Sapling",
"#0f52ba": "Sapphire",
"#0067a5": "Sapphire Blue",
"#555b10": "Saratoga",
"#ff4681": "Sasquatch Socks",
"#e6e4d4": "Satin Linen",
"#cba135": "Satin Sheen Gold",
"#fff5f3": "Sauvignon",
"#fff4e0": "Sazerac",
"#675fa6": "Scampi",
"#cffaf4": "Scandal",
"#ff2400": "Scarlet",
"#431560": "Scarlet Gum",
"#950015": "Scarlett",
"#585562": "Scarpa Flow",
"#a9b497": "Schist",
"#ffd800": "School Bus Yellow",
"#8b847e": "Schooner",
"#0066cc": "Science Blue",
"#2ebfd4": "Scooter",
"#695f62": "Scorpion",
"#fffbdc": "Scotch Mist",
"#66ff66": "Screamin Green",
"#006994": "Sea Blue",
"#fba129": "Sea Buckthorn",
"#2e8b57": "Sea Green",
"#c5dbca": "Sea Mist",
"#78a39c": "Sea Nymph",
"#ed989e": "Sea Pink",
"#4bc7cf": "Sea Serpent",
"#80ccea": "Seagull",
"#59260b": "Seal Brown",
"#731e8f": "Seance",
"#fff5ee": "Seashell",
"#1b2f11": "Seaweed",
"#f0eefd": "Selago",
"#ffba00": "Selective Yellow",
"#704214": "Sepia",
"#2b0202": "Sepia Black",
"#9e5b40": "Sepia Skin",
"#fff4e8": "Serenade",
"#8a795d": "Shadow",
"#778ba5": "Shadow Blue",
"#9ac2b8": "Shadow Green",
"#aaa5a9": "Shady Lady",
"#4eabd1": "Shakespeare",
"#fbffba": "Shalimar",
"#ffcff1": "Shampoo",
"#33cc99": "Shamrock",
"#009e60": "Shamrock Green",
"#25272c": "Shark",
"#8fd400": "Sheen Green",
"#004950": "Sherpa Blue",
"#02402c": "Sherwood Green",
"#e8b9b3": "Shilo",
"#d98695": "Shimmering Blush",
"#6b4e31": "Shingle Fawn",
"#5fa778": "Shiny Shamrock",
"#788bba": "Ship Cove",
"#3e3a44": "Ship Gray",
"#b20931": "Shiraz",
"#e292c0": "Shocking",
"#fc0fc0": "Shocking Pink",
"#5f6672": "Shuttle Gray",
"#646a54": "Siam",
"#f3e7bb": "Sidecar",
"#882d17": "Sienna",
"#bdb1a8": "Silk",
"#c0c0c0": "Silver",
"#acacac": "Silver Chalice",
"#5d89ba": "Silver Lake Blue",
"#c4aead": "Silver Pink",
"#bfc1c2": "Silver Sand",
"#66b58f": "Silver Tree",
"#9fd7d3": "Sinbad",
"#cb410b": "Sinopia",
"#7a013a": "Siren",
"#718080": "Sirocco",
"#d3cbba": "Sisal",
"#ff3855": "Sizzling Red",
"#ffdb00": "Sizzling Sunrise",
"#cae6da": "Skeptic",
"#007474": "Skobeloff",
"#87ceeb": "Sky Blue",
"#cf71af": "Sky Magenta",
"#6a5acd": "Slate Blue",
"#708090": "Slate Gray",
"#299617": "Slimy Green",
"#003399": "Smalt",
"#51808f": "Smalt Blue",
"#ff6d3a": "Smashed Pumpkin",
"#c84186": "Smitten",
"#738276": "Smoke",
"#832a0d": "Smokey Topaz",
"#605b73": "Smoky",
"#100c08": "Smoky Black",
"#933d41": "Smoky Topaz",
"#fffafa": "Snow",
"#f7faf7": "Snow Drift",
"#e4ffd1": "Snow Flurry",
"#d6ffdb": "Snowy Mint",
"#e2d8ed": "Snuff",
"#cec8ef": "Soap",
"#fffbf9": "Soapstone",
"#d1c6b4": "Soft Amber",
"#f5edef": "Soft Peach",
"#893843": "Solid Pink",
"#fef8e2": "Solitaire",
"#eaf6ff": "Solitude",
"#757575": "Sonic Silver",
"#fd7c07": "Sorbus",
"#ceb98f": "Sorrell Brown",
"#6a6051": "Soya Bean",
"#1d2951": "Space Cadet",
"#807532": "Spanish Bistre",
"#0070b8": "Spanish Blue",
"#d10047": "Spanish Carmine",
"#e51a4c": "Spanish Crimson",
"#989898": "Spanish Gray",
"#009150": "Spanish Green",
"#e86100": "Spanish Orange",
"#f7bfbe": "Spanish Pink",
"#e60026": "Spanish Red",
"#00aae4": "Spanish Sky Blue",
"#4c2882": "Spanish Violet",
"#007f5c": "Spanish Viridian",
"#9e1316": "Spartan Crimson",
"#2f5a57": "Spectra",
"#6a442e": "Spice",
"#8b5f4d": "Spicy Mix",
"#74640d": "Spicy Mustard",
"#816e71": "Spicy Pink",
"#b6d1ea": "Spindle",
"#0fc0fc": "Spiro Disco Ball",
"#79deec": "Spray",
"#a7fc00": "Spring Bud",
"#87ff2a": "Spring Frost",
"#00ff7f": "Spring Green",
"#578363": "Spring Leaves",
"#accbb1": "Spring Rain",
"#f6ffdc": "Spring Sun",
"#f8f6f1": "Spring Wood",
"#c1d7b0": "Sprout",
"#aaabb7": "Spun Pearl",
"#8f8176": "Squirrel",
"#23297a": "St Patricks Blue",
"#2d569b": "St Tropaz",
"#8a8f8a": "Stack",
"#007bb8": "Star Command Blue",
"#9f9f9c": "Star Dust",
"#e5d7bd": "Stark White",
"#ecf245": "Starship",
"#4682b4": "Steel Blue",
"#262335": "Steel Gray",
"#cc33cc": "Steel Pink",
"#5f8a8b": "Steel Teal",
"#9c3336": "Stiletto",
"#928573": "Stonewall",
"#646463": "Storm Dust",
"#717486": "Storm Gray",
"#4f666a": "Stormcloud",
"#000741": "Stratos",
"#e4d96f": "Straw",
"#fc5a8d": "Strawberry",
"#956387": "Strikemaster",
"#325d52": "Stromboli",
"#714ab2": "Studio",
"#bac7c9": "Submarine",
"#f9fff6": "Sugar Cane",
"#914e75": "Sugar Plum",
"#c1f07c": "Sulu",
"#96bbab": "Summer Green",
"#fbac13": "Sun",
"#ff404c": "Sunburnt Cyclops",
"#c9b35b": "Sundance",
"#ffb1b3": "Sundown",
"#e4d422": "Sunflower",
"#e16865": "Sunglo",
"#ffcc33": "Sunglow",
"#f2f27a": "Sunny",
"#e3ab57": "Sunray",
"#fad6a5": "Sunset",
"#fd5e53": "Sunset Orange",
"#ff9e2c": "Sunshade",
"#cf6ba9": "Super Pink",
"#ffc901": "Supernova",
"#bbd7c1": "Surf",
"#cfe5d2": "Surf Crest",
"#0c7a79": "Surfie Green",
"#87ab39": "Sushi",
"#888387": "Suva Gray",
"#001b1c": "Swamp",
"#acb78e": "Swamp Green",
"#dcf0ea": "Swans Down",
"#a83731": "Sweet Brown",
"#fbea8c": "Sweet Corn",
"#fd9fa2": "Sweet Pink",
"#d3cdc5": "Swirl",
"#ddd6d5": "Swiss Coffee",
"#908d39": "Sycamore",
"#a02712": "Tabasco",
"#edb381": "Tacao",
"#d6c562": "Tacha",
"#e97c07": "Tahiti Gold",
"#eef0c8": "Tahuna Sands",
"#b32d29": "Tall Poppy",
"#a8a589": "Tallow",
"#991613": "Tamarillo",
"#341515": "Tamarind",
"#d2b48c": "Tan",
"#fa9d5a": "Tan Hide",
"#d9dcc1": "Tana",
"#03163c": "Tangaroa",
"#f94d00": "Tangelo",
"#f28500": "Tangerine",
"#ffcc00": "Tangerine Yellow",
"#ed7a1c": "Tango",
"#e4717a": "Tango Pink",
"#7b7874": "Tapa",
"#b05e81": "Tapestry",
"#e1f6e8": "Tara",
"#073a50": "Tarawera",
"#fb4d46": "Tart Orange",
"#cfdccf": "Tasman",
"#483c32": "Taupe",
"#8b8589": "Taupe Gray",
"#692545": "Tawny Port",
"#1e433c": "Te Papa Green",
"#c1bab0": "Tea",
"#d0f0c0": "Tea Green",
"#f4c2c2": "Tea Rose",
"#b19461": "Teak",
"#008080": "Teal",
"#367588": "Teal Blue",
"#99e6b3": "Teal Deer",
"#00827f": "Teal Green",
"#cf3476": "Telemagenta",
"#3b000b": "Temptress",
"#cd5700": "Tenne",
"#ffe6c7": "Tequila",
"#e2725b": "Terra Cotta",
"#f8f99c": "Texas",
"#ffb555": "Texas Rose",
"#b69d98": "Thatch",
"#403d19": "Thatch Green",
"#d8bfd8": "Thistle",
"#cccaa8": "Thistle Green",
"#de6fa1": "Thulian Pink",
"#33292f": "Thunder",
"#c02b18": "Thunderbird",
"#c1440e": "Tia Maria",
"#c3d1d1": "Tiara",
"#063537": "Tiber",
"#fc89ac": "Tickle Me Pink",
"#f1ffad": "Tidal",
"#bfb8b0": "Tide",
"#0abab5": "Tiffany Blue",
"#e08d3c": "Tigers Eye",
"#16322c": "Timber Green",
"#dbd7d2": "Timberwolf",
"#f0eeff": "Titan White",
"#eee600": "Titanium Yellow",
"#9a6e61": "Toast",
"#715d47": "Tobacco Brown",
"#3a0020": "Toledo",
"#1b0245": "Tolopea",
"#3f583b": "Tom Thumb",
"#ff6347": "Tomato",
"#e79f8c": "Tonys Pink",
"#746cc0": "Toolbox",
"#ffc87c": "Topaz",
"#0f2d9e": "Torea Bay",
"#1450aa": "Tory Blue",
"#8d3f3f": "Tosca",
"#991b07": "Totem Pole",
"#a9bdbf": "Tower Gray",
"#fd0e35": "Tractor Red",
"#5fb3ac": "Tradewind",
"#e6ffff": "Tranquil",
"#fffde8": "Travertine",
"#fc9c1d": "Tree Poppy",
"#3b2820": "Treehouse",
"#7c881a": "Trendy Green",
"#8c6495": "Trendy Pink",
"#e64e03": "Trinidad",
"#c3ddf9": "Tropical Blue",
"#00755e": "Tropical Rain Forest",
"#cda4de": "Tropical Violet",
"#4a4e5a": "Trout",
"#0073cf": "True Blue",
"#8a73d6": "True V",
"#363534": "Tuatara",
"#ffddcd": "Tuft Bush",
"#417dc1": "Tufts Blue",
"#ff878d": "Tulip",
"#eab33b": "Tulip Tree",
"#deaa88": "Tumbleweed",
"#353542": "Tuna",
"#4a4244": "Tundora",
"#fae600": "Turbo",
"#b57281": "Turkish Rose",
"#cabb48": "Turmeric",
"#40e0d0": "Turquoise",
"#00ffef": "Turquoise Blue",
"#a0d6b4": "Turquoise Green",
"#2a380b": "Turtle Green",
"#7c4848": "Tuscan Red",
"#a67b5b": "Tuscan Tan",
"#c09999": "Tuscany",
"#eef3c3": "Tusk",
"#c5994b": "Tussock",
"#fff1f9": "Tutu",
"#e4cfde": "Twilight",
"#eefdff": "Twilight Blue",
"#8a496b": "Twilight Lavender",
"#c2955d": "Twine",
"#66023c": "Tyrian Purple",
"#0033aa": "UA Blue",
"#d9004c": "UA Red",
"#536895": "UCLA Blue",
"#ffb300": "UCLA Gold",
"#3cd070": "UFO Green",
"#014421": "UP Forest Green",
"#7b1113": "UP Maroon",
"#004f98": "USAFA Blue",
"#8878c3": "Ube",
"#ff6fff": "Ultra Pink",
"#3f00ff": "Ultramarine",
"#4166f5": "Ultramarine Blue",
"#635147": "Umber",
"#ffddca": "Unbleached Silk",
"#f9e6f4": "Underage Pink",
"#5b92e5": "United Nations Blue",
"#b78727": "University Of California Gold",
"#f77f00": "University Of Tennessee Orange",
"#ffff66": "Unmellow Yellow",
"#ae2029": "Upsdell Red",
"#e1ad21": "Urobilin",
"#d3003f": "Utah Crimson",
"#d84437": "Valencia",
"#350e42": "Valentino",
"#2b194f": "Valhalla",
"#49170c": "Van Cleef",
"#664228": "Van Dyke Brown",
"#f3e5ab": "Vanilla",
"#f38fa9": "Vanilla Ice",
"#fff6df": "Varden",
"#c5b358": "Vegas Gold",
"#c80815": "Venetian Red",
"#055989": "Venice Blue",
"#928590": "Venus",
"#43b3ae": "Verdigris",
"#495400": "Verdun Green",
"#d9381e": "Vermilion",
"#a020f0": "Veronica",
"#74bbfb": "Very Light Azure",
"#6666ff": "Very Light Blue",
"#64e986": "Very Light Malachite Green",
"#ffb077": "Very Light Tangelo",
"#ffdfbf": "Very Pale Orange",
"#ffffbf": "Very Pale Yellow",
"#b14a0b": "Vesuvius",
"#534491": "Victoria",
"#549019": "Vida Loca",
"#64ccdb": "Viking",
"#983d61": "Vin Rouge",
"#cb8fa9": "Viola",
"#290c5e": "Violent Violet",
"#7f00ff": "Violet",
"#324ab2": "Violet Blue",
"#991199": "Violet Eggplant",
"#f75394": "Violet Red",
"#40826d": "Viridian",
"#009698": "Viridian Green",
"#ffefa1": "Vis Vis",
"#7c9ed9": "Vista Blue",
"#fcf8f7": "Vista White",
"#cc9900": "Vivid Amber",
"#922724": "Vivid Auburn",
"#9f1d35": "Vivid Burgundy",
"#da1d81": "Vivid Cerise",
"#00aaee": "Vivid Cerulean",
"#cc0033": "Vivid Crimson",
"#ff9900": "Vivid Gamboge",
"#a6d608": "Vivid Lime Green",
"#00cc33": "Vivid Malachite",
"#b80ce3": "Vivid Mulberry",
"#ff5f00": "Vivid Orange",
"#ffa000": "Vivid Orange Peel",
"#cc00ff": "Vivid Orchid",
"#ff006c": "Vivid Raspberry",
"#f70d1a": "Vivid Red",
"#df6124": "Vivid Red Tangelo",
"#00ccff": "Vivid Sky Blue",
"#f07427": "Vivid Tangelo",
"#ffa089": "Vivid Tangerine",
"#e56024": "Vivid Vermilion",
"#9f00ff": "Vivid Violet",
"#ffe302": "Vivid Yellow",
"#ceff00": "Volt",
"#533455": "Voodoo",
"#10121d": "Vulcan",
"#decbc6": "Wafer",
"#5a6e9c": "Waikawa Gray",
"#363c0d": "Waiouru",
"#773f1a": "Walnut",
"#004242": "Warm Black",
"#788a25": "Wasabi",
"#a1e9de": "Water Leaf",
"#056f57": "Watercourse",
"#7b7c94": "Waterloo ",
"#a4f4f9": "Waterspout",
"#dcd747": "Wattle",
"#ffddcf": "Watusi",
"#ffc0a8": "Wax Flower",
"#f7dbe6": "We Peep",
"#7fff00": "Web Chartreuse",
"#ffa500": "Web Orange",
"#4e7f9e": "Wedgewood",
"#7c98ab": "Weldon Blue",
"#b43332": "Well Read",
"#645452": "Wenge",
"#625119": "West Coast",
"#ff910f": "West Side",
"#dcd9d2": "Westar",
"#f19bab": "Wewak",
"#f5deb3": "Wheat",
"#f3edcf": "Wheatfield",
"#d59a6f": "Whiskey",
"#f7f5fa": "Whisper",
"#ffffff": "White",
"#ddf9f1": "White Ice",
"#f8f7fc": "White Lilac",
"#f8f0e8": "White Linen",
"#fef8ff": "White Pointer",
"#eae8d4": "White Rock",
"#f5f5f5": "White Smoke",
"#a2add0": "Wild Blue Yonder",
"#d470a2": "Wild Orchid",
"#ece090": "Wild Rice",
"#f4f4f4": "Wild Sand",
"#ff43a4": "Wild Strawberry",
"#fc6c85": "Wild Watermelon",
"#b9c46a": "Wild Willow",
"#3a686c": "William",
"#dfecda": "Willow Brook",
"#65745d": "Willow Grove",
"#fd5800": "Willpower Orange",
"#3c0878": "Windsor",
"#a75502": "Windsor Tan",
"#722f37": "Wine",
"#591d35": "Wine Berry",
"#673147": "Wine Dregs",
"#d5d195": "Winter Hazel",
"#ff007c": "Winter Sky",
"#a0e6ff": "Winter Wizard",
"#56887d": "Wintergreen Dream",
"#fef4f8": "Wisp Pink",
"#c9a0dc": "Wisteria",
"#a4a6d3": "Wistful",
"#fffc99": "Witch Haze",
"#261105": "Wood Bark",
"#4d5328": "Woodland",
"#302a0f": "Woodrush",
"#0c0d0f": "Woodsmoke",
"#483131": "Woody Brown",
"#006400": "X11 Dark Green",
"#bebebe": "X11 Gray",
"#738678": "Xanadu",
"#0f4d92": "Yale Blue",
"#1c2841": "Yankees Blue",
"#ffff00": "Yellow",
"#9acd32": "Yellow Green",
"#716338": "Yellow Metal",
"#ffae42": "Yellow Orange",
"#fff000": "Yellow Rose",
"#fea904": "Yellow Sea",
"#ffc3c0": "Your Pink",
"#7b6608": "Yukon Gold",
"#cec291": "Yuma",
"#0014a8": "Zaffre",
"#685558": "Zambezi",
"#daecd6": "Zanah",
"#e5841b": "Zest",
"#292319": "Zeus",
"#bfdbe2": "Ziggurat",
"#ebc2af": "Zinnwaldite",
"#2c1608": "Zinnwaldite Brown",
"#f4f8ff": "Zircon",
"#e4d69b": "Zombie",
"#39a78e": "Zomp",
"#a59b91": "Zorba",
"#044022": "Zuccini",
"#edf6ff": "Zumthor"
}
    
    
    Color = namedtuple("Color", "red, green, blue")
    colors = {}  # dict of colors

    # Color Contants
    ALICEBLUE = Color(240, 248, 255)
    ANTIQUEWHITE = Color(250, 235, 215)
    ANTIQUEWHITE1 = Color(255, 239, 219)
    ANTIQUEWHITE2 = Color(238, 223, 204)
    ANTIQUEWHITE3 = Color(205, 192, 176)
    ANTIQUEWHITE4 = Color(139, 131, 120)
    AQUA = Color(0, 255, 255)
    AQUAMARINE1 = Color(127, 255, 212)
    AQUAMARINE2 = Color(118, 238, 198)
    AQUAMARINE3 = Color(102, 205, 170)
    AQUAMARINE4 = Color(69, 139, 116)
    AZURE1 = Color(240, 255, 255)
    AZURE2 = Color(224, 238, 238)
    AZURE3 = Color(193, 205, 205)
    AZURE4 = Color(131, 139, 139)
    BANANA = Color(227, 207, 87)
    BEIGE = Color(245, 245, 220)
    BISQUE1 = Color(255, 228, 196)
    BISQUE2 = Color(238, 213, 183)
    BISQUE3 = Color(205, 183, 158)
    BISQUE4 = Color(139, 125, 107)
    BLACK = Color(0, 0, 0)
    BLANCHEDALMOND = Color(255, 235, 205)
    BLUE = Color(0, 0, 255)
    BLUE2 = Color(0, 0, 238)
    BLUE3 = Color(0, 0, 205)
    BLUE4 = Color(0, 0, 139)
    BLUEVIOLET = Color(138, 43, 226)
    BRICK = Color(156, 102, 31)
    BROWN = Color(165, 42, 42)
    BROWN1 = Color(255, 64, 64)
    BROWN2 = Color(238, 59, 59)
    BROWN3 = Color(205, 51, 51)
    BROWN4 = Color(139, 35, 35)
    BURLYWOOD = Color(222, 184, 135)
    BURLYWOOD1 = Color(255, 211, 155)
    BURLYWOOD2 = Color(238, 197, 145)
    BURLYWOOD3 = Color(205, 170, 125)
    BURLYWOOD4 = Color(139, 115, 85)
    BURNTSIENNA = Color(138, 54, 15)
    BURNTUMBER = Color(138, 51, 36)
    CADETBLUE = Color(95, 158, 160)
    CADETBLUE1 = Color(152, 245, 255)
    CADETBLUE2 = Color(142, 229, 238)
    CADETBLUE3 = Color(122, 197, 205)
    CADETBLUE4 = Color(83, 134, 139)
    CADMIUMORANGE = Color(255, 97, 3)
    CADMIUMYELLOW = Color(255, 153, 18)
    CARROT = Color(237, 145, 33)
    CHARTREUSE1 = Color(127, 255, 0)
    CHARTREUSE2 = Color(118, 238, 0)
    CHARTREUSE3 = Color(102, 205, 0)
    CHARTREUSE4 = Color(69, 139, 0)
    CHOCOLATE = Color(210, 105, 30)
    CHOCOLATE1 = Color(255, 127, 36)
    CHOCOLATE2 = Color(238, 118, 33)
    CHOCOLATE3 = Color(205, 102, 29)
    CHOCOLATE4 = Color(139, 69, 19)
    COBALT = Color(61, 89, 171)
    COBALTGREEN = Color(61, 145, 64)
    COLDGREY = Color(128, 138, 135)
    CORAL = Color(255, 127, 80)
    CORAL1 = Color(255, 114, 86)
    CORAL2 = Color(238, 106, 80)
    CORAL3 = Color(205, 91, 69)
    CORAL4 = Color(139, 62, 47)
    CORNFLOWERBLUE = Color(100, 149, 237)
    CORNSILK1 = Color(255, 248, 220)
    CORNSILK2 = Color(238, 232, 205)
    CORNSILK3 = Color(205, 200, 177)
    CORNSILK4 = Color(139, 136, 120)
    CRIMSON = Color(220, 20, 60)
    CYAN2 = Color(0, 238, 238)
    CYAN3 = Color(0, 205, 205)
    CYAN4 = Color(0, 139, 139)
    DARKGOLDENROD = Color(184, 134, 11)
    DARKGOLDENROD1 = Color(255, 185, 15)
    DARKGOLDENROD2 = Color(238, 173, 14)
    DARKGOLDENROD3 = Color(205, 149, 12)
    DARKGOLDENROD4 = Color(139, 101, 8)
    DARKGRAY = Color(169, 169, 169)
    DARKGREEN = Color(0, 100, 0)
    DARKKHAKI = Color(189, 183, 107)
    DARKOLIVEGREEN = Color(85, 107, 47)
    DARKOLIVEGREEN1 = Color(202, 255, 112)
    DARKOLIVEGREEN2 = Color(188, 238, 104)
    DARKOLIVEGREEN3 = Color(162, 205, 90)
    DARKOLIVEGREEN4 = Color(110, 139, 61)
    DARKORANGE = Color(255, 140, 0)
    DARKORANGE1 = Color(255, 127, 0)
    DARKORANGE2 = Color(238, 118, 0)
    DARKORANGE3 = Color(205, 102, 0)
    DARKORANGE4 = Color(139, 69, 0)
    DARKORCHID = Color(153, 50, 204)
    DARKORCHID1 = Color(191, 62, 255)
    DARKORCHID2 = Color(178, 58, 238)
    DARKORCHID3 = Color(154, 50, 205)
    DARKORCHID4 = Color(104, 34, 139)
    DARKSALMON = Color(233, 150, 122)
    DARKSEAGREEN = Color(143, 188, 143)
    DARKSEAGREEN1 = Color(193, 255, 193)
    DARKSEAGREEN2 = Color(180, 238, 180)
    DARKSEAGREEN3 = Color(155, 205, 155)
    DARKSEAGREEN4 = Color(105, 139, 105)
    DARKSLATEBLUE = Color(72, 61, 139)
    DARKSLATEGRAY = Color(47, 79, 79)
    DARKSLATEGRAY1 = Color(151, 255, 255)
    DARKSLATEGRAY2 = Color(141, 238, 238)
    DARKSLATEGRAY3 = Color(121, 205, 205)
    DARKSLATEGRAY4 = Color(82, 139, 139)
    DARKTURQUOISE = Color(0, 206, 209)
    DARKVIOLET = Color(148, 0, 211)
    DEEPPINK1 = Color(255, 20, 147)
    DEEPPINK2 = Color(238, 18, 137)
    DEEPPINK3 = Color(205, 16, 118)
    DEEPPINK4 = Color(139, 10, 80)
    DEEPSKYBLUE1 = Color(0, 191, 255)
    DEEPSKYBLUE2 = Color(0, 178, 238)
    DEEPSKYBLUE3 = Color(0, 154, 205)
    DEEPSKYBLUE4 = Color(0, 104, 139)
    DIMGRAY = Color(105, 105, 105)
    DIMGRAY = Color(105, 105, 105)
    DODGERBLUE1 = Color(30, 144, 255)
    DODGERBLUE2 = Color(28, 134, 238)
    DODGERBLUE3 = Color(24, 116, 205)
    DODGERBLUE4 = Color(16, 78, 139)
    EGGSHELL = Color(252, 230, 201)
    EMERALDGREEN = Color(0, 201, 87)
    FIREBRICK = Color(178, 34, 34)
    FIREBRICK1 = Color(255, 48, 48)
    FIREBRICK2 = Color(238, 44, 44)
    FIREBRICK3 = Color(205, 38, 38)
    FIREBRICK4 = Color(139, 26, 26)
    FLESH = Color(255, 125, 64)
    FLORALWHITE = Color(255, 250, 240)
    FORESTGREEN = Color(34, 139, 34)
    GAINSBORO = Color(220, 220, 220)
    GHOSTWHITE = Color(248, 248, 255)
    GOLD1 = Color(255, 215, 0)
    GOLD2 = Color(238, 201, 0)
    GOLD3 = Color(205, 173, 0)
    GOLD4 = Color(139, 117, 0)
    GOLDENROD = Color(218, 165, 32)
    GOLDENROD1 = Color(255, 193, 37)
    GOLDENROD2 = Color(238, 180, 34)
    GOLDENROD3 = Color(205, 155, 29)
    GOLDENROD4 = Color(139, 105, 20)
    GRAY = Color(128, 128, 128)
    GRAY1 = Color(3, 3, 3)
    GRAY10 = Color(26, 26, 26)
    GRAY11 = Color(28, 28, 28)
    GRAY12 = Color(31, 31, 31)
    GRAY13 = Color(33, 33, 33)
    GRAY14 = Color(36, 36, 36)
    GRAY15 = Color(38, 38, 38)
    GRAY16 = Color(41, 41, 41)
    GRAY17 = Color(43, 43, 43)
    GRAY18 = Color(46, 46, 46)
    GRAY19 = Color(48, 48, 48)
    GRAY2 = Color(5, 5, 5)
    GRAY20 = Color(51, 51, 51)
    GRAY21 = Color(54, 54, 54)
    GRAY22 = Color(56, 56, 56)
    GRAY23 = Color(59, 59, 59)
    GRAY24 = Color(61, 61, 61)
    GRAY25 = Color(64, 64, 64)
    GRAY26 = Color(66, 66, 66)
    GRAY27 = Color(69, 69, 69)
    GRAY28 = Color(71, 71, 71)
    GRAY29 = Color(74, 74, 74)
    GRAY3 = Color(8, 8, 8)
    GRAY30 = Color(77, 77, 77)
    GRAY31 = Color(79, 79, 79)
    GRAY32 = Color(82, 82, 82)
    GRAY33 = Color(84, 84, 84)
    GRAY34 = Color(87, 87, 87)
    GRAY35 = Color(89, 89, 89)
    GRAY36 = Color(92, 92, 92)
    GRAY37 = Color(94, 94, 94)
    GRAY38 = Color(97, 97, 97)
    GRAY39 = Color(99, 99, 99)
    GRAY4 = Color(10, 10, 10)
    GRAY40 = Color(102, 102, 102)
    GRAY42 = Color(107, 107, 107)
    GRAY43 = Color(110, 110, 110)
    GRAY44 = Color(112, 112, 112)
    GRAY45 = Color(115, 115, 115)
    GRAY46 = Color(117, 117, 117)
    GRAY47 = Color(120, 120, 120)
    GRAY48 = Color(122, 122, 122)
    GRAY49 = Color(125, 125, 125)
    GRAY5 = Color(13, 13, 13)
    GRAY50 = Color(127, 127, 127)
    GRAY51 = Color(130, 130, 130)
    GRAY52 = Color(133, 133, 133)
    GRAY53 = Color(135, 135, 135)
    GRAY54 = Color(138, 138, 138)
    GRAY55 = Color(140, 140, 140)
    GRAY56 = Color(143, 143, 143)
    GRAY57 = Color(145, 145, 145)
    GRAY58 = Color(148, 148, 148)
    GRAY59 = Color(150, 150, 150)
    GRAY6 = Color(15, 15, 15)
    GRAY60 = Color(153, 153, 153)
    GRAY61 = Color(156, 156, 156)
    GRAY62 = Color(158, 158, 158)
    GRAY63 = Color(161, 161, 161)
    GRAY64 = Color(163, 163, 163)
    GRAY65 = Color(166, 166, 166)
    GRAY66 = Color(168, 168, 168)
    GRAY67 = Color(171, 171, 171)
    GRAY68 = Color(173, 173, 173)
    GRAY69 = Color(176, 176, 176)
    GRAY7 = Color(18, 18, 18)
    GRAY70 = Color(179, 179, 179)
    GRAY71 = Color(181, 181, 181)
    GRAY72 = Color(184, 184, 184)
    GRAY73 = Color(186, 186, 186)
    GRAY74 = Color(189, 189, 189)
    GRAY75 = Color(191, 191, 191)
    GRAY76 = Color(194, 194, 194)
    GRAY77 = Color(196, 196, 196)
    GRAY78 = Color(199, 199, 199)
    GRAY79 = Color(201, 201, 201)
    GRAY8 = Color(20, 20, 20)
    GRAY80 = Color(204, 204, 204)
    GRAY81 = Color(207, 207, 207)
    GRAY82 = Color(209, 209, 209)
    GRAY83 = Color(212, 212, 212)
    GRAY84 = Color(214, 214, 214)
    GRAY85 = Color(217, 217, 217)
    GRAY86 = Color(219, 219, 219)
    GRAY87 = Color(222, 222, 222)
    GRAY88 = Color(224, 224, 224)
    GRAY89 = Color(227, 227, 227)
    GRAY9 = Color(23, 23, 23)
    GRAY90 = Color(229, 229, 229)
    GRAY91 = Color(232, 232, 232)
    GRAY92 = Color(235, 235, 235)
    GRAY93 = Color(237, 237, 237)
    GRAY94 = Color(240, 240, 240)
    GRAY95 = Color(242, 242, 242)
    GRAY97 = Color(247, 247, 247)
    GRAY98 = Color(250, 250, 250)
    GRAY99 = Color(252, 252, 252)
    GREEN = Color(0, 128, 0)
    GREEN1 = Color(0, 255, 0)
    GREEN2 = Color(0, 238, 0)
    GREEN3 = Color(0, 205, 0)
    GREEN4 = Color(0, 139, 0)
    GREENYELLOW = Color(173, 255, 47)
    HONEYDEW1 = Color(240, 255, 240)
    HONEYDEW2 = Color(224, 238, 224)
    HONEYDEW3 = Color(193, 205, 193)
    HONEYDEW4 = Color(131, 139, 131)
    HOTPINK = Color(255, 105, 180)
    HOTPINK1 = Color(255, 110, 180)
    HOTPINK2 = Color(238, 106, 167)
    HOTPINK3 = Color(205, 96, 144)
    HOTPINK4 = Color(139, 58, 98)
    INDIANRED = Color(176, 23, 31)
    INDIANRED = Color(205, 92, 92)
    INDIANRED1 = Color(255, 106, 106)
    INDIANRED2 = Color(238, 99, 99)
    INDIANRED3 = Color(205, 85, 85)
    INDIANRED4 = Color(139, 58, 58)
    INDIGO = Color(75, 0, 130)
    IVORY1 = Color(255, 255, 240)
    IVORY2 = Color(238, 238, 224)
    IVORY3 = Color(205, 205, 193)
    IVORY4 = Color(139, 139, 131)
    IVORYBLACK = Color(41, 36, 33)
    KHAKI = Color(240, 230, 140)
    KHAKI1 = Color(255, 246, 143)
    KHAKI2 = Color(238, 230, 133)
    KHAKI3 = Color(205, 198, 115)
    KHAKI4 = Color(139, 134, 78)
    LAVENDER = Color(230, 230, 250)
    LAVENDERBLUSH1 = Color(255, 240, 245)
    LAVENDERBLUSH2 = Color(238, 224, 229)
    LAVENDERBLUSH3 = Color(205, 193, 197)
    LAVENDERBLUSH4 = Color(139, 131, 134)
    LAWNGREEN = Color(124, 252, 0)
    LEMONCHIFFON1 = Color(255, 250, 205)
    LEMONCHIFFON2 = Color(238, 233, 191)
    LEMONCHIFFON3 = Color(205, 201, 165)
    LEMONCHIFFON4 = Color(139, 137, 112)
    LIGHTBLUE = Color(173, 216, 230)
    LIGHTBLUE1 = Color(191, 239, 255)
    LIGHTBLUE2 = Color(178, 223, 238)
    LIGHTBLUE3 = Color(154, 192, 205)
    LIGHTBLUE4 = Color(104, 131, 139)
    LIGHTCORAL = Color(240, 128, 128)
    LIGHTCYAN1 = Color(224, 255, 255)
    LIGHTCYAN2 = Color(209, 238, 238)
    LIGHTCYAN3 = Color(180, 205, 205)
    LIGHTCYAN4 = Color(122, 139, 139)
    LIGHTGOLDENROD1 = Color(255, 236, 139)
    LIGHTGOLDENROD2 = Color(238, 220, 130)
    LIGHTGOLDENROD3 = Color(205, 190, 112)
    LIGHTGOLDENROD4 = Color(139, 129, 76)
    LIGHTGOLDENRODYELLOW = Color(250, 250, 210)
    LIGHTGREY = Color(211, 211, 211)
    LIGHTPINK = Color(255, 182, 193)
    LIGHTPINK1 = Color(255, 174, 185)
    LIGHTPINK2 = Color(238, 162, 173)
    LIGHTPINK3 = Color(205, 140, 149)
    LIGHTPINK4 = Color(139, 95, 101)
    LIGHTSALMON1 = Color(255, 160, 122)
    LIGHTSALMON2 = Color(238, 149, 114)
    LIGHTSALMON3 = Color(205, 129, 98)
    LIGHTSALMON4 = Color(139, 87, 66)
    LIGHTSEAGREEN = Color(32, 178, 170)
    LIGHTSKYBLUE = Color(135, 206, 250)
    LIGHTSKYBLUE1 = Color(176, 226, 255)
    LIGHTSKYBLUE2 = Color(164, 211, 238)
    LIGHTSKYBLUE3 = Color(141, 182, 205)
    LIGHTSKYBLUE4 = Color(96, 123, 139)
    LIGHTSLATEBLUE = Color(132, 112, 255)
    LIGHTSLATEGRAY = Color(119, 136, 153)
    LIGHTSTEELBLUE = Color(176, 196, 222)
    LIGHTSTEELBLUE1 = Color(202, 225, 255)
    LIGHTSTEELBLUE2 = Color(188, 210, 238)
    LIGHTSTEELBLUE3 = Color(162, 181, 205)
    LIGHTSTEELBLUE4 = Color(110, 123, 139)
    LIGHTYELLOW1 = Color(255, 255, 224)
    LIGHTYELLOW2 = Color(238, 238, 209)
    LIGHTYELLOW3 = Color(205, 205, 180)
    LIGHTYELLOW4 = Color(139, 139, 122)
    LIMEGREEN = Color(50, 205, 50)
    LINEN = Color(250, 240, 230)
    MAGENTA = Color(255, 0, 255)
    MAGENTA2 = Color(238, 0, 238)
    MAGENTA3 = Color(205, 0, 205)
    MAGENTA4 = Color(139, 0, 139)
    MANGANESEBLUE = Color(3, 168, 158)
    MAROON = Color(128, 0, 0)
    MAROON1 = Color(255, 52, 179)
    MAROON2 = Color(238, 48, 167)
    MAROON3 = Color(205, 41, 144)
    MAROON4 = Color(139, 28, 98)
    MEDIUMORCHID = Color(186, 85, 211)
    MEDIUMORCHID1 = Color(224, 102, 255)
    MEDIUMORCHID2 = Color(209, 95, 238)
    MEDIUMORCHID3 = Color(180, 82, 205)
    MEDIUMORCHID4 = Color(122, 55, 139)
    MEDIUMPURPLE = Color(147, 112, 219)
    MEDIUMPURPLE1 = Color(171, 130, 255)
    MEDIUMPURPLE2 = Color(159, 121, 238)
    MEDIUMPURPLE3 = Color(137, 104, 205)
    MEDIUMPURPLE4 = Color(93, 71, 139)
    MEDIUMSEAGREEN = Color(60, 179, 113)
    MEDIUMSLATEBLUE = Color(123, 104, 238)
    MEDIUMSPRINGGREEN = Color(0, 250, 154)
    MEDIUMTURQUOISE = Color(72, 209, 204)
    MEDIUMVIOLETRED = Color(199, 21, 133)
    MELON = Color(227, 168, 105)
    MIDNIGHTBLUE = Color(25, 25, 112)
    MINT = Color(189, 252, 201)
    MINTCREAM = Color(245, 255, 250)
    MISTYROSE1 = Color(255, 228, 225)
    MISTYROSE2 = Color(238, 213, 210)
    MISTYROSE3 = Color(205, 183, 181)
    MISTYROSE4 = Color(139, 125, 123)
    MOCCASIN = Color(255, 228, 181)
    NAVAJOWHITE1 = Color(255, 222, 173)
    NAVAJOWHITE2 = Color(238, 207, 161)
    NAVAJOWHITE3 = Color(205, 179, 139)
    NAVAJOWHITE4 = Color(139, 121, 94)
    NAVY = Color(0, 0, 128)
    OLDLACE = Color(253, 245, 230)
    OLIVE = Color(128, 128, 0)
    OLIVEDRAB = Color(107, 142, 35)
    OLIVEDRAB1 = Color(192, 255, 62)
    OLIVEDRAB2 = Color(179, 238, 58)
    OLIVEDRAB3 = Color(154, 205, 50)
    OLIVEDRAB4 = Color(105, 139, 34)
    ORANGE = Color(255, 128, 0)
    ORANGE1 = Color(255, 165, 0)
    ORANGE2 = Color(238, 154, 0)
    ORANGE3 = Color(205, 133, 0)
    ORANGE4 = Color(139, 90, 0)
    ORANGERED1 = Color(255, 69, 0)
    ORANGERED2 = Color(238, 64, 0)
    ORANGERED3 = Color(205, 55, 0)
    ORANGERED4 = Color(139, 37, 0)
    ORCHID = Color(218, 112, 214)
    ORCHID1 = Color(255, 131, 250)
    ORCHID2 = Color(238, 122, 233)
    ORCHID3 = Color(205, 105, 201)
    ORCHID4 = Color(139, 71, 137)
    PALEGOLDENROD = Color(238, 232, 170)
    PALEGREEN = Color(152, 251, 152)
    PALEGREEN1 = Color(154, 255, 154)
    PALEGREEN2 = Color(144, 238, 144)
    PALEGREEN3 = Color(124, 205, 124)
    PALEGREEN4 = Color(84, 139, 84)
    PALETURQUOISE1 = Color(187, 255, 255)
    PALETURQUOISE2 = Color(174, 238, 238)
    PALETURQUOISE3 = Color(150, 205, 205)
    PALETURQUOISE4 = Color(102, 139, 139)
    PALEVIOLETRED = Color(219, 112, 147)
    PALEVIOLETRED1 = Color(255, 130, 171)
    PALEVIOLETRED2 = Color(238, 121, 159)
    PALEVIOLETRED3 = Color(205, 104, 137)
    PALEVIOLETRED4 = Color(139, 71, 93)
    PAPAYAWHIP = Color(255, 239, 213)
    PEACHPUFF1 = Color(255, 218, 185)
    PEACHPUFF2 = Color(238, 203, 173)
    PEACHPUFF3 = Color(205, 175, 149)
    PEACHPUFF4 = Color(139, 119, 101)
    PEACOCK = Color(51, 161, 201)
    PINK = Color(255, 192, 203)
    PINK1 = Color(255, 181, 197)
    PINK2 = Color(238, 169, 184)
    PINK3 = Color(205, 145, 158)
    PINK4 = Color(139, 99, 108)
    PLUM = Color(221, 160, 221)
    PLUM1 = Color(255, 187, 255)
    PLUM2 = Color(238, 174, 238)
    PLUM3 = Color(205, 150, 205)
    PLUM4 = Color(139, 102, 139)
    POWDERBLUE = Color(176, 224, 230)
    PURPLE = Color(128, 0, 128)
    PURPLE1 = Color(155, 48, 255)
    PURPLE2 = Color(145, 44, 238)
    PURPLE3 = Color(125, 38, 205)
    PURPLE4 = Color(85, 26, 139)
    RASPBERRY = Color(135, 38, 87)
    RAWSIENNA = Color(199, 97, 20)
    RED1 = Color(255, 0, 0)
    RED2 = Color(238, 0, 0)
    RED3 = Color(205, 0, 0)
    RED4 = Color(139, 0, 0)
    ROSYBROWN = Color(188, 143, 143)
    ROSYBROWN1 = Color(255, 193, 193)
    ROSYBROWN2 = Color(238, 180, 180)
    ROSYBROWN3 = Color(205, 155, 155)
    ROSYBROWN4 = Color(139, 105, 105)
    ROYALBLUE = Color(65, 105, 225)
    ROYALBLUE1 = Color(72, 118, 255)
    ROYALBLUE2 = Color(67, 110, 238)
    ROYALBLUE3 = Color(58, 95, 205)
    ROYALBLUE4 = Color(39, 64, 139)
    SALMON = Color(250, 128, 114)
    SALMON1 = Color(255, 140, 105)
    SALMON2 = Color(238, 130, 98)
    SALMON3 = Color(205, 112, 84)
    SALMON4 = Color(139, 76, 57)
    SANDYBROWN = Color(244, 164, 96)
    SAPGREEN = Color(48, 128, 20)
    SEAGREEN1 = Color(84, 255, 159)
    SEAGREEN2 = Color(78, 238, 148)
    SEAGREEN3 = Color(67, 205, 128)
    SEAGREEN4 = Color(46, 139, 87)
    SEASHELL1 = Color(255, 245, 238)
    SEASHELL2 = Color(238, 229, 222)
    SEASHELL3 = Color(205, 197, 191)
    SEASHELL4 = Color(139, 134, 130)
    SEPIA = Color(94, 38, 18)
    SGIBEET = Color(142, 56, 142)
    SGIBRIGHTGRAY = Color(197, 193, 170)
    SGICHARTREUSE = Color(113, 198, 113)
    SGIDARKGRAY = Color(85, 85, 85)
    SGIGRAY12 = Color(30, 30, 30)
    SGIGRAY16 = Color(40, 40, 40)
    SGIGRAY32 = Color(81, 81, 81)
    SGIGRAY36 = Color(91, 91, 91)
    SGIGRAY52 = Color(132, 132, 132)
    SGIGRAY56 = Color(142, 142, 142)
    SGIGRAY72 = Color(183, 183, 183)
    SGIGRAY76 = Color(193, 193, 193)
    SGIGRAY92 = Color(234, 234, 234)
    SGIGRAY96 = Color(244, 244, 244)
    SGILIGHTBLUE = Color(125, 158, 192)
    SGILIGHTGRAY = Color(170, 170, 170)
    SGIOLIVEDRAB = Color(142, 142, 56)
    SGISALMON = Color(198, 113, 113)
    SGISLATEBLUE = Color(113, 113, 198)
    SGITEAL = Color(56, 142, 142)
    SIENNA = Color(160, 82, 45)
    SIENNA1 = Color(255, 130, 71)
    SIENNA2 = Color(238, 121, 66)
    SIENNA3 = Color(205, 104, 57)
    SIENNA4 = Color(139, 71, 38)
    SILVER = Color(192, 192, 192)
    SKYBLUE = Color(135, 206, 235)
    SKYBLUE1 = Color(135, 206, 255)
    SKYBLUE2 = Color(126, 192, 238)
    SKYBLUE3 = Color(108, 166, 205)
    SKYBLUE4 = Color(74, 112, 139)
    SLATEBLUE = Color(106, 90, 205)
    SLATEBLUE1 = Color(131, 111, 255)
    SLATEBLUE2 = Color(122, 103, 238)
    SLATEBLUE3 = Color(105, 89, 205)
    SLATEBLUE4 = Color(71, 60, 139)
    SLATEGRAY = Color(112, 128, 144)
    SLATEGRAY1 = Color(198, 226, 255)
    SLATEGRAY2 = Color(185, 211, 238)
    SLATEGRAY3 = Color(159, 182, 205)
    SLATEGRAY4 = Color(108, 123, 139)
    SNOW1 = Color(255, 250, 250)
    SNOW2 = Color(238, 233, 233)
    SNOW3 = Color(205, 201, 201)
    SNOW4 = Color(139, 137, 137)
    SPRINGGREEN = Color(0, 255, 127)
    SPRINGGREEN1 = Color(0, 238, 118)
    SPRINGGREEN2 = Color(0, 205, 102)
    SPRINGGREEN3 = Color(0, 139, 69)
    STEELBLUE = Color(70, 130, 180)
    STEELBLUE1 = Color(99, 184, 255)
    STEELBLUE2 = Color(92, 172, 238)
    STEELBLUE3 = Color(79, 148, 205)
    STEELBLUE4 = Color(54, 100, 139)
    TAN = Color(210, 180, 140)
    TAN1 = Color(255, 165, 79)
    TAN2 = Color(238, 154, 73)
    TAN3 = Color(205, 133, 63)
    TAN4 = Color(139, 90, 43)
    TEAL = Color(0, 128, 128)
    THISTLE = Color(216, 191, 216)
    THISTLE1 = Color(255, 225, 255)
    THISTLE2 = Color(238, 210, 238)
    THISTLE3 = Color(205, 181, 205)
    THISTLE4 = Color(139, 123, 139)
    TOMATO1 = Color(255, 99, 71)
    TOMATO2 = Color(238, 92, 66)
    TOMATO3 = Color(205, 79, 57)
    TOMATO4 = Color(139, 54, 38)
    TURQUOISE = Color(64, 224, 208)
    TURQUOISE1 = Color(0, 245, 255)
    TURQUOISE2 = Color(0, 229, 238)
    TURQUOISE3 = Color(0, 197, 205)
    TURQUOISE4 = Color(0, 134, 139)
    TURQUOISEBLUE = Color(0, 199, 140)
    VIOLET = Color(238, 130, 238)
    VIOLETRED = Color(208, 32, 144)
    VIOLETRED1 = Color(255, 62, 150)
    VIOLETRED2 = Color(238, 58, 140)
    VIOLETRED3 = Color(205, 50, 120)
    VIOLETRED4 = Color(139, 34, 82)
    WARMGREY = Color(128, 128, 105)
    WHEAT = Color(245, 222, 179)
    WHEAT1 = Color(255, 231, 186)
    WHEAT2 = Color(238, 216, 174)
    WHEAT3 = Color(205, 186, 150)
    WHEAT4 = Color(139, 126, 102)
    WHITE = Color(255, 255, 255)
    WHITESMOKE = Color(245, 245, 245)
    WHITESMOKE = Color(245, 245, 245)
    YELLOW1 = Color(255, 255, 0)
    YELLOW2 = Color(238, 238, 0)
    YELLOW3 = Color(205, 205, 0)
    YELLOW4 = Color(139, 139, 0)

    # Add colors to colors dictionary
    colors["aliceblue"] = ALICEBLUE
    colors["antiquewhite"] = ANTIQUEWHITE
    colors["antiquewhite1"] = ANTIQUEWHITE1
    colors["antiquewhite2"] = ANTIQUEWHITE2
    colors["antiquewhite3"] = ANTIQUEWHITE3
    colors["antiquewhite4"] = ANTIQUEWHITE4
    colors["aqua"] = AQUA
    colors["aquamarine1"] = AQUAMARINE1
    colors["aquamarine2"] = AQUAMARINE2
    colors["aquamarine3"] = AQUAMARINE3
    colors["aquamarine4"] = AQUAMARINE4
    colors["azure1"] = AZURE1
    colors["azure2"] = AZURE2
    colors["azure3"] = AZURE3
    colors["azure4"] = AZURE4
    colors["banana"] = BANANA
    colors["beige"] = BEIGE
    colors["bisque1"] = BISQUE1
    colors["bisque2"] = BISQUE2
    colors["bisque3"] = BISQUE3
    colors["bisque4"] = BISQUE4
    colors["black"] = BLACK
    colors["blanchedalmond"] = BLANCHEDALMOND
    colors["blue"] = BLUE
    colors["blue2"] = BLUE2
    colors["blue3"] = BLUE3
    colors["blue4"] = BLUE4
    colors["blueviolet"] = BLUEVIOLET
    colors["brick"] = BRICK
    colors["brown"] = BROWN
    colors["brown1"] = BROWN1
    colors["brown2"] = BROWN2
    colors["brown3"] = BROWN3
    colors["brown4"] = BROWN4
    colors["burlywood"] = BURLYWOOD
    colors["burlywood1"] = BURLYWOOD1
    colors["burlywood2"] = BURLYWOOD2
    colors["burlywood3"] = BURLYWOOD3
    colors["burlywood4"] = BURLYWOOD4
    colors["burntsienna"] = BURNTSIENNA
    colors["burntumber"] = BURNTUMBER
    colors["cadetblue"] = CADETBLUE
    colors["cadetblue1"] = CADETBLUE1
    colors["cadetblue2"] = CADETBLUE2
    colors["cadetblue3"] = CADETBLUE3
    colors["cadetblue4"] = CADETBLUE4
    colors["cadmiumorange"] = CADMIUMORANGE
    colors["cadmiumyellow"] = CADMIUMYELLOW
    colors["carrot"] = CARROT
    colors["chartreuse1"] = CHARTREUSE1
    colors["chartreuse2"] = CHARTREUSE2
    colors["chartreuse3"] = CHARTREUSE3
    colors["chartreuse4"] = CHARTREUSE4
    colors["chocolate"] = CHOCOLATE
    colors["chocolate1"] = CHOCOLATE1
    colors["chocolate2"] = CHOCOLATE2
    colors["chocolate3"] = CHOCOLATE3
    colors["chocolate4"] = CHOCOLATE4
    colors["cobalt"] = COBALT
    colors["cobaltgreen"] = COBALTGREEN
    colors["coldgrey"] = COLDGREY
    colors["coral"] = CORAL
    colors["coral1"] = CORAL1
    colors["coral2"] = CORAL2
    colors["coral3"] = CORAL3
    colors["coral4"] = CORAL4
    colors["cornflowerblue"] = CORNFLOWERBLUE
    colors["cornsilk1"] = CORNSILK1
    colors["cornsilk2"] = CORNSILK2
    colors["cornsilk3"] = CORNSILK3
    colors["cornsilk4"] = CORNSILK4
    colors["crimson"] = CRIMSON
    colors["cyan2"] = CYAN2
    colors["cyan3"] = CYAN3
    colors["cyan4"] = CYAN4
    colors["darkgoldenrod"] = DARKGOLDENROD
    colors["darkgoldenrod1"] = DARKGOLDENROD1
    colors["darkgoldenrod2"] = DARKGOLDENROD2
    colors["darkgoldenrod3"] = DARKGOLDENROD3
    colors["darkgoldenrod4"] = DARKGOLDENROD4
    colors["darkgray"] = DARKGRAY
    colors["darkgreen"] = DARKGREEN
    colors["darkkhaki"] = DARKKHAKI
    colors["darkolivegreen"] = DARKOLIVEGREEN
    colors["darkolivegreen1"] = DARKOLIVEGREEN1
    colors["darkolivegreen2"] = DARKOLIVEGREEN2
    colors["darkolivegreen3"] = DARKOLIVEGREEN3
    colors["darkolivegreen4"] = DARKOLIVEGREEN4
    colors["darkorange"] = DARKORANGE
    colors["darkorange1"] = DARKORANGE1
    colors["darkorange2"] = DARKORANGE2
    colors["darkorange3"] = DARKORANGE3
    colors["darkorange4"] = DARKORANGE4
    colors["darkorchid"] = DARKORCHID
    colors["darkorchid1"] = DARKORCHID1
    colors["darkorchid2"] = DARKORCHID2
    colors["darkorchid3"] = DARKORCHID3
    colors["darkorchid4"] = DARKORCHID4
    colors["darksalmon"] = DARKSALMON
    colors["darkseagreen"] = DARKSEAGREEN
    colors["darkseagreen1"] = DARKSEAGREEN1
    colors["darkseagreen2"] = DARKSEAGREEN2
    colors["darkseagreen3"] = DARKSEAGREEN3
    colors["darkseagreen4"] = DARKSEAGREEN4
    colors["darkslateblue"] = DARKSLATEBLUE
    colors["darkslategray"] = DARKSLATEGRAY
    colors["darkslategray1"] = DARKSLATEGRAY1
    colors["darkslategray2"] = DARKSLATEGRAY2
    colors["darkslategray3"] = DARKSLATEGRAY3
    colors["darkslategray4"] = DARKSLATEGRAY4
    colors["darkturquoise"] = DARKTURQUOISE
    colors["darkviolet"] = DARKVIOLET
    colors["deeppink1"] = DEEPPINK1
    colors["deeppink2"] = DEEPPINK2
    colors["deeppink3"] = DEEPPINK3
    colors["deeppink4"] = DEEPPINK4
    colors["deepskyblue1"] = DEEPSKYBLUE1
    colors["deepskyblue2"] = DEEPSKYBLUE2
    colors["deepskyblue3"] = DEEPSKYBLUE3
    colors["deepskyblue4"] = DEEPSKYBLUE4
    colors["dimgray"] = DIMGRAY
    colors["dimgray"] = DIMGRAY
    colors["dodgerblue1"] = DODGERBLUE1
    colors["dodgerblue2"] = DODGERBLUE2
    colors["dodgerblue3"] = DODGERBLUE3
    colors["dodgerblue4"] = DODGERBLUE4
    colors["eggshell"] = EGGSHELL
    colors["emeraldgreen"] = EMERALDGREEN
    colors["firebrick"] = FIREBRICK
    colors["firebrick1"] = FIREBRICK1
    colors["firebrick2"] = FIREBRICK2
    colors["firebrick3"] = FIREBRICK3
    colors["firebrick4"] = FIREBRICK4
    colors["flesh"] = FLESH
    colors["floralwhite"] = FLORALWHITE
    colors["forestgreen"] = FORESTGREEN
    colors["gainsboro"] = GAINSBORO
    colors["ghostwhite"] = GHOSTWHITE
    colors["gold1"] = GOLD1
    colors["gold2"] = GOLD2
    colors["gold3"] = GOLD3
    colors["gold4"] = GOLD4
    colors["goldenrod"] = GOLDENROD
    colors["goldenrod1"] = GOLDENROD1
    colors["goldenrod2"] = GOLDENROD2
    colors["goldenrod3"] = GOLDENROD3
    colors["goldenrod4"] = GOLDENROD4
    colors["gray"] = GRAY
    colors["gray1"] = GRAY1
    colors["gray10"] = GRAY10
    colors["gray11"] = GRAY11
    colors["gray12"] = GRAY12
    colors["gray13"] = GRAY13
    colors["gray14"] = GRAY14
    colors["gray15"] = GRAY15
    colors["gray16"] = GRAY16
    colors["gray17"] = GRAY17
    colors["gray18"] = GRAY18
    colors["gray19"] = GRAY19
    colors["gray2"] = GRAY2
    colors["gray20"] = GRAY20
    colors["gray21"] = GRAY21
    colors["gray22"] = GRAY22
    colors["gray23"] = GRAY23
    colors["gray24"] = GRAY24
    colors["gray25"] = GRAY25
    colors["gray26"] = GRAY26
    colors["gray27"] = GRAY27
    colors["gray28"] = GRAY28
    colors["gray29"] = GRAY29
    colors["gray3"] = GRAY3
    colors["gray30"] = GRAY30
    colors["gray31"] = GRAY31
    colors["gray32"] = GRAY32
    colors["gray33"] = GRAY33
    colors["gray34"] = GRAY34
    colors["gray35"] = GRAY35
    colors["gray36"] = GRAY36
    colors["gray37"] = GRAY37
    colors["gray38"] = GRAY38
    colors["gray39"] = GRAY39
    colors["gray4"] = GRAY4
    colors["gray40"] = GRAY40
    colors["gray42"] = GRAY42
    colors["gray43"] = GRAY43
    colors["gray44"] = GRAY44
    colors["gray45"] = GRAY45
    colors["gray46"] = GRAY46
    colors["gray47"] = GRAY47
    colors["gray48"] = GRAY48
    colors["gray49"] = GRAY49
    colors["gray5"] = GRAY5
    colors["gray50"] = GRAY50
    colors["gray51"] = GRAY51
    colors["gray52"] = GRAY52
    colors["gray53"] = GRAY53
    colors["gray54"] = GRAY54
    colors["gray55"] = GRAY55
    colors["gray56"] = GRAY56
    colors["gray57"] = GRAY57
    colors["gray58"] = GRAY58
    colors["gray59"] = GRAY59
    colors["gray6"] = GRAY6
    colors["gray60"] = GRAY60
    colors["gray61"] = GRAY61
    colors["gray62"] = GRAY62
    colors["gray63"] = GRAY63
    colors["gray64"] = GRAY64
    colors["gray65"] = GRAY65
    colors["gray66"] = GRAY66
    colors["gray67"] = GRAY67
    colors["gray68"] = GRAY68
    colors["gray69"] = GRAY69
    colors["gray7"] = GRAY7
    colors["gray70"] = GRAY70
    colors["gray71"] = GRAY71
    colors["gray72"] = GRAY72
    colors["gray73"] = GRAY73
    colors["gray74"] = GRAY74
    colors["gray75"] = GRAY75
    colors["gray76"] = GRAY76
    colors["gray77"] = GRAY77
    colors["gray78"] = GRAY78
    colors["gray79"] = GRAY79
    colors["gray8"] = GRAY8
    colors["gray80"] = GRAY80
    colors["gray81"] = GRAY81
    colors["gray82"] = GRAY82
    colors["gray83"] = GRAY83
    colors["gray84"] = GRAY84
    colors["gray85"] = GRAY85
    colors["gray86"] = GRAY86
    colors["gray87"] = GRAY87
    colors["gray88"] = GRAY88
    colors["gray89"] = GRAY89
    colors["gray9"] = GRAY9
    colors["gray90"] = GRAY90
    colors["gray91"] = GRAY91
    colors["gray92"] = GRAY92
    colors["gray93"] = GRAY93
    colors["gray94"] = GRAY94
    colors["gray95"] = GRAY95
    colors["gray97"] = GRAY97
    colors["gray98"] = GRAY98
    colors["gray99"] = GRAY99
    colors["green"] = GREEN
    colors["green1"] = GREEN1
    colors["green2"] = GREEN2
    colors["green3"] = GREEN3
    colors["green4"] = GREEN4
    colors["greenyellow"] = GREENYELLOW
    colors["honeydew1"] = HONEYDEW1
    colors["honeydew2"] = HONEYDEW2
    colors["honeydew3"] = HONEYDEW3
    colors["honeydew4"] = HONEYDEW4
    colors["hotpink"] = HOTPINK
    colors["hotpink1"] = HOTPINK1
    colors["hotpink2"] = HOTPINK2
    colors["hotpink3"] = HOTPINK3
    colors["hotpink4"] = HOTPINK4
    colors["indianred"] = INDIANRED
    colors["indianred"] = INDIANRED
    colors["indianred1"] = INDIANRED1
    colors["indianred2"] = INDIANRED2
    colors["indianred3"] = INDIANRED3
    colors["indianred4"] = INDIANRED4
    colors["indigo"] = INDIGO
    colors["ivory1"] = IVORY1
    colors["ivory2"] = IVORY2
    colors["ivory3"] = IVORY3
    colors["ivory4"] = IVORY4
    colors["ivoryblack"] = IVORYBLACK
    colors["khaki"] = KHAKI
    colors["khaki1"] = KHAKI1
    colors["khaki2"] = KHAKI2
    colors["khaki3"] = KHAKI3
    colors["khaki4"] = KHAKI4
    colors["lavender"] = LAVENDER
    colors["lavenderblush1"] = LAVENDERBLUSH1
    colors["lavenderblush2"] = LAVENDERBLUSH2
    colors["lavenderblush3"] = LAVENDERBLUSH3
    colors["lavenderblush4"] = LAVENDERBLUSH4
    colors["lawngreen"] = LAWNGREEN
    colors["lemonchiffon1"] = LEMONCHIFFON1
    colors["lemonchiffon2"] = LEMONCHIFFON2
    colors["lemonchiffon3"] = LEMONCHIFFON3
    colors["lemonchiffon4"] = LEMONCHIFFON4
    colors["lightblue"] = LIGHTBLUE
    colors["lightblue1"] = LIGHTBLUE1
    colors["lightblue2"] = LIGHTBLUE2
    colors["lightblue3"] = LIGHTBLUE3
    colors["lightblue4"] = LIGHTBLUE4
    colors["lightcoral"] = LIGHTCORAL
    colors["lightcyan1"] = LIGHTCYAN1
    colors["lightcyan2"] = LIGHTCYAN2
    colors["lightcyan3"] = LIGHTCYAN3
    colors["lightcyan4"] = LIGHTCYAN4
    colors["lightgoldenrod1"] = LIGHTGOLDENROD1
    colors["lightgoldenrod2"] = LIGHTGOLDENROD2
    colors["lightgoldenrod3"] = LIGHTGOLDENROD3
    colors["lightgoldenrod4"] = LIGHTGOLDENROD4
    colors["lightgoldenrodyellow"] = LIGHTGOLDENRODYELLOW
    colors["lightgrey"] = LIGHTGREY
    colors["lightpink"] = LIGHTPINK
    colors["lightpink1"] = LIGHTPINK1
    colors["lightpink2"] = LIGHTPINK2
    colors["lightpink3"] = LIGHTPINK3
    colors["lightpink4"] = LIGHTPINK4
    colors["lightsalmon1"] = LIGHTSALMON1
    colors["lightsalmon2"] = LIGHTSALMON2
    colors["lightsalmon3"] = LIGHTSALMON3
    colors["lightsalmon4"] = LIGHTSALMON4
    colors["lightseagreen"] = LIGHTSEAGREEN
    colors["lightskyblue"] = LIGHTSKYBLUE
    colors["lightskyblue1"] = LIGHTSKYBLUE1
    colors["lightskyblue2"] = LIGHTSKYBLUE2
    colors["lightskyblue3"] = LIGHTSKYBLUE3
    colors["lightskyblue4"] = LIGHTSKYBLUE4
    colors["lightslateblue"] = LIGHTSLATEBLUE
    colors["lightslategray"] = LIGHTSLATEGRAY
    colors["lightsteelblue"] = LIGHTSTEELBLUE
    colors["lightsteelblue1"] = LIGHTSTEELBLUE1
    colors["lightsteelblue2"] = LIGHTSTEELBLUE2
    colors["lightsteelblue3"] = LIGHTSTEELBLUE3
    colors["lightsteelblue4"] = LIGHTSTEELBLUE4
    colors["lightyellow1"] = LIGHTYELLOW1
    colors["lightyellow2"] = LIGHTYELLOW2
    colors["lightyellow3"] = LIGHTYELLOW3
    colors["lightyellow4"] = LIGHTYELLOW4
    colors["limegreen"] = LIMEGREEN
    colors["linen"] = LINEN
    colors["magenta"] = MAGENTA
    colors["magenta2"] = MAGENTA2
    colors["magenta3"] = MAGENTA3
    colors["magenta4"] = MAGENTA4
    colors["manganeseblue"] = MANGANESEBLUE
    colors["maroon"] = MAROON
    colors["maroon1"] = MAROON1
    colors["maroon2"] = MAROON2
    colors["maroon3"] = MAROON3
    colors["maroon4"] = MAROON4
    colors["mediumorchid"] = MEDIUMORCHID
    colors["mediumorchid1"] = MEDIUMORCHID1
    colors["mediumorchid2"] = MEDIUMORCHID2
    colors["mediumorchid3"] = MEDIUMORCHID3
    colors["mediumorchid4"] = MEDIUMORCHID4
    colors["mediumpurple"] = MEDIUMPURPLE
    colors["mediumpurple1"] = MEDIUMPURPLE1
    colors["mediumpurple2"] = MEDIUMPURPLE2
    colors["mediumpurple3"] = MEDIUMPURPLE3
    colors["mediumpurple4"] = MEDIUMPURPLE4
    colors["mediumseagreen"] = MEDIUMSEAGREEN
    colors["mediumslateblue"] = MEDIUMSLATEBLUE
    colors["mediumspringgreen"] = MEDIUMSPRINGGREEN
    colors["mediumturquoise"] = MEDIUMTURQUOISE
    colors["mediumvioletred"] = MEDIUMVIOLETRED
    colors["melon"] = MELON
    colors["midnightblue"] = MIDNIGHTBLUE
    colors["mint"] = MINT
    colors["mintcream"] = MINTCREAM
    colors["mistyrose1"] = MISTYROSE1
    colors["mistyrose2"] = MISTYROSE2
    colors["mistyrose3"] = MISTYROSE3
    colors["mistyrose4"] = MISTYROSE4
    colors["moccasin"] = MOCCASIN
    colors["navajowhite1"] = NAVAJOWHITE1
    colors["navajowhite2"] = NAVAJOWHITE2
    colors["navajowhite3"] = NAVAJOWHITE3
    colors["navajowhite4"] = NAVAJOWHITE4
    colors["navy"] = NAVY
    colors["oldlace"] = OLDLACE
    colors["olive"] = OLIVE
    colors["olivedrab"] = OLIVEDRAB
    colors["olivedrab1"] = OLIVEDRAB1
    colors["olivedrab2"] = OLIVEDRAB2
    colors["olivedrab3"] = OLIVEDRAB3
    colors["olivedrab4"] = OLIVEDRAB4
    colors["orange"] = ORANGE
    colors["orange1"] = ORANGE1
    colors["orange2"] = ORANGE2
    colors["orange3"] = ORANGE3
    colors["orange4"] = ORANGE4
    colors["orangered1"] = ORANGERED1
    colors["orangered2"] = ORANGERED2
    colors["orangered3"] = ORANGERED3
    colors["orangered4"] = ORANGERED4
    colors["orchid"] = ORCHID
    colors["orchid1"] = ORCHID1
    colors["orchid2"] = ORCHID2
    colors["orchid3"] = ORCHID3
    colors["orchid4"] = ORCHID4
    colors["palegoldenrod"] = PALEGOLDENROD
    colors["palegreen"] = PALEGREEN
    colors["palegreen1"] = PALEGREEN1
    colors["palegreen2"] = PALEGREEN2
    colors["palegreen3"] = PALEGREEN3
    colors["palegreen4"] = PALEGREEN4
    colors["paleturquoise1"] = PALETURQUOISE1
    colors["paleturquoise2"] = PALETURQUOISE2
    colors["paleturquoise3"] = PALETURQUOISE3
    colors["paleturquoise4"] = PALETURQUOISE4
    colors["palevioletred"] = PALEVIOLETRED
    colors["palevioletred1"] = PALEVIOLETRED1
    colors["palevioletred2"] = PALEVIOLETRED2
    colors["palevioletred3"] = PALEVIOLETRED3
    colors["palevioletred4"] = PALEVIOLETRED4
    colors["papayawhip"] = PAPAYAWHIP
    colors["peachpuff1"] = PEACHPUFF1
    colors["peachpuff2"] = PEACHPUFF2
    colors["peachpuff3"] = PEACHPUFF3
    colors["peachpuff4"] = PEACHPUFF4
    colors["peacock"] = PEACOCK
    colors["pink"] = PINK
    colors["pink1"] = PINK1
    colors["pink2"] = PINK2
    colors["pink3"] = PINK3
    colors["pink4"] = PINK4
    colors["plum"] = PLUM
    colors["plum1"] = PLUM1
    colors["plum2"] = PLUM2
    colors["plum3"] = PLUM3
    colors["plum4"] = PLUM4
    colors["powderblue"] = POWDERBLUE
    colors["purple"] = PURPLE
    colors["purple1"] = PURPLE1
    colors["purple2"] = PURPLE2
    colors["purple3"] = PURPLE3
    colors["purple4"] = PURPLE4
    colors["raspberry"] = RASPBERRY
    colors["rawsienna"] = RAWSIENNA
    colors["red1"] = RED1
    colors["red2"] = RED2
    colors["red3"] = RED3
    colors["red4"] = RED4
    colors["rosybrown"] = ROSYBROWN
    colors["rosybrown1"] = ROSYBROWN1
    colors["rosybrown2"] = ROSYBROWN2
    colors["rosybrown3"] = ROSYBROWN3
    colors["rosybrown4"] = ROSYBROWN4
    colors["royalblue"] = ROYALBLUE
    colors["royalblue1"] = ROYALBLUE1
    colors["royalblue2"] = ROYALBLUE2
    colors["royalblue3"] = ROYALBLUE3
    colors["royalblue4"] = ROYALBLUE4
    colors["salmon"] = SALMON
    colors["salmon1"] = SALMON1
    colors["salmon2"] = SALMON2
    colors["salmon3"] = SALMON3
    colors["salmon4"] = SALMON4
    colors["sandybrown"] = SANDYBROWN
    colors["sapgreen"] = SAPGREEN
    colors["seagreen1"] = SEAGREEN1
    colors["seagreen2"] = SEAGREEN2
    colors["seagreen3"] = SEAGREEN3
    colors["seagreen4"] = SEAGREEN4
    colors["seashell1"] = SEASHELL1
    colors["seashell2"] = SEASHELL2
    colors["seashell3"] = SEASHELL3
    colors["seashell4"] = SEASHELL4
    colors["sepia"] = SEPIA
    colors["sgibeet"] = SGIBEET
    colors["sgibrightgray"] = SGIBRIGHTGRAY
    colors["sgichartreuse"] = SGICHARTREUSE
    colors["sgidarkgray"] = SGIDARKGRAY
    colors["sgigray12"] = SGIGRAY12
    colors["sgigray16"] = SGIGRAY16
    colors["sgigray32"] = SGIGRAY32
    colors["sgigray36"] = SGIGRAY36
    colors["sgigray52"] = SGIGRAY52
    colors["sgigray56"] = SGIGRAY56
    colors["sgigray72"] = SGIGRAY72
    colors["sgigray76"] = SGIGRAY76
    colors["sgigray92"] = SGIGRAY92
    colors["sgigray96"] = SGIGRAY96
    colors["sgilightblue"] = SGILIGHTBLUE
    colors["sgilightgray"] = SGILIGHTGRAY
    colors["sgiolivedrab"] = SGIOLIVEDRAB
    colors["sgisalmon"] = SGISALMON
    colors["sgislateblue"] = SGISLATEBLUE
    colors["sgiteal"] = SGITEAL
    colors["sienna"] = SIENNA
    colors["sienna1"] = SIENNA1
    colors["sienna2"] = SIENNA2
    colors["sienna3"] = SIENNA3
    colors["sienna4"] = SIENNA4
    colors["silver"] = SILVER
    colors["skyblue"] = SKYBLUE
    colors["skyblue1"] = SKYBLUE1
    colors["skyblue2"] = SKYBLUE2
    colors["skyblue3"] = SKYBLUE3
    colors["skyblue4"] = SKYBLUE4
    colors["slateblue"] = SLATEBLUE
    colors["slateblue1"] = SLATEBLUE1
    colors["slateblue2"] = SLATEBLUE2
    colors["slateblue3"] = SLATEBLUE3
    colors["slateblue4"] = SLATEBLUE4
    colors["slategray"] = SLATEGRAY
    colors["slategray1"] = SLATEGRAY1
    colors["slategray2"] = SLATEGRAY2
    colors["slategray3"] = SLATEGRAY3
    colors["slategray4"] = SLATEGRAY4
    colors["snow1"] = SNOW1
    colors["snow2"] = SNOW2
    colors["snow3"] = SNOW3
    colors["snow4"] = SNOW4
    colors["springgreen"] = SPRINGGREEN
    colors["springgreen1"] = SPRINGGREEN1
    colors["springgreen2"] = SPRINGGREEN2
    colors["springgreen3"] = SPRINGGREEN3
    colors["steelblue"] = STEELBLUE
    colors["steelblue1"] = STEELBLUE1
    colors["steelblue2"] = STEELBLUE2
    colors["steelblue3"] = STEELBLUE3
    colors["steelblue4"] = STEELBLUE4
    colors["tan"] = TAN
    colors["tan1"] = TAN1
    colors["tan2"] = TAN2
    colors["tan3"] = TAN3
    colors["tan4"] = TAN4
    colors["teal"] = TEAL
    colors["thistle"] = THISTLE
    colors["thistle1"] = THISTLE1
    colors["thistle2"] = THISTLE2
    colors["thistle3"] = THISTLE3
    colors["thistle4"] = THISTLE4
    colors["tomato1"] = TOMATO1
    colors["tomato2"] = TOMATO2
    colors["tomato3"] = TOMATO3
    colors["tomato4"] = TOMATO4
    colors["turquoise"] = TURQUOISE
    colors["turquoise1"] = TURQUOISE1
    colors["turquoise2"] = TURQUOISE2
    colors["turquoise3"] = TURQUOISE3
    colors["turquoise4"] = TURQUOISE4
    colors["turquoiseblue"] = TURQUOISEBLUE
    colors["violet"] = VIOLET
    colors["violetred"] = VIOLETRED
    colors["violetred1"] = VIOLETRED1
    colors["violetred2"] = VIOLETRED2
    colors["violetred3"] = VIOLETRED3
    colors["violetred4"] = VIOLETRED4
    colors["warmgrey"] = WARMGREY
    colors["wheat"] = WHEAT
    colors["wheat1"] = WHEAT1
    colors["wheat2"] = WHEAT2
    colors["wheat3"] = WHEAT3
    colors["wheat4"] = WHEAT4
    colors["white"] = WHITE
    colors["whitesmoke"] = WHITESMOKE
    colors["whitesmoke"] = WHITESMOKE
    colors["yellow1"] = YELLOW1
    colors["yellow2"] = YELLOW2
    colors["yellow3"] = YELLOW3
    colors["yellow4"] = YELLOW4
    colors = OrderedDict(sorted(colors.items(), key=lambda t: t[0]))

    colors["A"] = Color(0, 0, 180)  # blue
    colors["B"] = Color(175, 13, 102)  # red-violet
    colors["C"] = Color(146, 248, 70)  # green-yellow

    colors["a"] = Color(0, 0, 180)  # blue
    colors["b"] = Color(175, 13, 102)  # red-violet
    colors["c"] = Color(146, 248, 70)  # green-yellow
    colors["d"] = Color(255, 200, 47)  # yellow-orange
    colors["e"] = Color(255, 118, 0)  # orange
    colors["f"] = Color(185, 185, 185)  # light-gray
    colors["g"] = Color(235, 235, 222)  # off-white
    colors["h"] = Color(100, 100, 100)  # gray
    colors["i"] = Color(255, 255, 0)  # yellow
    colors["j"] = Color(55, 19, 112)  # dark-purple
    colors["k"] = Color(255, 255, 150)  # light-yellow
    colors["l"] = Color(202, 62, 94)  # dark-pink
    colors["m"] = Color(205, 145, 63)  # dark-orange
    colors["n"] = Color(12, 75, 100)  # teal
    colors["o"] = Color(255, 0, 0)  # red
    colors["p"] = Color(175, 155, 50)  # dark-yellow
    colors["q"] = Color(0, 0, 0)  # black
    colors["r"] = Color(37, 70, 25)  # dark-green
    colors["s"] = Color(121, 33, 135)  # purple
    colors["t"] = Color(83, 140, 208)  # light-blue
    colors["u"] = Color(0, 154, 37)  # green
    colors["v"] = Color(178, 220, 205)  # cyan
    colors["w"] = Color(255, 152, 213)  # pink
    colors["x"] = Color(0, 0, 74)  # dark blue
    colors["y"] = Color(175, 200, 74)  # olive-green
    colors["z"] = Color(63, 25, 12)  # red-brown
