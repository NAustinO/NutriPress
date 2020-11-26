
import pymysql
import sys
import os
from operator import itemgetter
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
sys.path.append('/pjrd')
sys.path.append('..')

class CustomTableModel(QAbstractTableModel):
    def __init__(self, headers: list = None, tableData=None):
        super(CustomTableModel, self).__init__()
        self.tableData = tableData
        self.headers = headers
    
        if headers is not None:
            self.inputHeaders(headers)
        if tableData is not None:
            self.inputData(tableData)

    # creates the map[nutrient ID] -> column of table
    '''def initialize(self):
        self.map = {}
        # self.map[nutrient_id] = column_applicable
        self.map[1] = 11 #monosaccharides
        self.map[203] = 5 # protein
        self.map[204] = 13 #total fat
        self.map[205] = 6 # total carbs
        self.map[208] = 4 # calories
        self.map[221] = 23 # alcohol
        self.map[255] = 22 # water
        self.map[262] = 24 # caffeiene
        self.map[263] = None # theobromine
        self.map[269] = 9 # total sugars
        self.map[291] = 7 # total dietary fiber
        self.map[301] = 27 # calcium
        self.map[303] = 32 # iron
        self.map[305] = 36 # phosphorus
        self.map[306] = 37 # potassium
        self.map[307] = 39 # sodium
        self.map[309] = 40 # zinc
        self.map[312] = 29 # copper
        self.map[317] = 38 # selenium
        self.map[319] = None # retinol
        self.map[320] = 43 # vitamin A RAE 
        self.map[321] = None # beta carotene
        self.map[322] = None # alpha carotene
        self.map[323] = 52 # vitamn E (alpha tocopherol)
        self.map[328] = 51 #vitamin D (D2 + D3) <---- needs conversion
        self.map[334] = None # cryptoxanthinin
        self.map[337] = None # lycopene
        self.map[338] = None # lutein + zeaxanthinin
        self.map[401] = 50 # vitamin c
        self.map[404] = 44 # vitamin b1/thiamin
        self.map[405] = 45 # vitamin b3/riboflavin
        self.map[406] = 46 # vitamin b3/niacin <----- 47 is b3/niacin equivalent
        self.map[415] = 48 # vitamin b6
        self.map[417] = 53 # folate <----- folate, dfe is 54
        self.map[418] = 49 # vitamin b12
        self.map[421] = 25 # choline
        self.map[430] = 55 # vitamin k 
        self.map[431] = None # folic acid?????
        self.map[432] = None # folate, food
        self.map[435] = 54 # folate, dfe
        self.map[573] = None # vitamin e added
        self.map[578] = None # vitamin b12 added
        self.map[601] = 21 # cholestrol
        self.map[606] = 14 # total sat fat
        self.map[607] = None # 4:0
        self.map[608] = None #6:0
        self.map[609] = None # 8:0
        self.map[610] = None #10:0
        self.map[611] = None # 12:0
        self.map[612] = None #14:0
        self.map[613] = None # 16:0
        self.map[614] = None #18:0
        self.map[617] = None #18:1
        self.map[618] = None #18:2
        self.map[619] = None #18:3
        self.map[620] = None #20:4
        self.map[621] = None #22:6 n-3
        self.map[626] = None #16:1
        self.map[627] = None #18:4
        self.map[628] = None # 20:1
        self.map[629] = None # 20:5 n-3
        self.map[630] = None # 22:1
        self.map[631] = None # 22:5 n-3
        self.map[645] = 16 # total monounsat fat 
        self.map[646] = 17 # total polyunsat fat 
        self.map[647] = 26 # sugar alcohol
        self.map[648] = 8 # total soluble fiber 
        self.map[649] = 12 # disaccharides
        self.map[651] = 33 # magnesium
        self.map[652] = 30 # fluoride
        self.map[654] = 28 # chromium
        self.map[655] = 31 # iodine
        self.map[656] = 33 # manganese
        self.map[657] = 35 # molybdenum 
        self.map[658] = 56 # vitamin b5/panothenic acid
        self.map[659] = 10 # added sugars
        self.map[660] = 19 # omega 3
        self.map[661] = 20 # omega 6 
        self.map[662] = None # other carbs
        self.map[663] = 18 # total unsat fat  <--- make sure that 645 and 646 add to make 663
        self.map[664] = 15 # total trans fat
        return self.map'''
  
    def rowCount(self, parent: QModelIndex):
        if self.tableData is None:
            return 0
        else:
            return len(self.tableData)
    
    def columnCount(self, parent: QModelIndex):
        if self.tableData is None:
            if self.headers is None:
                return 0
            else:
                return len(self.headers)
        else:
            return len(self.tableData[0])

    def inputHeaders(self, headers: list):
        self.headers = headers
        for index, value in enumerate(headers):
            self.setHeaderData(index, Qt.Horizontal, value, Qt.DisplayRole)

    def inputTableData(self, tableData):
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.tableData = tableData
        self.emit(SIGNAL("layoutChanged()"))
    
    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        elif self.tableData is None:
            return None
        return self.tableData[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def sort(self, nCol, order):
        try:
            self.emit(SIGNAL("layoutAboutToBeChanged()"))
            self.tableData = sorted(self.tableData, key=itemgetter(nCol))
            if order == Qt.DescendingOrder:
                self.tableData.reverse()
            self.emit(SIGNAL("layoutChanged()"))
        except:
            return





