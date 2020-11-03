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
from helpers import test, connectDB, connectionDB
import sys
from confirmAddDialog import confirmationDialog

class searchResults(QDialog):

    # query: the search query passed in from the formulaEditor window
    # updateRefs: a dictionary(not) that holds the references of QWidgets that are updated
    def __init__(self, query, updateRefs=None):
        super(searchResults, self).__init__()
        self.setupUi(self)
        self.searchEvent(query)
        self.setupSignals()
        self.setupEvents()
        self.updateRefs = updateRefs
        

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

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.cancelPushBtn = QPushButton(searchResults)
        self.cancelPushBtn.setObjectName(u"cancelPushBtn")
        self.cancelPushBtn.setText(u"Cancel")

        self.horizontalLayout_2.addWidget(self.cancelPushBtn)

        self.okPushBtn = QPushButton(searchResults)
        self.okPushBtn.setObjectName(u"okPushBtn")
        self.okPushBtn.setAutoDefault(False)
        self.okPushBtn.setText(u"Ok")

        self.horizontalLayout_2.addWidget(self.okPushBtn)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(searchResults)

        QMetaObject.connectSlotsByName(searchResults)

        #####--------------_#####
        #self.searchEvent(query)
        #####--------------_#####
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

    def self(self):
        return self
         
    #TODO on double click from table, send the data back to the confirmadd dialog. Bring up dialog 

    def setupSignals(self):
        self.goBtn.clicked.connect(self.searchEvent)
        self.searchLineEdit.returnPressed.connect(self.searchEvent)
        self.okPushBtn.clicked.connect(self.accept)
        self.cancelPushBtn.clicked.connect(self.cancel)
    #setupSignals

    def setupEvents(self):
        self.searchResultsTable.viewport().installEventFilter(self)
    #setupEvents

    # called by return/enter or pressing search button and on startup
    def searchEvent(self, query=False): # TODO needs error handling
        if query is False:
            query = self.searchLineEdit.text()
        if query is None:
            query = ''
        connection = connectionDB('FormulaSchema') #<------------------------ needs error handling
        cursor = connection.cursor()
        rows = cursor.execute("SELECT ing_common_name, ing_specific_name, supplier_name, supplier_ing_item_code, ingredient_statement, ing_id FROM ingredient INNER JOIN supplier ON supplier.supplier_id = ingredient.supplier_id WHERE ing_common_name LIKE %s OR ing_specific_name LIKE %s OR supplier_name LIKE %s OR ingredient_statement LIKE %s", ("%" + query + "%", "%" + query + "%", "%" + query + "%", "%" + query + "%",))
        queryResults = cursor.fetchall()
        # data comes in order of index ing_common_name, ing_specific_name, supplier_name, supplier_ing_item_code, ingredient_statement, ing_id
        cursor.close()

        # updates the header
        if rows == 0:
            self.resultsLabel.setText("Your search had no results. Please try another search to add to formula.")
        elif rows == 1:
            self.resultsLabel.setText("Seach returned {count} result. Double click to add to formula.".format(count = rows))
        else:
            self.resultsLabel.setText("Seach returned {count} results. Double click to add to formula.".format(count = rows))

        # refreshes table with results 
        self.searchResultsTable.setRowCount(0)
        for result in queryResults:
            if self.searchResultsTable.rowCount() == 0:
                rowIndex = 0
            else:
                rowCount = self.searchResultsTable.rowCount()
                rowIndex = rowCount - 1

            self.searchResultsTable.insertRow(rowIndex)

            # sets common name. Assigns the ingredient id as data to this column
            widgetItem = QTableWidgetItem(result[0])
            widgetItem.setData(Qt.UserRole, result[5])
            widgetItem.setText(result[0])

            self.searchResultsTable.setItem(rowIndex, 0, widgetItem)
            #self.searchResultsTable.setItem(rowIndex, 0, QTableWidgetItem(result[0]))
            # sets specific name
            self.searchResultsTable.setItem(rowIndex, 1, QTableWidgetItem(result[1]))
            # sets supplier name
            self.searchResultsTable.setItem(rowIndex, 2, QTableWidgetItem(result[2]))
            # sets supplier item code 
            self.searchResultsTable.setItem(rowIndex, 3, QTableWidgetItem(result[3]))
            # sets ingredient statement 
            self.searchResultsTable.setItem(rowIndex, 4, QTableWidgetItem(result[4]))
            self.searchResultsTable.update()

    # double click event filter TODO call the confirmAddUI passing in thek
    # called when user double clicks within table viewport to choose ingredient. Returns the ingredientID 
    def eventFilter(self, source, event):
        if (event.type() == QEvent.MouseButtonDblClick and event.buttons() == Qt.LeftButton and source is self.searchResultsTable.viewport()):
            self.accept()
            #item = self.searchResultsTable.itemAt(event.pos())
            #itemID = self.searchResultsTable.item(item.row(), 0).data(Qt.UserRole)
            #if item is not None: #<--------------------debug
             #   print('You clicked', item.row(), item.column())
              #  with connectionDB('FormulaSchema').cursor() as cursor: 
               #     cursor.execute('SELECT ing_common_name FROM ingredient WHERE ing_id = %s', (itemID,))
                #    itemName = cursor.fetchone()
                #   print('This item is: ', itemName[0])
            
            return True
        return super(searchResults, self).eventFilter(source, event)
    # eventFilter

    def enterEventFilter(self, source, event):
        if (event.type() == QEvent.KeyPress and source == self.searchLineEdit and event.key() == Qt.Key_Enter):
            query = self.searchLineEdit.text()
            self.searchEvent(query)
            return True
        return super(searchResults, self).eventFilter(source, event)
    # enterEventFilter

    def accept(self, id=False):
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
            if id is False:
                ingItem = self.searchResultsTable.selectedItems().pop()
                ingRow = ingItem.row()
                id = self.searchResultsTable.item(ingRow, 0).data(Qt.UserRole)
                print(id)
            #self.hide()
            enterValue = confirmationDialog(self.updateRefs, id)
            enterValue.setModal(False)
            enterValue.exec_()
            #self.close()

    def cancel(self):
        self.close()

#if __name__ == '__main__':
#    searchResults()

'''
app = QApplication(sys.argv)
gui = searchResults('grape')
gui.show()
sys.exit(app.exec_())'''