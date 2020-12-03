# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulaEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
import math
import os
from PyQt5.QtCore import pyqtSlot

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtPrintSupport import *
from PySide2.QtCharts import * 
import PySide2.QtCharts
from operator import itemgetter

sys.path.append('../pjrd')
import pymysql
from pjrd.helpers import compareTableRowMap, displayNfp, test, dbConnection, TimedMessageBox, nutrientColMap, numberWithCommas, nutrientRowMap, initialize2DArray
from pjrd.formulaEditorSearchResults import searchResults
from pjrd.helperClasses import CustomTableModel, UnitOfMeasure, Nutrient, Ingredient, Formula
from pjrd.quickTableView import QuickTableView

# Fixes compatibility bug with mac big sur and pyqt
os.environ['QT_MAC_WANTS_LAYER'] = '1' 


class formulaEditorDialog(QDialog):
    
    def __init__(self, formulaName: str, revision: bool = None, prevRevisionID: int = None, differences: str = None):
        super(formulaEditorDialog, self).__init__()
        self.setupUi(self)
        self.formula = Formula(formulaName, isRevision = revision, prevRevisionID = prevRevisionID)
        self.fromSetupDialog(revision=revision, formulaName=formulaName, revisionID=prevRevisionID, differences=differences)
        self.setupLogic()
        
        
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(822, 1005)
        self.horizontalLayout_9 = QHBoxLayout(Dialog)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.formulaEditorTabWidget = QTabWidget(Dialog)
        self.formulaEditorTabWidget.setObjectName(u"formulaEditorTabWidget")
        self.formulaEditorTabWidget.setMinimumSize(QSize(500, 400))
        self.formulaEditorTabWidget.setUsesScrollButtons(True)
        self.ingredientsTab = QWidget()
        self.ingredientsTab.setObjectName(u"ingredientsTab")
        self.verticalLayout_11 = QVBoxLayout(self.ingredientsTab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.ingredientsTabHeaderWidget = QWidget(self.ingredientsTab)
        self.ingredientsTabHeaderWidget.setObjectName(u"ingredientsTabHeaderWidget")
        self.horizontalLayout = QHBoxLayout(self.ingredientsTabHeaderWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formulaNameHeaderLabel = QLabel(self.ingredientsTabHeaderWidget)
        self.formulaNameHeaderLabel.setObjectName(u"formulaNameHeaderLabel")

        self.horizontalLayout.addWidget(self.formulaNameHeaderLabel)

        self.formulaNameLineEdit = QLineEdit(self.ingredientsTabHeaderWidget)
        self.formulaNameLineEdit.setObjectName(u"formulaNameLineEdit")
        self.formulaNameLineEdit.setReadOnly(False)

        self.horizontalLayout.addWidget(self.formulaNameLineEdit)

        self.ingredientsTabHeaderSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.ingredientsTabHeaderSpacer)

        self.formulaIDHeaderLabel = QLabel(self.ingredientsTabHeaderWidget)
        self.formulaIDHeaderLabel.setObjectName(u"formulaIDHeaderLabel")

        self.horizontalLayout.addWidget(self.formulaIDHeaderLabel)

        self.formulaIDPlaceholder = QLabel(self.ingredientsTabHeaderWidget)
        self.formulaIDPlaceholder.setObjectName(u"formulaIDPlaceholder")

        self.horizontalLayout.addWidget(self.formulaIDPlaceholder)

        self.revisionNumberHeaderLabel = QLabel(self.ingredientsTabHeaderWidget)
        self.revisionNumberHeaderLabel.setObjectName(u"revisionNumberHeaderLabel")

        self.horizontalLayout.addWidget(self.revisionNumberHeaderLabel)

        self.revisionNumberPlaceholder = QLabel(self.ingredientsTabHeaderWidget)
        self.revisionNumberPlaceholder.setObjectName(u"revisionNumberPlaceholder")

        self.horizontalLayout.addWidget(self.revisionNumberPlaceholder)


        self.verticalLayout_11.addWidget(self.ingredientsTabHeaderWidget)

        self.ingTabLine1 = QFrame(self.ingredientsTab)
        self.ingTabLine1.setObjectName(u"ingTabLine1")
        self.ingTabLine1.setFrameShape(QFrame.HLine)
        self.ingTabLine1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.ingTabLine1)

        self.generalInfoContainerWidget = QWidget(self.ingredientsTab)
        self.generalInfoContainerWidget.setObjectName(u"generalInfoContainerWidget")
        self.horizontalLayout_11 = QHBoxLayout(self.generalInfoContainerWidget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.generalFrame1 = QFrame(self.generalInfoContainerWidget)
        self.generalFrame1.setObjectName(u"generalFrame1")
        self.generalFrame1.setFrameShape(QFrame.StyledPanel)
        self.generalFrame1.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.generalFrame1)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.categoryLabel = QLabel(self.generalFrame1)
        self.categoryLabel.setObjectName(u"categoryLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.categoryLabel)

        self.categoryComboBox = QComboBox(self.generalFrame1)
        self.categoryComboBox.setObjectName(u"categoryComboBox")
        self.categoryComboBox.setEditable(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.categoryComboBox)

        self.percentYieldLabel = QLabel(self.generalFrame1)
        self.percentYieldLabel.setObjectName(u"percentYieldLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.percentYieldLabel)

        self.percentYieldDoubleSpinBox = QDoubleSpinBox(self.generalFrame1)
        self.percentYieldDoubleSpinBox.setObjectName(u"percentYieldDoubleSpinBox")
        self.percentYieldDoubleSpinBox.setMaximum(1000.000000000000000)
        self.percentYieldDoubleSpinBox.setSingleStep(10.000000000000000)
        self.percentYieldDoubleSpinBox.setValue(100.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.percentYieldDoubleSpinBox)

        self.revisionStatusLabel = QLabel(self.generalFrame1)
        self.revisionStatusLabel.setObjectName(u"revisionStatusLabel")
        self.revisionStatusLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.revisionStatusLabel)

        self.widget_2 = QWidget(self.generalFrame1)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.revisionCheckBox = QCheckBox(self.widget_2)
        self.revisionCheckBox.setObjectName(u"revisionCheckBox")
        self.revisionCheckBox.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.revisionCheckBox)

        self.notRevisionCheckBox = QCheckBox(self.widget_2)
        self.notRevisionCheckBox.setObjectName(u"notRevisionCheckBox")

        self.horizontalLayout_6.addWidget(self.notRevisionCheckBox)


        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.widget_2)

        self.previousVersionNumberLabel = QLabel(self.generalFrame1)
        self.previousVersionNumberLabel.setObjectName(u"previousVersionNumberLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.previousVersionNumberLabel)

        self.previousVersionNumberLineEdit = QLineEdit(self.generalFrame1)
        self.previousVersionNumberLineEdit.setObjectName(u"previousVersionNumberLineEdit")
        self.previousVersionNumberLineEdit.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.previousVersionNumberLineEdit)

        self.previousFormulaLabel = QLabel(self.generalFrame1)
        self.previousFormulaLabel.setObjectName(u"previousFormulaLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.previousFormulaLabel)

        self.previousFormulaNameLineEdit = QLineEdit(self.generalFrame1)
        self.previousFormulaNameLineEdit.setObjectName(u"previousFormulaNameLineEdit")
        self.previousFormulaNameLineEdit.setReadOnly(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.previousFormulaNameLineEdit)

        self.horizontalLayout_11.addWidget(self.generalFrame1)

        self.generalFrame2 = QFrame(self.generalInfoContainerWidget)
        self.generalFrame2.setObjectName(u"generalFrame2")
        self.generalFrame2.setFrameShape(QFrame.StyledPanel)
        self.generalFrame2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.generalFrame2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.generalNutritionalsHeaderWidget = QWidget(self.generalFrame2)
        self.generalNutritionalsHeaderWidget.setObjectName(u"generalNutritionalsHeaderWidget")
        self.horizontalLayout_12 = QHBoxLayout(self.generalNutritionalsHeaderWidget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.generalNutritionalsHeaderLabel = QLabel(self.generalNutritionalsHeaderWidget)
        self.generalNutritionalsHeaderLabel.setObjectName(u"generalNutritionalsHeaderLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generalNutritionalsHeaderLabel.sizePolicy().hasHeightForWidth())
        self.generalNutritionalsHeaderLabel.setSizePolicy(sizePolicy)
        self.generalNutritionalsHeaderLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.generalNutritionalsHeaderLabel)


        self.verticalLayout_14.addWidget(self.generalNutritionalsHeaderWidget)

        self.widget = QWidget(self.generalFrame2)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.servingSizeLabel_2 = QLabel(self.widget)
        self.servingSizeLabel_2.setObjectName(u"servingSizeLabel_2")
        self.servingSizeLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.servingSizeLabel_2, 1, 0, 1, 1)

        self.totalCarbsLabel = QLabel(self.widget)
        self.totalCarbsLabel.setObjectName(u"totalCarbsLabel")

        self.gridLayout.addWidget(self.totalCarbsLabel, 5, 0, 1, 1)

        self.servingWeightLabel = QLabel(self.widget)
        self.servingWeightLabel.setObjectName(u"servingWeightLabel")
        self.servingWeightLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.servingWeightLabel, 2, 0, 1, 1)

        self.dietaryFiberLabel = QLabel(self.widget)
        self.dietaryFiberLabel.setObjectName(u"dietaryFiberLabel")

        self.gridLayout.addWidget(self.dietaryFiberLabel, 9, 0, 1, 1)

        self.caloriesPlaceholderLabel = QLabel(self.widget)
        self.caloriesPlaceholderLabel.setObjectName(u"caloriesPlaceholderLabel")

        self.gridLayout.addWidget(self.caloriesPlaceholderLabel, 3, 1, 1, 1)

        self.totalFatLabel = QLabel(self.widget)
        self.totalFatLabel.setObjectName(u"totalFatLabel")

        self.gridLayout.addWidget(self.totalFatLabel, 4, 0, 1, 1)

        self.totalCarbsPlaceholderLabel = QLabel(self.widget)
        self.totalCarbsPlaceholderLabel.setObjectName(u"totalCarbsPlaceholderLabel")

        self.gridLayout.addWidget(self.totalCarbsPlaceholderLabel, 5, 1, 1, 1)

        self.sugarLabel = QLabel(self.widget)
        self.sugarLabel.setObjectName(u"sugarLabel")

        self.gridLayout.addWidget(self.sugarLabel, 6, 0, 1, 1)

        self.totalFatPlaceholderLabel = QLabel(self.widget)
        self.totalFatPlaceholderLabel.setObjectName(u"totalFatPlaceholderLabel")

        self.gridLayout.addWidget(self.totalFatPlaceholderLabel, 4, 1, 1, 1)

        self.servingSizePlaceholderLabel = QLabel(self.widget)
        self.servingSizePlaceholderLabel.setObjectName(u"servingSizePlaceholderLabel")

        self.gridLayout.addWidget(self.servingSizePlaceholderLabel, 1, 1, 1, 1)

        self.addedSugarLabel = QLabel(self.widget)
        self.addedSugarLabel.setObjectName(u"addedSugarLabel")

        self.gridLayout.addWidget(self.addedSugarLabel, 7, 0, 1, 1)

        self.sugarsPlaceholderLabel = QLabel(self.widget)
        self.sugarsPlaceholderLabel.setObjectName(u"sugarsPlaceholderLabel")

        self.gridLayout.addWidget(self.sugarsPlaceholderLabel, 6, 1, 1, 1)

        self.calorieLabel = QLabel(self.widget)
        self.calorieLabel.setObjectName(u"calorieLabel")

        self.gridLayout.addWidget(self.calorieLabel, 3, 0, 1, 1)

        self.dietaryFiberPlaceholderLabel = QLabel(self.widget)
        self.dietaryFiberPlaceholderLabel.setObjectName(u"dietaryFiberPlaceholderLabel")

        self.gridLayout.addWidget(self.dietaryFiberPlaceholderLabel, 9, 1, 1, 1)

        self.servingWeightPlaceholder = QLabel(self.widget)
        self.servingWeightPlaceholder.setObjectName(u"servingWeightPlaceholder")

        self.gridLayout.addWidget(self.servingWeightPlaceholder, 2, 1, 1, 1)

        self.proteinLabel = QLabel(self.widget)
        self.proteinLabel.setObjectName(u"proteinLabel")

        self.gridLayout.addWidget(self.proteinLabel, 8, 0, 1, 1)

        self.addedSugarPlaceholderLabel = QLabel(self.widget)
        self.addedSugarPlaceholderLabel.setObjectName(u"addedSugarPlaceholderLabel")

        self.gridLayout.addWidget(self.addedSugarPlaceholderLabel, 7, 1, 1, 1)

        self.proteinPlaceholderLabel = QLabel(self.widget)
        self.proteinPlaceholderLabel.setObjectName(u"proteinPlaceholderLabel")

        self.gridLayout.addWidget(self.proteinPlaceholderLabel, 8, 1, 1, 1)

        self.totalWeightLabel = QLabel(self.widget)
        self.totalWeightLabel.setObjectName(u"totalWeightLabel")
        self.totalWeightLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.totalWeightLabel, 0, 0, 1, 1)

        self.totalWeightPlaceholderLabel = QLabel(self.widget)
        self.totalWeightPlaceholderLabel.setObjectName(u"totalWeightPlaceholderLabel")

        self.gridLayout.addWidget(self.totalWeightPlaceholderLabel, 0, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.widget)

        self.displayNFPBtn = QPushButton(self.generalFrame2)
        self.displayNFPBtn.setObjectName(u"displayNFPBtn")

        self.verticalLayout_14.addWidget(self.displayNFPBtn)


        self.horizontalLayout_11.addWidget(self.generalFrame2)

        self.verticalLayout_11.addWidget(self.generalInfoContainerWidget)

        self.ingTabLine2 = QFrame(self.ingredientsTab)
        self.ingTabLine2.setObjectName(u"ingTabLine2")
        self.ingTabLine2.setFrameShape(QFrame.HLine)
        self.ingTabLine2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.ingTabLine2)

        self.formulaIngredientHeaderWidget = QWidget(self.ingredientsTab)
        self.formulaIngredientHeaderWidget.setObjectName(u"formulaIngredientHeaderWidget")
        self.horizontalLayout_10 = QHBoxLayout(self.formulaIngredientHeaderWidget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.formulaIngredientSearchLineEdit = QLineEdit(self.formulaIngredientHeaderWidget)
        self.formulaIngredientSearchLineEdit.setObjectName(u"formulaIngredientSearchLineEdit")

        self.horizontalLayout_10.addWidget(self.formulaIngredientSearchLineEdit)

        self.formulaIngredientSearchBtn = QPushButton(self.formulaIngredientHeaderWidget)
        self.formulaIngredientSearchBtn.setObjectName(u"formulaIngredientSearchBtn")
        self.horizontalLayout_10.addWidget(self.formulaIngredientSearchBtn)

        self.removeSelectedBtn = QPushButton(self.formulaIngredientHeaderWidget)
        self.removeSelectedBtn.setObjectName(u"removeSelectedBtn")
        self.removeSelectedBtn.setText(u"Remove Selected")
        self.horizontalLayout_10.addWidget(self.removeSelectedBtn)

        self.verticalLayout_11.addWidget(self.formulaIngredientHeaderWidget)

        self.ingTabFormulaTableWidget = QTableWidget(self.ingredientsTab)
        if (self.ingTabFormulaTableWidget.columnCount() < 6):
            self.ingTabFormulaTableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.ingTabFormulaTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ingTabFormulaTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ingTabFormulaTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.ingTabFormulaTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ingTabFormulaTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.ingTabFormulaTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
    
        self.ingTabFormulaTableWidget.setObjectName(u"ingTabFormulaTableWidget")
        #self.ingTabFormulaTableWidget.horizontalHeader().setStretchLastSection(True)
        self.ingTabFormulaTableWidget.horizontalHeader().setStretchLastSection(False)
        self.ingTabFormulaTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.ingTabFormulaTableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.ingTabFormulaTableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.ingTabFormulaTableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        #self.ingTabFormulaTableWidget.setColumnWidth(0, 300)   

        self.verticalLayout_11.addWidget(self.ingTabFormulaTableWidget)

        self.formulaEditorTabWidget.addTab(self.ingredientsTab, "")
        self.qualityTab = QWidget()
        self.qualityTab.setObjectName(u"qualityTab")
        self.verticalLayout_8 = QVBoxLayout(self.qualityTab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.qualityTabScrollArea = QScrollArea(self.qualityTab)
        self.qualityTabScrollArea.setObjectName(u"qualityTabScrollArea")
        self.qualityTabScrollArea.setWidgetResizable(True)
        self.qualityTabScrollAreaContents = QWidget()
        self.qualityTabScrollAreaContents.setObjectName(u"qualityTabScrollAreaContents")
        self.qualityTabScrollAreaContents.setGeometry(QRect(0, 0, 750, 924))
        
        self.verticalLayout_7 = QVBoxLayout(self.qualityTabScrollAreaContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.qualityAttributeFrame = QFrame(self.qualityTabScrollAreaContents)
        self.qualityAttributeFrame.setObjectName(u"qualityAttributeFrame")
        self.qualityAttributeFrame.setFrameShape(QFrame.StyledPanel)
        self.qualityAttributeFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10 = QVBoxLayout(self.qualityAttributeFrame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.qualityAttributeHeaderWidget = QWidget(self.qualityAttributeFrame)
        self.qualityAttributeHeaderWidget.setObjectName(u"qualityAttributeHeaderWidget")

        self.horizontalLayout_13 = QHBoxLayout(self.qualityAttributeHeaderWidget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")

        self.inputQualityAttributeLabel = QLabel(self.qualityAttributeHeaderWidget)
        self.inputQualityAttributeLabel.setObjectName(u"inputQualityAttributeLabel")
        sizePolicy.setHeightForWidth(self.inputQualityAttributeLabel.sizePolicy().hasHeightForWidth())
        self.inputQualityAttributeLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.inputQualityAttributeLabel)

        self.attributeSpacer1 = QSpacerItem(398, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.attributeSpacer1)
        self.addQAttributeBtn = QPushButton(self.qualityAttributeHeaderWidget)
        self.addQAttributeBtn.setObjectName(u"addQAttributeBtn")

        self.horizontalLayout_13.addWidget(self.addQAttributeBtn)


        self.verticalLayout_10.addWidget(self.qualityAttributeHeaderWidget)

        

        self.qualityAttributeTableWidget = QTableWidget(self.qualityAttributeFrame)
        if (self.qualityAttributeTableWidget.columnCount() < 3):
            self.qualityAttributeTableWidget.setColumnCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.qualityAttributeTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.qualityAttributeTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.qualityAttributeTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        if (self.qualityAttributeTableWidget.rowCount() < 1):
            self.qualityAttributeTableWidget.setRowCount(1)
        self.qualityAttributeTableWidget.setObjectName(u"qualityAttributeTableWidget")
        self.qualityAttributeTableWidget.setRowCount(1)
        self.qualityAttributeTableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.qualityAttributeTableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_10.addWidget(self.qualityAttributeTableWidget)


        self.verticalLayout_7.addWidget(self.qualityAttributeFrame)

        self.ingStatementFrame = QFrame(self.qualityTabScrollAreaContents)
        self.ingStatementFrame.setObjectName(u"ingStatementFrame")
        self.ingStatementFrame.setFrameShape(QFrame.StyledPanel)
        self.ingStatementFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.ingStatementFrame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.ingStatementHeader = QWidget(self.ingStatementFrame)
        self.ingStatementHeader.setObjectName(u"ingStatementHeader")
        self.horizontalLayout_7 = QHBoxLayout(self.ingStatementHeader)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.ingStatementLabel = QLabel(self.ingStatementHeader)
        self.ingStatementLabel.setObjectName(u"ingStatementLabel")
        self.ingStatementLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.ingStatementLabel)


        self.verticalLayout_9.addWidget(self.ingStatementHeader)

        self.ingStatementTable = QTableWidget(self.ingStatementFrame)
        if (self.ingStatementTable.columnCount() < 3):
            self.ingStatementTable.setColumnCount(3)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.ingStatementTable.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.ingStatementTable.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.ingStatementTable.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        self.ingStatementTable.setObjectName(u"ingStatementTable")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ingStatementTable.sizePolicy().hasHeightForWidth())
        self.ingStatementTable.setSizePolicy(sizePolicy2)
        self.ingStatementTable.setMinimumSize(QSize(0, 100))
        self.ingStatementTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ingStatementTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ingStatementTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ingStatementTable.setAlternatingRowColors(True)
        self.ingStatementTable.setSortingEnabled(False)
        self.ingStatementTable.horizontalHeader().setStretchLastSection(True)
        self.ingStatementTable.setWordWrap(True)

        

        self.verticalLayout_9.addWidget(self.ingStatementTable)

        self.ingStatementContainer = QWidget(self.ingStatementFrame)
        self.ingStatementContainer.setObjectName(u"ingStatementContainer")
        self.ingStatementContainer.setFocusPolicy(Qt.NoFocus)
        self.ingStatementContainer.setAutoFillBackground(False)
        self.verticalLayout_6 = QVBoxLayout(self.ingStatementContainer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ingStatetmentTxtLabel = QLabel(self.ingStatementContainer)
        self.ingStatetmentTxtLabel.setObjectName(u"ingStatetmentTxtLabel")
        self.ingStatetmentTxtLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.ingStatetmentTxtLabel)

        self.ingStatementTextBox = QTextEdit(self.ingStatementContainer)
        self.ingStatementTextBox.setObjectName(u"ingStatementTextBox")
        self.ingStatementTextBox.setReadOnly(True)

        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ingStatementTextBox.sizePolicy().hasHeightForWidth())
        self.ingStatementTextBox.setSizePolicy(sizePolicy3)

        self.verticalLayout_6.addWidget(self.ingStatementTextBox)

        self.ingStatementButtonBox = QWidget(self.ingStatementContainer)
        self.ingStatementButtonBox.setObjectName(u"ingStatementButtonBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ingStatementButtonBox.sizePolicy().hasHeightForWidth())
        self.ingStatementButtonBox.setSizePolicy(sizePolicy4)
        self.horizontalLayout_8 = QHBoxLayout(self.ingStatementButtonBox)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

        self.editIngStatementBtn = QPushButton(self.ingStatementButtonBox)
        self.editIngStatementBtn.setObjectName(u"editIngStatementBtn")

        self.horizontalLayout_8.addWidget(self.editIngStatementBtn)

        self.copyIngStatementBtn = QPushButton(self.ingStatementButtonBox)
        self.copyIngStatementBtn.setObjectName(u"copyIngStatementBtn")

        self.horizontalLayout_8.addWidget(self.copyIngStatementBtn)

        self.ingStatementPrintBtn = QPushButton(self.ingStatementButtonBox)
        self.ingStatementPrintBtn.setObjectName(u"ingStatementPrintBtn")

        self.horizontalLayout_8.addWidget(self.ingStatementPrintBtn)


        self.verticalLayout_6.addWidget(self.ingStatementButtonBox)


        self.verticalLayout_9.addWidget(self.ingStatementContainer)


        self.verticalLayout_7.addWidget(self.ingStatementFrame)

        self.qualityTabScrollArea.setWidget(self.qualityTabScrollAreaContents)
        self.qualityTabScrollArea.setFrameStyle(QFrame.NoFrame)

        self.verticalLayout_8.addWidget(self.qualityTabScrollArea)

        self.formulaEditorTabWidget.addTab(self.qualityTab, "")
        self.labelTab = QWidget()
        self.labelTab.setObjectName(u"labelTab")
        self.verticalLayout_3 = QVBoxLayout(self.labelTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelScrollArea = QScrollArea(self.labelTab)
        self.labelScrollArea.setObjectName(u"labelScrollArea")
        self.labelScrollArea.setWidgetResizable(True)
        self.labelScrollAreaContents = QWidget()
        self.labelScrollAreaContents.setObjectName(u"labelScrollAreaContents")
        self.labelScrollAreaContents.setGeometry(QRect(0, 0, 750, 890))
        self.verticalLayout_4 = QVBoxLayout(self.labelScrollAreaContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.scaleFrame = QFrame(self.labelScrollAreaContents)
        self.scaleFrame.setObjectName(u"scaleFrame")
        self.scaleFrame.setFrameShape(QFrame.StyledPanel)
        self.scaleFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.scaleFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scalingHeaderLabel = QLabel(self.scaleFrame)
        self.scalingHeaderLabel.setObjectName(u"scalingHeaderLabel")


        sizePolicy.setHeightForWidth(self.scalingHeaderLabel.sizePolicy().hasHeightForWidth())
        self.scalingHeaderLabel.setSizePolicy(sizePolicy)
        self.scalingHeaderLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.scalingHeaderLabel)

        self.scaleByLabel = QLabel(self.scaleFrame)
        self.scaleByLabel.setObjectName(u"scaleByLabel")
        self.scaleByLabel.setText("How should we scale the formula entered? (Choose one)")
        self.scaleByLabel.setAlignment(Qt.AlignLeft)
        self.verticalLayout.addWidget(self.scaleByLabel)

        self.scaleCombobox = QComboBox(self.scaleFrame)
        servingsItem = QStandardItem()
        servingsItem.setText('Total Number of Servings')
        servingsItem.setData('servings', Qt.UserRole)
        weightItem = QStandardItem()
        weightItem.setText('Weight of One Serving')
        weightItem.setData('weight', Qt.UserRole)
        itemModel = QStandardItemModel()
        itemModel.appendRow(servingsItem) 
        itemModel.appendRow(weightItem)
        self.scaleCombobox.setModel(itemModel)
        self.scaleCombobox.setCurrentIndex(-1)

        self.verticalLayout.addWidget(self.scaleCombobox)

        self.scaleByServingsWidget = QWidget(self.scaleFrame)
        self.scaleByServingsWidget.setObjectName(u"scaleByServingsWidget")
        sizePolicy.setHeightForWidth(self.scaleByServingsWidget.sizePolicy().hasHeightForWidth())
        self.scaleByServingsWidget.setSizePolicy(sizePolicy)
        self.scaleByServingsWidget.setDisabled(True)
        self.horizontalLayout_4 = QHBoxLayout(self.scaleByServingsWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.questionLabel2 = QLabel()
        self.questionLabel2.setText('How many servings does the inputted formula make?')
        self.horizontalLayout_4.addWidget(self.questionLabel2)

        self.scaleRecipeSpacer = QSpacerItem(0,0,QSizePolicy.MinimumExpanding,QSizePolicy.Minimum)
        self.horizontalLayout_4.addSpacerItem(self.scaleRecipeSpacer)

        self.numServingsSpinbox = QDoubleSpinBox(self.scaleByServingsWidget)
        self.numServingsSpinbox.setObjectName(u"numServingsSpinbox")
        self.numServingsSpinbox.setValue(1)
        self.numServingsSpinbox.setMinimumWidth(100)
        self.numServingsSpinbox.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.numServingsSpinbox)

        self.servingsLabel = QLabel(self.scaleByServingsWidget)
        self.servingsLabel.setObjectName(u"servingsLabel")

        self.horizontalLayout_4.addWidget(self.servingsLabel)


        self.verticalLayout.addWidget(self.scaleByServingsWidget)

        self.scaleByWeightWidget = QWidget(self.scaleFrame)
        self.scaleByWeightWidget.setObjectName(u"scaleByWeightWidget")
        sizePolicy.setHeightForWidth(self.scaleByWeightWidget.sizePolicy().hasHeightForWidth())
        self.scaleByWeightWidget.setSizePolicy(sizePolicy)
        self.scaleByWeightWidget.setDisabled(True)
        self.horizontalLayout_5 = QHBoxLayout(self.scaleByWeightWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.questionLabel1 = QLabel(self.scaleByWeightWidget)
        self.questionLabel1.setText('How much does 1 serving weigh?')
        self.horizontalLayout_5.addWidget(self.questionLabel1)

        self.servingWeightSpinBox = QSpinBox(self.scaleByWeightWidget)
        self.servingWeightSpinBox.setObjectName(u"servingWeightSpinBox")
        self.servingWeightSpinBox.setMaximum(5000)
        self.servingWeightSpinBox.setMinimum(0)
        self.servingWeightSpinBox.setSingleStep(10)
        self.servingWeightSpinBox.setAlignment(Qt.AlignCenter)


        self.horizontalLayout_5.addWidget(self.servingWeightSpinBox)

        self.unitWeightCombobox = QComboBox(self.scaleByWeightWidget)
        self.unitWeightCombobox.setObjectName(u"unitWeightCombobox")

        self.horizontalLayout_5.addWidget(self.unitWeightCombobox)


        self.verticalLayout.addWidget(self.scaleByWeightWidget)

        self.verticalLayout_4.addWidget(self.scaleFrame)


        self.servingInfoFrame = QFrame(self.labelScrollAreaContents)
        self.servingInfoFrame.setObjectName(u"servingInfoFrame")
        self.servingInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.servingInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.servingInfoFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.servingInfoLabelHeader = QLabel(self.servingInfoFrame)
        self.servingInfoLabelHeader.setObjectName(u"servingInfoLabelHeader")
        sizePolicy.setHeightForWidth(self.servingInfoLabelHeader.sizePolicy().hasHeightForWidth())
        self.servingInfoLabelHeader.setSizePolicy(sizePolicy)
        self.servingInfoLabelHeader.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.servingInfoLabelHeader)

        self.servingSizeWidget = QWidget(self.servingInfoFrame)
        self.servingSizeWidget.setObjectName(u"servingSizeWidget")
        sizePolicy.setHeightForWidth(self.servingSizeWidget.sizePolicy().hasHeightForWidth())
        self.servingSizeWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.servingSizeWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.servingSizeLabel = QLabel(self.servingSizeWidget)
        self.servingSizeLabel.setObjectName(u"servingSizeLabel")

        self.horizontalLayout_3.addWidget(self.servingSizeLabel)

        self.servingSizeLineEdit = QLineEdit(self.servingSizeWidget)
        self.servingSizeLineEdit.setObjectName(u"servingSizeLineEdit")

        self.horizontalLayout_3.addWidget(self.servingSizeLineEdit)

        self.calculatedServingSizeLabel = QLabel(self.servingSizeWidget)
        self.calculatedServingSizeLabel.setObjectName(u"calculatedServingSizeLabel")

        self.horizontalLayout_3.addWidget(self.calculatedServingSizeLabel)

        self.servingSizeWidgetSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.servingSizeWidgetSpacer)

        self.hideServingSizeCheckbox = QCheckBox(self.servingSizeWidget)
        self.hideServingSizeCheckbox.setObjectName(u"hideServingSizeCheckbox")

        self.horizontalLayout_3.addWidget(self.hideServingSizeCheckbox)


        self.verticalLayout_2.addWidget(self.servingSizeWidget)

        self.servingsPerWidget = QWidget(self.servingInfoFrame)
        self.servingsPerWidget.setObjectName(u"servingsPerWidget")
        sizePolicy.setHeightForWidth(self.servingsPerWidget.sizePolicy().hasHeightForWidth())
        self.servingsPerWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.servingsPerWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.servingsPerSpinbox = QSpinBox(self.servingsPerWidget)
        self.servingsPerSpinbox.setObjectName(u"servingsPerSpinbox")
        self.servingsPerSpinbox.setValue(1)

        self.horizontalLayout_2.addWidget(self.servingsPerSpinbox)

        self.servingsComboBox = QComboBox(self.servingsPerWidget)
        self.servingsComboBox.addItem("")
        self.servingsComboBox.addItem("")
        self.servingsComboBox.setObjectName(u"servingsComboBox")
        self.servingsComboBox.setEditable(False)

        self.horizontalLayout_2.addWidget(self.servingsComboBox)

        self.perContainerLabel = QLabel(self.servingsPerWidget)
        self.perContainerLabel.setObjectName(u"perContainerLabel")

        self.horizontalLayout_2.addWidget(self.perContainerLabel)

        self.servingsPerSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.servingsPerSpacer)

        self.hidePerContainerCheckBox = QCheckBox(self.servingsPerWidget)
        self.hidePerContainerCheckBox.setObjectName(u"hidePerContainerCheckBox")

        self.horizontalLayout_2.addWidget(self.hidePerContainerCheckBox)


        self.verticalLayout_2.addWidget(self.servingsPerWidget)

        # add nutrition label example
        self.exampleWidget = QWidget(self.servingInfoFrame)
        self.nfpPlaceholder = QLabel()
        nfpPixmap = QPixmap(QSize())
        nfpPixmap.load('pjrd/static/media/nutrition-facts-label.png')
        nfpPixmap = nfpPixmap.scaledToHeight(400, Qt.SmoothTransformation)
        self.nfpPlaceholder.setPixmap(nfpPixmap)
        self.verticalLayout_2.addWidget(self.nfpPlaceholder)
   
        self.verticalLayout_4.addWidget(self.servingInfoFrame)


        self.verticalSpacer = QSpacerItem(20,60, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_4.addSpacerItem(self.verticalSpacer)

        self.labelScrollArea.setWidget(self.labelScrollAreaContents)

        self.verticalLayout_3.addWidget(self.labelScrollArea)

        self.displayNutritionalLabelBtn = QPushButton(self.labelTab)
        self.displayNutritionalLabelBtn.setObjectName(u"displayNutritionalLabelBtn")
        self.displayNutritionalLabelBtn.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_3.addWidget(self.displayNutritionalLabelBtn, 0, Qt.AlignHCenter)


        self.formulaEditorTabWidget.addTab(self.labelTab, "")
        self.nutrientReportTab = QWidget()
        self.nutrientReportTab.setObjectName(u"nutrientReportTab")
        self.verticalLayout_15 = QVBoxLayout(self.nutrientReportTab)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.nutrientReportScrollArea = QScrollArea(self.nutrientReportTab)
        self.nutrientReportScrollArea.setObjectName(u"nutrientReportScrollArea")
        self.nutrientReportScrollArea.setWidgetResizable(True)
        self.nutrientReportScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 793, 714))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.nutrientSpreadsheetLabel = QLabel(self.scrollAreaWidgetContents)
        self.nutrientSpreadsheetLabel.setObjectName(u"nutrientSpreadsheetLabel")

        self.verticalLayout_5.addWidget(self.nutrientSpreadsheetLabel)

        self.spreadSheetBasedOnLabel = QLabel(self.scrollAreaWidgetContents)
        self.spreadSheetBasedOnLabel.setObjectName(u"spreadSheetBasedOnLabel")
        self.spreadSheetBasedOnLabel.setText('Add an ingredient to update')
        self.verticalLayout_5.addWidget(self.spreadSheetBasedOnLabel)

        self.nutrientReportTableView = QTableView(self.scrollAreaWidgetContents)
        self.nutrientReportTableView.setMinimumHeight(275)
        self.nutrientReportTableView.setHorizontalScrollBarPolicy((Qt.ScrollBarAlwaysOn))
        self.nutrientReportTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.nutrientReportTableView.setAlternatingRowColors(True) # Might remove this
        self.nutrientReportTableView.setSortingEnabled(True)
        font = QFont()
        font.setPointSize(10)
        self.nutrientReportTableView.setFont(font)
        self.nutrientReportTableView.setObjectName(u"nutrientReportTableView")
        headerLabels = ['Item Desc', 'Quantity', 'Unit', 'Weight (g)', 'Calories (kCal)', 'Protein (g)', 'Carbohydrates (g)', 'Dietary Fiber (g)', 'Soluble Fiber (g)', 'Total Sugar (g)', 'Added Sugar (g)', 'Monosac (g)', 'Disac (g)', 'Total Fat (g)', 'Sat Fat (g)', 'Trans Fat (g)', 'Mono Unsat Fat (g)', 'Poly Unsat Fat (g)', 'Total Unsat Fat (g)', 'Omega-3 FA (g)', 'Omega-6 FA (g)', 'Cholestrol (mg)', 'Water (g)', 'Alcohol (g)', 'Caffeine (mg)', 'Choline (mg)', 'Sugar Alcohol (g)', 'Calcium (mg)', 'Chromium (µg)', 'Copper (mg)', 'Fluoride (mg)', 'Iodine (µg)', 'Iron (mg)', 'Magnesium (mg)', 'Manganese (mg)', 'Molybdenum (µg)', 'Phosphorus (mg)', 'Potassium (mg)', 'Selenium (µg)', 'Sodium (mg)', 'Zinc (mg)', 'Vitamin A (IU)', 'Vitamin A - RE (µg)', 'Vitamin A - RAE (µg)', 'Vitamin B1/Thiamin (mg)', 'Vitamin B2/Riboflavin (mg)', 'Vitamin B3/Niacin (mg)', 'Vitamin B3/Niac. Eq (mg)', 'Vitamin B6 (mg)', 'Vitamin B12 (µg)', 'Vitamin C (mg)', 'Vitamin D (IU)', 'Vitamin E/Alpha-toco (mg)', 'Folate (µg)', 'Folate, DFE (µg DFE)', 'Vitamin K (µg)', 'Panothenic Acid (mg)']


        model = CustomTableModel(headerLabels)
        self.nutrientReportTableView.setModel(model)
        self.nutrientReportTableView.setColumnWidth(0, 200)

        self.verticalLayout_5.addWidget(self.nutrientReportTableView)

        self.horizLine1 = QFrame(self.scrollAreaWidgetContents)
        self.horizLine1.setObjectName(u"horizLine1")
        self.horizLine1.setFrameShape(QFrame.HLine)
        self.horizLine1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.horizLine1)

        self.singleNutrientLabel = QLabel(self.scrollAreaWidgetContents)
        self.singleNutrientLabel.setObjectName(u"singleNutrientLabel")

        self.verticalLayout_5.addWidget(self.singleNutrientLabel)

        self.disclaimerLabel = QLabel(self.scrollAreaWidgetContents)
        self.disclaimerLabel.setText('Disclaimer: A 0% indicates may be due to no data being entered, or that there is no content in the food.')
        disclaimerFont = QFont()
        disclaimerFont.setPointSize(10)
        self.disclaimerLabel.setFont(disclaimerFont)
        self.verticalLayout_5.addWidget(self.disclaimerLabel)


        self.nutrientReportCombobox = QComboBox(self.scrollAreaWidgetContents)
        self.nutrientReportCombobox.setObjectName(u"nutrientReportCombobox")
        self.nutrientReportCombobox.setCurrentText(u"")

        self.verticalLayout_5.addWidget(self.nutrientReportCombobox)

        self.singleNutrientChartView = QtCharts.QChartView(self.scrollAreaWidgetContents)
        self.singleNutrientChartView.setObjectName(u"singleNutrientChartView")
        self.singleNutrientChartView.setMinimumHeight(300)

        self.verticalLayout_5.addWidget(self.singleNutrientChartView)

        self.horizLine2 = QFrame(self.scrollAreaWidgetContents)
        self.horizLine2.setObjectName(u"horizLine2")
        self.horizLine2.setFrameShape(QFrame.HLine)
        self.horizLine2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.horizLine2)

        self.dailyValueLabel = QLabel(self.scrollAreaWidgetContents)
        self.dailyValueLabel.setObjectName(u"dailyValueLabel")

        self.verticalLayout_5.addWidget(self.dailyValueLabel)

        self.dvToggleBtn = QPushButton(self.scrollAreaWidgetContents)
        self.dvToggleBtn.setObjectName(u"dvToggleBtn")
        self.dvToggleBtn.setText('Show')

        self.verticalLayout_5.addWidget(self.dvToggleBtn)

        self.horizLine3 = QFrame(self.scrollAreaWidgetContents)
        self.horizLine3.setObjectName(u"horizLine3")
        self.horizLine3.setFrameShape(QFrame.HLine)
        self.horizLine3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.horizLine3)

        self.byComparisonLabel = QLabel(self.scrollAreaWidgetContents)
        self.byComparisonLabel.setObjectName(u"byComparisonLabel")
        
        self.verticalLayout_5.addWidget(self.byComparisonLabel)

        self.showComparisonBtn = QPushButton(self.scrollAreaWidgetContents)
        self.showComparisonBtn.setText('Show')
    
        self.verticalLayout_5.addWidget(self.showComparisonBtn)

        self.comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setObjectName(u"comboBox")
        
        self.verticalLayout_5.addWidget(self.comboBox)

        self.nutrientReportScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_15.addWidget(self.nutrientReportScrollArea)

        self.formulaEditorTabWidget.addTab(self.nutrientReportTab, "")
        self.imagesTab = QWidget()
        self.imagesTab.setObjectName(u"imagesTab")
        self.verticalLayout_12 = QVBoxLayout(self.imagesTab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.imagesTableWidget = QTableWidget(self.imagesTab)
        if (self.imagesTableWidget.columnCount() < 2):
            self.imagesTableWidget.setColumnCount(2)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.imagesTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.imagesTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem76)
        self.imagesTableWidget.setObjectName(u"imagesTableWidget")
        self.imagesTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.imagesTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.imagesTableWidget.horizontalHeader().setDefaultSectionSize(260)
        self.imagesTableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_12.addWidget(self.imagesTableWidget)

        self.formulaEditorTabWidget.addTab(self.imagesTab, "")

        self.horizontalLayout_9.addWidget(self.formulaEditorTabWidget)

        self.ingTabFormulaTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ingTabFormulaTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.retranslateUi(Dialog)

        self.formulaEditorTabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def setupLogic(self):
        # signal setup
        self.formulaIngredientSearchBtn.clicked.connect(self.search)
        self.formulaIngredientSearchLineEdit.returnPressed.connect(self.search)
        self.displayNFPBtn.clicked.connect(displayNfp)
        self.removeSelectedBtn.clicked.connect(self.removeSelected)
        self.scaleCombobox.currentIndexChanged.connect(self.toggleFocus)
        self.dvToggleBtn.clicked.connect(self.openDVTableViewer)
        self.comboBox.currentIndexChanged.connect(self.openComparisonTableViewer)
        
        #temporary
        self.showComparisonBtn.clicked.connect(self.openComparisonTableViewer)

        ## TODO
        # Optimize the refresh method for less queryies to database
        self.servingWeightSpinBox.valueChanged.connect(self.refresh) #<----- could substitute for just refreshgeneralnutritionals and remove *arg for total weight 
        self.unitWeightCombobox.currentIndexChanged.connect(self.refresh)
        self.numServingsSpinbox.valueChanged.connect(self.refresh)
        ######
        self.editIngStatementBtn.clicked.connect(self.toggleReadOnly)
        self.copyIngStatementBtn.clicked.connect(self.copy)
        self.addQAttributeBtn.clicked.connect(self.insertRow)
        self.ingStatementPrintBtn.clicked.connect(self.printPreview)

        self.nutrientReportCombobox.currentIndexChanged.connect(self.nutrComparisonChosen)

        # event setup
        self.formulaIngredientSearchBtn.installEventFilter(self)
        # sets up all of the completer logic with appropriate data 
        with dbConnection('FormulaSchema').cursor() as cursor:
            # sets up the complter for the categories combobox
            cursor.execute('SELECT category_id, category_name FROM category WHERE scope = "formula"')
            categoriesDict = cursor.fetchall()
            categoryCompleter = QCompleter()
            categoryModel = QStandardItemModel()
            for category in categoriesDict:
                categoryItem = QStandardItem()
                categoryItem.setText(category['category_name'].title())
                categoryItem.setData(category, Qt.UserRole)
                categoryModel.appendRow(categoryItem)
            categoryCompleter.setModel(categoryModel)
            self.categoryComboBox.setCompleter(categoryCompleter)
            self.categoryComboBox.setModel(categoryModel)
            self.categoryComboBox.setCurrentIndex(-1)


            # sets up the completer for the formula combobox
            unitModel = QStandardItemModel()
            unitCompleter = QCompleter()
            cursor.execute('SELECT unit_id, unit_name, unit_symbol, conversion_factor, conversion_offset FROM unit WHERE unit_class = "mass" ORDER BY conversion_factor ASC')
            uoms = cursor.fetchall()
            for uom in uoms:
                unit = UnitOfMeasure(uom['unit_id'], uom['unit_name'], uom['conversion_factor'], uom['conversion_offset'], uom['unit_symbol'])
                unit.setText('{unitName} ({unitSymbol})'.format(unitName=uom['unit_name'], unitSymbol = uom['unit_symbol']))
                unitModel.appendRow(unit)
            unitCompleter.setModel(unitModel)
            unitCompleter.setCompletionMode(QCompleter.InlineCompletion)
            self.unitWeightCombobox.setModel(unitModel)
            self.unitWeightCombobox.setCurrentIndex(-1)

            # sets up the model for the compari
            compareModel = QStandardItemModel() 
            cursor.execute('SELECT formula.formula_id, formula.food_id, formula.formula_name, food.food_desc FROM formula LEFT JOIN food ON formula.food_id = food.food_id ORDER BY formula.formula_name ASC')
            compareFoods = cursor.fetchall()
            for cFood in compareFoods:
                compareItem = QStandardItem()
                compareItem.setText(cFood['food_desc'].capitalize())
                compareItem.setData(cFood, Qt.UserRole)
                compareModel.appendRow(compareItem)
            self.comboBox.setModel(compareModel)
            
            #excludes theobromine,  unsaturated fatty acids, retinol, beta carotene, alpha carotene, cryptoxanthinin, lycopene, luteine + zeaxanthinin, folic acid, folate, vitamin e added, vitamin b12 added, other carbs
            excluding = (263, 319, 321, 322, 334, 337, 338, 431, 432, 573, 578, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 626, 627, 628, 629, 630, 631, 662)
            ##### 
            # sets up completer for the nutrient 
            # completer for nutrient
            nutModel = QStandardItemModel()
            cursor.execute('SELECT nutrient_id, nutrient_name FROM nutrient WHERE nutrient_id NOT IN %s ', (excluding,))
            nuts = cursor.fetchall()
            for nut in nuts:
                nutItem = QStandardItem()
                nutItem.setText(nut['nutrient_name'].title())
                nutItem.setData(nut, Qt.UserRole)
                nutModel.appendRow(nutItem)
            self.nutrientReportCombobox.setModel(nutModel)
            self.nutrientReportCombobox.setCurrentIndex(-1)
        #####

    # Opens a separate QDialog containing the tableview with the nutrient report broken down by daily recommended value, per 100 gram, per serving and % Daily Value per serving    
    def openDVTableViewer(self):

        # for the daily value report 
        totalWeightG = self.getTotalTableWeight()
        map = nutrientRowMap()

        model = CustomTableModel()
        dvHeaders = ['Daily Recommended Value','Per 100g', 'Per Serving', '% Daily Value Per Serving']
        vHeaders = ['Calories (kCal)', 'Fat (g)', 'Saturated Fat (g)', 'Cholestrol (mg)', 'Total Carbohydrates (g)', 'Total Dietary Fiber (g)', 'Total Sugar (g)', 'Protein (g)', 'Vitamn A (µg RAE)', 'Vitamin B1/Thiamin (mg)', 'Vitamin B2/Riboflavin (mg)', 'Vitamin B3/Niacin (mg)', 'Vitamin B5/Panothenic Acid (mg)', 'Vitamin B6 (µg)', 'Vitamin B9/Folic Acid (mg)', 'Vitamin B12 (mg)', 'Vitamin C (mg)', 'Vitamin D (µg)', 'Vitamin E/Alpha-tocopherol (mg)', 'Vitamin K/Phylloquinone (µg)', 'Choline (mg)', 'Calcium (mg)', 'Copper (mg)', 'Iron (mg)', 'Magnesium (mg)', 'Manganese (mg)', 'Molybdenum (µg)','Phosphorus (mg)', 'Potassium (mg)', 'Selenium (µg)', 'Sodium (mg)', 'Zinc (mg)']
        model.setHeaderLabels(dvHeaders, Qt.Horizontal, Qt.DisplayRole)
        model.setHeaderLabels(vHeaders, Qt.Vertical, Qt.DisplayRole)
        data = initialize2DArray(len(vHeaders), len(dvHeaders), None)
        
        for row in range(self.ingTabFormulaTableWidget.rowCount()):
            ingredient = self.ingTabFormulaTableWidget.item(row, 0).data(Qt.UserRole)
            unitConversionScale = 1/ingredient.unit.conversionFactor
            
            amountOfIngG = ingredient.inputWeightInGrams()
            
            #####   X grams of nutrient/100 grams of ingredient = Z grams of nutrient/Y grams of ingredient (because nutrient_weight_g gives value as unscaled amount, we need to divide it by 100)
            # therefore 
            # Z grams of nutrient = (X grams of nutrient * Y grams of ingredient)/100  (ie. PER 100 grams)
            multiplyBy = amountOfIngG/100 
            
            foodID = ingredient.foodID

            with dbConnection('FormulaSchema').cursor() as cursor:
                cursor.execute('SELECT nutrient.nutrient_id, nutrient.nutrient_name, nutrient.daily_value_g, food_nutrient.nutrient_weight_g_per_100g * %s AS amount_in_g, unit.conversion_factor, unit.conversion_offset, unit.unit_name FROM nutrient LEFT JOIN food_nutrient ON nutrient.nutrient_id = food_nutrient.nutrient_id LEFT JOIN unit ON unit.unit_id = nutrient.unit_id WHERE food_nutrient.food_id = %s AND nutrient.nutrient_id IN (203, 204, 205, 208, 269, 291, 301, 303, 305, 309, 312, 317, 320, 323, 328, 401, 404, 405, 406, 415, 418, 421, 430, 431, 601, 606, 651, 656, 658)', (multiplyBy, foodID))
                results = cursor.fetchall()

            for result in results:
                nutrientID = result['nutrient_id']
                dailyValueInStdUnit = result['daily_value_g'] * unitConversionScale
                amountInStdUnit = result['amount_in_g'] * unitConversionScale
                per100g = amountInStdUnit * (100/totalWeightG) # <----- goes into
                rowIndex = map.get(nutrientID)
                try:
                    servingWeight = self.servingWeightSpinBox.value()
                    numberServings = totalWeightG/servingWeight
                except:
                    numberServings = 1
                else:
                    try:
                        numberServings = self.numServingsSpinbox.value()
                    except:
                        pass
                    else:
                        numberServings = 1
                        servingWeight = totalWeightG
                perServing = amountInStdUnit/numberServings 
                data[rowIndex][0] = dailyValueInStdUnit
                data[rowIndex][1] = per100g
                data[rowIndex][2] = perServing
                data[rowIndex][3] = '{}%'.format(round(((amountInStdUnit/dailyValueInStdUnit)*100), 1))
        model.inputTableData(data)

        view = QuickTableView(model, label="Comparison by Daily Value and 100 g")
        view.setSubheaderLabel('Percent daily values are based on a 2,000 calorie diet for healthy adults. Daily values last updated in 2016.')
        view.exec_()

    # Opens a separate QDialog containing the tableview for a comparison per 100g of current recipe vs recipe chosen
    def openComparisonTableViewer(self):
        totalWeightG = self.getTotalTableWeight()

        rowMap = compareTableRowMap()

        horizHeaders = ['Current (per 100g)', 'Comparison (per 100g)']
        vertHeaders = ['Calories (kCal)', 'Total Fat (g)', 'Saturated Fat (g)', 'Trans Fat (g)', 'Mono Unsat Fat (g)', 'Poly Unsat Fat (g)', 'Total Unsat Fat (g)','Omega-3 FA (g)', 'Omega-6 FA (g)', 'Cholestrol (mg)', 'Total Carbohydrates (g)', 'Total Dietary Fiber (g)', 'Total Sugar (g)', 'Added Sugar (g)', 'Monosaccharides (g)', 'Disaccharides (g)', 'Protein (g)', 'Vitamin A (IU)', 'Vitamin A - RE (µg)', 'Vitamin A - RAE (µg)', 'Vitamin B1/Thiamin (mg)', 'Vitamin B2/Riboflavin (mg)', 'Vitamin B3/Niacin (mg)', 'Vitamin B3/Niac. Eq (mg)', 'Vitamin B5/Panothenic Acid (mg)', 'Vitamin B6 (µg)', 'Vitamin B9/Folic Acid (mg)', 'Vitamin B12 (mg)', 'Vitamin C (mg)', 'Vitamin D (µg)', 'Vitamin D (IU)', 'Vitamin E/Alpha-tocopherol (mg)', 'Vitamin K/Phylloquinone (µg)', 'Choline (mg)', 'Calcium (mg)', 'Copper (mg)', 'Iron (mg)', 'Magnesium (mg)', 'Manganese (mg)', 'Phosphorus (mg)', 'Potassium (mg)', 'Selenium (µg)', 'Sodium (mg)', 'Zinc (mg)']
        model = CustomTableModel()
        model.setHeaderLabels(horizHeaders, Qt.Horizontal, Qt.DisplayRole)
        model.setHeaderLabels(vertHeaders, Qt.Vertical, Qt.DisplayRole)
        # temporary
        data = initialize2DArray(len(vertHeaders), len(horizHeaders), None)

        for row in range(self.ingTabFormulaTableWidget.rowCount()):
            ingredient = self.ingTabFormulaTableWidget.item(row, 0).data(Qt.UserRole)
            unitConversionScale = 1/ingredient.unit.conversionFactor
            amountOfIngG = ingredient.inputWeightInGrams()
            multiplyBy = amountOfIngG/100
            foodID = ingredient.foodID

            with dbConnection('FormulaSchema').cursor() as cursor:
                cursor.execute('SELECT nutrient.nutrient_id, nutrient.nutrient_name, nutrient.daily_value_g, food_nutrient.nutrient_weight_g_per_100g * %s AS amount_in_g, unit.conversion_factor, unit.conversion_offset, unit.unit_name FROM nutrient LEFT JOIN food_nutrient ON nutrient.nutrient_id = food_nutrient.nutrient_id LEFT JOIN unit ON unit.unit_id = nutrient.unit_id WHERE food_nutrient.food_id = %s AND nutrient.nutrient_id IN (203, 204, 205, 208, 269, 291, 301, 303, 305, 309, 312, 317, 320, 323, 328, 401, 404, 405, 406, 415, 418, 421, 430, 431, 601, 606, 651, 656, 658)', (multiplyBy, foodID))
                results = cursor.fetchall()

            for result in results:
                nutrientID = result['nutrient_id']
                amountInStdUnit = result['amount_in_g'] * unitConversionScale
                per100g = amountInStdUnit * (100/totalWeightG) # <----- goes into
                rowIndex = rowMap.get(nutrientID)
                if rowIndex is None:
                    continue
                print('This is row index' + str(rowIndex))
                data[rowIndex][0] = per100g
        model.inputTableData(data)

        #end temporary
        view = QuickTableView(model)
        view.setHeaderLabel('Comparison of the current formula and the chosen formula, each scaled to 100 g')
        view.exec_()

    # toggles the focus of the scale formula portion 
    @pyqtSlot()
    def toggleFocus(self):
        if self.scaleCombobox.currentIndex() == -1:
            return
        else:
            var = self.scaleCombobox.currentData(Qt.UserRole)
            # scale by weight
            if var == 'weight':
                self.scaleByWeightWidget.setEnabled(True)
                self.scaleByServingsWidget.setDisabled(True)
            # scale by number of servings
            if var == 'servings':
                self.scaleByServingsWidget.setEnabled(True)
                self.scaleByWeightWidget.setDisabled(True)
    
    # toggles the widget disabling affect 
    @pyqtSlot()
    def toggleReadOnly(self):
        # if the box is not editable, make editable and change button to done editing
        if self.ingStatementTextBox.isReadOnly():
            self.ingStatementTextBox.setReadOnly(False)
            self.editIngStatementBtn.setText('Finalize Edits')
        # if the box is editable
        else:
            self.ingStatementTextBox.setReadOnly(True)
            self.editIngStatementBtn.setText('Edit')


    # opens print preview for ingredient statement
    @pyqtSlot()
    def printPreview(self):
        dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.ingStatementTextBox.print_)
        dialog.exec_()
    
    # copies ingredient statement to user clipboard
    @pyqtSlot()
    def copy(self):
        text = self.ingStatementTextBox.toPlainText()
        text = text.replace("<b>", "")
        text = text.replace("</b>", "")
        clipboard = QClipboard()
        clipboard.setText(text)
        msg = TimedMessageBox(timeout=2)
        msg.setText('Copied to clipboard')
        msg.exec_()
        return

    # Status: Mostly done
    # TODO: didn't use conversion variable. Possible bug 
    def refreshGeneralNutritionals(self, totalWeight, idList: list=None):
        if totalWeight is None or totalWeight == 0:
            return
        # initializes all nutrient values
        calories = 0
        fat = 0 
        carbs = 0 
        sugar = 0 
        addedSugar = 0
        protein = 0
        dietaryFiber = 0
        servingWeight = 'None'
        # places id in set so we can get number of unique ids
        idSet = set(idList)
        format_strings = ','.join(['%s'] * len(idList))

        # gets all the nutrient totals grouped by nutrient for all the ids in table widget
        with dbConnection('FormulaSchema').cursor() as cursor:
            query = 'SELECT food_nutrient.nutrient_id, nutrient.nutrient_name, SUM(food_nutrient.nutrient_weight_g_per_100g) AS "amount" FROM food LEFT JOIN food_nutrient ON food_nutrient.food_id = food.food_id LEFT JOIN nutrient ON nutrient.nutrient_id = food_nutrient.nutrient_id WHERE food.food_id IN ({}) AND nutrient.nutrient_id IN (203, 204, 205, 208, 291, 269, 659) GROUP BY nutrient_id'.format(format_strings)
            cursor.execute(query, tuple(idList))
            results = cursor.fetchall()
            for result in results: 
                nutrID = result['nutrient_id']
                if nutrID == 203:
                    protein = result['amount']
                elif nutrID == 204:
                    fat = result['amount']
                elif nutrID == 205:
                    carbs = result['amount']
                elif nutrID == 208:
                    calories = result['amount']
                elif nutrID == 269:
                    sugar = result['amount']
                elif nutrID == 291:
                    dietaryFiber == result['amount']
                elif nutrID == 659:
                    addedSugar == result['amount']

        # if the user has changed at least how to scale the formula
        if self.scaleCombobox.currentIndex() != -1:
            scaleMethod = self.scaleCombobox.currentData(Qt.UserRole)
            # if user chooses to scale by weight
            if scaleMethod == 'weight':
                # ERROR
                # if user does not choose unit or does not input a serving weight
                if self.unitWeightCombobox.currentData(Qt.UserRole) is not None and self.servingWeightSpinBox.value() == 0: #<--- default is 0
                    msg = QMessageBox()
                    msg.setText('Please complete the scale by weight information on Tab 3 - Label')
                    msg.exec_()

                    self.totalWeightPlaceholderLabel.setText(f'{totalWeight:,}')
                    if self.servingSizeLineEdit.text() != '':
                        self.servingSizePlaceholderLabel.setText(self.servingSizeLineEdit.text())
                    else:
                        self.servingSizePlaceholderLabel.setText('Use label tab to change')
                    self.servingWeightPlaceholder.setText('Could not calculate. Complete the scaling information on Label tab')
                    self.proteinPlaceholderLabel.setText('')
                    self.totalFatPlaceholderLabel.setText('')
                    self.totalCarbsPlaceholderLabel.setText('')
                    self.caloriesPlaceholderLabel.setText('')
                    self.sugarsPlaceholderLabel.setText('')
                    self.dietaryFiberPlaceholderLabel.setText('')
                    self.addedSugarPlaceholderLabel.setText('')
                    return

                # NO ERROR 
                # if user inputs all boxes correclty for scaling by weight 
                else:
                    servingWeight = self.servingWeightSpinBox.value()
                    unitData = self.unitWeightCombobox.currentData(Qt.UserRole)
                    conversion = unitData['conversion_factor']
                    offset = unitData['conversion_offset']
                    servingWeight = (servingWeight + offset) * conversion

            # if user chooses to scale by number of servings
            else: # <--------------scaleMethod == 'servings':
                servings = self.numServingsSpinbox.value()# <------default is 1 serving 
                if servings is None: 
                    msg = QMessageBox()
                    msg.setText('Must input the number of servings')
                    msg.exec_()
                    return 
                else:
                    try:
                        servingWeight = totalWeight/servings
                    except Exception:
                        print('There was an erorr finding servingWeight')

        # if the user hasn't inputted any scaling information
        else:
            servingWeight = totalWeight
            conversion = 1 # <------------------------------------------- # did not use

        # recalculates the nutrient values based on scaling input
        scalingFactor = (servingWeight/(100 * len(idSet)))
        protein = round(protein*scalingFactor, 1)
        fat = round(fat*scalingFactor, 1)
        carbs = round(carbs * scalingFactor, 1)
        
        calories = '{:.0f}'.format(round(calories * scalingFactor, -1))
        sugar = round(sugar * scalingFactor, 1)
        dietaryFiber = round(dietaryFiber * scalingFactor, 1)
        addedSugar = int(round(addedSugar * scalingFactor, 0)) # MIGHT REMOVE ADDED SUGAR
        servingWeight = int(round(servingWeight, 0))
        totalWeight = int(round(totalWeight, 0))

        # inputs all information into the placeholder labels
        self.totalWeightPlaceholderLabel.setText(f'{totalWeight:,}')
        if self.servingSizeLineEdit.text() != '':
            self.servingSizePlaceholderLabel.setText(self.servingSizeLineEdit.text())
        else:
            self.servingSizePlaceholderLabel.setText('Use label tab to change')
        self.servingWeightPlaceholder.setText(f'{servingWeight:,}')
        self.proteinPlaceholderLabel.setText(str(protein))
        self.totalFatPlaceholderLabel.setText(str(fat))
        self.totalCarbsPlaceholderLabel.setText(str(carbs))
        self.caloriesPlaceholderLabel.setText(str(calories))
        self.sugarsPlaceholderLabel.setText(str(sugar))
        self.dietaryFiberPlaceholderLabel.setText(str(dietaryFiber))
        self.addedSugarPlaceholderLabel.setText(str(addedSugar))

    @pyqtSlot()
    # main function that calls other refresh functions 
    def refresh(self):
        totalWeightG = self.getTotalTableWeight()
        self.refreshTable(totalWeightG)
        idList = [] # multiple applications
        foodList = [] # for refreshing ingredient statement
        for rowIndex in range(self.ingTabFormulaTableWidget.rowCount()):
            itemData = self.ingTabFormulaTableWidget.item(rowIndex, 0).data(Qt.UserRole)
            percentByWeight = self.ingTabFormulaTableWidget.item(rowIndex, 1).data(Qt.UserRole + 1)
            itemData['percent'] = percentByWeight
            idList.append(itemData['food_id'])
            foodList.append(itemData)

        if len(idList) != 0 and len(foodList) != 0:
            self.refreshGeneralNutritionals(totalWeightG, idList=idList)
            self.refreshIngStatement(foodList=foodList)
            self.refreshReport(totalWeightG, idList=idList)
            #self.refreshDVTable(totalWeightG=totalWeightG, idList=idList)

    
    #@pyqtSlot()
    # clears the highlighted rows from the ingredients table widget 
    def removeSelected(self):
        selected = self.ingTabFormulaTableWidget.selectionModel().selectedRows()
        ingredientsToRemove = []
        if len(selected) == 0:
            return
        else:
            toRemove = ''
            for selection in selected:
                data = selection.data(Qt.UserRole)
                ingredientsToRemove.append(data)
                foodDesc = data['food_desc']
                if toRemove == '':
                    toRemove = foodDesc
                else: 
                    toRemove = toRemove + ', ' + foodDesc
            confirm = QMessageBox.question(self, 'Confirm', 'Would you like to remove {} from the formula?'.format(toRemove), QMessageBox.No | QMessageBox.YesToAll)
            if confirm == QMessageBox.YesToAll:
                for selection in selected:
                    self.ingTabFormulaTableWidget.removeRow(selection.row())
                for ingredient in ingredientsToRemove:
                    self.formula.removeIngredient(ingredient)
                self.refresh()

    # inserts row into qtablewidget 
    #@pyqtSlot()
    def insertRow(self):
        rowCount = self.qualityAttributeTableWidget.rowCount()
        self.qualityAttributeTableWidget.insertRow(rowCount)
        
    '''
    CALLED: called during refresh(). r
    PURPOSE: 
    '''
    def refreshReport(self, totalWeight, idList: list):  
        if self.scaleCombobox.currentIndex() == -1:
            self.spreadSheetBasedOnLabel.setText('Nutritionals in spreadsheet are based on 1 serving ({} grams). The total inputted weight is {} grams'.format(numberWithCommas(round(totalWeight)), numberWithCommas(round(totalWeight))))
        else:
            try: 
                scaleMethod = self.scaleCombobox.currentData(Qt.UserRole)
                # if user chooses to scale by weight
                if scaleMethod == 'weight':
                    weight = self.servingWeightSpinBox.value()
                    unitData = self.unitWeightCombobox.currentData(Qt.UserRole)
                    unitName = unitData['unit_name']
                    conversion = unitData['conversion_factor']
                    offset = unitData['conversion_offset']
                    servingWeight = (weight + offset) * conversion
                    totalServings = totalWeight/servingWeight
                    self.spreadSheetBasedOnLabel.setText('Nutritionals in spreadsheet are based on a serving weight of {} {}s ({} g). There are approximately {} servings inputted'.format(numberWithCommas(weight), unitName, numberWithCommas(round(servingWeight)), totalServings))
                else:
                    servings = self.numServingsSpinbox.value()
                    if servings > 1:s='s'
                    else: s=''
                    servingWeight = totalWeight/servings
                    totalServings = totalWeight/servingWeight

                    self.spreadSheetBasedOnLabel.setText('Nutritionals in spreadsheet are based on 1 serving ({} g). There are approximately {} serving{} inputted'.format(numberWithCommas(round(servingWeight)), totalServings, s))
            except Exception:
                servingWeight = totalWeight
                self.spreadSheetBasedOnLabel.setText('Nutritionals in spreadsheet are based on 1 serving ({} g). There is 1 serving inputted'.format(numberWithCommas(round(servingWeight))))
                print('something went wrong during scaling')       


        ##### updates nutrient spreadsheet
        map = nutrientColMap()
        data = [] # maintains the dataframe
        totals = [0 for i in range(57)] # list for the totals of each nutrient, 57 is the number of columns in the self.nutrientReportTableView
        totals[0] = 'TOTAL'
        totals[1] = '-'
        totals[2] = '-'
        for row in range(self.ingTabFormulaTableWidget.rowCount()):
            dataRow = [0 for i in range(57)]
            itemData = self.ingTabFormulaTableWidget.item(row, 0).data(Qt.UserRole)
            id = itemData['food_id']
            dataRow[0] = itemData['food_desc']
            dataRow[1] = itemData['weight']
            dataRow[2] = itemData['unit_name']
            dataRow[3] = itemData['weight_in_g']
            totals[3] += itemData['weight_in_g']
            scalingFactor = itemData['weight_in_g']/100
            with dbConnection('FormulaSchema').cursor() as cursor:
                cursor.execute('SELECT food.food_desc, nutrient.nutrient_id, nutrient_name, (nutrient_weight_g_per_100g * %s) as amount FROM food LEFT JOIN food_nutrient ON food.food_id = food_nutrient.food_id LEFT JOIN nutrient ON nutrient.nutrient_id = food_nutrient.nutrient_id WHERE food.food_id = %s', (scalingFactor, id))
                results = cursor.fetchall()
                for result in results:
                    nutrientID = result['nutrient_id']
                    try:
                        col = map[nutrientID]
                    except:
                        pass    
                    if col == None:
                        pass
                    else:
                        if result['amount'] == None:
                            dataRow[col] = '-'
                        else:
                            dataRow[col] = result['amount']
                            totals[col] += result['amount']
            data.append(dataRow)
        data.append(totals)
        model = self.nutrientReportTableView.model()
        model.inputTableData(data)
        self.nutrientReportTableView.setModel(model)            
            
    # SEEMS TO WORK OKAY 
    def refreshIngStatement(self, foodList: list=None): 
        if foodList is None:
            return
        ingStatement = []
        # sorts the items from food list by percent weight ASC
        sortedFoodList = sorted(foodList, key = itemgetter('percent'), reverse=True)
        # clears the table
        self.ingStatementTable.setRowCount(0)
        rowIndex = 0
    
        # iterates through sorted list of ingredients
        #   adds to the ingredient statement table the percent weight and the dictionary with the data
        for food in sortedFoodList: 
            self.ingStatementTable.insertRow(rowIndex)
            foodData = QTableWidgetItem()
            foodData.setData(Qt.UserRole, food)
            foodData.setText(food['food_desc'])
            foodID = food['food_id']
            self.ingStatementTable.setItem(rowIndex, 0, foodData)
            percentItem = QTableWidgetItem(food['percent'])
            percentItem.setText(str(food['percent']))
            self.ingStatementTable.setItem(rowIndex, 1, percentItem)
            subIngsForTable = []
            subIngsForStatement = []
            counter = 1

            with dbConnection('FormulaSchema').cursor() as cursor: # <---- bad practice to execute cursor query in loop?
                # if the food is a fndds ingredient preloaded from database
                # gets the subingredients from subfood_food table and appends as
                # 
                if cursor.execute('SELECT food.food_id, food_desc, subfood_desc, subfood_food.ingredient_weight FROM food LEFT JOIN subfood_food ON food.food_id = subfood_food.food_id WHERE food.food_id = %s ORDER BY food.food_id ASC, ingredient_weight DESC', (foodID,)) != 0:
                    subfoods = cursor.fetchall()
                    for food in subfoods:
                        subIngsForTable.append('({})'.format(counter) + ' ' + food['subfood_desc'])
                        subIngsForStatement.append(food['subfood_desc'])
                        counter += 1
                else:
                    # if the food is a formula (composed of other foods), combines all its components by food_desc and concatenates to an ingredient statement string
                    if cursor.execute('SELECT formula.formula_name, formula_food.food_id, food.food_desc, food.ing_statement FROM formula LEFT JOIN formula_food ON formula.formula_id = formula_food.formula_id LEFT JOIN food ON food.food_id = formula_food.food_id WHERE food.food_id = %s ORDER BY formula_food.weight_g DESC', (foodID)) != 0:
                        ingredients = cursor.fetchall()
                        formulaStatement = ''
                        for ing in ingredients:
                            if formulaStatement == '':
                                formulaStatement = ing['food_desc']
                            else:
                                formulaStatement = formulaStatement + ', ' + ing['food_desc']
                            if ing['ing_statement']:
                                formulaStatement = formulaStatement + ' ({})'.format(ing['ing_statement'].capitalize())

                        subIngsForTable.append('({})'.format(counter) + ' ' + formulaStatement)
                        subIngsForStatement.append(formulaStatement)
                    else:
                        # if the food is a manufacturer supplied ingredient or a user inputted generic ingredient
                        if food['ing_statement']:
                            subIngsForTable.append(food['ing_statement'])
                            subIngsForStatement.append(food['ing_statement'].capitalize())
                        else:
                            subIngsForTable.append('None')
                            subIngsForStatement.append(food['food_desc'].capitalize())

            subIngsForTable = ', '.join(subIngsForTable)
            subIngsForStatement = ', '.join(subIngsForStatement)
            self.ingStatementTable.setItem(rowIndex, 2, QTableWidgetItem(subIngsForTable)) 
            foodStatement = '<b>{food}</b> ({subFoods})'.format(food=food['food_desc'].title(), subFoods=subIngsForStatement)
            ingStatement.append(foodStatement)
            rowIndex += 1 
        self.ingStatementTable.resizeRowsToContents()

        ingStatement = ', '.join(ingStatement)
        self.ingStatementTextBox.setText(ingStatement)

    # updates the chartview to display a barchart 
    # The barchart shows what percentage of the total nutrient amount is attributed to the given ingredient
    # TODO needs to be redone to make more efficient and less sloppy
    # TODO consider adding amounts on each bar
    # TODO make the category labels wrap so they are not hidden
    def nutrComparisonChosen(self):

        self.singleNutrientChartView.resetCachedContent() # not sure if needed
        totalWeightG = self.getTotalTableWeight()

        if totalWeightG == 0:
            return
    
        nutrientID = self.nutrientReportCombobox.currentData(Qt.UserRole)['nutrient_id']
        nutrientName = self.nutrientReportCombobox.currentData(Qt.UserRole)['nutrient_name']
        chart = QtCharts.QChart()
        nutrientSum = 0
        categories = []
        amounts = []
    
        # TODO make more efficient
        for row in range(self.ingTabFormulaTableWidget.rowCount()):
            ingredient = self.ingTabFormulaTableWidget.item(row, 0).data(Qt.UserRole)
            scalingFactor = ingredient['weight_in_g']/100
            with dbConnection('FormulaSchema').cursor() as cursor:
                cursor.execute('SELECT nutrient_weight_g_per_100g * %s AS amount FROM food_nutrient WHERE nutrient_id = %s AND food_id = %s', (scalingFactor, nutrientID, ingredient['food_id']))
                result = cursor.fetchone()
                if result is None:
                    continue
                try:
                    categories.append(ingredient['food_desc'])
                    amounts.append(result['amount'])
                    nutrientSum += result['amount']
                except Exception:
                    continue
            cursor.close()
    
        # if none of the ingredients have inputted data for the given nutrient
        # TODO create a view when none of the ingredients have a given value. Currently does not work because the view does not go away once a nutrient with values is chosen 
        '''if len(categories) == 0:
            path = QPainterPath()
            sceneFont = QFont()
            sceneFont.setPixelSize(100)
            path.addText(100, 100, sceneFont, 'There is no data for the specified nutrient')
            scene = QGraphicsScene()
            graphicsTextItem = QGraphicsTextItem()
            graphicsTextItem.setPos(150, 150)
            graphicsTextItem.setPlainText('There is no data for the specified nutrient. Please try another')
            scene.addItem(graphicsTextItem)
            self.singleNutrientChartView.setScene(scene)
            return'''

        percentages = [0 for i in range(len(categories))]
        #for i in range(len(amounts)):
            #sum += amounts[i]
        if nutrientSum != 0: 
            for i in range(len(amounts)):
                percentages[i] = (amounts[i]/nutrientSum) * 100
        '''for i in range(len(amounts)):
            percentages[i] = (amounts[i]/sum) * 100'''

        # creates and displays the bar chart 
        barset = QtCharts.QBarSet('barsetlabel')
        barset.append(percentages)
        series = QtCharts.QBarSeries()
        series.append(barset)
        xAxis = QtCharts.QBarCategoryAxis()
        xAxis.append(categories)
       #xAxis.setLabelsAngle(-45)
        font = QFont()
        font.setPointSize(10)
        font.setHintingPreference(QFont.PreferFullHinting)
        xAxis.setLabelsFont(font)
        yAxis = QtCharts.QValueAxis()
        yAxis.setRange(0, 100)
        yAxis.setTitleText('% of Total')
        chart.addSeries(series)
        chart.setTitle("How each ingredient contributes to amount of {}".format(nutrientName))
        chart.addAxis(xAxis, Qt.AlignBottom)
        series.attachAxis(xAxis)
        chart.addAxis(yAxis, Qt.AlignLeft)
        series.attachAxis(yAxis)
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        chart.legend().setVisible(False)
        chart.legend().setAlignment(Qt.AlignBottom)
        #self.singleNutrientChartView.scene().deleteLater()
        self.singleNutrientChartView.setChart(chart)
        #self.singleNutrientChartView.update()

    # parameters taken from previous setup window to create the UI for this window
    def fromSetupDialog(self, revision=None, formulaName=None, revisionID=None, differences=None):
        self.formulaNameLineEdit.setText(formulaName)
        self.formulaNameLineEdit.setReadOnly(True)
        self.revisionNumberPlaceholder.setText(revisionID)
        if revision is True:
            self.revisionCheckBox.setChecked(True)
        else:
            self.notRevisionCheckBox.setChecked(True)
        self.revisionCheckBox.setEnabled(False)
        self.notRevisionCheckBox.setEnabled(False)

    # opens the search results window with user query
    def search(self):
        query = self.formulaIngredientSearchLineEdit.text()
        root = self
        dialog = searchResults(query, root)
        dialog.setModal(True)
        dialog.exec_()


    # refreshes the percent by weight column of the formula when called
    def refreshTable(self, totalWeightG):
        # calculates the % by weight of each ingredient and adds to the table widget
        for row in range(self.ingTabFormulaTableWidget.rowCount()):
            ingredient = self.ingTabFormulaTableWidget.item(row, 0).data(Qt.UserRole)
            percentWeight = (ingredient['weight_in_g']/totalWeightG) * 100
            percentWeight = round(percentWeight, 3)
            percentTableItem = QTableWidgetItem()
            percentTableItem.setData(Qt.UserRole + 1, percentWeight)
            if percentWeight < 0.001:
                percentTableItem.setText('<.001')
                self.ingTabFormulaTableWidget.setItem(row, 1, percentTableItem)
            else:
                percentTableItem.setText(str(percentWeight))
                self.ingTabFormulaTableWidget.setItem(row, 1, percentTableItem)
    
    

    # submits the form to the database
    def formSubmit(self):
        pass
        
    # returns the sum of total weight in the formula table in grams
    def getTotalTableWeight(self):
        totalWeightG = 0
        # calculatest the total weight of all ingredients in the formula
        for row in range(self.ingTabFormulaTableWidget.rowCount()):
            ingredient = self.ingTabFormulaTableWidget.item(row, 0).data(Qt.UserRole)
            weightOfItemG = ingredient['weight_in_g']
            totalWeightG += weightOfItemG
        return totalWeightG

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Formula Editor", u"Formula Editor", None))
        self.formulaNameHeaderLabel.setText(QCoreApplication.translate("Dialog", u"Formula Name", None))
        self.formulaIDHeaderLabel.setText(QCoreApplication.translate("Dialog", u"Formula ID: ", None))
        self.formulaIDPlaceholder.setText(QCoreApplication.translate("Dialog", u"#", None))
        self.revisionNumberHeaderLabel.setText(QCoreApplication.translate("Dialog", u"Revision Number:", None))
        self.revisionNumberPlaceholder.setText(QCoreApplication.translate("Dialog", u"#", None))
        self.categoryLabel.setText(QCoreApplication.translate("Dialog", u"Category", None))
        self.percentYieldLabel.setText(QCoreApplication.translate("Dialog", u"Percent Yield", None))
        self.revisionStatusLabel.setText(QCoreApplication.translate("Dialog", u"Revision Status", None))
        self.revisionCheckBox.setText(QCoreApplication.translate("Dialog", u"Revision", None))
        self.notRevisionCheckBox.setText(QCoreApplication.translate("Dialog", u"Not A Revision", None))
        self.previousVersionNumberLabel.setText(QCoreApplication.translate("Dialog", u"Previous Version Number", None))
        self.previousVersionNumberLineEdit.setText("")
        self.previousVersionNumberLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"If Applicable", None))
        self.previousFormulaLabel.setText(QCoreApplication.translate("Dialog", u"Previous Formula Name", None))
        self.previousFormulaNameLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"If Applicable", None))
        self.generalNutritionalsHeaderLabel.setText(QCoreApplication.translate("Dialog", u"General Nutritionals", None))
        self.servingSizeLabel_2.setText(QCoreApplication.translate("Dialog", u"Serving Size", None))
        self.totalCarbsLabel.setText(QCoreApplication.translate("Dialog", u"Total Carbs (g)", None))
        self.servingWeightLabel.setText(QCoreApplication.translate("Dialog", u"Serving Weight (g) ", None))
        self.dietaryFiberLabel.setText(QCoreApplication.translate("Dialog", u"Dietary Fiber (g)", None))
        self.caloriesPlaceholderLabel.setText("")
        self.totalFatLabel.setText(QCoreApplication.translate("Dialog", u"Total Fat (g)", None))
        self.totalCarbsPlaceholderLabel.setText("")
        self.sugarLabel.setText(QCoreApplication.translate("Dialog", u"Sugar (g)", None))
        self.totalFatPlaceholderLabel.setText("")
        self.servingSizePlaceholderLabel.setText(QCoreApplication.translate("Dialog", u"Use label tab to change", None))
        self.addedSugarLabel.setText(QCoreApplication.translate("Dialog", u"Added Sugar (g)", None))
        self.sugarsPlaceholderLabel.setText("")
        self.calorieLabel.setText(QCoreApplication.translate("Dialog", u"Calories (kCal)", None))
        self.dietaryFiberPlaceholderLabel.setText("")
        self.servingWeightPlaceholder.setText(QCoreApplication.translate("Dialog", u"Must input serving size", None))
        self.proteinLabel.setText(QCoreApplication.translate("Dialog", u"Protein (g)", None))
        self.addedSugarPlaceholderLabel.setText("")
        self.proteinPlaceholderLabel.setText("")
        self.totalWeightLabel.setText(QCoreApplication.translate("Dialog", u"Total Weight (g)", None))
        self.totalWeightPlaceholderLabel.setText(QCoreApplication.translate("Dialog", u"Must input an ingredient ", None))
        self.displayNFPBtn.setText(QCoreApplication.translate("Dialog", u"Display Nutrition Label", None))
        self.formulaIngredientSearchLineEdit.setText("")
        self.formulaIngredientSearchLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Ingredient, Supplier", None))
        self.formulaIngredientSearchBtn.setText(QCoreApplication.translate("Dialog", u"Search", None))
        ___qtablewidgetitem = self.ingTabFormulaTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Ingredient Name", None));
        ___qtablewidgetitem1 = self.ingTabFormulaTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"% by Weight", None));
        ___qtablewidgetitem2 = self.ingTabFormulaTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Quantity", None));
        ___qtablewidgetitem3 = self.ingTabFormulaTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Unit", None));
        ___qtablewidgetitem4 = self.ingTabFormulaTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Supplier", None));
        ___qtablewidgetitem5 = self.ingTabFormulaTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Item Number", None));
        self.formulaEditorTabWidget.setTabText(self.formulaEditorTabWidget.indexOf(self.ingredientsTab), QCoreApplication.translate("Dialog", u"Ingredients", None))
        self.inputQualityAttributeLabel.setText(QCoreApplication.translate("Dialog", u"Input Quality Attributes", None))
        self.addQAttributeBtn.setText(QCoreApplication.translate("Dialog", u"Add Row", None))
        ___qtablewidgetitem6 = self.qualityAttributeTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"Quality", None));
        ___qtablewidgetitem7 = self.qualityAttributeTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"Unit", None));
        ___qtablewidgetitem8 = self.qualityAttributeTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"Value", None));
        self.ingStatementLabel.setText(QCoreApplication.translate("Dialog", u"Ingredient Statement", None))
        ___qtablewidgetitem9 = self.ingStatementTable.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"Ingredient Name", None));
        ___qtablewidgetitem10 = self.ingStatementTable.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"% by Weight", None));
        ___qtablewidgetitem11 = self.ingStatementTable.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"Sub-Ingredients", None));
        self.ingStatetmentTxtLabel.setText(QCoreApplication.translate("Dialog", u"Click generate below to autofill statement. Click edit to input manually or change auto-generated text", None))
        self.editIngStatementBtn.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.copyIngStatementBtn.setText(QCoreApplication.translate("Dialog", u"Copy", None))
        self.ingStatementPrintBtn.setText(QCoreApplication.translate("Dialog", u"Print", None))
        self.formulaEditorTabWidget.setTabText(self.formulaEditorTabWidget.indexOf(self.qualityTab), QCoreApplication.translate("Dialog", u"Quality", None))
        self.servingInfoLabelHeader.setText(QCoreApplication.translate("Dialog", u"How Serving Information Appears On Label", None))
        self.servingSizeLabel.setText(QCoreApplication.translate("Dialog", u"Serving Size ", None))
        self.calculatedServingSizeLabel.setText(QCoreApplication.translate("Dialog", u"()", None))
        self.hideServingSizeCheckbox.setText(QCoreApplication.translate("Dialog", u"Hide Calculated Serving Size", None))
        self.servingsComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Serving", None))
        self.servingsComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Servings", None))

        self.perContainerLabel.setText(QCoreApplication.translate("Dialog", u"Per Container", None))
        self.hidePerContainerCheckBox.setText(QCoreApplication.translate("Dialog", u"Hide on Label", None))
        self.scalingHeaderLabel.setText(QCoreApplication.translate("Dialog", u"Scale Formula", None))
        self.servingsLabel.setText(QCoreApplication.translate("Dialog", u"Serving(s)", None))

