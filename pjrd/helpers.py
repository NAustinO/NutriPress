
import pymysql
import sys
import os

from PySide2 import QtWebEngineWidgets, QtWebChannel
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import PySide2.QtQml


sys.path.append('/pjrd')
sys.path.append('..')


def dbConnection(database: str, cursorclass=pymysql.cursors.DictCursor):
    connection = pymysql.connect(host='localhost', user='root', password='Pj@bW1!G1-4', database=database, cursorclass=cursorclass)
    return connection

def displayNfp(): # parent

    #html = open('pjrd/static/templates/nfp.html', 'r').read().splitlines()
    #html = open('pjrd/static/templates/nfp.html', 'r').read()
    html = open('ext/nutrition-label/dist/demo/legacy-version/demo.html', 'r').read().rstrip('\n')
    html.rstrip('\t')
    #jsFile = open('ext/nutrition-label/dist/js/nutritionLabel.js', 'r')
    #jsFunc = jsFile.read().splitlines()
    webEngineView = QWebEngineView()
    webEngineView.resize(QSize(800, 600))
    webEngineView.setHtml(html)
    #run = "('#nfp').nutritionLabel({})".format("{showLegacyVersion: false}")
    #js = 'document.getElementById("nfp").nutritionLabel()'
    #webEngineView.page().setHtml(html)
    #webEngineView.page().runJavaScript(js)
    webEngineView.show()
 

# called to test if the window works
def test(window):
    app = QApplication(sys.argv)
    gui = window()
    gui.show()
    sys.exit(app.exec_())

# returns a dictionary that maps the nutrient id to the which column in self.nutrientReportTableView 
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

            