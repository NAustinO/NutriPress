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
import PySide2.QtCharts

from PyQt5.QtCore import Q_RETURN_ARG, pyqtSlot

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtPrintSupport import *
from PySide2.QtCharts import * 


from operator import itemgetter, attrgetter

sys.path.append('../pjrd')
import pymysql
from pjrd.helpers import compareTableRowMap, extractIngredientStatement, test, dbConnection, TimedMessageBox, nutrientColMap, numberWithCommas, nutrientRowMap, initialize2DArray, getIngredientStatement
from pjrd.formulaEditorSearchResults import searchResults
from pjrd.helperClasses import CustomTableModel, UnitOfMeasure, Nutrient, Ingredient, Formula
from pjrd.quickTableView import QuickTableView

# Fixes compatibility bug with mac big sur and pyqt
os.environ['QT_MAC_WANTS_LAYER'] = '1' 


class formulaEditorDialog(QDialog):
    
    def __init__(self, formulaName: str, revision: bool = None, prevRevisionID: int = None, differences: str = None):
        super(formulaEditorDialog, self).__init__()
        self.setupUi(self)
        self.formula = Formula(formulaName, isRevision = revision, prevRevisionID = prevRevisionID, formulaTableRef= self.ingTabFormulaTableWidget)
        self.fromSetupDialog(revision=revision, formulaName=formulaName, revisionID=prevRevisionID, differences=differences)
        self.setupLogic()
        
        
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog") 
        Dialog.resize(822, 1005)
        tenPointFont = QFont()
        tenPointFont.setPointSize(10)
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

        self.submitBtn = QPushButton()
        self.submitBtn.setText('Submit')
        self.horizontalLayout.add


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
        self.generalFrame2.setToolTip('This frame provides the user a quick glimpse of the major nutritionals, which can be based on how the user defines the serving. Otherwise it defaults to the total amount entered.')
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
        self.qualityAttributeFrame.setToolTip('This allows the user to input any notes related to ensure the quality of the product is recorded. Can also include processing/cooking details, parameters and calculated or measured attributes')

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

        self.qualityAttributeSubheaderLabel = QLabel()
        self.qualityAttributeSubheaderLabel.setFont(tenPointFont)
        self.qualityAttributeSubheaderLabel.setText('Used to record any quality attributes and or parameters to ensure consistency when recreating.')

        self.verticalLayout_10.addWidget(self.qualityAttributeSubheaderLabel)

        self.qualityAttributeTableWidget = QTableWidget(self.qualityAttributeFrame)
        if (self.qualityAttributeTableWidget.columnCount() < 4):
            self.qualityAttributeTableWidget.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.qualityAttributeTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.qualityAttributeTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.qualityAttributeTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        qtablewidgetitem11 = QTableWidgetItem()
        self.qualityAttributeTableWidget.setHorizontalHeaderItem(3, qtablewidgetitem11)
        if (self.qualityAttributeTableWidget.rowCount() < 1):
            self.qualityAttributeTableWidget.setRowCount(1)
        self.qualityAttributeTableWidget.setObjectName(u"qualityAttributeTableWidget")
        self.qualityAttributeTableWidget.setRowCount(1)
        self.qualityAttributeTableWidget.horizontalHeader().setDefaultSectionSize(175)
        self.qualityAttributeTableWidget.horizontalHeader().setStretchLastSection(True)
        #self.qualityAttributeTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

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
        self.ingStatementTxtLabel = QLabel(self.ingStatementContainer)
        self.ingStatementTxtLabel.setObjectName(u"ingStatementTxtLabel")
        self.ingStatementTxtLabel.setAlignment(Qt.AlignCenter)
        self.ingStatementTxtLabel.setText('Auto-generated ingredient statement. Click the edit button below to make changes.')

        self.verticalLayout_6.addWidget(self.ingStatementTxtLabel)

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
        self.scaleByLabel.setText("Select below to indicate how to scale the current formula weight quantities")
        self.scaleByLabel.setAlignment(Qt.AlignLeft)
        self.verticalLayout.addWidget(self.scaleByLabel)

        self.scaleCombobox = QComboBox(self.scaleFrame)
        servingsItem = QStandardItem()
        servingsItem.setText('By Total Number of Servings The Formula Makes')
        servingsItem.setData('servings', Qt.UserRole)
        weightItem = QStandardItem()
        weightItem.setText('By The Weight of One Serving')
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

        '''self.displayNutritionalLabelBtn = QPushButton(self.labelTab)
        self.displayNutritionalLabelBtn.setObjectName(u"displayNutritionalLabelBtn")
        self.displayNutritionalLabelBtn.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_3.addWidget(self.displayNutritionalLabelBtn, 0, Qt.AlignHCenter)'''


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
        self.spreadSheetBasedOnLabel.setFont(tenPointFont)
        self.verticalLayout_5.addWidget(self.spreadSheetBasedOnLabel)

        self.nutrientReportTableView = QTableView(self.scrollAreaWidgetContents)
        self.nutrientReportTableView.setMinimumHeight(275)
        self.nutrientReportTableView.setHorizontalScrollBarPolicy((Qt.ScrollBarAlwaysOn))
        self.nutrientReportTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.nutrientReportTableView.setAlternatingRowColors(True) # Might remove this
        self.nutrientReportTableView.setSortingEnabled(True)
        self.nutrientReportTableView.setFont(tenPointFont)
        self.nutrientReportTableView.setObjectName(u"nutrientReportTableView")
        headerLabels = ['Item Desc', 'Quantity', 'Unit', 'Weight Per Serv. (g)', 'Calories (kCal)', 'Protein (g)', 'Carbohydrates (g)', 'Dietary Fiber (g)', 'Soluble Fiber (g)', 'Total Sugar (g)', 'Added Sugar (g)', 'Monosac (g)', 'Disac (g)', 'Total Fat (g)', 'Sat Fat (g)', 'Trans Fat (g)', 'Mono Unsat Fat (g)', 'Poly Unsat Fat (g)', 'Total Unsat Fat (g)', 'Omega-3 FA (g)', 'Omega-6 FA (g)', 'Cholestrol (mg)', 'Water (g)', 'Alcohol (g)', 'Caffeine (mg)', 'Choline (mg)', 'Sugar Alcohol (g)', 'Calcium (mg)', 'Chromium (µg)', 'Copper (mg)', 'Fluoride (mg)', 'Iodine (µg)', 'Iron (mg)', 'Magnesium (mg)', 'Manganese (mg)', 'Molybdenum (µg)', 'Phosphorus (mg)', 'Potassium (mg)', 'Selenium (µg)', 'Sodium (mg)', 'Zinc (mg)', 'Vitamin A (IU)', 'Vitamin A - RE (µg)', 'Vitamin A - RAE (µg)', 'Vitamin B1/Thiamin (mg)', 'Vitamin B2/Riboflavin (mg)', 'Vitamin B3/Niacin (mg)', 'Vitamin B3/Niac. Eq (mg)', 'Vitamin B6 (mg)', 'Vitamin B12 (µg)', 'Vitamin C (mg)', 'Vitamin D (IU)', 'Vitamin E/Alpha-toco (mg)', 'Folate (µg)', 'Folate, DFE (µg DFE)', 'Vitamin K (µg)', 'Panothenic Acid (mg)']


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
        self.disclaimerLabel.setText('Choose a nutrient below to see how each ingredient contributes to the total amount')
        self.disclaimerLabel.setFont(tenPointFont)
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

        self.dailyValueSubHeader = QLabel(self.scrollAreaWidgetContents)
        self.dailyValueSubHeader.setObjectName(u"dailyValueSubHeader")
    
        self.dailyValueSubHeader.setText('Click below to see how a serving and 100 gram equivalent of the current formula contributes to the recommended daily value of nutrients')
        self.dailyValueSubHeader.setFont(tenPointFont)
        
        self.verticalLayout_5.addWidget(self.dailyValueSubHeader)

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

        self.byComparisonSubHeaderLabel = QLabel(self.scrollAreaWidgetContents)
        self.byComparisonSubHeaderLabel.setObjectName(u"byComparisonSubHeaderLabel")
 
        self.byComparisonSubHeaderLabel.setFont(tenPointFont)
        self.byComparisonSubHeaderLabel.setText('Select a previous formula or ingredient below to see how identical quantities of each compare by nutrient')

        self.verticalLayout_5.addWidget(self.byComparisonSubHeaderLabel)


        self.comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setObjectName(u"comboBox")
        
        self.verticalLayout_5.addWidget(self.comboBox)


        self.showComparisonBtn = QPushButton(self.scrollAreaWidgetContents)
        self.showComparisonBtn.setText('Show')
    
        self.verticalLayout_5.addWidget(self.showComparisonBtn)

        self.nutrientReportScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_15.addWidget(self.nutrientReportScrollArea)

        self.formulaEditorTabWidget.addTab(self.nutrientReportTab, "")
        '''self.imagesTab = QWidget()
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

        self.formulaEditorTabWidget.addTab(self.imagesTab, "")'''

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
        self.removeSelectedBtn.clicked.connect(self.removeSelected)
        self.scaleCombobox.currentIndexChanged.connect(self.toggleFocus)
        self.dvToggleBtn.clicked.connect(self.openDVTableViewer)
        #self.comboBox.currentIndexChanged.connect(self.openComparisonTableViewer)
        self.showComparisonBtn.clicked.connect(self.openComparisonTableViewer)
        self.servingWeightSpinBox.valueChanged.connect(self.refresh) 
        self.unitWeightCombobox.currentIndexChanged.connect(self.refresh)
        self.numServingsSpinbox.valueChanged.connect(self.refresh)
        self.editIngStatementBtn.clicked.connect(self.toggleReadOnly)
        self.copyIngStatementBtn.clicked.connect(self.copy)
        self.addQAttributeBtn.clicked.connect(self.insertRow)
        self.ingStatementPrintBtn.clicked.connect(self.printPreview)

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
                unit.setData(unit, Qt.UserRole)
                unit.setText('{unitName} ({unitSymbol})'.format(unitName=uom['unit_name'], unitSymbol = uom['unit_symbol']))
                unitModel.appendRow(unit)
            unitCompleter.setModel(unitModel)
            unitCompleter.setCompletionMode(QCompleter.InlineCompletion)
            self.unitWeightCombobox.setModel(unitModel)
            self.unitWeightCombobox.setCurrentIndex(-1)

            # sets up the model for the comparison combobox
            compareModel = QStandardItemModel() 

            # starts by adding the formulas to the comparisons
            cursor.execute('SELECT formula.formula_id, formula.food_id, formula.formula_name, food.food_desc FROM formula LEFT JOIN food ON formula.food_id = food.food_id ORDER BY formula.formula_name ASC')
            compareFoods = cursor.fetchall()
            for cFood in compareFoods:
                compareItem = QStandardItem()
                compareItem.setText(cFood['food_desc'].capitalize() + ' (Formula)')
                compareItem.setData(cFood, Qt.UserRole)
                compareModel.appendRow(compareItem)
            
            # finishes by adding the ingredients
            cursor.execute('SELECT food_id, food_desc, user_inputted FROM food ORDER BY food_desc ASC')
            compareFoods = cursor.fetchall()
            for cFood in compareFoods:
                compareItem = QStandardItem()
                if cFood['user_inputted'] == 1:
                    compareItem.setText(cFood['food_desc'].capitalize() + ' (User Ingredient)')
                else: compareItem.setText(cFood['food_desc'].capitalize())
                compareItem.setData(cFood, Qt.UserRole)
                compareModel.appendRow(compareItem)
    
            self.comboBox.setModel(compareModel)
            self.comboBox.setCurrentIndex(-1)
            
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


        self.nutrientReportCombobox.currentIndexChanged.connect(self.nutrComparisonChosen)
        #####

    # Opens a separate QDialog containing the tableview with the nutrient report broken down by daily recommended value, per 100 gram, per serving and % Daily Value per serving    
    def openDVTableViewer(self):

        # for the daily value report 
        totalWeightG = self.formula.totalFormulaWeight()
        rowMap = nutrientRowMap()

        model = CustomTableModel()
        dvHeaders = ['Daily Recommended Value','Per 100g', 'Per Serving', '% Daily Value Per Serving']
        vHeaders = ['Calories (kCal)', 'Fat (g)', 'Saturated Fat (g)', 'Cholestrol (mg)', 'Total Carbohydrates (g)', 'Total Dietary Fiber (g)', 'Total Sugar (g)', 'Protein (g)', 'Vitamn A (µg RAE)', 'Vitamin B1/Thiamin (mg)', 'Vitamin B2/Riboflavin (mg)', 'Vitamin B3/Niacin (mg)', 'Vitamin B5/Panothenic Acid (mg)', 'Vitamin B6 (µg)', 'Vitamin B9/Folic Acid (mg)', 'Vitamin B12 (mg)', 'Vitamin C (mg)', 'Vitamin D (µg)', 'Vitamin E/Alpha-tocopherol (mg)', 'Vitamin K/Phylloquinone (µg)', 'Choline (mg)', 'Calcium (mg)', 'Copper (mg)', 'Iron (mg)', 'Magnesium (mg)', 'Manganese (mg)','Phosphorus (mg)', 'Potassium (mg)', 'Selenium (µg)', 'Sodium (mg)', 'Zinc (mg)']

        nutrientIDList = [203, 204, 205, 208, 269, 291, 301, 303, 305, 306, 307, 309, 312, 317, 320, 323, 328, 401, 404, 405, 406, 415, 418, 421, 430, 431, 601, 606, 651, 656, 658]

        model.setHeaderLabels(dvHeaders, Qt.Horizontal, Qt.DisplayRole)
        model.setHeaderLabels(vHeaders, Qt.Vertical, Qt.DisplayRole)
        data = initialize2DArray(len(vHeaders), len(dvHeaders), None)
        
        try:
            servingWeight = self.servingWeightSpinBox.value()
            #if servingWeight == 0:
              #  servingWeight = totalWeightG
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

        for nutrientID in nutrientIDList:
            nutrientDict = self.formula.allNutritionals.get(nutrientID)
            rowIndex = rowMap.get(nutrientID)
            if nutrientDict is None:
                data[rowIndex][0] = '-'
                data[rowIndex][1] = '-'
                data[rowIndex][2] = '-'
                data[rowIndex][3] = '-'
                continue
            amountInG = nutrientDict['totalInG']
            amountInStdUnit = Nutrient.getStdUnitWeight(amountInG, nutrientDict['unit'])[0]
            per100g = amountInStdUnit * (100/totalWeightG)
            dailyRecommendedValueStdUnit = Nutrient.getStdUnitWeight(nutrientDict['dailyValueInG'], nutrientDict['unit'])[0]
            
            if rowIndex is None:
                continue
            if float(str(dailyRecommendedValueStdUnit).split('.')[1]) >= .1:
                round(dailyRecommendedValueStdUnit, 2)
            else:
                dailyRecommendedValueStdUnit = int(dailyRecommendedValueStdUnit)


            data[rowIndex][0] = dailyRecommendedValueStdUnit
            data[rowIndex][1] = numberWithCommas(round(per100g, 3))
            data[rowIndex][2] = numberWithCommas(round(amountInStdUnit/numberServings, 3))
            data[rowIndex][3] = '{}%'.format(round(((amountInStdUnit/dailyRecommendedValueStdUnit) * 100), 1))
            
        model.inputTableData(data)
        view = QuickTableView(model, label="Comparison by Daily Value and 100 g")
        view.setSubheaderLabel('Percent daily values are based on a 2,000 calorie diet for healthy adults. Daily values last updated in 2016.')
        view.exec_()

    # Opens a separate QDialog containing the tableview for a comparison per 100g of current recipe vs recipe chosen
    def openComparisonTableViewer(self):
        if len(self.formula.getCurrentIngredients()) == 0: 
            return
        if self.comboBox.currentIndex() == -1:
            comparedTo = None
        else:
            comparedTo = self.comboBox.currentData(Qt.UserRole)['food_id']
        totalWeightG = self.formula.totalFormulaWeight()
        compareToName = 'No comparison chosen'

        rowMap = compareTableRowMap()
        # header information for the table
        horizHeaders = ['Current (per 100g)', 'Comparison (per 100g)']
        vertHeaders = ['Calories (kCal)', 'Total Fat (g)', 'Saturated Fat (g)', 'Trans Fat (g)', 'Mono Unsat Fat (g)', 'Poly Unsat Fat (g)', 'Total Unsat Fat (g)','Omega-3 FA (g)', 'Omega-6 FA (g)', 'Cholestrol (mg)', 'Total Carbohydrates (g)', 'Total Dietary Fiber (g)', 'Total Sugar (g)', 'Added Sugar (g)', 'Monosaccharides (g)', 'Disaccharides (g)', 'Protein (g)', 'Vitamin A (Retinols)(IU)', 'Vitamin A (Retinols) - RE (µg)', 'Vitamin A (Retinols) - RAE (µg)', 'Vitamin B1/Thiamin (mg)', 'Vitamin B2/Riboflavin (mg)', 'Vitamin B3/Niacin (mg)', 'Vitamin B3/Niac. Eq (mg)', 'Vitamin B5/Panothenic Acid (mg)', 'Vitamin B6 (µg)', 'Vitamin B9/Folic Acid (mg)', 'Vitamin B12 (mg)', 'Vitamin C (mg)', 'Vitamin D (µg)', 'Vitamin D (IU)', 'Vitamin E/Alpha-tocopherol (mg)', 'Vitamin K/Phylloquinone (µg)', 'Choline (mg)', 'Calcium (mg)', 'Copper (mg)', 'Iron (mg)', 'Magnesium (mg)', 'Manganese (mg)', 'Phosphorus (mg)', 'Potassium (mg)', 'Selenium (µg)', 'Sodium (mg)', 'Zinc (mg)'] 

        # creates model for the table that holds the data
        model = CustomTableModel()
        model.setHeaderLabels(horizHeaders, Qt.Horizontal, Qt.DisplayRole)
        model.setHeaderLabels(vertHeaders, Qt.Vertical, Qt.DisplayRole)
        # temporary
        data = initialize2DArray(len(vertHeaders), len(horizHeaders), '-')

        # fill sin the data for the current formula
        allNutritionals = self.formula.getAllNutritionals()
        for nutrientID, rows in rowMap.items():
            if nutrientID == 320: # vitamin A RAE ID --> [vitamin A IU, vitamin A RE, Vitamin A RAE] (17, 18, 19)
                if nutrientID not in allNutritionals:
                    for rowIndex in rows:
                        data[rowIndex][0] = '-'
                else:
                    nutrientDict = allNutritionals.get(nutrientID)
                    amountVitAG = nutrientDict['totalInG']
                    for rowIndex in rows:
                        if rowIndex == 17: #vitamin A IU
                            amountStdUnit = amountVitAG * (100000/0.3)
                            per100g = amountStdUnit * (100/totalWeightG)
                            data[rowIndex][0] = round(per100g, 3) 
                        else: # vitamin A RE or vitamin A RAE
                            amountStdUnit = amountVitAG * 100000
                            per100g = amountStdUnit * (100/totalWeightG)
                            data[rowIndex][0] = round(per100g, 3)

            elif nutrientID == 406: # Niacin ID --> [Niacin, Niacin Equivalents] (22, 23)
                if nutrientID not in allNutritionals:
                    for rowIndex in rows:
                        data[rowIndex][0] = '-'
                else:
                    nutrientDict = allNutritionals.get(nutrientID)
                    for rowIndex in rows: 
                        amountStdUnit = Nutrient.getStdUnitWeight(nutrientDict['totalInG'], nutrientDict['unit'])[0]
                        per100g = amountStdUnit * (100/totalWeightG)
                        data[rowIndex][0] = round(per100g, 3)        
            else:
                if nutrientID not in allNutritionals:
                    data[rows][0] = '-'
                else:
                    nutrientDict = allNutritionals.get(nutrientID)
                    amountStdUnit = Nutrient.getStdUnitWeight(nutrientDict['totalInG'], nutrientDict['unit'])[0]
                    per100g = amountStdUnit * (100/totalWeightG)
                    data[rows][0] = round(per100g, 3)

        if comparedTo is not None:

            # sets data for nutritionals for the comparison
            with dbConnection('FormulaSchema').cursor() as cursor:
                
                # pulls the g per 100g of ingredient value from database, along with unit conversion values to convert to its standard unit
                cursor.execute('SELECT nutrient.nutrient_id, food_nutrient.nutrient_weight_g_per_100g, unit.conversion_factor, unit.conversion_offset FROM nutrient LEFT JOIN food_nutrient ON nutrient.nutrient_id = food_nutrient.nutrient_id LEFT JOIN unit ON nutrient.unit_id = unit.unit_id WHERE food_nutrient.food_id = %s',  (comparedTo,))
                results = cursor.fetchall()
                for result in results:
                    compareToName = 'Current formula being compared to ' + self.comboBox.currentText()
                    nutrientID = result['nutrient_id']
                    if nutrientID not in rowMap.keys():
                        continue
                    rowIndex = rowMap.get(nutrientID)
                    if rowIndex is None: continue
                    # vitamin A RAE ID --> [vitamin A IU, vitamin A RE, Vitamin A RAE] (17, 18, 19)
                    if nutrientID == 320:
                        for specialNutrient in rowIndex:
                            if specialNutrient == 17:
                                per100g = result['nutrient_weight_g_per_100g'] * (100000/0.3)
                                data[specialNutrient][1] = round(per100g, 3)
                            else:
                                per100g = result['nutrient_weight_g_per_100g'] * 100000
                                data[specialNutrient][1] = round(per100g, 3)
                    # Niacin ID --> [Niacin, Niacin Equivalents] (22, 23)
                    elif nutrientID == 406: 
                        for specialNutrient in rowIndex:
                            per100g = result['nutrient_weight_g_per_100g']/result['conversion_factor'] - result['conversion_offset']
                            data[specialNutrient][1] = round(per100g, 3)
                    else:
                        per100g = result['nutrient_weight_g_per_100g']/result['conversion_factor'] - result['conversion_offset']
                        data[rowIndex][1] = round(per100g, 3)
            
        model.inputTableData(data)
        view = QuickTableView(model, note=compareToName)
        view.setHeaderLabel('Comparison of the current formula and the chosen item, each scaled to 100 g')
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


    def refreshGeneralNutritionals(self):
        totalWeightG = self.formula.totalFormulaWeight()
        if self.scaleCombobox.currentIndex() != -1:
            scaleMethod = self.scaleCombobox.currentData(Qt.UserRole)
            if scaleMethod == 'weight':
                if self.servingWeightSpinBox.value() != 0 and self.unitWeightCombobox.currentData(Qt.UserRole) is None:
                    return
                # if user does not choose unit or does not input a serving weight, both are defaults
                if self.unitWeightCombobox.currentData(Qt.UserRole) is not None and self.servingWeightSpinBox.value() == 0: 
                    msg = QMessageBox()
                    msg.setText('Please complet ethe scale b weight information on Tab 3-Label')
                    msg.exec_()
                    totalWeight = self.formula.totalFormulaWeight()
                    # fills all the placeholders with no text
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
                # if user inputs all boxes correclty for scaling by weight
                else: 
                    servingWeight = self.servingWeightSpinBox.value()
                    unit = self.unitWeightCombobox.currentData(Qt.UserRole)
                    factor = unit.conversionFactor
                    offset = unit.conversionOffset
                    servingWeight = (servingWeight + offset)/factor

            # if user chooses to scale by number of servings 
            # scaleMethod == 'servings'
            else:
                servings = self.numServingsSpinbox.value()  # default is 1 serving
                if servings is None: 
                    msg = QMessageBox()
                    msg.setText('Please input a valid number of servings')
                    msg.exec_()
                    return
                else:
                    self.totalWeightPlaceholderLabel.setText(str(round(totalWeightG, 2)))
                    self.servingSizePlaceholderLabel.setText(str(round(totalWeightG/servings, 2)))
                    self.servingWeightPlaceholder.setText(str(round(totalWeightG/servings, 2)))
        
                    servingWeight = totalWeightG/servings
        else:
            servingWeight = totalWeightG

        scalingFactor = servingWeight/(100 * len(self.formula.getCurrentIngredients()))

        # checks whether a dictionary value has been placed for calories and other nutrients

        # TODO <-----------------------------------------
        # calories
        if self.formula.isNutrientInFormula(208):
            calories = self.formula.allNutritionals[208]['totalInG']
            calories = '{:.0f}'.format(round(calories * scalingFactor), 1)
            self.caloriesPlaceholderLabel.setText(str(calories))
        else: self.caloriesPlaceholderLabel.setText('Could not calculate')

        # fat
        if self.formula.isNutrientInFormula(204):
            fat = self.formula.allNutritionals[204]['totalInG']
            fat = round(fat*scalingFactor, 1)
            self.totalFatPlaceholderLabel.setText(str(fat))
        else: self.totalFatPlaceholderLabel.setText('Could not calculate')

        # carbs
        if self.formula.isNutrientInFormula(205):
            carbs = self.formula.allNutritionals[205]['totalInG']
            carbs = round(carbs*scalingFactor, 1)
            self.totalCarbsPlaceholderLabel.setText(str(carbs))
        else: self.totalCarbsPlaceholderLabel.setText('Could not calculate')

        # sugar
        if self.formula.isNutrientInFormula(269):
            sugar = self.formula.allNutritionals[269]['totalInG']
            sugar = round(sugar*scalingFactor, 1)
            self.sugarsPlaceholderLabel.setText(str(sugar))
        else: self.sugarsPlaceholderLabel.setText('Could not calculate')

        # added sugar
        if self.formula.isNutrientInFormula(659):
            addedSugar = self.formula.allNutritionals[659]['totalInG']
            addedSugar = round(addedSugar*scalingFactor, 1)
            self.addedSugarPlaceholderLabel.setText(str(addedSugar))
        else: self.addedSugarPlaceholderLabel.setText('Could not calculate')

        # protein
        if self.formula.isNutrientInFormula(203):
            protein = self.formula.allNutritionals[203]['totalInG']
            protein = round(protein*scalingFactor, 1)
            self.proteinPlaceholderLabel.setText(str(protein))
        else:  self.proteinPlaceholderLabel.setText('Could not calclulate')

        # dietary fiber
        if self.formula.isNutrientInFormula(291):
            dietaryFiber = self.formula.allNutritionals[291]['totalInG']
            dietaryFiber = round(dietaryFiber*scalingFactor, 1)
            self.dietaryFiberPlaceholderLabel.setText(str(dietaryFiber))
        else: self.dietaryFiberPlaceholderLabel.setText('Could not calculate')

        servingWeight = int(round(servingWeight, 0))
        totalWeightG = int(round(totalWeightG, 0))

    @pyqtSlot()
    # main function that calls other refresh functions 
    def refresh(self):
        if len(self.formula.getCurrentIngredients()) != 0:
            self.refreshGeneralNutritionals()
            self.refreshIngStatement()
            self.refreshReport()


    # clears the highlighted rows from the ingredients table widget 
    def removeSelected(self):
        rowIndeces = self.ingTabFormulaTableWidget.selectionModel().selectedRows(0)
        toRemove = []
        toRemoveDesc = ''
        for row in rowIndeces:
            toRemove.append(row.data(Qt.UserRole))
            if toRemoveDesc == '':
                toRemoveDesc = row.text()
            else: toRemoveDesc = toRemoveDesc + ', ' + row.text()
        confirm = QMessageBox.question(self, 'Confirm Removal', 'Are you sure you would like to remove {} from the formula?'.format(toRemoveDesc), QMessageBox.No | QMessageBox.YesTo)
        if confirm == QMessageBox.YesToAll:
            for id in toRemove: 
                self.formula.removeIngredient(foodID = id)
            self.refresh()

    # inserts row into qtablewidget 
    #@pyqtSlot()
    def insertRow(self):
        rowCount = self.qualityAttributeTableWidget.rowCount()
        self.qualityAttributeTableWidget.insertRow(rowCount)
        
    
    def refreshReport(self):  
        totalWeightG = self.formula.totalFormulaWeight()
        if self.scaleCombobox.currentIndex() == -1:
            self.spreadSheetBasedOnLabel.setText('Nutritionals in spreadsheet are based on 1 serving ({} grams). The total inputted weight is {} grams'.format(numberWithCommas(round(totalWeightG)), numberWithCommas(round(totalWeightG))))
            totalServings = 1
        else:
            # adjusts the header
            try: 
                scaleMethod = self.scaleCombobox.currentData(Qt.UserRole)
                # if user chooses to scale by weight
                if scaleMethod == 'weight':

                    if self.servingWeightSpinBox.value() == 0 or self.unitWeightCombobox.currentData(Qt.UserRole) is None:
                        self.spreadSheetBasedOnLabel.setText('Nutritionals in spreadsheet are based on 1 serving ({} g). There is 1 serving inputted'.format(numberWithCommas(round(totalWeightG))))
                        return 

                    weight = self.servingWeightSpinBox.value()
                    unit = self.unitWeightCombobox.currentData(Qt.UserRole)
                    factor = unit.conversionFactor
                    offset = unit.conversionOffset
                    servingWeight = (weight + offset) * factor
                    totalServings = totalWeightG/servingWeight
                    self.spreadSheetBasedOnLabel.setText('Nutritionals in spreadsheet are based on a serving weight of {} {}s ({} g). There are approximately {} servings inputted'.format(numberWithCommas(weight), unit.unitName, numberWithCommas(round(servingWeight)), totalServings))
                else:
                    servings = self.numServingsSpinbox.value()
                    if servings > 1:s='s'
                    else: s=''
                    servingWeight = totalWeightG/servings
                    totalServings = totalWeightG/servingWeight

                    self.spreadSheetBasedOnLabel.setText('Nutritionals in spreadsheet are based on 1 serving ({} g). There are approximately {} serving{} inputted'.format(numberWithCommas(round(servingWeight)), round(totalServings, 3), s))
            except Exception:
                servingWeight = totalWeightG
                self.spreadSheetBasedOnLabel.setText('Nutritionals in spreadsheet are based on 1 serving ({} g). There is 1 serving inputted'.format(numberWithCommas(round(servingWeight))))
                print('something went wrong during scaling')  
                totalServings = 1     


        ##### updates nutrient spreadsheet
        map = nutrientColMap()
        data = [] # maintains the dataframe
        totals = [0 for i in range(57)] # list for the totals of each nutrient, 57 is the number of columns in the self.nutrientReportTableView
        totals[0] = 'TOTAL'
        totals[1] = '-'
        totals[2] = '-'
        currentIngredients = self.formula.getCurrentIngredients()
        for ingredientDict in currentIngredients.values():
            ingredient = ingredientDict['object']
            dataframeRow = [0 for i in range(57)]

            # foodDesc
            dataframeRow[0] = ingredient.desc
            dataframeRow[1] = ingredient.getInputtedQuantity()[0]
            dataframeRow[2] = ingredient.getInputtedQuantity()[1].unitName
            dataframeRow[3] = ingredient.getInputWeightInGrams/totalServings
            totals[3] += ingredient.getInputWeightInGrams
            for nutrientID, dictItem in ingredient.nutrientDict.items():
                columnIndex = map[nutrientID]
                if columnIndex is None:
                    continue
                nutrient = dictItem['object']
                stdUnitAmount = nutrient.getStdUnitWeightFromG(dictItem['amountInIngredientG'])[0]/totalServings
                dataframeRow[columnIndex] = stdUnitAmount
                totals[columnIndex] += stdUnitAmount
            data.append(dataframeRow)
        data.append(totals)
        model = self.nutrientReportTableView.model()
        model.inputTableData(data)
        self.nutrientReportTableView.setModel(model)            
            
  
    def refreshIngStatement(self, foodList: list=None): 
        # if no ingredients, return
        if len(self.formula.getCurrentIngredients()) == 0:
            return
        listIng = list(self.formula.getCurrentIngredients().values())

        # gets ingredients by descending order of percent by weight
        sortedList = sorted(listIng, key = lambda i: i['percentByWeight'], reverse=True)
    
        # clears the table 
        self.ingStatementTable.setRowCount(0)
        rowIndex = 0
        
        
        mainStatement = []
        # for each ingredient
        for ingDict in sortedList:
            self.ingStatementTable.insertRow(rowIndex)
            ingredient = ingDict['object']

            # list of subingredients for the ingredient
            subIngsForTable = []
            

            # column headers are fooddesc, percentByWeight, subIngredients
            # sets the food description and percent in the table
            self.ingStatementTable.setItem(rowIndex, 0, QTableWidgetItem(str(ingredient.desc.capitalize())))
            self.ingStatementTable.setItem(rowIndex, 1, QTableWidgetItem(str(ingDict['percentByWeight'])))
    
            # if the ingredient has an ingredient statement stored
            if ingredient.ingredientStatement is not None:
                mainStatement.append(ingredient.ingredientStatement)
                subIngsForTable.append(ingredient.ingredentStatement.capitalize())
                self.ingStatementTable.setItem(rowIndex, 2, QTableWidgetItem(str(ingredient.ingredientStatement)))
                rowIndex += 1
                continue 

            nestedStatement = getIngredientStatement(ingredient.foodID) 
            extracted = extractIngredientStatement(nestedStatement)
            tableInsert = extracted.replace('<b>', '')
            tableInsert = tableInsert.replace('</b>', '')
            tableInsert = tableInsert.split('(')[1].replace('(', ' ').replace(')', ' ')
            self.ingStatementTable.setItem(rowIndex, 2, QTableWidgetItem(str(tableInsert)))
            mainStatement.append(extracted)
            rowIndex += 1
        mainStatement = ', '.join(mainStatement)
        self.ingStatementTable.resizeRowsToContents()
        self.ingStatementTable.resizeRowsToContents()
        self.ingStatementTextBox.setText(mainStatement)

    # updates the chartview to display a barchart 
    # The barchart shows what percentage of the total nutrient amount is 
    # attributed to the given ingredient

    def nutrComparisonChosen(self):

        self.singleNutrientChartView.resetCachedContent() # not sure if needed
        if self.formula.getNumberOfIngredients() == 0:
            msg = QMessageBox()
            msg.setText('No ingredients to show')
            msg.exec_()
            return

        # gets the nutrientID and nutrient name from the inputs
        nutrientID = self.nutrientReportCombobox.currentData(Qt.UserRole)['nutrient_id']
        nutrientName = self.nutrientReportCombobox.currentData(Qt.UserRole)['nutrient_name']
        if self.formula.nutrientExists(nutrientID = nutrientID) is not True:
            msg = QMessageBox()
            msg.setText('No nutrient to show')
            msg.exec_()
            return
        nutrientSum = 0
        # vvvvvvv these are related by index
        ingredientSeriesList = [] # stores the ingredient name, so we can input it into the chart
        nutrientAmountsG = [] # stores the amount of the nutrient in each index
        # ^^^^^^ these are related by index

        
        nutrientAmount = self.formula.getNutritientQuantity(nutrientID)


        nutrientAmount = Nutrient.getStdUnitWeight(nutrientAmount[0], nutrientAmount[1])
        # We are finding the sum of the nutrient content in the formula, as well as adding each ingredient to a list, with its respective amount of said nutrient
        # returns a dictionary data structure that contains that have been added to the formula so far
        formulaIngredients = self.formula.getCurrentIngredients()
        
        # iterates over ingredients
        for ingredientDict in formulaIngredients.values():
            
            # ingredient object that contains nutrient
            ingredientObject = ingredientDict['object']
            if nutrientID not in ingredientObject.nutrientDict:
                # using try block to make sure they both get appended at the same time
                try:
                    ingredientSeriesList.append(ingredientObject.desc.capitalize())
                    nutrientAmountsG.append(0)
                    nutrientSum += 0
                except:
                    continue
            else:
                try:
                    amountInIngredientG = float(ingredientObject.nutrientDict[nutrientID]['amountInIngredientG'])
                    ingredientSeriesList.append(ingredientObject.desc.capitalize())
                    nutrientAmountsG.append(amountInIngredientG)
                    nutrientSum += amountInIngredientG
                except Exception:
                    continue

        # stores the percentages of contribution for each ingredient
        percentages = [0 for i in range(len(ingredientSeriesList))]

        if nutrientSum != 0: 
            for i in range(len(nutrientAmountsG)):
                percentages[i] = (nutrientAmountsG[i]/nutrientSum) * 100

        # chart to display
        chart = QtCharts.QChart()

        # creates and displays the bar chart 
        barset = QtCharts.QBarSet('barsetlabel')
        barset.append(percentages)
        series = QtCharts.QBarSeries()
        series.append(barset)
        xAxis = QtCharts.QBarCategoryAxis()
        xAxis.append(ingredientSeriesList)
        #xAxis.setLabelsAngle(-45)
        font = QFont()
        font.setPointSize(10)
        font.setHintingPreference(QFont.PreferFullHinting)
        xAxis.setLabelsFont(font)
        yAxis = QtCharts.QValueAxis()
        yAxis.setRange(0, 100)
        yAxis.setTitleText('% of Total')
        chart.addSeries(series)
        amountString = str(round(nutrientAmount[0], 2)) + " " + nutrientAmount[1].unitName
        chart.setTitle("How each ingredient contributes to the total amount (<b>{amount}s</b>)  of <b>{nutrientName}</b>".format(amount=amountString,nutrientName=nutrientName))
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

    # submits the form to the database
    def formSubmit(self):
        pass

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
        qtablewidgetitem11 = self.qualityAttributeTableWidget.horizontalHeaderItem(3)
        qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"Description", None))

        self.ingStatementLabel.setText(QCoreApplication.translate("Dialog", u"Ingredient Statement", None))
        ___qtablewidgetitem9 = self.ingStatementTable.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"Ingredient Name", None));
        ___qtablewidgetitem10 = self.ingStatementTable.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"% by Weight", None));
        ___qtablewidgetitem11 = self.ingStatementTable.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"Sub-Ingredients", None));
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

        self.formulaEditorTabWidget.setTabText(self.formulaEditorTabWidget.indexOf(self.labelTab), QCoreApplication.translate("Dialog", u"Label", None))

        self.nutrientSpreadsheetLabel.setText(QCoreApplication.translate("Dialog", u"Nutrient Spreadsheet", None))
        self.singleNutrientLabel.setText(QCoreApplication.translate("Dialog", u"Single Nutrient ", None))
        self.dailyValueLabel.setText(QCoreApplication.translate("Dialog", u"Daily Value and Per 100g", None))
        self.byComparisonLabel.setText(QCoreApplication.translate("Dialog", u"Comparison", None))
        self.formulaEditorTabWidget.setTabText(self.formulaEditorTabWidget.indexOf(self.nutrientReportTab), QCoreApplication.translate("Dialog", u"Nutrient Report", None))
        #___qtablewidgetitem75 = self.imagesTableWidget.horizontalHeaderItem(0)
       # #___qtablewidgetitem75.setText(QCoreApplication.translate("Dialog", u"Context/Note", None));
        #___qtablewidgetitem76 = self.imagesTableWidget.horizontalHeaderItem(1)
        #___qtablewidgetitem76.setText(QCoreApplication.translate("Dialog", u"Image", None));
       # self.formulaEditorTabWidget.setTabText(self.formulaEditorTabWidget.indexOf(self.imagesTab), QCoreApplication.translate("Dialog", u"Images", None))
    # retranslateUi

app = QApplication(sys.argv)
gui = formulaEditorDialog('ExampleFormulaName')
gui.show()
sys.exit(app.exec_())



     