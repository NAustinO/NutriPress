# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulaEditorSearchResults.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


import sys

sys.path.append('../pjrd')

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from pjrd.helpers import test, dbConnection
from pjrd.helperClasses import Ingredient
from pjrd.confirmAddDialog import confirmationDialog

class searchResults(QDialog):

    def __init__(self, query: str, root=None):
        """
        -----------------------------
            Arguments:
                -  query: The string for what will be searched
                -  root: A reference to the Formula Editor to call methods 
        """
        super(searchResults, self).__init__()
        self.setupUi(self)
        self.searchEvent(query)
        self.setupLogic()
        self.root = root
        
    
    def setupUi(self, searchResults):
        if not searchResults.objectName():
            searchResults.setObjectName(u"searchResults")
        searchResults.resize(750, 502)
        self.verticalLayout_2 = QVBoxLayout(searchResults)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(searchResults)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.resultsLabel = QLabel(self.widget)
        self.resultsLabel.setObjectName(u"resultsLabel")

        self.verticalLayout.addWidget(self.resultsLabel)

        self.verticalLayout_2.addWidget(self.widget)

        self.searchResultsTable = QTableWidget(searchResults)
        if (self.searchResultsTable.columnCount() < 5):
            self.searchResultsTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.searchResultsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.searchResultsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.searchResultsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.searchResultsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.searchResultsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)

        self.searchResultsTable.setObjectName(u"searchResultsTable")
        self.searchResultsTable.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.searchResultsTable.setDragDropOverwriteMode(False)
        self.searchResultsTable.setWordWrap(True)
        self.searchResultsTable.horizontalHeader().setDefaultSectionSize(175)
        self.searchResultsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.searchResultsTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.searchResultsTable.setSortingEnabled(False)
        self.searchResultsTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.searchResultsTable.setColumnWidth(0, 175)

        self.verticalLayout_2.addWidget(self.searchResultsTable)

        self.frame = QFrame(searchResults)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.searchLineEdit = QLineEdit(self.frame)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setPlaceholderText('Press "Enter" or click Go to search')

        self.horizontalLayout.addWidget(self.searchLineEdit)

        self.goBtn = QPushButton(self.frame)
        self.goBtn.setObjectName(u"goBtn")

        self.horizontalLayout.addWidget(self.goBtn)

        self.verticalLayout_2.addWidget(self.frame)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.exitPushBtn = QPushButton(searchResults)
        self.exitPushBtn.setObjectName(u"exitPushBtn")
        self.exitPushBtn.setText(u"Exit")

        self.horizontalLayout_2.addWidget(self.exitPushBtn)

        self.addSelectedBtn = QPushButton(searchResults)
        self.addSelectedBtn.setObjectName(u"addSelectedBtn")
        self.addSelectedBtn.setAutoDefault(False)
        self.addSelectedBtn.setText(u"Add Selected")

        self.horizontalLayout_2.addWidget(self.addSelectedBtn)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(searchResults)

        QMetaObject.connectSlotsByName(searchResults)
    # setupUi

    def retranslateUi(self, searchResults):
        searchResults.setWindowTitle(QCoreApplication.translate("searchResults", u"Search Results", None))
        self.resultsLabel.setText(QCoreApplication.translate("searchResults", u"Search results. Double click to add to formula or search again using searchbar", None))
        ___qtablewidgetitem = self.searchResultsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("searchResults", u"Name", None));
        ___qtablewidgetitem1 = self.searchResultsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("searchResults", u"Specific Name", None));
        ___qtablewidgetitem2 = self.searchResultsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("searchResults", u"Supplier", None));
        ___qtablewidgetitem3 = self.searchResultsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("searchResults", u"Supplier Code", None));
        ___qtablewidgetitem4 = self.searchResultsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("searchResults", u"Ingredient Statement", None));

        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("searchResults", u"Search again", None))
        self.goBtn.setText(QCoreApplication.translate("searchResults", u"Go", None))
    # retranslateUi

    def setupLogic(self):
        """
        -----------------------------
            Purpose:
                -  Signal setup 
            Arguments:
                -  None
            Return Value:
                -  None
        """
        self.goBtn.clicked.connect(self.searchEvent)
        self.searchLineEdit.returnPressed.connect(self.searchEvent)
        self.addSelectedBtn.clicked.connect(self.accept)
        self.exitPushBtn.clicked.connect(self.cancel)
        self.searchResultsTable.viewport().installEventFilter(self)

    # called by return/enter or pressing search button and on startup
    def searchEvent(self, query=False): 
        #TODO error handling
        """
        -----------------------------
            Purpose:
                -  Handles the search event
                -  Updates the QTableWidget view 
            Arguments:
                -  query: The search query. Defaults to False if none exists 
            Return Value:
                -  None
        """
        if query is False:
            query = self.searchLineEdit.text()
        if query is None:
            query = ''
        with dbConnection('FormulaSchema').cursor() as cursor:
            rows = cursor.execute("SELECT food.food_desc, food.user_inputted, supplier_food.specific_name, supplier.supplier_id, supplier.supplier_name, supplier_food.supplier_ing_item_code, food.ing_statement, food.food_id, food.is_ingredient, food.is_formula FROM food LEFT JOIN supplier_food ON food.food_id = supplier_food.food_id LEFT JOIN supplier ON supplier.supplier_id = supplier_food.supplier_id WHERE food_desc LIKE %s OR specific_name LIKE %s OR supplier_name LIKE %s OR food.ing_statement LIKE %s OR supplier_food.supplier_ing_item_code LIKE %s ORDER BY CASE WHEN supplier_food.supplier_ing_item_code LIKE %s THEN 1 WHEN food.food_desc LIKE %s THEN 2 WHEN food.food_desc LIKE %s THEN 3 WHEN food.food_desc LIKE %s THEN 4 WHEN food.food_desc LIKE %s THEN 5 ELSE 6 END", ("%" + query + "%", "%" + query + "%", "%" + query + "%", "%" + query + "%", "%" + query + "%", "%" + query + "%", query + "%", "%" + query, "% " + query, "%" + query + "%"))
            queryResults = cursor.fetchall()

            # updates the header
            if rows == 0:
                self.resultsLabel.setText("Your search had no results. Please try another search to add to formula.")
            elif rows == 1:
                self.resultsLabel.setText("Seach returned {count} result. Double click to add to formula.".format(count=rows))
            else:
                self.resultsLabel.setText("Seach returned {count} results. Double click to add to formula.".format(count=rows))

        # refreshes table with results
        self.searchResultsTable.setRowCount(0)
        for result in queryResults:
            if self.searchResultsTable.rowCount() == 0:
                rowIndex = 0
            else:
                rowCount = self.searchResultsTable.rowCount()
                rowIndex = rowCount - 1
            self.searchResultsTable.insertRow(rowIndex)

            # IMPORTANT: data for each ingredient is contained in column 0 in dictionary form within QTableWidgetItem as Qt.UserRole
            ingredient = Ingredient(result['food_desc'], result['food_id'], specificName=result['specific_name'], supplierName=result['supplier_name'], supplierItemCode=result['supplier_ing_item_code'], ingredientStatement=result['ing_statement'], supplierID=result['supplier_id'])

            widgetItem = QTableWidgetItem(result['food_desc'])
            widgetItem.setData(Qt.UserRole, ingredient) # <------ ingredient holds all the data
            widgetItem.setText(ingredient.desc.capitalize())

            specificName = QTableWidgetItem(result['specific_name'])
            supplierName = QTableWidgetItem(result['supplier_name'])
            itemCode = QTableWidgetItem(result['supplier_ing_item_code'])
            ingStatement = QTableWidgetItem(result['ing_statement'])

            if result['user_inputted'] == 1 and result['is_ingredient'] == 1:
                widgetItem.setBackground(Qt.green)
                specificName.setBackground(Qt.green)
                supplierName.setBackground(Qt.green)
                itemCode.setBackground(Qt.green)
                ingStatement.setBackground(Qt.green)
            elif result['user_inputted'] == 1 and result['is_formula'] == 1:
                widgetItem.setBackground(Qt.darkGreen)
                specificName.setBackground(Qt.darkGreen)
                supplierName.setBackground(Qt.darkGreen)
                itemCode.setBackground(Qt.darkGreen)
                ingStatement.setBackground(Qt.darkGreen)
        
            self.searchResultsTable.setItem(rowIndex, 0, widgetItem)
            self.searchResultsTable.setItem(rowIndex, 1, specificName)
            self.searchResultsTable.setItem(rowIndex, 2, supplierName)
            self.searchResultsTable.setItem(rowIndex, 3, itemCode)
            self.searchResultsTable.setItem(rowIndex, 4, ingStatement)
            self.searchResultsTable.update()
    
    def eventFilter(self, source, event):
        """
        -----------------------------
            Purpose:
                -  Event handling for double clicking within serach table and Return pressed while typing a search query 
            Arguments:
                -  None
            Return Value:
                -  None
        """
        # continues when user double clicks within table viewport to choose an ingredient. Opens the confirmation window
        if (event.type() == QEvent.MouseButtonDblClick and event.buttons() == Qt.LeftButton and source is self.searchResultsTable.viewport()):
            ingItem = self.searchResultsTable.itemAt(event.pos())
            if ingItem is None:
                return False
            ingredient = self.searchResultsTable.item(ingItem.row(), 0).data(Qt.UserRole)
            self.accept(foodToAdd=ingredient)
            return True

        # enter event, called when enter is pressed. 
        if (event.type() == QEvent.KeyPress and source == self.self and event.key() == Qt.Key_Return):
            query = self.searchLineEdit.text()
            self.searchEvent(query)
            return True
        return super(searchResults, self).eventFilter(source, event)

    # ingredient is chosen, brings up confirmation window where user inputs the amount and unit
    def accept(self, foodToAdd=None): 
        """
        -----------------------------
            Purpose:
                -  Called during the confirmation event
            Arguments:
                -  None
            Return Value:
                -  None
        """

        # continues if the user uses the button to confirm selected ingredient
        if foodToAdd is None:
            chosen = self.searchResultsTable.selectedItems()
            rows = int(len(chosen)/self.searchResultsTable.columnCount())
            if not chosen:
                msg = QMessageBox()
                msg.setText('Please select an ingredient to add')
                msg.exec_()
            elif rows > 1:
                msg = QMessageBox()
                msg.setText('Choose only one ingredient')
                msg.exec_()
            else:
                ingItem = self.searchResultsTable.selectedItems().pop()
                ingredient = self.searchResultsTable.item(ingItem.row(), 0).data(Qt.UserRole)
                confirmWindow = confirmationDialog(self.root, ingredient)
                confirmWindow.setModal(True)
                confirmWindow.exec_()
                return True

        # continues if the user double clicks on ingredient to confirm selection
        else:
            confirmWindow = confirmationDialog(self.root, foodToAdd)
            confirmWindow.setModal(True)
            confirmWindow.exec_()
            return True


    def cancel(self):
        """
        -----------------------------
            Purpose:
                -  closes the window 
        """
        self.close()
