
import pymysql
import sys
import os

sys.path.append('/pjrd')
sys.path.append('..')

from PySide2 import QtWebEngineWidgets, QtWebChannel
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import PySide2.QtQml



''' ANY CHANGES TO TABLE MUST BE CHANGED HERE '''
# returns a dictionary that maps the nutrient id to the which column in self.nutrientReportTableView 
# example (nutrientID) -> column index of nutrient in formualEditor.nutrientReportTableView
def nutrientColMap():
    map = {}
    # self.map[nutrient_id] = column_applicable
    map[1] = 11 #monosaccharides
    map[203] = 5 # protein
    map[204] = 13 #total fat
    map[205] = 6 # total carbs
    map[208] = 4 # calories
    map[221] = 23 # alcohol
    map[255] = 22 # water
    map[262] = 24 # caffeiene
    map[263] = None # theobromine
    map[269] = 9 # total sugars
    map[291] = 7 # total dietary fiber
    map[301] = 27 # calcium
    map[303] = 32 # iron
    map[305] = 36 # phosphorus
    map[306] = 37 # potassium
    map[307] = 39 # sodium
    map[309] = 40 # zinc
    map[312] = 29 # copper
    map[317] = 38 # selenium
    map[319] = None # retinol
    map[320] = 43 # vitamin A RAE 
    map[321] = None # beta carotene
    map[322] = None # alpha carotene
    map[323] = 52 # vitamn E (alpha tocopherol)
    map[328] = 51 #vitamin D (D2 + D3) <---- needs conversion
    map[334] = None # cryptoxanthinin
    map[337] = None # lycopene
    map[338] = None # lutein + zeaxanthinin
    map[401] = 50 # vitamin c
    map[404] = 44 # vitamin b1/thiamin
    map[405] = 45 # vitamin b3/riboflavin
    map[406] = 46 # vitamin b3/niacin <----- 47 is b3/niacin equivalent
    map[415] = 48 # vitamin b6
    map[417] = 53 # folate <----- folate, dfe is 54
    map[418] = 49 # vitamin b12
    map[421] = 25 # choline
    map[430] = 55 # vitamin k 
    map[431] = None # folic acid?????
    map[432] = None # folate, food
    map[435] = 54 # folate, dfe
    map[573] = None # vitamin e added
    map[578] = None # vitamin b12 added
    map[601] = 21 # cholestrol
    map[606] = 14 # total sat fat
    map[607] = None # 4:0
    map[608] = None #6:0
    map[609] = None # 8:0
    map[610] = None #10:0
    map[611] = None # 12:0
    map[612] = None #14:0
    map[613] = None # 16:0
    map[614] = None #18:0
    map[617] = None #18:1
    map[618] = None #18:2
    map[619] = None #18:3
    map[620] = None #20:4
    map[621] = None #22:6 n-3
    map[626] = None #16:1
    map[627] = None #18:4
    map[628] = None # 20:1
    map[629] = None # 20:5 n-3
    map[630] = None # 22:1
    map[631] = None # 22:5 n-3
    map[645] = 16 # total monounsat fat 
    map[646] = 17 # total polyunsat fat 
    map[647] = 26 # sugar alcohol
    map[648] = 8 # total soluble fiber 
    map[649] = 12 # disaccharides
    map[651] = 33 # magnesium
    map[652] = 30 # fluoride
    map[654] = 28 # chromium
    map[655] = 31 # iodine
    map[656] = 33 # manganese
    map[657] = 35 # molybdenum 
    map[658] = 56 # vitamin b5/panothenic acid
    map[659] = 10 # added sugars
    map[660] = 19 # omega 3
    map[661] = 20 # omega 6 
    map[662] = None # other carbs
    map[663] = 18 # total unsat fat  <--- make sure that 645 and 646 add to make 663
    map[664] = 15 # total trans fat
    return map


''' ANY CHANGES TO TABLE MUST BE CHANGED HERE '''
# returns a dictionary that maps the nutrient id to the row in formulaEditor.dvReportTableView
def nutrientRowMap():
    map = {}
    map[203] = 7 # protein
    map[204] = 1 # total fat 
    map[205] = 4 # total carbs 
    map[208] = 0 # calories
    map[269] = 6 # total sugars
    map[291] = 5 # total fiber
    map[301] = 21 # calcium 
    map[303] = 23 # iron 
    map[305] = 26 # phosphorus
    map[306] = 27 # potassium
    map[307] = 29  # sodium
    map[309] = 30 # Zinc 
    map[312] = 22 # copper
    map[317] = 28 # selenium
    map[320] = 8 # vitamin a 
    map[323] = 18 # vitamin e 
    map[328] = 17 # vitamin d 
    map[401] = 16 # vitaimn C 
    map[404] = 9 # thiamin
    map[405] = 10 # riboflavin
    map[406] = 11 # niacin
    map[415] = 13 # vitamin b6
    map[418] = 15 # vitamin b12
    map[421] = 20 # choline
    map[430] = 19 # vitamin k 
    map[431] = 14 # folic acid
    map[601] = 3 # cholestrol
    map[606] = 2 # total sat fat 
    map[651] = 24 # magnesium
    map[656] = 25 # manganese 
    map[658] = 12 # vitamin b5, panothenic acid 
    return map 
 

