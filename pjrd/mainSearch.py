

import sys, os

sys.path.append('../pjrd')
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from pjrd.helperClasses import CustomTableModel
from pjrd.helpers import dbConnection

from pjrd.formulaEditor import formulaEditorDialog
from pjrd.add_ingredient import addIngredientDialog
# Fixes compatibility bug with mac big sur and pyqt
os.environ['QT_MAC_WANTS_LAYER'] = '1'

class MainSearch(QDialog):
    def __init__(self, mainWindow, query: str):
        super(MainSearch, self).__init__()
        self.setupUi(self)
        self.setupLogic()
        self.search(query)
        self.mainWindow = mainWindow

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"quickTableView")
        Dialog.resize(900, 700)
        tenPointFont = QFont()
        tenPointFont.setPointSize(10)

        self.verticalLayout_1 = QVBoxLayout(Dialog)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")

        self.headerLabel = QLabel()
        self.headerLabel.setText('Search Results')
        self.verticalLayout_1.addWidget(self.headerLabel)
        
        self.subheaderLabel = QLabel()
        self.subheaderLabel.setText('Double click to open the item editor')
        self.subheaderLabel.setFont(tenPointFont)
        self.verticalLayout_1.addWidget(self.subheaderLabel)

        self.resultsTable = QTableWidget()
        self.resultsTable.setColumnCount(5)

        self.resultsTable.horizontalHeader().setSizeAdjustPolicy(QHeaderView.AdjustToContents)
        self.resultsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.resultsTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.resultsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        headers = ['Description', 'Type', 'Supplier', 'Item Code', 'Date Inputted']
        self.resultsTable.setHorizontalHeaderLabels(headers)

        self.verticalLayout_1.addWidget(self.resultsTable)

        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.verticalLayout_1.addWidget(self.buttonBox)
        QMetaObject.connectSlotsByName(Dialog)

    # connets any signals to slots and/or adds data to any relevant inputs upon initialization
    def setupLogic(self):
        self.resultsTable.doubleClicked.connect(self.open)

    # called on initialization. Fills the data into the table
    def search(self, query: str):
        if query is None:
            self.close()
        self.resultsTable.setRowCount(0)
        rowIndex = 0
        
        with dbConnection('FormulaSchema').cursor() as cursor:

            # searches ingredients 
            # headers = ['Description', 'Type', 'Supplier', 'Item Code', 'Date Inputted']
            results = cursor.execute('SELECT food.food_desc, food.food_id, food.input_date, supplier_food.specific_name, supplier_food.supplier_ing_item_code, supplier.supplier_name FROM food LEFT JOIN supplier_food ON food.food_id = supplier_food.food_id LEFT JOIN supplier ON supplier.supplier_id = supplier_food.supplier_id WHERE food.food_desc LIKE %s AND food.user_inputted = %s AND food.food_id NOT IN (SELECT food_id FROM formula)', ('%' + query + '%', True))

            results = cursor.fetchall()
            for result in results:
                self.resultsTable.insertRow(rowIndex)
                item = QTableWidgetItem()
                itemData = {
                    'foodID': result['food_id'],
                    'type': 'ingredient'
                }
                item.setData(Qt.UserRole, itemData)
                item.setText(result['food_desc'])
                item.setBackground(Qt.green)
                item.setTextAlignment(Qt.AlignCenter)
            
                typeItem = QTableWidgetItem()
                typeItem.setText('Ingredient')
                typeItem.setBackground(Qt.green)
                typeItem.setTextAlignment(Qt.AlignCenter)
                
                supplierItem = QTableWidgetItem()
                supplierItem.setBackground(Qt.green)
                supplierItem.setTextAlignment(Qt.AlignCenter)

                itemCodeItem = QTableWidgetItem()
                itemCodeItem.setBackground(Qt.green)
                itemCodeItem.setTextAlignment(Qt.AlignCenter)

                dateItem = QTableWidgetItem()
                dateItem.setBackground(Qt.green)
                dateItem.setTextAlignment(Qt.AlignCenter)

                if result['supplier_name'] is not None:
                    supplierItem.setText(result['supplier_name'])
                
                if result['supplier_ing_item_code'] is not None:
                    itemCodeItem.setText(result['supplier_ing_item_code'])
                
                if result['input_date'] is not None:
                    dateItem.setText(str(result['input_date']))

                self.resultsTable.setItem(rowIndex, 0, item)
                self.resultsTable.setItem(rowIndex, 1, typeItem)
                self.resultsTable.setItem(rowIndex, 2, supplierItem)
                self.resultsTable.setItem(rowIndex, 3, itemCodeItem)
                self.resultsTable.setItem(rowIndex, 4, dateItem)

                rowIndex += 1
                
            # seraches formulas
            results = cursor.execute('SELECT food.food_id, formula.formula_id, formula.formula_name, food.input_date, supplier.supplier_name, supplier_food.supplier_ing_item_code, formula.date_inputted FROM food INNER JOIN formula ON food.food_id = formula.food_id LEFT JOIN supplier_food ON supplier_food.food_id = food.food_id LEFT JOIN supplier ON supplier.supplier_id = supplier_food.supplier_id  WHERE food.food_desc LIKE %s AND user_inputted = %s', ("%" + query + '%', True))

            results = cursor.fetchall()
            for result in results:
                self.resultsTable.insertRow(rowIndex)
                item = QTableWidgetItem()
                itemData = {
                    'foodID': result['food_id'],
                    'formulaID': result['formula_id'],
                    'type': 'formula'
                }

                item.setData(Qt.UserRole, itemData)
                item.setText(result['formula_name'])
                item.setBackground(Qt.darkGreen)
                item.setTextAlignment(Qt.AlignCenter)

                typeItem = QTableWidgetItem()
                typeItem.setText('Formula')
                typeItem.setBackground(Qt.darkGreen)
                typeItem.setTextAlignment(Qt.AlignCenter)
                
                supplierItem = QTableWidgetItem()
                supplierItem.setBackground(Qt.darkGreen)
                supplierItem.setTextAlignment(Qt.AlignCenter)

                itemCodeItem = QTableWidgetItem()
                itemCodeItem.setBackground(Qt.darkGreen)
                itemCodeItem.setTextAlignment(Qt.AlignCenter)

                dateItem = QTableWidgetItem()
                dateItem.setBackground(Qt.darkGreen)
                dateItem.setTextAlignment(Qt.AlignCenter)

                if result['supplier_name'] is not None:
                    supplierItem.setText(result['supplier_name'])
                
                if result['supplier_ing_item_code'] is not None:
                    itemCodeItem.setText(result['supplier_ing_item_code'])
        
                if result['input_date'] is not None:
                    dateItem.setText(str(result['date_inputted']))

                self.resultsTable.setItem(rowIndex, 0, item)
                self.resultsTable.setItem(rowIndex, 1, typeItem)
                self.resultsTable.setItem(rowIndex, 2, supplierItem)
                self.resultsTable.setItem(rowIndex, 3, itemCodeItem)
                self.resultsTable.setItem(rowIndex, 4, dateItem)
    
                rowIndex += 1

    # overrides the eventFilter method from QT
    def eventFilter(self, source, event):
        # calls the open method on a double click of the 
        if (event.type() == QEvent.MouseButtonDblClick and event.buttons() == Qt.LeftButton and source is self.resultsTable.viewport()):
            rowPointer = self.resultsTable.itemAt(event.pos())
            ingItem = self.resultsTable.item(rowPointer.row(), 0).data(Qt.UserRole)
            id = ingItem['id']
            type = ingItem['type']
            self.open(id, type)
            return True
        return super(MainSearch, self).eventFilter(source, event)
        
    # opens the formula editor or ingredient dialog based on the parameters passed in 
    def open(self):
        rowIndex = self.resultsTable.currentRow()
        ingItem = self.resultsTable.item(rowIndex, 0).data(Qt.UserRole)
        description = self.resultsTable.item(rowIndex, 0).text()
        foodIdToOpen = ingItem['foodID']
        type = ingItem['type']

        # id corresponds to the foodID in the database
        if foodIdToOpen is None:
            return
        if type == 'ingredient':
            widget = addIngredientDialog(self.mainWindow, openIngredientID = foodIdToOpen)
            widget.show()
            widget.exec_()
            return
        elif type == 'formula':
            formulaIdToOpen = ingItem['formulaID']
            widget = formulaEditorDialog(self.mainWindow, formulaName=description, openFormulaID=formulaIdToOpen, corrFoodID=foodIdToOpen)
            widget.show()
            widget.exec_()
            return
            
'''
app = QApplication(sys.argv)
gui = MainSearch(app, 'mint juice')
gui.show()
sys.exit(app.exec_())
'''
           