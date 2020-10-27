# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulaEditorSearchResults.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from helpers import test, connectDB

class searchResults(QDialog):

    def __init__(self):
        super(searchResults, self).__init__()
        self.setupUi(self)
        self.setupSignals()

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

        self.horizontalLayout.addWidget(self.searchLineEdit)

        self.goBtn = QPushButton(self.frame)
        self.goBtn.setObjectName(u"goBtn")

        self.horizontalLayout.addWidget(self.goBtn)

        self.verticalLayout_2.addWidget(self.frame)

        self.dialogButtonBox = QDialogButtonBox(searchResults)
        self.dialogButtonBox.setObjectName(u"dialogButtonBox")
        self.dialogButtonBox.setOrientation(Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.dialogButtonBox)


        self.retranslateUi(searchResults)
        self.dialogButtonBox.accepted.connect(searchResults.accept)
        self.dialogButtonBox.rejected.connect(searchResults.close)
        self.goBtn.clicked.connect(self.searchResultsTable.update)

        QMetaObject.connectSlotsByName(searchResults)
    # setupUi

    def retranslateUi(self, searchResults):
        searchResults.setWindowTitle(QCoreApplication.translate("searchResults", u"Search Results", None))
        self.resultsLabel.setText(QCoreApplication.translate("searchResults", u"Search returned # results. Double click to add to formula.", None))
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

    def setupSignals(self):
        self.goBtn.clicked.connect(self.search)
        self.searchResultsTable.cellDoubleClicked.connect(self.resultClicked(self.searchResultsTable.selectedItems))
        #self.searchLineEdit.enterEvent.connect(self.search)
        self.searchLineEdit.returnPressed.connect(self.search)
        #TODO on double click from table, send the data back to the confirmadd dialog. Bring up dialog TODO
       #self.connect(self.searchResultsTable, QAbstractItemView.DoubleClicked)

    def search(self):
        searchQuery = self.searchLineEdit.text()
        #searchQuery = 'Grape' #<--------------------------------------
        with connectDB().cursor() as cursor:

            query = """SELECT ing_common_name, ing_specific_name, supplier_name, supplier_ing_item_code, ingredient_statement FROM ingredient INNER JOIN supplier ON supplier.supplier_id = ingredient.supplier_id WHERE ing_common_name LIKE '%"%s"%' OR ing_specific_name LIKE '%"%s"%' OR supplier_name LIKE '%"%s"%' OR ingredient_statement LIKE '%"%s"%'"""
            
            cursor.execute("SELECT ing_common_name, ing_specific_name, supplier_name, supplier_ing_item_code, ingredient_statement, ing_id FROM ingredient INNER JOIN supplier ON supplier.supplier_id = ingredient.supplier_id WHERE ing_common_name LIKE %s OR ing_specific_name LIKE %s OR supplier_name LIKE %s OR ingredient_statement LIKE %s", ("%" + searchQuery + "%", "%" + searchQuery + "%", "%" + searchQuery + "%", "%" + searchQuery + "%",))
            searchResults = cursor.fetchall()
            print(searchResults)
            self.refreshTable(searchResults)

    # called in search() to refresh the table to reflect new results
    def refreshTable(self, searchResults):
    
        # search results are in list of tuples.
        # data comes in order of index ing_common_name, ing_specific_name, supplier_name, supplier_ing_item_code, ingredient_statement, ing_id
      
        self.searchResultsTable.setRowCount(0)

        for result in searchResults:
            if self.searchResultsTable.rowCount() == 0:
                rowIndex = 0
            else:
                rowCount = self.searchResultsTable.rowCount()
                rowIndex = rowCount - 1

            self.searchResultsTable.insertRow(rowIndex)

            # sets common name. Assigns the ingredient id as data to this column
            widgetItem = QTableWidgetItem(result[0])
            widgetItem.setData(0, result[5])
            self.searchResultsTable.setItem(rowIndex, 0, widgetItem)

            # sets specific name
            self.searchResultsTable.setItem(rowIndex, 1, QTableWidgetItem(result[1]))

            # sets supplier name
            self.searchResultsTable.setItem(rowIndex, 2, QTableWidgetItem(result[2]))

            # sets supplier item code 
            self.searchResultsTable.setItem(rowIndex, 3, QTableWidgetItem(result[3]))

            # sets ingredient statement 
            self.searchResultsTable.setItem(rowIndex, 4, QTableWidgetItem(result[4]))


    def resultClicked(self, selectedItems):
        # debug
        #for item in selectedItems:
        #    print(item)
        print(selectedItems)
        print('it works')

test(searchResults)
