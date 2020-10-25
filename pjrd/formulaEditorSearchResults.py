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


class Ui_searchResults(object):
    def setupUi(self, searchResults):
        if not searchResults.objectName():
            searchResults.setObjectName(u"searchResults")
        searchResults.resize(674, 502)
        self.verticalLayout_2 = QVBoxLayout(searchResults)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(searchResults)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.searchLineEdit = QLineEdit(self.frame)
        self.searchLineEdit.setObjectName(u"searchLineEdit")

        self.horizontalLayout.addWidget(self.searchLineEdit)

        self.searchBtn = QPushButton(self.frame)
        self.searchBtn.setObjectName(u"searchBtn")

        self.horizontalLayout.addWidget(self.searchBtn)


        self.verticalLayout_2.addWidget(self.frame)

        self.widget = QWidget(searchResults)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.resultsLabel = QLabel(self.widget)
        self.resultsLabel.setObjectName(u"resultsLabel")

        self.verticalLayout.addWidget(self.resultsLabel)


        self.verticalLayout_2.addWidget(self.widget)

        self.searchResultsTable = QTableWidget(searchResults)
        if (self.searchResultsTable.columnCount() < 6):
            self.searchResultsTable.setColumnCount(6)
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
        __qtablewidgetitem5 = QTableWidgetItem()
        self.searchResultsTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.searchResultsTable.setObjectName(u"searchResultsTable")
        self.searchResultsTable.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.searchResultsTable.setDragDropOverwriteMode(False)
        self.searchResultsTable.setWordWrap(True)
        self.searchResultsTable.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.searchResultsTable)

        self.dialogButtonBox = QDialogButtonBox(searchResults)
        self.dialogButtonBox.setObjectName(u"dialogButtonBox")
        self.dialogButtonBox.setOrientation(Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.dialogButtonBox)


        self.retranslateUi(searchResults)
        self.dialogButtonBox.accepted.connect(searchResults.accept)
        self.dialogButtonBox.rejected.connect(searchResults.reject)

        QMetaObject.connectSlotsByName(searchResults)
    # setupUi

    def retranslateUi(self, searchResults):
        searchResults.setWindowTitle(QCoreApplication.translate("searchResults", u"Search Results", None))
        self.searchBtn.setText(QCoreApplication.translate("searchResults", u"Search", None))
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
        ___qtablewidgetitem4.setText(QCoreApplication.translate("searchResults", u"Allergens", None));
        ___qtablewidgetitem5 = self.searchResultsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("searchResults", u"Ingredient Statement", None));
    # retranslateUi

