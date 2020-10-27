# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulaEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from helpers import connectDB, displayNFP


class formulaEditorDialog(QDialog):
    
    def __init__(self):
        super(formulaEditorDialog, self).__init__()
        self.setupUi(self)
        self.setupSuggestions()
        self.setupActions()
    
    def setupSuggestions(self):
        
        # Adds all cateogories to category box
        with connectDB().cursor() as cursor:
            cursor.execute("SELECT category_id, category_name FROM formula_category")
            allCategories = cursor.fetchall()
            for category in allCategories:
                name = category[1]
                id = category[0]
                index = self.categoryComboBox.currentIndex()
                self.categoryComboBox.insertItem(index, name, id)
            self.categoryComboBox.setCurrentText("")

        # Adds completer to searchbar
        with connectDB().cursor() as cursor:
            cursor.execute(
                'SELECT ing_common_name, ing_specific_name,             supplier_name, supplier_ing_item_code FROM ingredient INNER JOIN supplier ON ingredient.supplier_id = supplier.supplier_id'
            )
            ingredients = cursor.fetchall()
            suggestions = []
            for ingredient in ingredients:
                if ingredient[2] is None:
                    if ingredient[1] is None:
                        suggestion = ingredient[0] + '(General)'
                    else:
                        suggestion = ingredient[0] + '(' + ingredient[1] + ')'
                else:
                    suggestion = ingredient[1] + '(' + ingredient[2] + ',' + ingredient[0] + ')'
                suggestions.append(suggestion)
            completer = QCompleter(suggestions)
            self.formulaIngredientSearchLineEdit.setCompleter(completer)
            
       # Adds          
        
    def setupActions(self):
        # self.displayNFPBtn.clicked.connect(displayNFP())
        
    

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

        self.perLabel = QLabel(self.widget)
        self.perLabel.setObjectName(u"perLabel")
        self.perLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.perLabel, 2, 0, 1, 1)

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

        self.perPlaceholderLabel = QLabel(self.widget)
        self.perPlaceholderLabel.setObjectName(u"perPlaceholderLabel")

        self.gridLayout.addWidget(self.perPlaceholderLabel, 2, 1, 1, 1)

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


        self.addFromSearchBtn = QPushButton(self.formulaIngredientHeaderWidget)
        self.addFromSearchBtn.setObjectName(u"addFromSearchBtn")
        self.addFromSearchBtn.setText(u"Add")
        self.horizontalLayout_10.addWidget(self.addFromSearchBtn)


        self.formulaIngredientSearchBtn = QPushButton(self.formulaIngredientHeaderWidget)
        self.formulaIngredientSearchBtn.setObjectName(u"formulaIngredientSearchBtn")

        self.horizontalLayout_10.addWidget(self.formulaIngredientSearchBtn)


        self.verticalLayout_11.addWidget(self.formulaIngredientHeaderWidget)

        self.ingTabFormulaTableWidget = QTableWidget(self.ingredientsTab)
        if (self.ingTabFormulaTableWidget.columnCount() < 8):
            self.ingTabFormulaTableWidget.setColumnCount(8)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.ingTabFormulaTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.ingTabFormulaTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.ingTabFormulaTableWidget.setObjectName(u"ingTabFormulaTableWidget")
        self.ingTabFormulaTableWidget.horizontalHeader().setStretchLastSection(True)
        self.ingTabFormulaTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.ingTabFormulaTableWidget.verticalHeader().setProperty("showSortIndicator", True)

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
        if (self.ingStatementTable.columnCount() < 4):
            self.ingStatementTable.setColumnCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.ingStatementTable.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.ingStatementTable.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.ingStatementTable.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.ingStatementTable.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        self.ingStatementTable.setObjectName(u"ingStatementTable")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ingStatementTable.sizePolicy().hasHeightForWidth())
        self.ingStatementTable.setSizePolicy(sizePolicy2)
        self.ingStatementTable.setMinimumSize(QSize(0, 100))
        self.ingStatementTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ingStatementTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ingStatementTable.setAlternatingRowColors(True)
        self.ingStatementTable.setSortingEnabled(True)
        self.ingStatementTable.horizontalHeader().setDefaultSectionSize(130)
        self.ingStatementTable.horizontalHeader().setStretchLastSection(True)

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
        self.ingStatementGenerateBtn = QPushButton(self.ingStatementButtonBox)
        self.ingStatementGenerateBtn.setObjectName(u"ingStatementGenerateBtn")

        self.horizontalLayout_8.addWidget(self.ingStatementGenerateBtn)

        self.ingStatementRefreshBtn = QPushButton(self.ingStatementButtonBox)
        self.ingStatementRefreshBtn.setObjectName(u"ingStatementRefreshBtn")

        self.horizontalLayout_8.addWidget(self.ingStatementRefreshBtn)

        self.ingStatementEditBtn = QPushButton(self.ingStatementButtonBox)
        self.ingStatementEditBtn.setObjectName(u"ingStatementEditBtn")

        self.horizontalLayout_8.addWidget(self.ingStatementEditBtn)

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

        self.servingScaleSpinBox = QDoubleSpinBox(self.recipeMakesWidget)
        self.servingScaleSpinBox.setObjectName(u"servingScaleSpinBox")

        self.horizontalLayout_4.addWidget(self.servingScaleSpinBox)

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
        self.recipeWeighsCheckbox = QCheckBox(self.recipeWeighsWidget)
        self.recipeWeighsCheckbox.setObjectName(u"recipeWeighsCheckbox")

        self.horizontalLayout_5.addWidget(self.recipeWeighsCheckbox)

        self.servingWeightSpinBox = QSpinBox(self.recipeWeighsWidget)
        self.servingWeightSpinBox.setObjectName(u"servingWeightSpinBox")

        self.horizontalLayout_5.addWidget(self.servingWeightSpinBox)

        self.unitWeightSpinBox = QComboBox(self.recipeWeighsWidget)
        self.unitWeightSpinBox.setObjectName(u"unitWeightSpinBox")

        self.horizontalLayout_5.addWidget(self.unitWeightSpinBox)


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


        self.retranslateUi(Dialog)

        self.formulaEditorTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

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
        self.perLabel.setText(QCoreApplication.translate("Dialog", u"Per ", None))
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
        self.perPlaceholderLabel.setText(QCoreApplication.translate("Dialog", u"Must input serving size", None))
        self.proteinLabel.setText(QCoreApplication.translate("Dialog", u"Protein (g)", None))
        self.addedSugarPlaceholderLabel.setText("")
        self.proteinPlaceholderLabel.setText("")
        self.totalWeightLabel.setText(QCoreApplication.translate("Dialog", u"Total Weight", None))
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
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"Specific Name", None));
        ___qtablewidgetitem11 = self.ingStatementTable.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"% by Weight", None));
        ___qtablewidgetitem12 = self.ingStatementTable.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"Sub-Ingredients", None));
        self.ingStatetmentTxtLabel.setText(QCoreApplication.translate("Dialog", u"Click generate below to autofill statement. Click edit to input manually or change auto-generated text", None))
        self.ingStatementGenerateBtn.setText(QCoreApplication.translate("Dialog", u"Generate", None))
        self.ingStatementRefreshBtn.setText(QCoreApplication.translate("Dialog", u"Refresh", None))
        self.ingStatementEditBtn.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.ingStatementPrintBtn.setText(QCoreApplication.translate("Dialog", u"Print", None))
        self.formulaEditorTabWidget.setTabText(self.formulaEditorTabWidget.indexOf(self.qualityTab), QCoreApplication.translate("Dialog", u"Quality", None))
        self.servingInfoLabelHeader.setText(QCoreApplication.translate("Dialog", u"Serving Information", None))
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
        self.recipeWeighsCheckbox.setText(QCoreApplication.translate("Dialog", u"Recipe weighs", None))
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




if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = formulaEditorDialog()
    gui.show()
    sys.exit(app.exec_())
    