''' ANY CHANGES TO TABLE MUST BE CHANGED HERE '''
# returns a dictionary that maps the nutrient id to the row in formulaEditor -> compareTable(QuickTableView class)
def compareTableRowMap():
    map = {}
    map[208] = 0 # calories
    map[204] = 1 # total fat
    map[606] = 2 # total saturated fat
    map[664] = 3 # total trans fat
    map[645] = 4 # total monounsaturated fat
    map[646] = 5 # total polyunsaturated fat 
    map[663] = 6 # total unsaturated fat
    map[660] = 7 # omega 3
    map[661] = 8 # omega 6
    map[601] = 9 # cholestrol
    map[205] = 10 # total carbs
    map[291] = 11 # total dietary fiber
    map[269] = 12 # total sugar
    map[659] = 13 # added sugar 
    map[1] = 14 # monosaccharides
    map[649] = 15 # disaccharides
    map[203] = 16 # protein
    map[320] = [17, 18, 19] # vitamin A RAE ID --> [vitamin A IU, vitamin A RE, Vitamin A RAE]
    #map[-1] = 17 # vitamin A IU # TODO
    #map[-1] = 18 # vitamin A RE # TODO 
    #map[320] = 19 # Vitamin A RAE 
    map[404] = 20 # Thiamin
    map[405] = 21 # Riboflaving
    map[406] = [22, 23] # Niacin ID --> [Niacin, Niacin Equivalents]
    #map[406] = 22 # Niacin
    #map[-1] = 23 # Niacin Equivalent # TODO
    map[658] = 24 # Vitamin B5/Panothenic Acid
    map[415] = 25 # Vitamin B6
    map[417] = 26 # Folate (there is also 432 -> folate, food and 435-> folate, DFE) Not sure which to use 
    map[418] = 27 # Vitamin B12
    map[401] = 28 # Vitamin C 
    map[328] = 29 # Vitamin D (D2 + D3). Not sure if right
    map[323] = 30 # Vitamin E/alpha tocopherol
    map[430] = 31 # Vitamin K 
    map[421] = 32 # Choline
    map[301] = 33 # Calcium
    map[312] = 34 # Copper
    map[303] = 35 # Iron
    map[651] = 36 # Magnesium
    map[656] = 37 # Manganese 
    map[657] = 38 # Molybdenum
    map[305] = 39 # Phosphorus
    map[306] = 40 # potassium
    map[317] = 41 # Selenium
    map[307] = 42 # Sodium
    map[309] = 43 # Zinc
    return map


def dbConnection(database: str, cursorclass=pymysql.cursors.DictCursor):
    connection = pymysql.connect(host='localhost', user='root', password='Pj@bW1!G1-4', database=database, cursorclass=cursorclass)
    return connection


# returns a 2d array with each value set to value
def initialize2DArray(rowCount: int, colCount: int, value=None):
    array = [[value] * colCount for _ in range(rowCount)]
    return array

# called to test if the window works
def test(window):
    app = QApplication(sys.argv)
    gui = window()
    gui.show()
    sys.exit(app.exec_())


# returns a formatted string of a number with commas separating the thousands
# example 2432532.12 -> 2,432,432.12
def numberWithCommas(number):
    return f"{number:,.2f}"


class TimedMessageBox(QMessageBox):
    
    def __init__(self, autoClose=True, timeout=2):
        ##### must call when inheriting a base class in order to gain access to everything
        super(TimedMessageBox, self).__init__()
        self.timeout = timeout
        self.autoClose = autoClose
        
    def showEvent(self, showEvent):
        self.currentTimer = 0
        if self.autoClose:
            self.startTimer(1000)
    
    def timerEvent(self, timerEvent):
        self.currentTimer += 1
        if self.currentTimer >= self.timeout:
            self.done(0)

