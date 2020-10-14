# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_ingredient.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
##
## TODO: ADD CALORIES 
################################################################################
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtCore import QSize, QObject, Qt
from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout, QGridLayout, QWidget, QTabWidget, QFormLayout, QFrame, QLabel, QCheckBox, QLineEdit, QSpinBox, QPushButton, QDialog, QCompleter

from helpers import connectDB

class addIngredientDialog(QDialog):

    def __init__(self):
        super(addIngredientDialog, self).__init__()
        self.setupUi(self)
        self.db = connectDB()


    def setupUi(self, addIngredientDialog):

        if not addIngredientDialog.objectName():
            addIngredientDialog.setObjectName(u"addIngredientDialog")

        addIngredientDialog.resize(1067, 1037)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addIngredientDialog.sizePolicy().hasHeightForWidth())
        addIngredientDialog.setSizePolicy(sizePolicy)
        addIngredientDialog.setWindowTitle(u"Add Ingredient")
        addIngredientDialog.setSizeGripEnabled(False)

        self.verticalLayout = QVBoxLayout(addIngredientDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.addIngredientTabWidget = QTabWidget(addIngredientDialog)
        self.addIngredientTabWidget.setObjectName(u"addIngredientTabWidget")

        ######## Top Frame of General Tab of Add Ingredient Widget ###########
        self.genInfoTab = QWidget()
        self.genInfoTab.setObjectName(u"genInfoTab")

        self.verticalLayout_4 = QVBoxLayout(self.genInfoTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.generalFrame1 = QFrame(self.genInfoTab)
        self.generalFrame1.setObjectName(u"generalFrame1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.generalFrame1.sizePolicy().hasHeightForWidth())
        self.generalFrame1.setSizePolicy(sizePolicy1)
        self.generalFrame1.setAutoFillBackground(True)
        self.generalFrame1.setFrameShape(QFrame.StyledPanel)
        self.generalFrame1.setFrameShadow(QFrame.Sunken)

        self.formLayout = QFormLayout(self.generalFrame1)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignCenter)

        self.ingredientNameLabel = QLabel(self.generalFrame1)
        self.ingredientNameLabel.setObjectName(u"ingredientNameLabel")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.ingredientNameLabel)

        self.ingredientNameLineEdit = QLineEdit(self.generalFrame1)
        self.ingredientNameLineEdit.setObjectName(u"ingredientNameLineEdit")
        self.ingredientNameLineEdit.setMinimumSize(QSize(300, 0))
        self.ingredientNameLineEdit.setPlaceholderText(u"ie. Pre-Hydrated\u00ae Ticalose\u00ae CMC 15 Powder")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ingredientNameLineEdit)

        self.commonNameLabel = QLabel(self.generalFrame1)
        self.commonNameLabel.setObjectName(u"commonNameLabel")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.commonNameLabel)

        self.commonNameLineEdit = QLineEdit(self.generalFrame1)
        self.commonNameLineEdit.setObjectName(u"commonNameLineEdit")
        self.commonNameLineEdit.setMinimumSize(QSize(300, 0))

        # adds suggestions/autocomplete to common name line input box 
        with connectDB().cursor() as cursor:
            cursor.execute("SELECT ing_common_name FROM ingredient")
            cNameRows = [row[0] for row in cursor.fetchall()]
            completer = QCompleter(cNameRows)
            completer.setCaseSensitivity(Qt.CaseInsensitive)
            completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
            completer.setMaxVisibleItems(10)
            self.commonNameLineEdit.setCompleter(completer)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.commonNameLineEdit)

        self.supplierLabel_2 = QLabel(self.generalFrame1)
        self.supplierLabel_2.setObjectName(u"supplierLabel_2")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.supplierLabel_2)

        self.supplierComboBox = QComboBox(self.generalFrame1)
        self.supplierComboBox.setObjectName(u"supplierComboBox")
        self.supplierComboBox.setMinimumSize(QSize(200, 0))
        self.supplierComboBox.setEditable(True)
        
        # adds all suppliers to supplier combobox 
        with connectDB().cursor() as cursor:
            cursor.execute("SELECT supplier_name FROM supplier")
            allSuppliers = cursor.fetchall()
            for supplierRow in allSuppliers:
                self.supplierComboBox.addItem(supplierRow[0])
    
        self.supplierComboBox.setCurrentText(u"")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.supplierComboBox)

        self.supplierIngIDLabel = QLabel(self.generalFrame1)
        self.supplierIngIDLabel.setObjectName(u"supplierIngIDLabel")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.supplierIngIDLabel)

        self.supplierIngredientNumberLineEdit = QLineEdit(self.generalFrame1)
        self.supplierIngredientNumberLineEdit.setObjectName(u"supplierIngredientNumberLineEdit")
        self.supplierIngredientNumberLineEdit.setMinimumSize(QSize(200, 0))
        self.supplierIngredientNumberLineEdit.setPlaceholderText(u"ie. CMC 15")
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.supplierIngredientNumberLineEdit)

        self.percentYieldIfApplicableLabel = QLabel(self.generalFrame1)
        self.percentYieldIfApplicableLabel.setObjectName(u"percentYieldIfApplicableLabel")
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.percentYieldIfApplicableLabel)

        self.percentYieldDoubleSpinBox = QDoubleSpinBox(self.generalFrame1)
        self.percentYieldDoubleSpinBox.setMaximum(100)
        self.percentYieldDoubleSpinBox.setMinimum(0)
        self.percentYieldDoubleSpinBox.setObjectName(u"percentYieldDoubleSpinBox")
        self.percentYieldDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.percentYieldDoubleSpinBox)

        self.supplierLabel = QLabel(self.generalFrame1)
        self.supplierLabel.setObjectName(u"supplierLabel")
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.supplierLabel)

        self.verticalLayout_4.addWidget(self.generalFrame1)

        ######## Bottom Frame of General Tab of Add Ingredient Widget ###########
        self.optionalLabel = QLabel(self.genInfoTab)
        self.optionalLabel.setObjectName(u"optionalLabel")
        self.verticalLayout_4.addWidget(self.optionalLabel)

        self.generalFrame2 = QFrame(self.genInfoTab)
        self.generalFrame2.setObjectName(u"generalFrame2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.generalFrame2.sizePolicy().hasHeightForWidth())
        self.generalFrame2.setSizePolicy(sizePolicy2)
        self.generalFrame2.setAutoFillBackground(True)
        self.generalFrame2.setFrameShape(QFrame.StyledPanel)
        self.generalFrame2.setFrameShadow(QFrame.Raised)

        self.gridLayout_3 = QGridLayout(self.generalFrame2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.allergenCheckBoxWidget = QWidget(self.generalFrame2)
        self.allergenCheckBoxWidget.setObjectName(u"allergenCheckBoxWidget")
        self.allergenCheckBoxWidget.setAutoFillBackground(True)

        self.formLayout_9 = QFormLayout(self.allergenCheckBoxWidget)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.allergenLabel = QLabel(self.allergenCheckBoxWidget)
        self.allergenLabel.setObjectName(u"allergenLabel")
        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.allergenLabel)

        self.dairyCheckbox = QCheckBox(self.allergenCheckBoxWidget)
        self.dairyCheckbox.setObjectName(u"dairyCheckbox")
        self.formLayout_9.setWidget(1, QFormLayout.LabelRole, self.dairyCheckbox)

        self.eggCheckbox = QCheckBox(self.allergenCheckBoxWidget)
        self.eggCheckbox.setObjectName(u"eggCheckbox")
        self.formLayout_9.setWidget(2, QFormLayout.LabelRole, self.eggCheckbox)

        self.fishCheckbox = QCheckBox(self.allergenCheckBoxWidget)
        self.fishCheckbox.setObjectName(u"fishCheckbox")
        self.formLayout_9.setWidget(3, QFormLayout.LabelRole, self.fishCheckbox)

        self.shellfishCheckbox = QCheckBox(self.allergenCheckBoxWidget)
        self.shellfishCheckbox.setObjectName(u"shellfishCheckbox")
        self.formLayout_9.setWidget(4, QFormLayout.LabelRole, self.shellfishCheckbox)

        self.treeNutsCheckbox = QCheckBox(self.allergenCheckBoxWidget)
        self.treeNutsCheckbox.setObjectName(u"treeNutsCheckbox")
        self.formLayout_9.setWidget(5, QFormLayout.LabelRole, self.treeNutsCheckbox)

        self.peanutsCheckbox = QCheckBox(self.allergenCheckBoxWidget)
        self.peanutsCheckbox.setObjectName(u"peanutsCheckbox")
        self.formLayout_9.setWidget(6, QFormLayout.LabelRole, self.peanutsCheckbox)

        self.wheatCheckbox = QCheckBox(self.allergenCheckBoxWidget)
        self.wheatCheckbox.setObjectName(u"wheatCheckbox")
        self.formLayout_9.setWidget(7, QFormLayout.LabelRole, self.wheatCheckbox)

        self.soyCheckbox = QCheckBox(self.allergenCheckBoxWidget)
        self.soyCheckbox.setObjectName(u"soyCheckbox")
        self.formLayout_9.setWidget(8, QFormLayout.LabelRole, self.soyCheckbox)

        self.gridLayout_3.addWidget(self.allergenCheckBoxWidget, 0, 0, 1, 1)

        self.claimsCheckBoxWidget = QWidget(self.generalFrame2)
        self.claimsCheckBoxWidget.setObjectName(u"claimsCheckBoxWidget")
        self.formLayout_10 = QFormLayout(self.claimsCheckBoxWidget)

        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.veganCheckbox = QCheckBox(self.claimsCheckBoxWidget)
        self.veganCheckbox.setObjectName(u"veganCheckbox")
        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.veganCheckbox)

        self.organicCheckbox = QCheckBox(self.claimsCheckBoxWidget)
        self.organicCheckbox.setObjectName(u"organicCheckbox")
        self.formLayout_10.setWidget(3, QFormLayout.LabelRole, self.organicCheckbox)

        self.ngmvCheckbox = QCheckBox(self.claimsCheckBoxWidget)
        self.ngmvCheckbox.setObjectName(u"ngmvCheckbox")
        self.formLayout_10.setWidget(4, QFormLayout.LabelRole, self.ngmvCheckbox)

        self.kosherCheckbox = QCheckBox(self.claimsCheckBoxWidget)
        self.kosherCheckbox.setObjectName(u"kosherCheckbox")
        self.formLayout_10.setWidget(5, QFormLayout.LabelRole, self.kosherCheckbox)

        self.ketoCheckbox = QCheckBox(self.claimsCheckBoxWidget)
        self.ketoCheckbox.setObjectName(u"ketoCheckbox")
        self.formLayout_10.setWidget(6, QFormLayout.LabelRole, self.ketoCheckbox)

        self.wholeFoodsCheckbox = QCheckBox(self.claimsCheckBoxWidget)
        self.wholeFoodsCheckbox.setObjectName(u"wholeFoodsCheckbox")
        self.formLayout_10.setWidget(7, QFormLayout.LabelRole, self.wholeFoodsCheckbox)

        self.nsaCheckbox = QCheckBox(self.claimsCheckBoxWidget)
        self.nsaCheckbox.setObjectName(u"nsaCheckbox")
        self.formLayout_10.setWidget(8, QFormLayout.LabelRole, self.nsaCheckbox)

        self.claimsLabel = QLabel(self.claimsCheckBoxWidget)
        self.claimsLabel.setObjectName(u"claimsLabel")
        self.formLayout_10.setWidget(0, QFormLayout.SpanningRole, self.claimsLabel)

        self.halalCheckbox = QCheckBox(self.claimsCheckBoxWidget)
        self.halalCheckbox.setObjectName(u"halalCheckbox")
        self.formLayout_10.setWidget(2, QFormLayout.LabelRole, self.halalCheckbox)

        self.gridLayout_3.addWidget(self.claimsCheckBoxWidget, 0, 1, 1, 1)

        self.notesLabel = QLabel(self.generalFrame2)
        self.notesLabel.setObjectName(u"notesLabel")
        self.gridLayout_3.addWidget(self.notesLabel, 2, 0, 1, 1)

        self.notesLineEdit = QLineEdit(self.generalFrame2)
        self.notesLineEdit.setObjectName(u"notesLineEdit")
        self.notesLineEdit.setMinimumSize(QSize(100, 100))

        self.gridLayout_3.addWidget(self.notesLineEdit, 2, 1, 1, 1)

        self.ingredientStatementLineEdit = QLineEdit(self.generalFrame2)
        self.ingredientStatementLineEdit.setObjectName(u"ingredientStatementLineEdit")
        self.ingredientStatementLineEdit.setMinimumSize(QSize(0, 100))

        self.gridLayout_3.addWidget(self.ingredientStatementLineEdit, 1, 1, 1, 1)

        self.ingredientStatementLabel = QLabel(self.generalFrame2)
        self.ingredientStatementLabel.setObjectName(u"ingredientStatementLabel")

        self.gridLayout_3.addWidget(self.ingredientStatementLabel, 1, 0, 1, 1)

        self.verticalLayout_4.addWidget(self.generalFrame2)

        self.widget = QWidget(self.genInfoTab)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4.addWidget(self.widget)

        self.addIngredientTabWidget.addTab(self.genInfoTab, "")
        self.addIngredientTabWidget.setTabText(self.addIngredientTabWidget.indexOf(self.genInfoTab), u"General")
        

        ######## Nutritionals Tab of Add Ingredient Widget ###########
        # Top Widget 
        self.nutritionalsTab = QWidget()
        self.nutritionalsTab.setObjectName(u"nutritionalsTab")

        self.verticalLayout_3 = QVBoxLayout(self.nutritionalsTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.widget_2 = QWidget(self.nutritionalsTab)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setAutoFillBackground(True)

        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.perLabel = QLabel(self.widget_2)
        self.perLabel.setObjectName(u"perLabel")
        self.perLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.perLabel)

        self.perGramsSpinBox = QSpinBox(self.widget_2)
        self.perGramsSpinBox.setObjectName(u"perGramsSpinBox")

        self.perGramsSpinBox.setAlignment(Qt.AlignCenter)
        self.perGramsSpinBox.setMaximum(1000)
        self.perGramsSpinBox.setSingleStep(10)
        self.perGramsSpinBox.setValue(100)

        self.horizontalLayout.addWidget(self.perGramsSpinBox)

        self.gramsLabel = QLabel(self.widget_2)
        self.gramsLabel.setObjectName(u"gramsLabel")

        self.horizontalLayout.addWidget(self.gramsLabel)

        self.checkDataBtn = QPushButton(self.widget_2)
        self.checkDataBtn.setObjectName(u"checkDataBtn")

        self.horizontalLayout.addWidget(self.checkDataBtn)

        self.generateNFPPushBtn = QPushButton(self.widget_2)
        self.generateNFPPushBtn.setObjectName(u"generateNFPPushBtn")

        self.horizontalLayout.addWidget(self.generateNFPPushBtn)

        self.verticalLayout_3.addWidget(self.widget_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        # Vitamins Frame
        self.vitaminsFrame = QFrame(self.nutritionalsTab)
        self.vitaminsFrame.setObjectName(u"vitaminsFrame")
        self.vitaminsFrame.setAutoFillBackground(True)
        self.vitaminsFrame.setInputMethodHints(Qt.ImhDigitsOnly)
        self.vitaminsFrame.setFrameShape(QFrame.StyledPanel)
        self.formLayout_7 = QFormLayout(self.vitaminsFrame)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.vitaminAIUIULabel = QLabel(self.vitaminsFrame)
        self.vitaminAIUIULabel.setObjectName(u"vitaminAIUIULabel")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.vitaminAIUIULabel)

        self.vitaminAIUIULineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminAIUIULineEdit.setObjectName(u"vitaminAIUIULineEdit")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.vitaminAIUIULineEdit)

        self.vitaminAREMcgLabel = QLabel(self.vitaminsFrame)
        self.vitaminAREMcgLabel.setObjectName(u"vitaminAREMcgLabel")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.vitaminAREMcgLabel)

        self.vitaminAREMcgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminAREMcgLineEdit.setObjectName(u"vitaminAREMcgLineEdit")

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.vitaminAREMcgLineEdit)

        self.vitaminARAEMcgLabel = QLabel(self.vitaminsFrame)
        self.vitaminARAEMcgLabel.setObjectName(u"vitaminARAEMcgLabel")

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.vitaminARAEMcgLabel)

        self.vitaminARAEMcgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminARAEMcgLineEdit.setObjectName(u"vitaminARAEMcgLineEdit")

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.vitaminARAEMcgLineEdit)

        self.vitaminB1ThiaminMgLabel = QLabel(self.vitaminsFrame)
        self.vitaminB1ThiaminMgLabel.setObjectName(u"vitaminB1ThiaminMgLabel")

        self.formLayout_7.setWidget(4, QFormLayout.LabelRole, self.vitaminB1ThiaminMgLabel)

        self.vitaminB1ThiaminMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB1ThiaminMgLineEdit.setObjectName(u"vitaminB1ThiaminMgLineEdit")

        self.formLayout_7.setWidget(4, QFormLayout.FieldRole, self.vitaminB1ThiaminMgLineEdit)

        self.vitaminB2RiboflavinMgLabel = QLabel(self.vitaminsFrame)
        self.vitaminB2RiboflavinMgLabel.setObjectName(u"vitaminB2RiboflavinMgLabel")

        self.formLayout_7.setWidget(5, QFormLayout.LabelRole, self.vitaminB2RiboflavinMgLabel)

        self.vitaminB2RiboflavinMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB2RiboflavinMgLineEdit.setObjectName(u"vitaminB2RiboflavinMgLineEdit")

        self.formLayout_7.setWidget(5, QFormLayout.FieldRole, self.vitaminB2RiboflavinMgLineEdit)

        self.vitaminB3NiacinMgLabel = QLabel(self.vitaminsFrame)
        self.vitaminB3NiacinMgLabel.setObjectName(u"vitaminB3NiacinMgLabel")

        self.formLayout_7.setWidget(6, QFormLayout.LabelRole, self.vitaminB3NiacinMgLabel)

        self.vitaminB3NiacinMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB3NiacinMgLineEdit.setObjectName(u"vitaminB3NiacinMgLineEdit")

        self.formLayout_7.setWidget(6, QFormLayout.FieldRole, self.vitaminB3NiacinMgLineEdit)

        self.vitaminB3NiacinEquivMgLabel = QLabel(self.vitaminsFrame)
        self.vitaminB3NiacinEquivMgLabel.setObjectName(u"vitaminB3NiacinEquivMgLabel")

        self.formLayout_7.setWidget(7, QFormLayout.LabelRole, self.vitaminB3NiacinEquivMgLabel)

        self.vitaminB3NiacinEquivMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB3NiacinEquivMgLineEdit.setObjectName(u"vitaminB3NiacinEquivMgLineEdit")

        self.formLayout_7.setWidget(7, QFormLayout.FieldRole, self.vitaminB3NiacinEquivMgLineEdit)

        self.vitaminB6MgLabel = QLabel(self.vitaminsFrame)
        self.vitaminB6MgLabel.setObjectName(u"vitaminB6MgLabel")

        self.formLayout_7.setWidget(8, QFormLayout.LabelRole, self.vitaminB6MgLabel)

        self.vitaminB6MgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB6MgLineEdit.setObjectName(u"vitaminB6MgLineEdit")

        self.formLayout_7.setWidget(8, QFormLayout.FieldRole, self.vitaminB6MgLineEdit)

        self.vitaminB12McgLabel = QLabel(self.vitaminsFrame)
        self.vitaminB12McgLabel.setObjectName(u"vitaminB12McgLabel")

        self.formLayout_7.setWidget(9, QFormLayout.LabelRole, self.vitaminB12McgLabel)

        self.vitaminB12McgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB12McgLineEdit.setObjectName(u"vitaminB12McgLineEdit")

        self.formLayout_7.setWidget(9, QFormLayout.FieldRole, self.vitaminB12McgLineEdit)

        self.vitaminCMgLabel = QLabel(self.vitaminsFrame)
        self.vitaminCMgLabel.setObjectName(u"vitaminCMgLabel")

        self.formLayout_7.setWidget(10, QFormLayout.LabelRole, self.vitaminCMgLabel)

        self.vitaminCMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminCMgLineEdit.setObjectName(u"vitaminCMgLineEdit")

        self.formLayout_7.setWidget(10, QFormLayout.FieldRole, self.vitaminCMgLineEdit)

        self.vitaminDIUIULabel = QLabel(self.vitaminsFrame)
        self.vitaminDIUIULabel.setObjectName(u"vitaminDIUIULabel")

        self.formLayout_7.setWidget(11, QFormLayout.LabelRole, self.vitaminDIUIULabel)

        self.vitaminDIUIULineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminDIUIULineEdit.setObjectName(u"vitaminDIUIULineEdit")

        self.formLayout_7.setWidget(11, QFormLayout.FieldRole, self.vitaminDIUIULineEdit)

        self.vitaminEAlphaTocoMgLabel = QLabel(self.vitaminsFrame)
        self.vitaminEAlphaTocoMgLabel.setObjectName(u"vitaminEAlphaTocoMgLabel")

        self.formLayout_7.setWidget(12, QFormLayout.LabelRole, self.vitaminEAlphaTocoMgLabel)

        self.vitaminEAlphaTocoMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminEAlphaTocoMgLineEdit.setObjectName(u"vitaminEAlphaTocoMgLineEdit")

        self.formLayout_7.setWidget(12, QFormLayout.FieldRole, self.vitaminEAlphaTocoMgLineEdit)

        self.folateMcgLabel = QLabel(self.vitaminsFrame)
        self.folateMcgLabel.setObjectName(u"folateMcgLabel")

        self.formLayout_7.setWidget(13, QFormLayout.LabelRole, self.folateMcgLabel)

        self.folateMcgLineEdit = QLineEdit(self.vitaminsFrame)
        self.folateMcgLineEdit.setObjectName(u"folateMcgLineEdit")

        self.formLayout_7.setWidget(13, QFormLayout.FieldRole, self.folateMcgLineEdit)

        self.folateDFEMcgDFELabel = QLabel(self.vitaminsFrame)
        self.folateDFEMcgDFELabel.setObjectName(u"folateDFEMcgDFELabel")

        self.formLayout_7.setWidget(14, QFormLayout.LabelRole, self.folateDFEMcgDFELabel)

        self.folateDFEMcgDFELineEdit = QLineEdit(self.vitaminsFrame)
        self.folateDFEMcgDFELineEdit.setObjectName(u"folateDFEMcgDFELineEdit")

        self.formLayout_7.setWidget(14, QFormLayout.FieldRole, self.folateDFEMcgDFELineEdit)

        self.vitaminKMcgLabel = QLabel(self.vitaminsFrame)
        self.vitaminKMcgLabel.setObjectName(u"vitaminKMcgLabel")

        self.formLayout_7.setWidget(15, QFormLayout.LabelRole, self.vitaminKMcgLabel)

        self.vitaminKMcgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminKMcgLineEdit.setObjectName(u"vitaminKMcgLineEdit")

        self.formLayout_7.setWidget(15, QFormLayout.FieldRole, self.vitaminKMcgLineEdit)

        self.panothenicAcidMgLabel = QLabel(self.vitaminsFrame)
        self.panothenicAcidMgLabel.setObjectName(u"panothenicAcidMgLabel")

        self.formLayout_7.setWidget(16, QFormLayout.LabelRole, self.panothenicAcidMgLabel)

        self.panothenicAcidMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.panothenicAcidMgLineEdit.setObjectName(u"panothenicAcidMgLineEdit")

        self.formLayout_7.setWidget(16, QFormLayout.FieldRole, self.panothenicAcidMgLineEdit)

        self.label_5 = QLabel(self.vitaminsFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.formLayout_7.setWidget(0, QFormLayout.SpanningRole, self.label_5)

        self.gridLayout_2.addWidget(self.vitaminsFrame, 1, 2, 1, 1)

        
        # Fats Frame 
        self.fatsFrame = QFrame(self.nutritionalsTab)
        self.fatsFrame.setObjectName(u"fatsFrame")
        self.fatsFrame.setAutoFillBackground(True)
        self.fatsFrame.setFrameShape(QFrame.StyledPanel)
        self.formLayout_6 = QFormLayout(self.fatsFrame)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.totalFatGLabel = QLabel(self.fatsFrame)
        self.totalFatGLabel.setObjectName(u"totalFatGLabel")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.totalFatGLabel)

        self.totalFatGLineEdit = QLineEdit(self.fatsFrame)
        self.totalFatGLineEdit.setObjectName(u"totalFatGLineEdit")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.totalFatGLineEdit)

        self.saturatedFatGLabel = QLabel(self.fatsFrame)
        self.saturatedFatGLabel.setObjectName(u"saturatedFatGLabel")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.saturatedFatGLabel)

        self.saturatedFatGLineEdit = QLineEdit(self.fatsFrame)
        self.saturatedFatGLineEdit.setObjectName(u"saturatedFatGLineEdit")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.saturatedFatGLineEdit)

        self.totalUnsaturatedFatGLabel = QLabel(self.fatsFrame)
        self.totalUnsaturatedFatGLabel.setObjectName(u"totalUnsaturatedFatGLabel")

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.totalUnsaturatedFatGLabel)

        self.totalUnsaturatedFatGLineEdit = QLineEdit(self.fatsFrame)
        self.totalUnsaturatedFatGLineEdit.setObjectName(u"totalUnsaturatedFatGLineEdit")

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.totalUnsaturatedFatGLineEdit)

        self.monounsaturatedFatGLabel = QLabel(self.fatsFrame)
        self.monounsaturatedFatGLabel.setObjectName(u"monounsaturatedFatGLabel")

        self.formLayout_6.setWidget(4, QFormLayout.LabelRole, self.monounsaturatedFatGLabel)

        self.monounsaturatedFatGLineEdit = QLineEdit(self.fatsFrame)
        self.monounsaturatedFatGLineEdit.setObjectName(u"monounsaturatedFatGLineEdit")

        self.formLayout_6.setWidget(4, QFormLayout.FieldRole, self.monounsaturatedFatGLineEdit)

        self.polyunsaturatedFatGLabel = QLabel(self.fatsFrame)
        self.polyunsaturatedFatGLabel.setObjectName(u"polyunsaturatedFatGLabel")

        self.formLayout_6.setWidget(5, QFormLayout.LabelRole, self.polyunsaturatedFatGLabel)

        self.polyunsaturatedFatGLineEdit = QLineEdit(self.fatsFrame)
        self.polyunsaturatedFatGLineEdit.setObjectName(u"polyunsaturatedFatGLineEdit")

        self.formLayout_6.setWidget(5, QFormLayout.FieldRole, self.polyunsaturatedFatGLineEdit)

        self.transFatGLabel = QLabel(self.fatsFrame)
        self.transFatGLabel.setObjectName(u"transFatGLabel")

        self.formLayout_6.setWidget(6, QFormLayout.LabelRole, self.transFatGLabel)

        self.transFatGLineEdit = QLineEdit(self.fatsFrame)
        self.transFatGLineEdit.setObjectName(u"transFatGLineEdit")

        self.formLayout_6.setWidget(6, QFormLayout.FieldRole, self.transFatGLineEdit)

        self.cholestrolMgLabel = QLabel(self.fatsFrame)
        self.cholestrolMgLabel.setObjectName(u"cholestrolMgLabel")

        self.formLayout_6.setWidget(7, QFormLayout.LabelRole, self.cholestrolMgLabel)

        self.cholestrolMgLineEdit = QLineEdit(self.fatsFrame)
        self.cholestrolMgLineEdit.setObjectName(u"cholestrolMgLineEdit")

        self.formLayout_6.setWidget(7, QFormLayout.FieldRole, self.cholestrolMgLineEdit)

        self.omega3FattyAcidGLabel = QLabel(self.fatsFrame)
        self.omega3FattyAcidGLabel.setObjectName(u"omega3FattyAcidGLabel")

        self.formLayout_6.setWidget(8, QFormLayout.LabelRole, self.omega3FattyAcidGLabel)

        self.omega3FattyAcidGLineEdit = QLineEdit(self.fatsFrame)
        self.omega3FattyAcidGLineEdit.setObjectName(u"omega3FattyAcidGLineEdit")

        self.formLayout_6.setWidget(8, QFormLayout.FieldRole, self.omega3FattyAcidGLineEdit)

        self.omega6FattyAcidGLabel = QLabel(self.fatsFrame)
        self.omega6FattyAcidGLabel.setObjectName(u"omega6FattyAcidGLabel")

        self.formLayout_6.setWidget(9, QFormLayout.LabelRole, self.omega6FattyAcidGLabel)

        self.omega6FattyAcidGLineEdit = QLineEdit(self.fatsFrame)
        self.omega6FattyAcidGLineEdit.setObjectName(u"omega6FattyAcidGLineEdit")

        self.formLayout_6.setWidget(9, QFormLayout.FieldRole, self.omega6FattyAcidGLineEdit)

        self.label_4 = QLabel(self.fatsFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout_6.setWidget(0, QFormLayout.SpanningRole, self.label_4)


        self.gridLayout_2.addWidget(self.fatsFrame, 0, 1, 1, 1)

        self.formFrame_4 = QFrame(self.nutritionalsTab)
        self.formFrame_4.setObjectName(u"formFrame_4")
        self.formFrame_4.setAutoFillBackground(True)
        self.formFrame_4.setFrameShape(QFrame.StyledPanel)
        self.formLayout_8 = QFormLayout(self.formFrame_4)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.calciumMgLabel = QLabel(self.formFrame_4)
        self.calciumMgLabel.setObjectName(u"calciumMgLabel")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.calciumMgLabel)

        self.calciumMgLineEdit = QLineEdit(self.formFrame_4)
        self.calciumMgLineEdit.setObjectName(u"calciumMgLineEdit")

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.calciumMgLineEdit)

        self.chromiumMcgLabel = QLabel(self.formFrame_4)
        self.chromiumMcgLabel.setObjectName(u"chromiumMcgLabel")

        self.formLayout_8.setWidget(2, QFormLayout.LabelRole, self.chromiumMcgLabel)

        self.chromiumMcgLineEdit = QLineEdit(self.formFrame_4)
        self.chromiumMcgLineEdit.setObjectName(u"chromiumMcgLineEdit")

        self.formLayout_8.setWidget(2, QFormLayout.FieldRole, self.chromiumMcgLineEdit)

        self.copperMgLabel = QLabel(self.formFrame_4)
        self.copperMgLabel.setObjectName(u"copperMgLabel")

        self.formLayout_8.setWidget(3, QFormLayout.LabelRole, self.copperMgLabel)

        self.copperMgLineEdit = QLineEdit(self.formFrame_4)
        self.copperMgLineEdit.setObjectName(u"copperMgLineEdit")

        self.formLayout_8.setWidget(3, QFormLayout.FieldRole, self.copperMgLineEdit)

        self.fluorideMgLabel = QLabel(self.formFrame_4)
        self.fluorideMgLabel.setObjectName(u"fluorideMgLabel")

        self.formLayout_8.setWidget(4, QFormLayout.LabelRole, self.fluorideMgLabel)

        self.fluorideMgLineEdit = QLineEdit(self.formFrame_4)
        self.fluorideMgLineEdit.setObjectName(u"fluorideMgLineEdit")

        self.formLayout_8.setWidget(4, QFormLayout.FieldRole, self.fluorideMgLineEdit)

        self.iodineMcgLabel = QLabel(self.formFrame_4)
        self.iodineMcgLabel.setObjectName(u"iodineMcgLabel")

        self.formLayout_8.setWidget(5, QFormLayout.LabelRole, self.iodineMcgLabel)

        self.iodineMcgLineEdit = QLineEdit(self.formFrame_4)
        self.iodineMcgLineEdit.setObjectName(u"iodineMcgLineEdit")

        self.formLayout_8.setWidget(5, QFormLayout.FieldRole, self.iodineMcgLineEdit)

        self.ironMgLabel = QLabel(self.formFrame_4)
        self.ironMgLabel.setObjectName(u"ironMgLabel")

        self.formLayout_8.setWidget(6, QFormLayout.LabelRole, self.ironMgLabel)

        self.ironMgLineEdit = QLineEdit(self.formFrame_4)
        self.ironMgLineEdit.setObjectName(u"ironMgLineEdit")

        self.formLayout_8.setWidget(6, QFormLayout.FieldRole, self.ironMgLineEdit)

        self.magnesiumMgLabel = QLabel(self.formFrame_4)
        self.magnesiumMgLabel.setObjectName(u"magnesiumMgLabel")

        self.formLayout_8.setWidget(7, QFormLayout.LabelRole, self.magnesiumMgLabel)

        self.magnesiumMgLineEdit = QLineEdit(self.formFrame_4)
        self.magnesiumMgLineEdit.setObjectName(u"magnesiumMgLineEdit")

        self.formLayout_8.setWidget(7, QFormLayout.FieldRole, self.magnesiumMgLineEdit)

        self.manganeseMgLabel = QLabel(self.formFrame_4)
        self.manganeseMgLabel.setObjectName(u"manganeseMgLabel")

        self.formLayout_8.setWidget(8, QFormLayout.LabelRole, self.manganeseMgLabel)

        self.manganeseMgLineEdit = QLineEdit(self.formFrame_4)
        self.manganeseMgLineEdit.setObjectName(u"manganeseMgLineEdit")

        self.formLayout_8.setWidget(8, QFormLayout.FieldRole, self.manganeseMgLineEdit)

        self.molybdenumMcgLabel = QLabel(self.formFrame_4)
        self.molybdenumMcgLabel.setObjectName(u"molybdenumMcgLabel")

        self.formLayout_8.setWidget(9, QFormLayout.LabelRole, self.molybdenumMcgLabel)

        self.molybdenumMcgLineEdit = QLineEdit(self.formFrame_4)
        self.molybdenumMcgLineEdit.setObjectName(u"molybdenumMcgLineEdit")

        self.formLayout_8.setWidget(9, QFormLayout.FieldRole, self.molybdenumMcgLineEdit)

        self.phosphorusMgLabel = QLabel(self.formFrame_4)
        self.phosphorusMgLabel.setObjectName(u"phosphorusMgLabel")

        self.formLayout_8.setWidget(10, QFormLayout.LabelRole, self.phosphorusMgLabel)

        self.phosphorusMgLineEdit = QLineEdit(self.formFrame_4)
        self.phosphorusMgLineEdit.setObjectName(u"phosphorusMgLineEdit")

        self.formLayout_8.setWidget(10, QFormLayout.FieldRole, self.phosphorusMgLineEdit)

        self.potassiumMgLabel = QLabel(self.formFrame_4)
        self.potassiumMgLabel.setObjectName(u"potassiumMgLabel")

        self.formLayout_8.setWidget(11, QFormLayout.LabelRole, self.potassiumMgLabel)

        self.potassiumMgLineEdit = QLineEdit(self.formFrame_4)
        self.potassiumMgLineEdit.setObjectName(u"potassiumMgLineEdit")
        self.formLayout_8.setWidget(11, QFormLayout.FieldRole, self.potassiumMgLineEdit)

        self.seleniumMcgLabel = QLabel(self.formFrame_4)
        self.seleniumMcgLabel.setObjectName(u"seleniumMcgLabel")

        self.formLayout_8.setWidget(12, QFormLayout.LabelRole, self.seleniumMcgLabel)

        self.seleniumMcgLineEdit = QLineEdit(self.formFrame_4)
        self.seleniumMcgLineEdit.setObjectName(u"seleniumMcgLineEdit")

        self.formLayout_8.setWidget(12, QFormLayout.FieldRole, self.seleniumMcgLineEdit)

        self.sodiumMgLabel = QLabel(self.formFrame_4)
        self.sodiumMgLabel.setObjectName(u"sodiumMgLabel")

        self.formLayout_8.setWidget(13, QFormLayout.LabelRole, self.sodiumMgLabel)

        self.sodiumMgLineEdit = QLineEdit(self.formFrame_4)
        self.sodiumMgLineEdit.setObjectName(u"sodiumMgLineEdit")

        self.formLayout_8.setWidget(13, QFormLayout.FieldRole, self.sodiumMgLineEdit)

        self.zincMgLabel = QLabel(self.formFrame_4)
        self.zincMgLabel.setObjectName(u"zincMgLabel")

        self.formLayout_8.setWidget(14, QFormLayout.LabelRole, self.zincMgLabel)

        self.zincMgLineEdit = QLineEdit(self.formFrame_4)
        self.zincMgLineEdit.setObjectName(u"zincMgLineEdit")

        self.formLayout_8.setWidget(14, QFormLayout.FieldRole, self.zincMgLineEdit)

        self.mineralsFrame = QLabel(self.formFrame_4)
        self.mineralsFrame.setObjectName(u"mineralsFrame")
        self.mineralsFrame.setAlignment(Qt.AlignCenter)

        self.formLayout_8.setWidget(0, QFormLayout.SpanningRole, self.mineralsFrame)


        self.gridLayout_2.addWidget(self.formFrame_4, 1, 1, 1, 1)

        # Carbs Frame
        self.carbsFrame = QFrame(self.nutritionalsTab)
        self.carbsFrame.setObjectName(u"carbsFrame")
        self.carbsFrame.setAutoFillBackground(True)
        self.carbsFrame.setFrameShape(QFrame.StyledPanel)
        self.formLayout_4 = QFormLayout(self.carbsFrame)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.totalCarbohydratesGLabel = QLabel(self.carbsFrame)
        self.totalCarbohydratesGLabel.setObjectName(u"totalCarbohydratesGLabel")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.totalCarbohydratesGLabel)

        self.totalCarbohydratesGLineEdit = QLineEdit(self.carbsFrame)
        self.totalCarbohydratesGLineEdit.setObjectName(u"totalCarbohydratesGLineEdit")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.totalCarbohydratesGLineEdit)

        self.totalSugarsGramLabel = QLabel(self.carbsFrame)
        self.totalSugarsGramLabel.setObjectName(u"totalSugarsGramLabel")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.totalSugarsGramLabel)

        self.totalSugarsGLineEdit = QLineEdit(self.carbsFrame)
        self.totalSugarsGLineEdit.setObjectName(u"totalSugarsGLineEdit")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.totalSugarsGLineEdit)

        self.addedSugarsGramLabel = QLabel(self.carbsFrame)
        self.addedSugarsGramLabel.setObjectName(u"addedSugarsGramLabel")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.addedSugarsGramLabel)

        self.addedSugarsGLineEdit = QLineEdit(self.carbsFrame)
        self.addedSugarsGLineEdit.setObjectName(u"addedSugarsGLineEdit")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.addedSugarsGLineEdit)

        self.totalDietaryFiberGLabel = QLabel(self.carbsFrame)
        self.totalDietaryFiberGLabel.setObjectName(u"totalDietaryFiberGLabel")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.totalDietaryFiberGLabel)

        self.totalDietaryFiberGLineEdit = QLineEdit(self.carbsFrame)
        self.totalDietaryFiberGLineEdit.setObjectName(u"totalDietaryFiberGLineEdit")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.totalDietaryFiberGLineEdit)

        self.totalSolubleFiberGLabel = QLabel(self.carbsFrame)
        self.totalSolubleFiberGLabel.setObjectName(u"totalSolubleFiberGLabel")

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.totalSolubleFiberGLabel)

        self.totalSolubleFiberGLineEdit = QLineEdit(self.carbsFrame)
        self.totalSolubleFiberGLineEdit.setObjectName(u"totalSolubleFiberGLineEdit")

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.totalSolubleFiberGLineEdit)

        self.monosaccharidesGLabel = QLabel(self.carbsFrame)
        self.monosaccharidesGLabel.setObjectName(u"monosaccharidesGLabel")

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.monosaccharidesGLabel)

        self.monosaccharidesGLineEdit = QLineEdit(self.carbsFrame)
        self.monosaccharidesGLineEdit.setObjectName(u"monosaccharidesGLineEdit")

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.monosaccharidesGLineEdit)

        self.disaccharidesGLabel = QLabel(self.carbsFrame)
        self.disaccharidesGLabel.setObjectName(u"disaccharidesGLabel")

        self.formLayout_4.setWidget(7, QFormLayout.LabelRole, self.disaccharidesGLabel)

        self.disaccharidesGLineEdit = QLineEdit(self.carbsFrame)
        self.disaccharidesGLineEdit.setObjectName(u"disaccharidesGLineEdit")

        self.formLayout_4.setWidget(7, QFormLayout.FieldRole, self.disaccharidesGLineEdit)

        self.otherCarbohydratesGLabel = QLabel(self.carbsFrame)
        self.otherCarbohydratesGLabel.setObjectName(u"otherCarbohydratesGLabel")

        self.formLayout_4.setWidget(8, QFormLayout.LabelRole, self.otherCarbohydratesGLabel)

        self.otherCarbohydratesGLineEdit = QLineEdit(self.carbsFrame)
        self.otherCarbohydratesGLineEdit.setObjectName(u"otherCarbohydratesGLineEdit")

        self.formLayout_4.setWidget(8, QFormLayout.FieldRole, self.otherCarbohydratesGLineEdit)

        self.carbsLabel = QLabel(self.carbsFrame)
        self.carbsLabel.setObjectName(u"carbsLabel")
        self.carbsLabel.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(0, QFormLayout.SpanningRole, self.carbsLabel)

        self.gridLayout_2.addWidget(self.carbsFrame, 0, 0, 1, 1)

        # Proteins Frame
        self.proteinsFrame = QFrame(self.nutritionalsTab)
        self.proteinsFrame.setObjectName(u"proteinsFrame")
        self.proteinsFrame.setAutoFillBackground(True)
        self.proteinsFrame.setFrameShape(QFrame.StyledPanel)
        self.formLayout_2 = QFormLayout(self.proteinsFrame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.proteinsFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.label_2)

        self.totalProteinGLabel = QLabel(self.proteinsFrame)
        self.totalProteinGLabel.setObjectName(u"totalProteinGLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.totalProteinGLabel)

        self.totalProteinGLineEdit = QLineEdit(self.proteinsFrame)
        self.totalProteinGLineEdit.setObjectName(u"totalProteinGLineEdit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.totalProteinGLineEdit)

        self.gridLayout_2.addWidget(self.proteinsFrame, 0, 2, 1, 1)

        # Other Nutrients Frame
        self.otherNutrientsFrame = QFrame(self.nutritionalsTab)
        self.otherNutrientsFrame.setObjectName(u"otherNutrientsFrame")
        self.otherNutrientsFrame.setAutoFillBackground(True)
        self.otherNutrientsFrame.setFrameShape(QFrame.StyledPanel)
        self.formLayout_5 = QFormLayout(self.otherNutrientsFrame)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_6 = QLabel(self.otherNutrientsFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(0, QFormLayout.SpanningRole, self.label_6)

        self.moistureGLabel = QLabel(self.otherNutrientsFrame)
        self.moistureGLabel.setObjectName(u"moistureGLabel")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.moistureGLabel)

        self.moistureGLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.moistureGLineEdit.setObjectName(u"moistureGLineEdit")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.moistureGLineEdit)

        self.caffeineMgLabel = QLabel(self.otherNutrientsFrame)
        self.caffeineMgLabel.setObjectName(u"caffeineMgLabel")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.caffeineMgLabel)

        self.caffeineMgLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.caffeineMgLineEdit.setObjectName(u"caffeineMgLineEdit")
        #self.caffeineMgLineEdit.setInputMask()

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.caffeineMgLineEdit)

        self.cholineMgLabel = QLabel(self.otherNutrientsFrame)
        self.cholineMgLabel.setObjectName(u"cholineMgLabel")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.cholineMgLabel)

        self.cholineMgLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.cholineMgLineEdit.setObjectName(u"cholineMgLineEdit")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.cholineMgLineEdit)

        self.alcoholGLabel = QLabel(self.otherNutrientsFrame)
        self.alcoholGLabel.setObjectName(u"alcoholGLabel")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.alcoholGLabel)

        self.alcoholGLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.alcoholGLineEdit.setObjectName(u"alcoholGLineEdit")

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.alcoholGLineEdit)

        self.sugarAlcoholGLabel = QLabel(self.otherNutrientsFrame)
        self.sugarAlcoholGLabel.setObjectName(u"sugarAlcoholGLabel")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.sugarAlcoholGLabel)

        self.sugarAlcoholGLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.sugarAlcoholGLineEdit.setObjectName(u"sugarAlcoholGLineEdit")

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.sugarAlcoholGLineEdit)

        self.gridLayout_2.addWidget(self.otherNutrientsFrame, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.addIngredientTabWidget.addTab(self.nutritionalsTab, "")


        ######## Documentation Tab of Add Ingredient Widget ###########
        self.documentationTab = QWidget()
        self.documentationTab.setObjectName(u"documentationTab")
        self.verticalLayout_7 = QVBoxLayout(self.documentationTab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.documentationTabWidget = QWidget(self.documentationTab)
        self.documentationTabWidget.setObjectName(u"documentationTabWidget")

        self.verticalLayout_7.addWidget(self.documentationTabWidget)

        self.addIngredientTabWidget.addTab(self.documentationTab, "")

        ######## Groups Tab of Add Ingredient Widget ###########
        self.groupsTab = QWidget()
        self.groupsTab.setObjectName(u"groupsTab")
        self.verticalLayout_6 = QVBoxLayout(self.groupsTab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupListWidget = QListWidget(self.groupsTab)
        self.groupListWidget.setObjectName(u"groupListWidget")

        self.verticalLayout_6.addWidget(self.groupListWidget)

        self.addIngredientTabWidget.addTab(self.groupsTab, "")

        ######## Cost Tab of Add Ingredient Widget ###########
        self.costTab = QWidget()
        self.costTab.setObjectName(u"costTab")
        self.verticalLayout_5 = QVBoxLayout(self.costTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.costTableWidget = QTableWidget(self.costTab)
        self.costTableWidget.setObjectName(u"costTableWidget")

        self.verticalLayout_5.addWidget(self.costTableWidget)

        self.addIngredientTabWidget.addTab(self.costTab, "")

        self.gridLayout.addWidget(self.addIngredientTabWidget, 0, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        ######## Buttons widget of Add Ingredient Widget ###########

        self.buttonBox = QDialogButtonBox(addIngredientDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy3)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok|QDialogButtonBox.Save)
        

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(addIngredientDialog)
        self.buttonBox.accepted.connect(addIngredientDialog.accept)
        ##self.buttonBox.accepted.connect(self.formSubmit())
        self.accepted.connect(lambda: self.formSubmit())
       # self.buttonBox.accepted.connect(self.formSubmit(self.name))
        #self.buttonBox.accepted.connect(self.formSubmit(self.ingredientNameLineEdit.text(), self.commonNameLineEdit.text()))
        self.buttonBox.rejected.connect(addIngredientDialog.reject)
        
        self.addIngredientTabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(addIngredientDialog)
    # setupUi
    

    def retranslateUi(self, addIngredientDialog):
        self.ingredientNameLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Specific Name (if applicable)", None))
        self.commonNameLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Common Name", None))
        self.commonNameLineEdit.setPlaceholderText(QCoreApplication.translate("addIngredientDialog", u"ie. Cellulose Gum", None))
        self.supplierLabel_2.setText(QCoreApplication.translate("addIngredientDialog", u"Supplier (if applicable)", None))
        self.supplierIngIDLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Supplier Ingredient Number (if applicable)", None))
        self.percentYieldIfApplicableLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Percent Yield (if applicable)", None))
        self.supplierLabel.setText("")
        self.optionalLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Optional", None))
        self.allergenLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Major Allergens", None))
        self.dairyCheckbox.setText(QCoreApplication.translate("addIngredientDialog", u"Dairy", None))
        self.eggCheckbox.setText(QCoreApplication.translate("addIngredientDialog", u"Eggs", None))
        self.fishCheckbox.setText(QCoreApplication.translate("addIngredientDialog", u"Fish", None))
        self.shellfishCheckbox.setText(QCoreApplication.translate("addIngredientDialog", u"Shellfish", None))
        self.treeNutsCheckbox.setText(QCoreApplication.translate("addIngredientDialog", u"Tree Nuts", None))
        self.peanutsCheckbox.setText(QCoreApplication.translate("addIngredientDialog", u"Peanuts", None))
        self.wheatCheckbox.setText(QCoreApplication.translate("addIngredientDialog", u"Wheat", None))
        self.soyCheckbox.setText(QCoreApplication.translate("addIngredientDialog", u"Soy", None))
        self.veganCheckbox.setText(QCoreApplication.translate("addIngredientDialog", u"Vegan", None))
        self.organicCheckbox.setText(QCoreApplication.translate("addIngredientDialog", u"Organic", None))
        self.ngmvCheckbox.setText(QCoreApplication.translate("addIngredientDialog", u"NGMO Verified", None))
        self.kosherCheckbox.setText(QCoreApplication.translate("addIngredientDialog", u"Kosher", None))
        self.ketoCheckbox.setText(QCoreApplication.translate("addIngredientDialog", u"Keto-Friendly", None))
        self.wholeFoodsCheckbox.setText(QCoreApplication.translate("addIngredientDialog", u"Whole Foods Complaint", None))
        self.nsaCheckbox.setText(QCoreApplication.translate("addIngredientDialog", u"No Sugar Added", None))
        self.claimsLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Claims", None))
        self.halalCheckbox.setText(QCoreApplication.translate("addIngredientDialog", u"Halal", None))
        self.notesLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Notes", None))
        self.ingredientStatementLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Ingredient Statement", None))
        self.perLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Per ", None))
        self.gramsLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Grams", None))
        self.checkDataBtn.setText(QCoreApplication.translate("addIngredientDialog", u"Check Data", None))
        self.generateNFPPushBtn.setText(QCoreApplication.translate("addIngredientDialog", u"Generate NFP", None))
        self.vitaminAIUIULabel.setText(QCoreApplication.translate("addIngredientDialog", u"Vitamin A - IU (IU)", None))
        self.vitaminAREMcgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Vitamin A - RE (mcg)", None))
        self.vitaminARAEMcgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Vitamin A - RAE (mcg)", None))
        self.vitaminB1ThiaminMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Vitamin B1/Thiamin (mg)", None))
        self.vitaminB2RiboflavinMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Vitamin B2/Riboflavin (mg)", None))
        self.vitaminB3NiacinMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Vitamin B3/Niacin (mg)", None))
        self.vitaminB3NiacinEquivMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Vitamin B3/Niacin Equiv (mg)", None))
        self.vitaminB6MgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Vitamin B6 (mg)", None))
        self.vitaminB12McgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Vitamin B12 (mcg)", None))
        self.vitaminCMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Vitamin C (mg)", None))
        self.vitaminDIUIULabel.setText(QCoreApplication.translate("addIngredientDialog", u"Vitamin D - IU (IU)", None))
        self.vitaminEAlphaTocoMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Vitamin E/Alpha-Toco (mg)", None))
        self.folateMcgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Folate (mcg)", None))
        self.folateDFEMcgDFELabel.setText(QCoreApplication.translate("addIngredientDialog", u"Folate, DFE (mcg DFE)", None))
        self.vitaminKMcgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Vitamin K (mcg)", None))
        self.panothenicAcidMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Panothenic Acid (mg)", None))
        self.label_5.setText(QCoreApplication.translate("addIngredientDialog", u"Vitamins", None))
        self.totalFatGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Total Fat (g)", None))
        self.saturatedFatGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Total Saturated Fat (g)", None))
        self.totalUnsaturatedFatGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Total Unsaturated Fat (g)", None))
        self.monounsaturatedFatGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Monounsaturated Fat (g)", None))
        self.polyunsaturatedFatGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Polyunsaturated Fat (g)", None))
        self.transFatGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Trans Fat (g)", None))
        self.cholestrolMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Cholestrol (mg)", None))
        self.omega3FattyAcidGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Omega 3 Fatty Acid (g)", None))
        self.omega6FattyAcidGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Omega 6 Fatty Acid (g)", None))
        self.label_4.setText(QCoreApplication.translate("addIngredientDialog", u"Fats", None))
        self.calciumMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Calcium (mg)", None))
        self.chromiumMcgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Chromium (mcg)", None))
        self.copperMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Copper (mg)", None))
        self.fluorideMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Fluoride (mg)", None))
        self.iodineMcgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Iodine (mcg)", None))
        self.ironMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Iron (mg)", None))
        self.magnesiumMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Magnesium (mg)", None))
        self.manganeseMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Manganese (mg)", None))
        self.molybdenumMcgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Molybdenum (mcg)", None))
        self.phosphorusMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Phosphorus (mg)", None))
        self.potassiumMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Potassium (mg)", None))
        self.seleniumMcgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Selenium (mcg)", None))
        self.sodiumMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Sodium (mg)", None))
        self.zincMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Zinc (mg)", None))
        self.mineralsFrame.setText(QCoreApplication.translate("addIngredientDialog", u"Minerals", None))
        self.totalCarbohydratesGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Total Carbohydrates (g)", None))
        self.totalSugarsGramLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Total Sugars (g)", None))
        self.addedSugarsGramLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Added Sugars (g)", None))
        self.totalDietaryFiberGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Total Dietary Fiber (g)", None))
        self.totalSolubleFiberGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Total Soluble Fiber (g)", None))
        self.monosaccharidesGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Monosaccharides (g)", None))
        self.disaccharidesGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Disaccharides (g)", None))
        self.otherCarbohydratesGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Other Carbohydrates (g)", None))
        self.carbsLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Carbohydrates", None))
        self.label_2.setText(QCoreApplication.translate("addIngredientDialog", u"Proteins", None))
        self.totalProteinGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Total Protein (g)", None))
        self.label_6.setText(QCoreApplication.translate("addIngredientDialog", u"Other Nutrients", None))
        self.moistureGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Moisture (g)", None))
        self.caffeineMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Caffeine (mg)", None))
        self.cholineMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Choline (mg)", None))
        self.alcoholGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Alcohol (g)", None))
        self.sugarAlcoholGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Sugar Alcohol (g)", None))
        self.addIngredientTabWidget.setTabText(self.addIngredientTabWidget.indexOf(self.nutritionalsTab), QCoreApplication.translate("addIngredientDialog", u"Nutritionals", None))
        self.addIngredientTabWidget.setTabText(self.addIngredientTabWidget.indexOf(self.documentationTab), QCoreApplication.translate("addIngredientDialog", u"Documentation", None))
        self.addIngredientTabWidget.setTabText(self.addIngredientTabWidget.indexOf(self.groupsTab), QCoreApplication.translate("addIngredientDialog", u"Groups", None))
        self.addIngredientTabWidget.setTabText(self.addIngredientTabWidget.indexOf(self.costTab), QCoreApplication.translate("addIngredientDialog", u"Cost", None))
        pass
    # retranslateUi

    def formSubmit(self): 
        
        nutrientMap = [
            {
                "nutrient_name" : "Added Sugars",
                "nutrient_id" : 42, 
                "value": self.addedSugarsGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Alcohol",
                "nutrient_id" : 52,
                "value": self.alcoholGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Caffeine",
                "nutrient_id" : 50, 
                "value": self.caffeineMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Calcium",
                "nutrient_id" : 26, 
                "value": self.calciumMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Cholestrol",
                "nutrient_id" : 23, 
                "value": self.cholestrolMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Choline",
                "nutrient_id" : 51, 
                "value": self.cholineMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Chromium",
                "nutrient_id" : 27, 
                "value": self.chromiumMcgLineEdit.text(),
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name" : "Copper",
                "nutrient_id" : 28, 
                "value": self.copperMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Disaccharides",
                "nutrient_id" : 46, 
                "value": self.disaccharidesGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Fluoride",
                "nutrient_id" : 29, 
                "value": self.fluorideMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Folate",
                "nutrient_id" : 13, 
                "value": self.folateMcgLineEdit.text(),
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name" : "Folate - DFE",
                "nutrient_id" : 14, 
                "value": self.folateDFEMcgDFELineEdit.text(),
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name" : "Iodine",
                "nutrient_id" : 30, 
                "value": self.iodineMcgLineEdit.text(),
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name" : "Iron",
                "nutrient_id" : 31, 
                "value": self.ironMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Magnesium",
                "nutrient_id" : 32, 
                "value": self.magnesiumMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Manganese",
                "nutrient_id" : 33, 
                "value": self.manganeseMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Moisture",
                "nutrient_id" : 49, 
                "value": self.moistureGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Molybdenum",
                "nutrient_id" : 34, 
                "value": self.molybdenumMcgLineEdit.text(),
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name" : "Monosaccharides",
                "nutrient_id" : 45, 
                "value": self.monosaccharidesGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Monounsaturated Fat",
                "nutrient_id" : 20, 
                "value": self.monounsaturatedFatGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Omega-3 Fatty Acid",
                "nutrient_id" : 24, 
                "value": self.omega3FattyAcidGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Omega-6 Fatty Acid",
                "nutrient_id" : 25, 
                "value": self.omega6FattyAcidGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Other Carbohydrates",
                "nutrient_id" : 47, 
                "value": self.otherCarbohydratesGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Panothenic Acid",
                "nutrient_id" : 16, 
                "value": self.panothenicAcidMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Phosphorus",
                "nutrient_id" : 35, 
                "value": self.phosphorusMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Polyunsaturated Fat",
                "nutrient_id" : 21,
                "value": self.polyunsaturatedFatGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Potassium",
                "nutrient_id" : 36,
                "value": self.potassiumMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Saturated Fat",
                "nutrient_id" : 18,
                "value": self.saturatedFatGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Selenium",
                "nutrient_id" : 37,
                "value": self.seleniumMcgLineEdit.text(),
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name" : "Sodium",
                "nutrient_id" : 38, 
                "value": self.sodiumMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Sugar Alcohol",
                "nutrient_id" : 53,
                "value": self.sugarAlcoholGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Total Carbohydrates",
                "nutrient_id" : 40,
                "value": self.totalCarbohydratesGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Total Dietary Fiber",
                "nutrient_id" : 43, 
                "value": self.totalDietaryFiberGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Total Fat",
                "nutrient_id" : 17,
                "value": self.totalFatGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Total Protein",
                "nutrient_id" : 48,
                "value": self.totalProteinGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Total Soluble Fiber",
                "nutrient_id" : 44,
                "value": self.totalSolubleFiberGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Total Sugars",
                "nutrient_id" : 41, 
                "value": self.totalSugarsGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Total Unsaturated Fat",
                "nutrient_id" : 19, 
                "value": self.totalUnsaturatedFatGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Trans Fat",
                "nutrient_id" : 22, 
                "value": self.transFatGLineEdit.text(),
                "weight_id": "Grams"
            },
            {
                "nutrient_name" : "Vitamin A - IU",
                "nutrient_id" : 1, 
                "value": self.vitaminAIUIULineEdit.text(), 
                "weight_id": "IU"
            },
            {
                "nutrient_name" : "Vitamin A - RAE",
                "nutrient_id" : 3, 
                "value": self.vitaminARAEMcgLineEdit.text(),
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name" : "Vitamin A - REM",
                "nutrient_id" : 2, 
                "value": self.vitaminAREMcgLineEdit.text(),
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name" : "Vitamin B1/Thiamin",
                "nutrient_id" : 4, 
                "value": self.vitaminB1ThiaminMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Vitamin B12",
                "nutrient_id" : 9, 
                "value": self.vitaminB12McgLineEdit.text(),
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name" : "Vitamin B2/Riboflavin",
                "nutrient_id" : 5, 
                "value": self.vitaminB2RiboflavinMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Vitamin B3/Niacin",
                "nutrient_id" : 6, 
                "value": self.vitaminB3NiacinMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Vitamin B3/Niacin Equivalent",
                "nutrient_id" : 7,
                "value": self.vitaminB3NiacinEquivMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Vitamin B6",
                "nutrient_id" : 8, 
                "value": self.vitaminB6MgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Vitamin C",
                "nutrient_id" : 10,
                "value": self.vitaminCMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Vitamin D - IU",
                "nutrient_id" : 11, 
                "value": self.vitaminDIUIULineEdit.text(),
                "weight_id": "IU"
            },
            {
                "nutrient_name" : "Vitamin E/alpha-Tocopherol",
                "nutrient_id" : 12, 
                "value": self.vitaminEAlphaTocoMgLineEdit.text(),
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name" : "Vitamin K",
                "nutrient_id" : 15,
                "value": self.vitaminKMcgLineEdit.text(),
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name" : "Zinc",
                "nutrient_id" : 39,
                "value": self.zincMgLineEdit.text(),
                "weight_id": "Milligrams"
            }
        ]
        allergenMap = [
            {'allergen': 'Dairy', 'object': self.dairyCheckbox},
            {'allergen': 'Eggs', 'object': self.eggCheckbox},
            {'allergen': 'Fish', 'object': self.fishCheckbox},
            {'allergen': 'Shellfish', 'object': self.shellfishCheckbox},
            {'allergen': 'Tree Nuts', 'object': self.treeNutsCheckbox},
            {'allergen': 'Peanuts', 'object': self.peanutsCheckbox},
            {'allergen': 'Wheat', 'object': self.wheatCheckbox},
            {'allergen': 'Soy', 'object': self.soyCheckbox},
        ]
        claimMap = [
            {'claim': 'Vegan', 'object': self.veganCheckbox},
            {'claim': 'Halal', 'object': self.halalCheckbox}, 
            {'claim': 'Organic', 'object': self.organicCheckbox}, 
            {'claim': 'NGMO Verified', 'object': self.ngmvCheckbox}, 
            {'claim': 'Kosher', 'object': self.kosherCheckbox}, 
            {'claim': 'Keto-friendly', 'object': self.ketoCheckbox}, 
            {'claim': 'Whole Foods Compliant', 'object': self.wholeFoodsCheckbox}, 
            {'claim': 'No Sugar Added', 'object': self.nsaCheckbox}
        ]
        
        db = connectDB()
        try: 
            with db.cursor() as cursor:   
                    cName = self.commonNameLineEdit.text()
                    supplier = self.supplierComboBox.currentText()
                    sName = self.ingredientNameLineEdit.text()
                    itemCode = self.supplierIngredientNumberLineEdit.text()

                    result = cursor.execute("INSERT IGNORE INTO ingredient(ing_common_name) VALUES (%s)", (cName,))
                    lastIngID = db.insert_id()

                    cursor.execute("INSERT IGNORE INTO supplier(supplier_name) VALUES (%s)", (supplier,))
                    lastSupplierID  = db.insert_id()
                    #db.commit()

            with db.cursor() as cursor: 

                cursor.execute("INSERT IGNORE INTO supplier_ingredient(supplier_id, ing_id, ing_specific_name, supplier_ing_item_code) VALUES (%s, %s, %s, %s)", (lastSupplierID, lastIngID, sName, itemCode,))

                for nutrient in nutrientMap: 
                    if nutrient['value']: 
                        cursor.execute("INSERT INTO ing_nutrient(ing_id, nutrient_id, nutrient_weight, unit) VALUES (%s, %s, %s, %s)", (lastIngID, nutrient['nutrient_id'], nutrient['value'], nutrient['weight_id'],))
                #db.commit()

            # inserts allergens into database
            with db.cursor() as cursor: 

                for allergen in allergenMap:
                    input = allergen['object']
                    if input.isChecked(): 
                        cursor.execute("INSERT INTO supplier_ingredient_allergens(supplier_id, supplier_ing_item_code, allergen) VALUES (%s, %s, %s)", (lastSupplierID, itemCode, allergen['allergen']))

            # inserts claims into database
            with db.cursor() as cursor: 
                for claim in claimMap: 
                    cla = claim['object']
                    if cla.isChecked(): 
                        cursor.execute("INSERT INTO supplier_ingredient_claims(supplier_id, supplier_ing_item_code, claim) VALUES (%s, %s, %s)", (lastSupplierID, itemCode, claim['claim']))

            #cursor.commit()       
            print('Everything went right')
        except: 
            print('something went wrong')
        
#def validateOnSubmit(self):
    #    if self.commonNameLineEdit.
##

#class validationWindow(QDialog): 

 #   def __init__(self): 





        

    