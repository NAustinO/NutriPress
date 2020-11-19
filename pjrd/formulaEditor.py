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
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from operator import itemgetter

sys.path.append('../pjrd')
from helpers import displayNFP, test, dbConnection, TimedMessageBox
from formulaEditorSearchResults import searchResults
#from import confirmAddDialog


class formulaEditorDialog(QDialog):
    
    def __init__(self, revision: bool = None, formulaName: str = None, prevRevisionID: int = None, differences: str = None):
        super(formulaEditorDialog, self).__init__()
        self.setupUi(self)
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
        self.ingTabFormulaTableWidget.horizontalHeader().setStretchLastSection(True)
        self.ingTabFormulaTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.ingTabFormulaTableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.ingTabFormulaTableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

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

        self.addAnAttributeBtn = QPushButton(self.qualityAttributeHeaderWidget)
        self.addAnAttributeBtn.setObjectName(u"addAnAttributeBtn")

        self.horizontalLayout_13.addWidget(self.addAnAttributeBtn)


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
        #self.ingStatementTable.horizontalHeader().setDefaultSectionSize(130)
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


        self.verticalLayout_4.addWidget(self.servingInfoFrame)

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

        self.recipeMakesWidget = QWidget(self.scaleFrame)
        self.recipeMakesWidget.setObjectName(u"recipeMakesWidget")
        sizePolicy.setHeightForWidth(self.recipeMakesWidget.sizePolicy().hasHeightForWidth())
        self.recipeMakesWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.recipeMakesWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.recipeMakesCheckbox = QCheckBox(self.recipeMakesWidget)
        self.recipeMakesCheckbox.setObjectName(u"recipeMakesCheckbox")

        self.horizontalLayout_4.addWidget(self.recipeMakesCheckbox)

        self.servingScaleCombobox = QDoubleSpinBox(self.recipeMakesWidget)
        self.servingScaleCombobox.setObjectName(u"servingScaleCombobox")
        self.servingScaleCombobox.setValue(1)

        self.horizontalLayout_4.addWidget(self.servingScaleCombobox)

        self.servingsLabel = QLabel(self.recipeMakesWidget)
        self.servingsLabel.setObjectName(u"servingsLabel")

        self.horizontalLayout_4.addWidget(self.servingsLabel)


        self.verticalLayout.addWidget(self.recipeMakesWidget)

        self.recipeWeighsWidget = QWidget(self.scaleFrame)
        self.recipeWeighsWidget.setObjectName(u"recipeWeighsWidget")
        sizePolicy.setHeightForWidth(self.recipeWeighsWidget.sizePolicy().hasHeightForWidth())
        self.recipeWeighsWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.recipeWeighsWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.servingWeighsCheckbox = QCheckBox(self.recipeWeighsWidget)
        self.servingWeighsCheckbox.setObjectName(u"servingWeighsCheckbox")

        self.horizontalLayout_5.addWidget(self.servingWeighsCheckbox)

        self.servingWeightSpinBox = QSpinBox(self.recipeWeighsWidget)
        self.servingWeightSpinBox.setObjectName(u"servingWeightSpinBox")
        self.servingWeightSpinBox.setMaximum(5000)
        self.servingWeightSpinBox.setMinimum(0)
        self.servingWeightSpinBox.setSingleStep(10)

        self.horizontalLayout_5.addWidget(self.servingWeightSpinBox)

        self.unitWeightCombobox = QComboBox(self.recipeWeighsWidget)
        self.unitWeightCombobox.setObjectName(u"unitWeightCombobox")

        self.horizontalLayout_5.addWidget(self.unitWeightCombobox)


        self.verticalLayout.addWidget(self.recipeWeighsWidget)


        self.verticalLayout_4.addWidget(self.scaleFrame)

        self.labelSettingsFrame = QFrame(self.labelScrollAreaContents)
        self.labelSettingsFrame.setObjectName(u"labelSettingsFrame")
        self.labelSettingsFrame.setFrameShape(QFrame.StyledPanel)
        self.labelSettingsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.labelSettingsFrame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.labelSettingsHeaderLabel = QLabel(self.labelSettingsFrame)
        self.labelSettingsHeaderLabel.setObjectName(u"labelSettingsHeaderLabel")
        self.labelSettingsHeaderLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.labelSettingsHeaderLabel)

        self.labelSettingsContainerWidget = QWidget(self.labelSettingsFrame)
        self.labelSettingsContainerWidget.setObjectName(u"labelSettingsContainerWidget")
        self.gridLayout_2 = QGridLayout(self.labelSettingsContainerWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.voluntaryNutritionalsContainerWidget = QWidget(self.labelSettingsContainerWidget)
        self.voluntaryNutritionalsContainerWidget.setObjectName(u"voluntaryNutritionalsContainerWidget")
        self.verticalLayout_5 = QVBoxLayout(self.voluntaryNutritionalsContainerWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.voluntaryNutritionalsLabel = QLabel(self.voluntaryNutritionalsContainerWidget)
        self.voluntaryNutritionalsLabel.setObjectName(u"voluntaryNutritionalsLabel")
        self.voluntaryNutritionalsLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.voluntaryNutritionalsLabel)

        self.voluntaryNutritionalsListWidget = QListWidget(self.voluntaryNutritionalsContainerWidget)
        self.voluntaryNutritionalsListWidget.setObjectName(u"voluntaryNutritionalsListWidget")

        self.verticalLayout_5.addWidget(self.voluntaryNutritionalsListWidget)


        self.gridLayout_2.addWidget(self.voluntaryNutritionalsContainerWidget, 0, 0, 1, 1)

        self.generalSettingsHeaderWidget = QWidget(self.labelSettingsContainerWidget)
        self.generalSettingsHeaderWidget.setObjectName(u"generalSettingsHeaderWidget")
        self.verticalLayout_12 = QVBoxLayout(self.generalSettingsHeaderWidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.generalSettingsHeaderLabel = QLabel(self.generalSettingsHeaderWidget)
        self.generalSettingsHeaderLabel.setObjectName(u"generalSettingsHeaderLabel")

        self.verticalLayout_12.addWidget(self.generalSettingsHeaderLabel)

        self.checkBox_2 = QCheckBox(self.generalSettingsHeaderWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_12.addWidget(self.checkBox_2)


        self.gridLayout_2.addWidget(self.generalSettingsHeaderWidget, 0, 1, 1, 1)


        self.verticalLayout_13.addWidget(self.labelSettingsContainerWidget)


        self.verticalLayout_4.addWidget(self.labelSettingsFrame)

        self.labelScrollArea.setWidget(self.labelScrollAreaContents)

        self.verticalLayout_3.addWidget(self.labelScrollArea)

        self.displayNutritionalLabelBtn = QPushButton(self.labelTab)
        self.displayNutritionalLabelBtn.setObjectName(u"displayNutritionalLabelBtn")
        self.displayNutritionalLabelBtn.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_3.addWidget(self.displayNutritionalLabelBtn, 0, Qt.AlignHCenter)

        self.formulaEditorTabWidget.addTab(self.labelTab, "")

        self.horizontalLayout_9.addWidget(self.formulaEditorTabWidget)


        ##########
        self.ingTabFormulaTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ingTabFormulaTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        ########
        self.retranslateUi(Dialog)

        self.formulaEditorTabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def setupLogic(self):
        # signal setup
        self.formulaIngredientSearchBtn.clicked.connect(self.openSearchResultsDialog)
        self.displayNFPBtn.clicked.connect(displayNFP())
        self.removeSelectedBtn.clicked.connect(self.removeSelected)
        self.servingWeighsCheckbox.stateChanged.connect(self.toggleFocus)
        self.recipeMakesCheckbox.stateChanged.connect(self.toggleFocus)
        self.editIngStatementBtn.clicked.connect(self.toggleReadOnly)
        self.copyIngStatementBtn.clicked.connect(self.copy)
        # self.ingTabFormulaTableWidget.cellChanged.connect(self.refreshGeneralNutritionals)

        # event setup
        self.formulaIngredientSearchBtn.installEventFilter(self)

        # categories completer and category_id added to the category box TODO add error handling
        with dbConnection('FormulaSchema').cursor() as cursor:
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

        # completer for scaling formula combobox
        with dbConnection('FormulaSchema').cursor() as cursor:
            completer = QCompleter()
            model = QStandardItemModel()
            cursor.execute('SELECT unit_id, unit_name, unit_symbol, conversion_factor, conversion_offset FROM unit WHERE unit_class = "mass" ORDER BY conversion_factor ASC')
            uoms = cursor.fetchall()
            for uom in uoms:
                unitItem = QStandardItem()
                unitItem.setText('{unitName} ({unitSymbol})'.format(unitName=uom['unit_name'], unitSymbol = uom['unit_symbol']))
                unitItem.setData(uom, Qt.UserRole)
                model.appendRow(unitItem)
            completer.setModel(model)
            completer.setCompletionMode(QCompleter.InlineCompletion)
            self.unitWeightCombobox.setModel(model)
            self.unitWeightCombobox.setCurrentIndex(-1)
            
    # toggles the focus of the scale formula portion 
    def toggleFocus(self):
        if self.recipeMakesCheckbox.isChecked() is False and self.servingWeighsCheckbox.isChecked() is False:
            self.recipeMakesWidget.setDisabled(False)
            self.recipeWeighsWidget.setDisabled(False)
        if self.servingWeighsCheckbox.isChecked() is True:
            self.recipeMakesWidget.setDisabled(True)
        if self.recipeMakesCheckbox.isChecked() is True:
            self.recipeWeighsWidget.setDisabled(True)
    
    # toggles 
    def toggleReadOnly(self):
        # if the box is not editable, make editable and change button to done editing
        if self.ingStatementTextBox.isReadOnly():
            self.ingStatementTextBox.setReadOnly(False)
            self.editIngStatementBtn.setText('Done Editing')
        # if the box is editable
        else:
            self.ingStatementTextBox.setReadOnly(True)
            self.editIngStatementBtn.setText('Edit')

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

    # TODO. 
    # Note: attached to signal cell changed in qtablewidget
    def refreshGeneralNutritionals(self, totalWeight):
        
        # initializes all nutrient values
        calories = 0
        fat = 0 
        carbs = 0 
        sugar = 0 
        addedSugar = 0
        protein = 0
        dietaryFiber = 0
        
        # stores food IDs
        idList = []

        # gets all food IDs currently in table 
        for rowIndex in range(self.ingTabFormulaTableWidget.rowCount()):
            itemData = self.ingTabFormulaTableWidget.item(rowIndex, 0).data(Qt.UserRole)
            id = itemData['food_id']
            idList.append(id)
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
        # places id in set so we can get number of unique ids
        idSet = set(idList)
        servingWeight = 'None'

        # determines factor for use when calculating the nutrients relative to the specified serving size
        # if user scales by number of servings
        if self.recipeMakesCheckbox.isChecked():
            servings = self.servingScaleCombobox.value() #default is 1 serving 
            scalingFactor = (1/servings)
            servingWeight = totalWeight * scalingFactor
        # if user scales by weight or does not check either box for scaling
        else: # --> if self.servingWeighsCheckbox.isChecked():
            servingWeight = self.servingWeightSpinBox.value()
            unitData = self.unitWeightCombobox.currentData(Qt.UserRole)
            # if user does not choose a unit, but inputs a weight
            if unitData is None and servingWeight != 0:
                msg = QMessageBox()
                msg.setText('Must choose a unit')
                self.unitWeightCombobox.setFocus()
                msg.exec_()
                return
            # if user does not input a weight regardless of if they choose a unit
            if servingWeight == 0:
                servingWeight = totalWeight
                conversion = 1
            
            else:
                # redundant
                if unitData is None:
                    servingWeight = totalWeight
                # if user chooses a inputs a weight 
                else:
                    conversion = unitData['conversion_factor']
                    offset = unitData['conversion_offset']
                    servingWeight = (servingWeight + offset) * conversion
        # recalculates the nutrient values based on scaling input
        scalingFactor = (servingWeight/(100 * len(idSet)))
        protein = round(protein*scalingFactor, 1)
        fat = round(fat*scalingFactor, 1)
        carbs = round(carbs * scalingFactor, 1)
        
        calories = '{:.0f}'.format(round(calories * scalingFactor, -1))
        #calories = int(round(calories * scalingFactor, 0))
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

    def self(self):
        return self

    # main function that calls other refresh functions 
    def refresh(self):
        totalWeight = self.refreshTable()
        self.refreshGeneralNutritionals(totalWeight)
        self.refreshIngStatement()

    # clears the highlighted rows from the ingredients table widget 
    def removeSelected(self):
        selected = self.ingTabFormulaTableWidget.selectionModel().selectedRows()
        if len(selected) == 0:
            return
        else:
            toRemove = ''
            for selection in selected:
                data = selection.data(Qt.UserRole)
                foodDesc = data['food_desc']
                if toRemove == '':
                    toRemove = foodDesc
                else: 
                    toRemove = toRemove + ', ' + foodDesc
            confirm = QMessageBox.question(self, 'Confirm', 'Would you like to remove {} from the formula?'.format(toRemove), QMessageBox.No | QMessageBox.YesToAll)
            if confirm == QMessageBox.YesToAll:
                for selection in selected:
                    self.ingTabFormulaTableWidget.removeRow(selection.row())
                self.refresh()

    # enter event. called when enter is pressed during
    def eventFilter(self, source, event):
        if (event.type() == QEvent.KeyPress and source == self.formulaIngredientSearchLineEdit and event.key() == Qt.Key_Enter):
            self.openSearchResultsDialog()
            return True
        return super(QDialog, self).eventFilter(source, event)

    def refreshIngStatement(self): 
        foodList =[]
        ingStatement = []

        # adds the percent by weight in formula to the food dictionary
        for rowIndex in range(self.ingTabFormulaTableWidget.rowCount()):
            itemData = self.ingTabFormulaTableWidget.item(rowIndex, 0).data(Qt.UserRole)
            percentByWeight = self.ingTabFormulaTableWidget.item(rowIndex, 1).data(Qt.UserRole + 1)
            itemData['percent'] = percentByWeight
            foodList.append(itemData)

        # sorts the items from food list by percent weight ASC
        sortedFoodList = sorted(foodList, key = itemgetter('percent'), reverse=False)
        # clears the table
        self.ingStatementTable.setRowCount(0)
        rowIndex = 0

        # iterates through sorted list of ingredients
        #   adds to the ingredient statement table the percent weight and the dictionary with the data
        #   

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
                rows = cursor.execute('SELECT food.food_id, food_desc, subfood_desc, ingredient_weight FROM food LEFT JOIN subfood_food ON food.food_id = subfood_food.food_id WHERE food.food_id = %s ORDER BY food.food_id ASC, ingredient_weight DESC', (foodID,))
                # if the food is a fndds ingredient preloaded from database
                if rows != 0:
                    subfoods = cursor.fetchall()
                    for food in subfoods:
                        subIngsForTable.append('({}.)'.format(counter) + food['subfood_desc'])
                        subIngsForStatement.append(food['subfood_desc'])
                        counter += 1
                #else:
                    # if the food is a formula (composed of other foods)
                 #   cursor.execute('')

            subIngsForTable = ', '.join(subIngsForTable)
            subIngsForStatement = ', '.join(subIngsForStatement)
            self.ingStatementTable.setItem(rowIndex, 2, QTableWidgetItem(subIngsForTable)) 
            foodStatement = '<b>{food}</b> ({subFoods})'.format(food=food['food_desc'].title(), subFoods=subIngsForStatement)
            ingStatement.append(foodStatement)
        self.ingStatementTable.resizeRowsToContents()

        ingStatement = ', '.join(ingStatement)
        self.ingStatementTextBox.setText(ingStatement)

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
    def openSearchResultsDialog(self):
        query = self.formulaIngredientSearchLineEdit.text()
        root = self.self()
        dialog = searchResults(query, root)
        dialog.setModal(True)
        dialog.exec_()

    # refreshes the percent by weight column of the formula when called, returns the total weight in grams
    def refreshTable(self):
        totalWeightG = 0

        # calculatest the total weight of all ingredients in the formula
        for row in range(self.ingTabFormulaTableWidget.rowCount()):
            foodItem = self.ingTabFormulaTableWidget.item(row, 0).data(Qt.UserRole)
            weightOfItemG = foodItem['weight'] * foodItem['conversion_factor']
            totalWeightG += weightOfItemG

        # calculates the % by weight of each ingredient and adds to the table widget
        for row in range(self.ingTabFormulaTableWidget.rowCount()):
            foodItem = self.ingTabFormulaTableWidget.item(row, 0).data(Qt.UserRole)
            percentWeight = ((foodItem['weight'] * foodItem['conversion_factor'])/totalWeightG) * 100
            percentWeight = round(percentWeight, 3)
            percentTableItem = QTableWidgetItem()
            percentTableItem.setData(Qt.UserRole + 1, percentWeight)
            if percentWeight < 0.001:
                percentTableItem.setText('<.001')
                self.ingTabFormulaTableWidget.setItem(row, 1, percentTableItem)
            else:
                percentTableItem.setText(str(percentWeight))
                self.ingTabFormulaTableWidget.setItem(row, 1, percentTableItem)
        return totalWeightG

    # TODO
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
        self.addAnAttributeBtn.setText(QCoreApplication.translate("Dialog", u"Add Attribute", None))
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
        self.recipeMakesCheckbox.setText(QCoreApplication.translate("Dialog", u"Recipe makes", None))
        self.servingsLabel.setText(QCoreApplication.translate("Dialog", u"Serving(s)", None))
        self.servingWeighsCheckbox.setText(QCoreApplication.translate("Dialog", u"Serving weighs", None))
        self.labelSettingsHeaderLabel.setText(QCoreApplication.translate("Dialog", u"General Label Settings", None))
#if QT_CONFIG(whatsthis)
        self.voluntaryNutritionalsContainerWidget.setWhatsThis(QCoreApplication.translate("Dialog", u"User inputted list for which nutritionals to display on label ", None))
#endif // QT_CONFIG(whatsthis)
        self.voluntaryNutritionalsLabel.setText(QCoreApplication.translate("Dialog", u"Voluntary Nutritional Configurations", None))
        self.generalSettingsHeaderLabel.setText(QCoreApplication.translate("Dialog", u"General Settings", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.displayNutritionalLabelBtn.setText(QCoreApplication.translate("Dialog", u"Display Nutrition Label", None))
        self.formulaEditorTabWidget.setTabText(self.formulaEditorTabWidget.indexOf(self.labelTab), QCoreApplication.translate("Dialog", u"Label", None))
    # retranslateUi

app = QApplication(sys.argv)
gui = formulaEditorDialog()
gui.show()
sys.exit(app.exec_())



     