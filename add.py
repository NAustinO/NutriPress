# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulaEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(865, 795)
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
        self.revisionCheckBox.setCheckable(False)

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

        self.line = QFrame(self.generalFrame1)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.line)


        self.horizontalLayout_11.addWidget(self.generalFrame1)

        self.generalNutritionalsFrame = QFrame(self.generalInfoContainerWidget)
        self.generalNutritionalsFrame.setObjectName(u"generalNutritionalsFrame")
        self.generalNutritionalsFrame.setFrameShape(QFrame.StyledPanel)
        self.generalNutritionalsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.generalNutritionalsFrame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.generalNutritionalsHeaderWidget = QWidget(self.generalNutritionalsFrame)
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

        self.widget = QWidget(self.generalNutritionalsFrame)
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

        self.displayNFPBtn = QPushButton(self.generalNutritionalsFrame)
        self.displayNFPBtn.setObjectName(u"displayNFPBtn")

        self.verticalLayout_14.addWidget(self.displayNFPBtn)


        self.horizontalLayout_11.addWidget(self.generalNutritionalsFrame)


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

        self.addBtn = QPushButton(self.formulaIngredientHeaderWidget)
        self.addBtn.setObjectName(u"addBtn")

        self.horizontalLayout_10.addWidget(self.addBtn)

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
        self.qualityTabScrollAreaContents.setGeometry(QRect(0, 0, 793, 714))
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
        self.ingStatementTextBox.setOverwriteMode(False)

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
        self.labelScrollAreaContents.setGeometry(QRect(0, 0, 793, 680))
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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

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
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 793, 714))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.nutrientSpreadsheetLabel = QLabel(self.scrollAreaWidgetContents)
        self.nutrientSpreadsheetLabel.setObjectName(u"nutrientSpreadsheetLabel")

        self.verticalLayout_5.addWidget(self.nutrientSpreadsheetLabel)

        self.nutrientReportTableWidget = QTableWidget(self.scrollAreaWidgetContents)
        if (self.nutrientReportTableWidget.columnCount() < 57):
            self.nutrientReportTableWidget.setColumnCount(57)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(15, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(16, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(17, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(18, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(19, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(20, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(21, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(22, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(23, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(24, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(25, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(26, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(27, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(28, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(29, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(30, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(31, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(32, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(33, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(34, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(35, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(36, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(37, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(38, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(39, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(40, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(41, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(42, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(43, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(44, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(45, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(46, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(47, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(48, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(49, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(50, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(51, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(52, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(53, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(54, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(55, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.nutrientReportTableWidget.setHorizontalHeaderItem(56, __qtablewidgetitem71)
        self.nutrientReportTableWidget.setObjectName(u"nutrientReportTableWidget")
        font = QFont()
        font.setPointSize(9)
        self.nutrientReportTableWidget.setFont(font)
        self.nutrientReportTableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.nutrientReportTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.nutrientReportTableWidget.setAlternatingRowColors(True)
        self.nutrientReportTableWidget.setSortingEnabled(True)

        self.verticalLayout_5.addWidget(self.nutrientReportTableWidget)

        self.horizLine1 = QFrame(self.scrollAreaWidgetContents)
        self.horizLine1.setObjectName(u"horizLine1")
        self.horizLine1.setFrameShape(QFrame.HLine)
        self.horizLine1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.horizLine1)

        self.singleNutrientLabel = QLabel(self.scrollAreaWidgetContents)
        self.singleNutrientLabel.setObjectName(u"singleNutrientLabel")

        self.verticalLayout_5.addWidget(self.singleNutrientLabel)

        self.nutrientReportCombobox = QComboBox(self.scrollAreaWidgetContents)
        self.nutrientReportCombobox.setObjectName(u"nutrientReportCombobox")
        self.nutrientReportCombobox.setCurrentText(u"")

        self.verticalLayout_5.addWidget(self.nutrientReportCombobox)

        self.singleNutrientGraphicsView = QGraphicsView(self.scrollAreaWidgetContents)
        self.singleNutrientGraphicsView.setObjectName(u"singleNutrientGraphicsView")

        self.verticalLayout_5.addWidget(self.singleNutrientGraphicsView)

        self.horizLine2 = QFrame(self.scrollAreaWidgetContents)
        self.horizLine2.setObjectName(u"horizLine2")
        self.horizLine2.setFrameShape(QFrame.HLine)
        self.horizLine2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.horizLine2)

        self.dailyValueLabel = QLabel(self.scrollAreaWidgetContents)
        self.dailyValueLabel.setObjectName(u"dailyValueLabel")

        self.verticalLayout_5.addWidget(self.dailyValueLabel)

        self.dvReportTableWidget = QTableWidget(self.scrollAreaWidgetContents)
        self.dvReportTableWidget.setObjectName(u"dvReportTableWidget")
        self.dvReportTableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_5.addWidget(self.dvReportTableWidget)

        self.horizLine3 = QFrame(self.scrollAreaWidgetContents)
        self.horizLine3.setObjectName(u"horizLine3")
        self.horizLine3.setFrameShape(QFrame.HLine)
        self.horizLine3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.horizLine3)

        self.byComparisonLabel = QLabel(self.scrollAreaWidgetContents)
        self.byComparisonLabel.setObjectName(u"byComparisonLabel")

        self.verticalLayout_5.addWidget(self.byComparisonLabel)

        self.comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_5.addWidget(self.comboBox)

        self.compareReportTableWidget = QTableWidget(self.scrollAreaWidgetContents)
        if (self.compareReportTableWidget.columnCount() < 3):
            self.compareReportTableWidget.setColumnCount(3)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.compareReportTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.compareReportTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.compareReportTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem74)
        self.compareReportTableWidget.setObjectName(u"compareReportTableWidget")
        self.compareReportTableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.compareReportTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_5.addWidget(self.compareReportTableWidget)

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


        self.retranslateUi(Dialog)
        self.ingTabFormulaTableWidget.itemChanged.connect(self.generalNutritionalsFrame.update)
        self.ingTabFormulaTableWidget.itemChanged.connect(self.ingStatementTextBox.update)
        self.ingTabFormulaTableWidget.itemChanged.connect(self.ingStatementTable.update)

        self.formulaEditorTabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Formula Editor", None))
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
        self.addBtn.setText(QCoreApplication.translate("Dialog", u"Add", None))
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
        ___qtablewidgetitem6 = self.ingTabFormulaTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"TODO - EDIT BTN", None));
        ___qtablewidgetitem7 = self.ingTabFormulaTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"TODO -DELETE BTN", None));
        self.formulaEditorTabWidget.setTabText(self.formulaEditorTabWidget.indexOf(self.ingredientsTab), QCoreApplication.translate("Dialog", u"Ingredients", None))
        self.inputQualityAttributeLabel.setText(QCoreApplication.translate("Dialog", u"Input Quality Attributes", None))
        self.addAnAttributeBtn.setText(QCoreApplication.translate("Dialog", u"Add Attribute", None))
        ___qtablewidgetitem8 = self.qualityAttributeTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"Quality", None));
        ___qtablewidgetitem9 = self.qualityAttributeTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"Unit", None));
        ___qtablewidgetitem10 = self.qualityAttributeTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"Value", None));
        self.ingStatementLabel.setText(QCoreApplication.translate("Dialog", u"Ingredient Statement", None))
        ___qtablewidgetitem11 = self.ingStatementTable.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"Ingredient Name", None));
        ___qtablewidgetitem12 = self.ingStatementTable.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"Specific Name", None));
        ___qtablewidgetitem13 = self.ingStatementTable.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"% by Weight", None));
        ___qtablewidgetitem14 = self.ingStatementTable.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"Sub-Ingredients", None));
        self.ingStatetmentTxtLabel.setText(QCoreApplication.translate("Dialog", u"Click generate below to autofill statement. Click edit to input manually or change auto-generated text", None))
        self.ingStatementTextBox.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ingredient statement", None))
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
        self.recipeWeighsCheckbox.setText(QCoreApplication.translate("Dialog", u"Serving weighs", None))
        self.displayNutritionalLabelBtn.setText(QCoreApplication.translate("Dialog", u"Display Nutrition Label", None))
        self.formulaEditorTabWidget.setTabText(self.formulaEditorTabWidget.indexOf(self.labelTab), QCoreApplication.translate("Dialog", u"Label", None))
        self.nutrientSpreadsheetLabel.setText(QCoreApplication.translate("Dialog", u"Nutrient Spreadsheet", None))
        ___qtablewidgetitem15 = self.nutrientReportTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Dialog", u"Item Desc", None));
        ___qtablewidgetitem16 = self.nutrientReportTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Dialog", u"Quantity", None));
        ___qtablewidgetitem17 = self.nutrientReportTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Dialog", u"Unit", None));
        ___qtablewidgetitem18 = self.nutrientReportTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Dialog", u"Weight (g)", None));
        ___qtablewidgetitem19 = self.nutrientReportTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Dialog", u"Cals (kCal)", None));
        ___qtablewidgetitem20 = self.nutrientReportTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Dialog", u"Protein (g)", None));
        ___qtablewidgetitem21 = self.nutrientReportTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Dialog", u"Total Carbohydrate (g)", None));
        ___qtablewidgetitem22 = self.nutrientReportTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Dialog", u"Dietary Fiber (g)", None));
        ___qtablewidgetitem23 = self.nutrientReportTableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Dialog", u"Soluble Fiber (g)", None));
        ___qtablewidgetitem24 = self.nutrientReportTableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Dialog", u"Total Sugar (g)", None));
        ___qtablewidgetitem25 = self.nutrientReportTableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Dialog", u"Added Sugar (g)", None));
        ___qtablewidgetitem26 = self.nutrientReportTableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Dialog", u"Monosac (g)", None));
        ___qtablewidgetitem27 = self.nutrientReportTableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Dialog", u"Disac (g)", None));
        ___qtablewidgetitem28 = self.nutrientReportTableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Dialog", u"Total Fat (g)", None));
        ___qtablewidgetitem29 = self.nutrientReportTableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Dialog", u"Sat Fat (g)", None));
        ___qtablewidgetitem30 = self.nutrientReportTableWidget.horizontalHeaderItem(15)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Dialog", u"Trans Fat (g)", None));
        ___qtablewidgetitem31 = self.nutrientReportTableWidget.horizontalHeaderItem(16)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Dialog", u"Mono Unsat Fat (g)", None));
        ___qtablewidgetitem32 = self.nutrientReportTableWidget.horizontalHeaderItem(17)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Dialog", u"Poly Unsat Fat (g)", None));
        ___qtablewidgetitem33 = self.nutrientReportTableWidget.horizontalHeaderItem(18)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Dialog", u"Unsat Fat (g)", None));
        ___qtablewidgetitem34 = self.nutrientReportTableWidget.horizontalHeaderItem(19)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Dialog", u"Omega-3 FA (g)", None));
        ___qtablewidgetitem35 = self.nutrientReportTableWidget.horizontalHeaderItem(20)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Dialog", u"Omega-6 FA (g)", None));
        ___qtablewidgetitem36 = self.nutrientReportTableWidget.horizontalHeaderItem(21)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Dialog", u"Cholestrol (mg)", None));
        ___qtablewidgetitem37 = self.nutrientReportTableWidget.horizontalHeaderItem(22)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Dialog", u"Water (g)", None));
        ___qtablewidgetitem38 = self.nutrientReportTableWidget.horizontalHeaderItem(23)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Dialog", u"Alcohol (g)", None));
        ___qtablewidgetitem39 = self.nutrientReportTableWidget.horizontalHeaderItem(24)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Dialog", u"Caffeine (mg)", None));
        ___qtablewidgetitem40 = self.nutrientReportTableWidget.horizontalHeaderItem(25)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("Dialog", u"Choline (mg)", None));
        ___qtablewidgetitem41 = self.nutrientReportTableWidget.horizontalHeaderItem(26)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("Dialog", u"Sugar Alcohol (g)", None));
        ___qtablewidgetitem42 = self.nutrientReportTableWidget.horizontalHeaderItem(27)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("Dialog", u"Calcium (mg)", None));
        ___qtablewidgetitem43 = self.nutrientReportTableWidget.horizontalHeaderItem(28)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("Dialog", u"Chromium (mcg)", None));
        ___qtablewidgetitem44 = self.nutrientReportTableWidget.horizontalHeaderItem(29)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("Dialog", u"Copper (mg)", None));
        ___qtablewidgetitem45 = self.nutrientReportTableWidget.horizontalHeaderItem(30)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("Dialog", u"Fluoride (mg)", None));
        ___qtablewidgetitem46 = self.nutrientReportTableWidget.horizontalHeaderItem(31)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("Dialog", u"Iodine (mcg)", None));
        ___qtablewidgetitem47 = self.nutrientReportTableWidget.horizontalHeaderItem(32)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("Dialog", u"Iron (mg)", None));
        ___qtablewidgetitem48 = self.nutrientReportTableWidget.horizontalHeaderItem(33)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("Dialog", u"Magnesium (mg)", None));
        ___qtablewidgetitem49 = self.nutrientReportTableWidget.horizontalHeaderItem(34)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("Dialog", u"Manganese (mg)", None));
        ___qtablewidgetitem50 = self.nutrientReportTableWidget.horizontalHeaderItem(35)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("Dialog", u"Molybdenum (mcg)", None));
        ___qtablewidgetitem51 = self.nutrientReportTableWidget.horizontalHeaderItem(36)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("Dialog", u"Phosphorus (mg)", None));
        ___qtablewidgetitem52 = self.nutrientReportTableWidget.horizontalHeaderItem(37)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("Dialog", u"Potassium (mg)", None));
        ___qtablewidgetitem53 = self.nutrientReportTableWidget.horizontalHeaderItem(38)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("Dialog", u"Selenium (mcg)", None));
        ___qtablewidgetitem54 = self.nutrientReportTableWidget.horizontalHeaderItem(39)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("Dialog", u"Sodium (mg)", None));
        ___qtablewidgetitem55 = self.nutrientReportTableWidget.horizontalHeaderItem(40)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("Dialog", u"Zinc (mg)", None));
        ___qtablewidgetitem56 = self.nutrientReportTableWidget.horizontalHeaderItem(41)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("Dialog", u"Vitamin A (IU)", None));
        ___qtablewidgetitem57 = self.nutrientReportTableWidget.horizontalHeaderItem(42)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("Dialog", u"Vitamin A - RE (mcg)", None));
        ___qtablewidgetitem58 = self.nutrientReportTableWidget.horizontalHeaderItem(43)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("Dialog", u"Vitamin A - RAE (mcg)", None));
        ___qtablewidgetitem59 = self.nutrientReportTableWidget.horizontalHeaderItem(44)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("Dialog", u"Vitamin B1/Thiamin (mg)", None));
        ___qtablewidgetitem60 = self.nutrientReportTableWidget.horizontalHeaderItem(45)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("Dialog", u"Vitamin B2/Riboflavin (mg)", None));
        ___qtablewidgetitem61 = self.nutrientReportTableWidget.horizontalHeaderItem(46)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("Dialog", u"Vitamin B3/Niacin (mg)", None));
        ___qtablewidgetitem62 = self.nutrientReportTableWidget.horizontalHeaderItem(47)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("Dialog", u"Vitamin B3/Niac. Eq (mg)", None));
        ___qtablewidgetitem63 = self.nutrientReportTableWidget.horizontalHeaderItem(48)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("Dialog", u"Vitamin B6 (mg)", None));
        ___qtablewidgetitem64 = self.nutrientReportTableWidget.horizontalHeaderItem(49)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("Dialog", u"Vitamin B12 (mcg)", None));
        ___qtablewidgetitem65 = self.nutrientReportTableWidget.horizontalHeaderItem(50)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("Dialog", u"Vitamin C (mg)", None));
        ___qtablewidgetitem66 = self.nutrientReportTableWidget.horizontalHeaderItem(51)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("Dialog", u"Vitamin D - IU (IU)", None));
        ___qtablewidgetitem67 = self.nutrientReportTableWidget.horizontalHeaderItem(52)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("Dialog", u"Vitamin E/Alpha-toco (mg)", None));
        ___qtablewidgetitem68 = self.nutrientReportTableWidget.horizontalHeaderItem(53)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("Dialog", u"Folate (mcg)", None));
        ___qtablewidgetitem69 = self.nutrientReportTableWidget.horizontalHeaderItem(54)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("Dialog", u"Folate, DFE (mcg DFE)", None));
        ___qtablewidgetitem70 = self.nutrientReportTableWidget.horizontalHeaderItem(55)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("Dialog", u"Vitamin K (mcg)", None));
        ___qtablewidgetitem71 = self.nutrientReportTableWidget.horizontalHeaderItem(56)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("Dialog", u"Panothenic Acid (mg)", None));
        self.singleNutrientLabel.setText(QCoreApplication.translate("Dialog", u"Single Nutrient ", None))
        self.dailyValueLabel.setText(QCoreApplication.translate("Dialog", u"Daily Value and Per 100g", None))
        self.byComparisonLabel.setText(QCoreApplication.translate("Dialog", u"Comparison", None))
        ___qtablewidgetitem72 = self.compareReportTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("Dialog", u"Nutrient", None));
        ___qtablewidgetitem73 = self.compareReportTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("Dialog", u"Current (per 100g)", None));
        ___qtablewidgetitem74 = self.compareReportTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("Dialog", u"Comparison (per 100g)", None));
        self.formulaEditorTabWidget.setTabText(self.formulaEditorTabWidget.indexOf(self.nutrientReportTab), QCoreApplication.translate("Dialog", u"Nutrient Report", None))
        ___qtablewidgetitem75 = self.imagesTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("Dialog", u"Context/Note", None));
        ___qtablewidgetitem76 = self.imagesTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("Dialog", u"Image", None));
        self.formulaEditorTabWidget.setTabText(self.formulaEditorTabWidget.indexOf(self.imagesTab), QCoreApplication.translate("Dialog", u"Images", None))
    # retranslateUi