# returns nested dictionary for all subIngredients in the food identified by foodID
# {
#   'parent' : parent ingredient name
#   'children': [
#       {
#           'parent': parent ingredient name
#           'children': []
#       }, ....
#       
#   ] 
# }
#
#
def getIngredientStatement(foodID: int):

    keys = ['parent', 'children']
    subIngredients = dict.fromkeys(keys)
    
    children = []
    with dbConnection('FormulaSchema').cursor() as cursor:

        # if the food is an fndds ingredient preloaded from database and has a subfood
        # gets the subingredients from subfood_food table and appends to list in descending order of predominance
        if cursor.execute('SELECT food.food_id, food_desc, subfood_desc, subfood_food.ingredient_weight FROM food LEFT JOIN subfood_food ON food.food_id = subfood_food.food_id WHERE food.food_id = %s ORDER BY food.food_id ASC, ingredient_weight DESC', (foodID,)) != 0:
            subfoods = cursor.fetchall()
            subIngredients['parent'] = subfoods[0]['food_desc']
    
            for food in subfoods:
                if food['subfood_desc'] is not None:
                    children.append(food['subfood_desc'])
        

        # if the food is a formula (composed of other foods),
        # combines all its components by food_desc and concatenates to an ingredient statement string
        elif cursor.execute('SELECT formula.formula_name, formula_food.food_id, food.food_desc, food.ing_statement FROM formula LEFT JOIN formula_food ON formula.formula_id = formula_food.formula_id LEFT JOIN food ON food.food_id = formula_food.food_id WHERE food.food_id = %s ORDER BY formula_food.weight_g DESC', (foodID,)) != 0:
            subfoods = cursor.fetchall()
            subIngredients['parent'] = subfoods[0]['food_desc']
    
            for food in subfoods:
                children.append(getIngredientStatement(food['food_id']))
        
        # if the food is a singular ingredient
        else:
            cursor.execute('SELECT food_id, food_desc, ing_statement, user_inputted FROM food WHERE food_id = %s', (foodID,))
            result = cursor.fetchone()
            subIngredients['parent'] = result['food_desc']

            if result['ing_statement'] is not None:
                children.append(result['ing_statement'])

    subIngredients['children'] = children
    return subIngredients
    

'''def extractIngredientStatement(toExtract: dict, next = None, separator: str=None):
   
    if separator is None:  #separators = ['(', '[', '{']
        separator = ('(', ')')
    elif separator == ('(', ')'):
        separator = ('[', ']')
    elif separator == ('[', ']'):
        separator = ('{', '}')
    elif separator == ('{', '}'):
        separator = ('(', ')')

    statement = ', '
    ingredients = []
    
    if next is None:
        next = {}
        next['parent'] = toExtract['parent']
        next['children'] = toExtract['children']
    if isinstance(next, dict):
        if len(next['children']) == 0:
            return str('<b>' + next['parent'] + '</b>')
        else:
            for child in next['children']:
                ingredients.append(extractIngredientStatement(toExtract, child, separator)) 
            statement = separator[0] + statement.join(ingredients) + separator[1]
            return '<b>' + next['parent'] + '</b>' + ' ' + statement
    else: 
        return str(next)'''

'''
def extractIngredientStatement(toExtract: dict, next = None, separator: str=None):

    if separator is None:  #separators = ['(', '[', '{']
        separator = ('(', ')')
    elif separator == ('(', ')'):
        separator = ('[', ']')
    elif separator == ('[', ']'):
        separator = ('{', '}')
    elif separator == ('{', '}'):
        separator = ('(', ')')

    statement = ', '
    ingredients = []
    
    if next is not None:
        next = {}
        next['parent'] = toExtract['parent']
        next['children'] = toExtract['children']
    else:
        next = toExtract['parent']
    if isinstance(next, dict):
        if len(next['children']) == 0:
            return str('<b>' + next['parent'] + '</b>')
        else:
            for child in next['children']:
                ingredients.append(extractIngredientStatement(toExtract, child, separator)) 
            statement = separator[0] + statement.join(ingredients) + separator[1]
            return '<b>' + next['parent'] + '</b>' + ' ' + statement
    #else: 
        #return str(next)
'''

# modified 
def extractIngredientStatement(toExtract: dict, next = None, separator: str=None):

    if separator is None:  #separators = ['(', '[', '{']
        separator = ('(', ')')
    elif separator == ('(', ')'):
        separator = ('[', ']')
    elif separator == ('[', ']'):
        separator = ('{', '}')
    elif separator == ('{', '}'):
        separator = ('(', ')')


    statement = ', '
    ingredients = []
    
    if next is None:
        next = {}
        next['parent'] = toExtract['parent']
        next['children'] = toExtract['children']

    if isinstance(next, dict):
        if len(next['children']) == 0 or next['children'] is None:
            return str('<b>' + next['parent'] + '</b>')
        else:
            for child in next['children']:
                ingredients.append(extractIngredientStatement(toExtract, child, separator)) 
            statement = separator[0] + statement.join(ingredients) + separator[1]
            return '<b>' + next['parent'] + '</b>' + ' ' + statement

    return next




'''def extractIngredientStatement(toExtract: dict, statement: str = None, separator = None):
    if separator is None:  #separators = ['(', '[', '{']
        separator = ('(', ')')
    elif separator == ('(', ')'):
        separator = ('[', ']')
    elif separator == ('[', ']'):
        separator = ('{', '}')
    elif separator == ('{', '}'):
        separator = ('(', ')')

    if statement is None:
        statement = ''

    parentIngredients = []

    if not toExtract['parent']:
        return statement
    if not toExtract['children'] or len(toExtract['children'] == 0):
        if statement == '':
            return statement + toExtract['parent']
        else:
            return statement + ', ' + toExtract['parent']
    for child in toExtract['children']:
        if isinstance(child, dict):
            parentIngredients.append(extractIngredientStatement(child, statement, separator))
        else:
            parentIngredients.append(child)
    statement = separator[0] + statement.join(parentIngredients) + separator[1]
    return '<b>' + next['parent'] + '</b>' + ' ' + statement'''
        
    


   
    

   