#if QT_CONFIG(whatsthis)
#endif // QT_CONFIG(whatsthis)

        self.displayNutritionalLabelBtn.setText(QCoreApplication.translate("Dialog", u"Display Nutrition Label", None))
        self.formulaEditorTabWidget.setTabText(self.formulaEditorTabWidget.indexOf(self.labelTab), QCoreApplication.translate("Dialog", u"Label", None))

        self.nutrientSpreadsheetLabel.setText(QCoreApplication.translate("Dialog", u"Nutrient Spreadsheet", None))
        self.singleNutrientLabel.setText(QCoreApplication.translate("Dialog", u"Single Nutrient ", None))
        self.dailyValueLabel.setText(QCoreApplication.translate("Dialog", u"Daily Value and Per 100g", None))
        self.byComparisonLabel.setText(QCoreApplication.translate("Dialog", u"Comparison", None))
        self.formulaEditorTabWidget.setTabText(self.formulaEditorTabWidget.indexOf(self.nutrientReportTab), QCoreApplication.translate("Dialog", u"Nutrient Report", None))
        ___qtablewidgetitem75 = self.imagesTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("Dialog", u"Context/Note", None));
        ___qtablewidgetitem76 = self.imagesTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("Dialog", u"Image", None));
        self.formulaEditorTabWidget.setTabText(self.formulaEditorTabWidget.indexOf(self.imagesTab), QCoreApplication.translate("Dialog", u"Images", None))
    # retranslateUi

app = QApplication(sys.argv)
gui = formulaEditorDialog()
gui.show()
sys.exit(app.exec_())



     