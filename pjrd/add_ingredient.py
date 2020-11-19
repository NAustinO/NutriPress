# -*- coding: utf-8 -*-

#########################################################################
## Form generated from reading UI file 'add_ingredient.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
#########################################################################

## TODO: ADD CALORIES
import os, sys
from datetime import date, datetime
from typing import NoReturn
#from pjrd.helpers import TimedMessageBox
from PyQt5.QtCore import QSize, QObject, Qt, QCoreApplication, QMetaObject, QDir, QRect
from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout, QGridLayout, QWidget, QTabWidget, QFormLayout, QFrame, QLabel, QCheckBox, QLineEdit, QSpinBox, QPushButton, QDialog, QCompleter, QComboBox, QDoubleSpinBox, QAbstractSpinBox, QHBoxLayout, QListWidget, QTableWidget, QDialogButtonBox, QFileDialog, QScrollArea, QSpacerItem, QTableWidgetItem, QAbstractItemView, QListWidgetItem, QMessageBox
from PySide2.QtGui import QStandardItem, QStandardItemModel

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pymysql import Connection
from helpers import displayNFP, dbConnection

class addIngredientDialog(QDialog):

    def __init__(self):
        super(addIngredientDialog, self).__init__()
        self.setupUi(self)
        self.setupLogic()
         
        # add to if needed 
        #TODO move these to a function in helpers where they return a dictionary for maintainability 
        self.allergenMap = [
            {'allergen': 'Dairy', 'id': 1, 'object': self.dairyCheckbox},
            {'allergen': 'Eggs', 'id': 2, 'object': self.eggCheckbox},
            {'allergen': 'Fish', 'id': 3, 'object': self.fishCheckbox},
            {'allergen': 'Shellfish', 'id': 4, 'object': self.shellfishCheckbox},
            {'allergen': 'Tree Nuts', 'id': 5, 'object': self.treeNutsCheckbox},
            {'allergen': 'Peanuts', 'id': 6, 'object': self.peanutsCheckbox},
            {'allergen': 'Wheat', 'id': 7, 'object': self.wheatCheckbox},
            {'allergen': 'Soy', 'id': 8, 'object': self.soyCheckbox},
        ]
        self.claimMap = [
            {'claim': 'Vegan', 'object': self.veganCheckbox},
            {'claim': 'Halal', 'object': self.halalCheckbox},
            {'claim': 'Organic', 'object': self.organicCheckbox},
            {'claim': 'NGMO Verified', 'object': self.ngmvCheckbox},
            {'claim': 'Kosher', 'object': self.kosherCheckbox},
            {'claim': 'Keto-friendly', 'object': self.ketoCheckbox},
            {'claim': 'Whole Foods Compliant', 'object': self.wholeFoodsCheckbox},
            {'claim': 'No Sugar Added', 'object': self.nsaCheckbox}
        ]
        self.nutrientMap = [
            {
                "nutrient_name": "Added Sugars",
                "nutrient_id": 659,
                "value": self.addedSugarsGLineEdit.text(),
                'factor': 1,
                'unit_id': 1,
                "weight_id": 'Gram'
            },
            {
                "nutrient_name": "Alcohol",
                "nutrient_id": 221,
                "value": self.alcoholGLineEdit.text(),
                'factor': 1,
                'unit_id': 1,
                "weight_id": 'Gram'
            },
            {
                "nutrient_name": "Caffeine",
                "nutrient_id": 262,
                "value": self.caffeineMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2,
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Calcium",
                "nutrient_id": 301,
                "value": self.calciumMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2,
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Cholestrol",
                "nutrient_id": 601, 
                "value": self.cholestrolMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2,
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Choline",
                "nutrient_id": 421,
                "value": self.cholineMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2, 
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Chromium",
                "nutrient_id": 654,
                "value": self.chromiumMcgLineEdit.text(),
                'factor': .000001,
                'unit_id': 4, 
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name": "Copper",
                "nutrient_id": 312,
                "value": self.copperMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2, 
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Disaccharides",
                "nutrient_id": 649,
                "value": self.disaccharidesGLineEdit.text(),
                'factor': 1,
                'unit_id': 1,
                "weight_id": "Grams"
            },
            {
                "nutrient_name": "Fluoride",
                "nutrient_id": 652,
                "value": self.fluorideMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2, 
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Folate",
                "nutrient_id": 417,
                "value": self.folateMcgLineEdit.text(),
                'factor': .000001, 
                'unit_id': 4, 
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name": "Folate - DFE",
                "nutrient_id": 435,
                "value": self.folateDFEMcgDFELineEdit.text(),
                'factor': .000001,
                'unit_id': 4, 
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name": "Iodine",
                "nutrient_id": 655,
                "value": self.iodineMcgLineEdit.text(),
                'factor': .000001, 
                'unit_id': 4, 
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name": "Iron",
                "nutrient_id": 303,
                "value": self.ironMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2,  
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Magnesium",
                "nutrient_id": 651,
                "value": self.magnesiumMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2,
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Manganese",
                "nutrient_id": 656,
                "value": self.manganeseMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2, 
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Moisture",
                "nutrient_id": 255,
                "value": self.moistureGLineEdit.text(),
                'factor': 1,
                'unit_id': 1, 
                "weight_id": "Grams"
            },
            {
                "nutrient_name": "Molybdenum",
                "nutrient_id": 657,
                "value": self.molybdenumMcgLineEdit.text(),
                'factor': .000001, 
                'unit_id': 4, 
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name": "Monosaccharides",
                "nutrient_id": 1,
                "value": self.monosaccharidesGLineEdit.text(),
                'factor': 1, 
                'unit_id': 1, 
                "weight_id": "Grams"
            },
            {
                "nutrient_name": "Monounsaturated Fat",
                "nutrient_id": 645,
                "value": self.monounsaturatedFatGLineEdit.text(),
                'factor': 1,
                'unit_id': 1, 
                "weight_id": "Grams"
            },
            {
                "nutrient_name": "Omega-3 Fatty Acid",
                "nutrient_id": 660,
                "value": self.omega3FattyAcidGLineEdit.text(),
                'factor': 1, 
                'unit_id': 1, 
                "weight_id": "Grams"
            },
            {
                "nutrient_name": "Omega-6 Fatty Acid",
                "nutrient_id": 661,
                "value": self.omega6FattyAcidGLineEdit.text(),
                'factor': 1, 
                'unit_id': 1,
                "weight_id": "Grams"
            },
            {
                "nutrient_name": "Other Carbohydrates",
                "nutrient_id": 662,
                "value": self.otherCarbohydratesGLineEdit.text(),
                'factor': 1, 
                'unit_id': 1, 
                "weight_id": "Grams"
            },
            {
                "nutrient_name": "Panothenic Acid",
                "nutrient_id": 658,
                "value": self.panothenicAcidMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2,
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Phosphorus",
                "nutrient_id": 305,
                "value": self.phosphorusMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2,
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Polyunsaturated Fat",
                "nutrient_id": 646,
                "value": self.polyunsaturatedFatGLineEdit.text(),
                'factor': 1,
                'unit_id': 1,
                "weight_id": "Grams"
            },
            {
                "nutrient_name": "Potassium",
                "nutrient_id": 306,
                "value": self.potassiumMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2,
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Saturated Fat",
                "nutrient_id": 606,
                "value": self.saturatedFatGLineEdit.text(),
                'factor': 1,
                'unit_id': 1,
                "weight_id": "Grams"
            },
            {
                "nutrient_name": "Selenium",
                "nutrient_id": 317,
                "value": self.seleniumMcgLineEdit.text(),
                'factor': .000001,
                'unit_id': 4,
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name": "Sodium",
                "nutrient_id": 307,
                "value": self.sodiumMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2, 
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Sugar Alcohol",
                "nutrient_id": 647,
                "value": self.sugarAlcoholGLineEdit.text(),
                'factor': 1,
                'unit_id': 1,
                "weight_id": "Grams"
            },
            {
                "nutrient_name": "Total Carbohydrates",
                "nutrient_id": 205,
                "value": self.totalCarbohydratesGLineEdit.text(),
                'factor': 1,
                'unit_id': 1,
                "weight_id": "Grams"
            },
            {
                "nutrient_name": "Total Dietary Fiber",
                "nutrient_id": 291,
                "value": self.totalDietaryFiberGLineEdit.text(),
                'factor': 1,
                'unit_id': 1,
                "weight_id": "Grams"
            },
            {
                "nutrient_name": "Total Fat",
                "nutrient_id": 204,
                "value": self.totalFatGLineEdit.text(),
                'factor': 1,
                'unit_id': 1,
                "weight_id": "Grams"
            },
            {
                "nutrient_name": "Total Protein",
                "nutrient_id": 203,
                "value": self.totalProteinGLineEdit.text(),
                'factor': 1,
                'unit_id': 1,
                "weight_id": "Grams"
            },
            {
                "nutrient_name": "Total Soluble Fiber",
                "nutrient_id": 648,
                "value": self.totalSolubleFiberGLineEdit.text(),
                'factor': 1,
                'unit_id': 1,
                "weight_id": "Grams"
            },
            {
                "nutrient_name": "Total Sugars",
                "nutrient_id": 269,
                "value": self.totalSugarsGLineEdit.text(),
                'factor': 1,
                'unit_id': 1,
                "weight_id": "Grams"
            },
            {
                "nutrient_name": "Total Unsaturated Fat",
                "nutrient_id": 663,
                "value": self.totalUnsaturatedFatGLineEdit.text(),
                'factor': 1,
                'unit_id': 1,
                "weight_id": "Grams"
            },
            {
                "nutrient_name": "Trans Fat",
                "nutrient_id": 664,
                "value": self.transFatGLineEdit.text(),
                'factor': 1,
                'unit_id': 1,
                "weight_id": "Grams"
            },
            {
                # retinol equivalents for factor NOT SURE ABOUT THIS ONE
                "nutrient_name": "Vitamin A - IU",
                "nutrient_id": 320,
                "value": self.vitaminAIUIULineEdit.text(),
                'factor': 0.3, 
                'unit_id': 10,
                "weight_id": "IU"
            },
            {
                "nutrient_name": "Vitamin A - RAE",
                "nutrient_id": 320,
                "value": self.vitaminARAEMcgLineEdit.text(),
                'factor': .000001,
                'unit_id': 4,
                "weight_id": "Micrograms"
            },
            {
                # NOT SURE ABOUT THIS ONE EITHER
                "nutrient_name": "Vitamin A - REM",
                "nutrient_id": 2,
                "value": self.vitaminAREMcgLineEdit.text(),
                'factor': .000001,
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name": "Vitamin B1/Thiamin",
                "nutrient_id": 404,
                "value": self.vitaminB1ThiaminMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2,
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Vitamin B12",
                "nutrient_id": 418,
                "value": self.vitaminB12McgLineEdit.text(),
                'factor': .000001,
                'unit_id': 4,
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name": "Vitamin B2/Riboflavin",
                "nutrient_id": 405,
                "value": self.vitaminB2RiboflavinMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2,
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Vitamin B3/Niacin",
                "nutrient_id": 406,
                "value": self.vitaminB3NiacinMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2,
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Vitamin B6",
                "nutrient_id": 415,
                "value": self.vitaminB6MgLineEdit.text(),
                'factor': .001,
                'unit_id': 2,
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Vitamin C",
                "nutrient_id": 401,
                "value": self.vitaminCMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2,
                "weight_id": "Milligrams"
            },
            {
                # NOT SURE ABOUT THIS ONE
                "nutrient_name": "Vitamin D",
                "nutrient_id": 328,
                "value": self.vitaminDIUIULineEdit.text(),
                'unit_id': 4,
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name": "Vitamin E/alpha-Tocopherol",
                "nutrient_id": 323,
                "value": self.vitaminEAlphaTocoMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2,
                "weight_id": "Milligrams"
            },
            {
                "nutrient_name": "Vitamin K",
                "nutrient_id": 430,
                "value": self.vitaminKMcgLineEdit.text(),
                'factor': .000001,
                'unit_id': 4,
                "weight_id": "Micrograms"
            },
            {
                "nutrient_name": "Zinc",
                "nutrient_id": 309,
                "value": self.zincMgLineEdit.text(),
                'factor': .001,
                'unit_id': 2,
                "weight_id": "Milligrams"
            },
            {
                # same as energy
                "nutrient_name": "Calories",
                "nutrient_id": 208,
                "value": self.caloriesKCalLineEdit.text(),
                'factor': 1,
                'unit_id': 3, 
                "weight_id": "kCal"
            }
        ]

    def setupUi(self, addIngredientDialog):
        if not addIngredientDialog.objectName():
            addIngredientDialog.setObjectName(u"addIngredientDialog")
        addIngredientDialog.resize(800, 600)
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

        self.ingDescLabel = QLabel(self.generalFrame1)
        self.ingDescLabel.setObjectName(u"ingDescLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.ingDescLabel)

        self.ingDescLineEdit = QLineEdit(self.generalFrame1)
        self.ingDescLineEdit.setObjectName(u"ingDescLineEdit")
        self.ingDescLineEdit.setMinimumSize(QSize(300, 0))
        self.ingDescLineEdit.setPlaceholderText(u"ie. Pre-Hydrated\u00ae Ticalose\u00ae CMC 15 Powder")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ingDescLineEdit)

        self.ingNameLabel = QLabel(self.generalFrame1)
        self.ingNameLabel.setObjectName(u"ingNameLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.ingNameLabel)

        self.ingNameLineEdit = QLineEdit(self.generalFrame1)
        self.ingNameLineEdit.setObjectName(u"ingNameLineEdit")
        self.ingNameLineEdit.setMinimumSize(QSize(300, 0))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ingNameLineEdit)

        self.supplierLabel_2 = QLabel(self.generalFrame1)
        self.supplierLabel_2.setObjectName(u"supplierLabel_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.supplierLabel_2)

        self.supplierComboBox = QComboBox(self.generalFrame1)
        self.supplierComboBox.setObjectName(u"supplierComboBox")
        self.supplierComboBox.setMinimumSize(QSize(200, 0))
        self.supplierComboBox.setEditable(True)
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
        self.percentYieldDoubleSpinBox.setObjectName(u"percentYieldDoubleSpinBox")
        self.percentYieldDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.PlusMinus)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.percentYieldDoubleSpinBox)

        self.supplierLabel = QLabel(self.generalFrame1)
        self.supplierLabel.setObjectName(u"supplierLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.supplierLabel)


        self.verticalLayout_4.addWidget(self.generalFrame1)

        self.genTabScrollArea = QScrollArea(self.genInfoTab)
        self.genTabScrollArea.setObjectName(u"genTabScrollArea")
        self.genTabScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 805, 444))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.ingredientStatementLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.ingredientStatementLabel.setObjectName(u"ingredientStatementLabel")
        self.ingredientStatementLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.ingredientStatementLabel, 3, 0, 1, 1)

        self.ingredientStatementLineEdit = QLineEdit(self.scrollAreaWidgetContents_2)
        self.ingredientStatementLineEdit.setObjectName(u"ingredientStatementLineEdit")
        self.ingredientStatementLineEdit.setMinimumSize(QSize(0, 75))

        self.gridLayout_5.addWidget(self.ingredientStatementLineEdit, 3, 1, 1, 1)

        self.allergenCheckBoxWidget = QWidget(self.scrollAreaWidgetContents_2)
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


        self.gridLayout_5.addWidget(self.allergenCheckBoxWidget, 1, 0, 1, 1)

        self.claimsCheckBoxWidget = QWidget(self.scrollAreaWidgetContents_2)
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


        self.gridLayout_5.addWidget(self.claimsCheckBoxWidget, 1, 1, 1, 1)

        self.notesLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.notesLabel.setObjectName(u"notesLabel")
        self.notesLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.notesLabel, 4, 0, 1, 1)

        self.notesLineEdit = QLineEdit(self.scrollAreaWidgetContents_2)
        self.notesLineEdit.setObjectName(u"notesLineEdit")
        self.notesLineEdit.setMinimumSize(QSize(100, 75))

        self.gridLayout_5.addWidget(self.notesLineEdit, 4, 1, 1, 1)

        self.optionalLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.optionalLabel.setObjectName(u"optionalLabel")

        self.gridLayout_5.addWidget(self.optionalLabel, 0, 0, 1, 1)

        self.genTabScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_4.addWidget(self.genTabScrollArea)

        self.addIngredientTabWidget.addTab(self.genInfoTab, "")
        self.addIngredientTabWidget.setTabText(self.addIngredientTabWidget.indexOf(self.genInfoTab), u"General")
        self.nutritionalsTab = QWidget()
        self.nutritionalsTab.setObjectName(u"nutritionalsTab")
        self.verticalLayout_3 = QVBoxLayout(self.nutritionalsTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.nutritionalHeader = QWidget(self.nutritionalsTab)
        self.nutritionalHeader.setObjectName(u"nutritionalHeader")
        self.nutritionalHeader.setAutoFillBackground(True)
        self.horizontalLayout = QHBoxLayout(self.nutritionalHeader)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.perLabel = QLabel(self.nutritionalHeader)
        self.perLabel.setObjectName(u"perLabel")
        self.perLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.perLabel)

        self.perGramsSpinBox = QSpinBox(self.nutritionalHeader)
        self.perGramsSpinBox.setObjectName(u"perGramsSpinBox")
        self.perGramsSpinBox.setAlignment(Qt.AlignCenter)
        self.perGramsSpinBox.setMaximum(1000)
        #self.perGramsSpinBox.setSingleStep(10)
        self.perGramsSpinBox.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.perGramsSpinBox.setValue(100)
        self.perGramsSpinBox.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout.addWidget(self.perGramsSpinBox)

        self.gramsLabel = QLabel(self.nutritionalHeader)
        self.gramsLabel.setObjectName(u"gramsLabel")

        self.horizontalLayout.addWidget(self.gramsLabel)

        self.checkDataBtn = QPushButton(self.nutritionalHeader)
        self.checkDataBtn.setObjectName(u"checkDataBtn")

        self.horizontalLayout.addWidget(self.checkDataBtn)

        self.generateNFPPushBtn = QPushButton(self.nutritionalHeader)
        self.generateNFPPushBtn.setObjectName(u"generateNFPPushBtn")

        self.horizontalLayout.addWidget(self.generateNFPPushBtn)


        self.verticalLayout_3.addWidget(self.nutritionalHeader)

        self.scrollArea = QScrollArea(self.nutritionalsTab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 805, 1525))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.mineralsFrame_2 = QFrame(self.scrollAreaWidgetContents)
        self.mineralsFrame_2.setObjectName(u"mineralsFrame_2")
        self.mineralsFrame_2.setAutoFillBackground(True)
        self.mineralsFrame_2.setFrameShape(QFrame.StyledPanel)
        self.formLayout_6 = QFormLayout(self.mineralsFrame_2)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.calciumMgLabel = QLabel(self.mineralsFrame_2)
        self.calciumMgLabel.setObjectName(u"calciumMgLabel")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.calciumMgLabel)

        self.chromiumMcgLabel = QLabel(self.mineralsFrame_2)
        self.chromiumMcgLabel.setObjectName(u"chromiumMcgLabel")

        self.formLayout_6.setWidget(4, QFormLayout.LabelRole, self.chromiumMcgLabel)

        self.copperMgLabel = QLabel(self.mineralsFrame_2)
        self.copperMgLabel.setObjectName(u"copperMgLabel")

        self.formLayout_6.setWidget(6, QFormLayout.LabelRole, self.copperMgLabel)

        self.fluorideMgLabel = QLabel(self.mineralsFrame_2)
        self.fluorideMgLabel.setObjectName(u"fluorideMgLabel")

        self.formLayout_6.setWidget(8, QFormLayout.LabelRole, self.fluorideMgLabel)

        self.iodineMcgLabel = QLabel(self.mineralsFrame_2)
        self.iodineMcgLabel.setObjectName(u"iodineMcgLabel")

        self.formLayout_6.setWidget(10, QFormLayout.LabelRole, self.iodineMcgLabel)

        self.ironMgLabel = QLabel(self.mineralsFrame_2)
        self.ironMgLabel.setObjectName(u"ironMgLabel")

        self.formLayout_6.setWidget(12, QFormLayout.LabelRole, self.ironMgLabel)

        self.magnesiumMgLabel = QLabel(self.mineralsFrame_2)
        self.magnesiumMgLabel.setObjectName(u"magnesiumMgLabel")

        self.formLayout_6.setWidget(14, QFormLayout.LabelRole, self.magnesiumMgLabel)

        self.manganeseMgLabel = QLabel(self.mineralsFrame_2)
        self.manganeseMgLabel.setObjectName(u"manganeseMgLabel")

        self.formLayout_6.setWidget(16, QFormLayout.LabelRole, self.manganeseMgLabel)

        self.molybdenumMcgLabel = QLabel(self.mineralsFrame_2)
        self.molybdenumMcgLabel.setObjectName(u"molybdenumMcgLabel")

        self.formLayout_6.setWidget(18, QFormLayout.LabelRole, self.molybdenumMcgLabel)

        self.phosphorusMgLabel = QLabel(self.mineralsFrame_2)
        self.phosphorusMgLabel.setObjectName(u"phosphorusMgLabel")

        self.formLayout_6.setWidget(20, QFormLayout.LabelRole, self.phosphorusMgLabel)

        self.potassiumMgLabel = QLabel(self.mineralsFrame_2)
        self.potassiumMgLabel.setObjectName(u"potassiumMgLabel")

        self.formLayout_6.setWidget(22, QFormLayout.LabelRole, self.potassiumMgLabel)

        self.seleniumMcgLabel = QLabel(self.mineralsFrame_2)
        self.seleniumMcgLabel.setObjectName(u"seleniumMcgLabel")

        self.formLayout_6.setWidget(24, QFormLayout.LabelRole, self.seleniumMcgLabel)

        self.sodiumMgLabel = QLabel(self.mineralsFrame_2)
        self.sodiumMgLabel.setObjectName(u"sodiumMgLabel")

        self.formLayout_6.setWidget(26, QFormLayout.LabelRole, self.sodiumMgLabel)

        self.zincMgLabel = QLabel(self.mineralsFrame_2)
        self.zincMgLabel.setObjectName(u"zincMgLabel")

        self.formLayout_6.setWidget(28, QFormLayout.LabelRole, self.zincMgLabel)

        self.calciumMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.calciumMgLineEdit.setObjectName(u"calciumMgLineEdit")
        self.calciumMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.calciumMgLineEdit)

        self.chromiumMcgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.chromiumMcgLineEdit.setObjectName(u"chromiumMcgLineEdit")
        self.chromiumMcgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_6.setWidget(4, QFormLayout.FieldRole, self.chromiumMcgLineEdit)

        self.copperMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.copperMgLineEdit.setObjectName(u"copperMgLineEdit")
        self.copperMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_6.setWidget(6, QFormLayout.FieldRole, self.copperMgLineEdit)

        self.fluorideMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.fluorideMgLineEdit.setObjectName(u"fluorideMgLineEdit")
        self.fluorideMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_6.setWidget(8, QFormLayout.FieldRole, self.fluorideMgLineEdit)

        self.iodineMcgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.iodineMcgLineEdit.setObjectName(u"iodineMcgLineEdit")
        self.iodineMcgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_6.setWidget(10, QFormLayout.FieldRole, self.iodineMcgLineEdit)

        self.ironMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.ironMgLineEdit.setObjectName(u"ironMgLineEdit")
        self.ironMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_6.setWidget(12, QFormLayout.FieldRole, self.ironMgLineEdit)

        self.magnesiumMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.magnesiumMgLineEdit.setObjectName(u"magnesiumMgLineEdit")
        self.magnesiumMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_6.setWidget(14, QFormLayout.FieldRole, self.magnesiumMgLineEdit)

        self.manganeseMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.manganeseMgLineEdit.setObjectName(u"manganeseMgLineEdit")
        self.manganeseMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_6.setWidget(16, QFormLayout.FieldRole, self.manganeseMgLineEdit)

        self.molybdenumMcgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.molybdenumMcgLineEdit.setObjectName(u"molybdenumMcgLineEdit")
        self.molybdenumMcgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_6.setWidget(18, QFormLayout.FieldRole, self.molybdenumMcgLineEdit)

        self.phosphorusMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.phosphorusMgLineEdit.setObjectName(u"phosphorusMgLineEdit")
        self.phosphorusMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_6.setWidget(20, QFormLayout.FieldRole, self.phosphorusMgLineEdit)

        self.potassiumMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.potassiumMgLineEdit.setObjectName(u"potassiumMgLineEdit")
        self.potassiumMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_6.setWidget(22, QFormLayout.FieldRole, self.potassiumMgLineEdit)

        self.seleniumMcgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.seleniumMcgLineEdit.setObjectName(u"seleniumMcgLineEdit")
        self.seleniumMcgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_6.setWidget(24, QFormLayout.FieldRole, self.seleniumMcgLineEdit)

        self.sodiumMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.sodiumMgLineEdit.setObjectName(u"sodiumMgLineEdit")
        self.sodiumMgLineEdit.setPlaceholderText('Recommended')
        self.sodiumMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_6.setWidget(26, QFormLayout.FieldRole, self.sodiumMgLineEdit)

        self.zincMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.zincMgLineEdit.setObjectName(u"zincMgLineEdit")
        self.zincMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_6.setWidget(28, QFormLayout.FieldRole, self.zincMgLineEdit)

        self.mineralsFrame = QLabel(self.mineralsFrame_2)
        self.mineralsFrame.setObjectName(u"mineralsFrame")
        self.mineralsFrame.setAlignment(Qt.AlignCenter)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.mineralsFrame)


        self.gridLayout_4.addWidget(self.mineralsFrame_2, 2, 0, 1, 1)

        self.carbsFrame = QFrame(self.scrollAreaWidgetContents)
        self.carbsFrame.setObjectName(u"carbsFrame")
        self.carbsFrame.setAutoFillBackground(True)
        self.carbsFrame.setFrameShape(QFrame.StyledPanel)
        self.formLayout_4 = QFormLayout(self.carbsFrame)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.totalCarbohydratesGLabel = QLabel(self.carbsFrame)
        self.totalCarbohydratesGLabel.setObjectName(u"totalCarbohydratesGLabel")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.totalCarbohydratesGLabel)

        self.totalSugarsGramLabel = QLabel(self.carbsFrame)
        self.totalSugarsGramLabel.setObjectName(u"totalSugarsGramLabel")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.totalSugarsGramLabel)

        self.addedSugarsGramLabel = QLabel(self.carbsFrame)
        self.addedSugarsGramLabel.setObjectName(u"addedSugarsGramLabel")

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.addedSugarsGramLabel)

        self.totalDietaryFiberGLabel = QLabel(self.carbsFrame)
        self.totalDietaryFiberGLabel.setObjectName(u"totalDietaryFiberGLabel")

        self.formLayout_4.setWidget(8, QFormLayout.LabelRole, self.totalDietaryFiberGLabel)

        self.totalSolubleFiberGLabel = QLabel(self.carbsFrame)
        self.totalSolubleFiberGLabel.setObjectName(u"totalSolubleFiberGLabel")

        self.formLayout_4.setWidget(10, QFormLayout.LabelRole, self.totalSolubleFiberGLabel)

        self.monosaccharidesGLabel = QLabel(self.carbsFrame)
        self.monosaccharidesGLabel.setObjectName(u"monosaccharidesGLabel")

        self.formLayout_4.setWidget(12, QFormLayout.LabelRole, self.monosaccharidesGLabel)

        self.disaccharidesGLabel = QLabel(self.carbsFrame)
        self.disaccharidesGLabel.setObjectName(u"disaccharidesGLabel")

        self.formLayout_4.setWidget(14, QFormLayout.LabelRole, self.disaccharidesGLabel)

        self.otherCarbohydratesGLabel = QLabel(self.carbsFrame)
        self.otherCarbohydratesGLabel.setObjectName(u"otherCarbohydratesGLabel")

        self.formLayout_4.setWidget(16, QFormLayout.LabelRole, self.otherCarbohydratesGLabel)

        self.otherCarbohydratesGLineEdit = QLineEdit(self.carbsFrame)
        self.otherCarbohydratesGLineEdit.setObjectName(u"otherCarbohydratesGLineEdit")
        self.otherCarbohydratesGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_4.setWidget(16, QFormLayout.FieldRole, self.otherCarbohydratesGLineEdit)

        self.disaccharidesGLineEdit = QLineEdit(self.carbsFrame)
        self.disaccharidesGLineEdit.setObjectName(u"disaccharidesGLineEdit")
        self.disaccharidesGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_4.setWidget(14, QFormLayout.FieldRole, self.disaccharidesGLineEdit)

        self.monosaccharidesGLineEdit = QLineEdit(self.carbsFrame)
        self.monosaccharidesGLineEdit.setObjectName(u"monosaccharidesGLineEdit")
        self.monosaccharidesGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_4.setWidget(12, QFormLayout.FieldRole, self.monosaccharidesGLineEdit)

        self.totalSolubleFiberGLineEdit = QLineEdit(self.carbsFrame)
        self.totalSolubleFiberGLineEdit.setObjectName(u"totalSolubleFiberGLineEdit")
        self.totalSolubleFiberGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))
        self.totalSolubleFiberGLineEdit.setPlaceholderText('Recommended')

        self.formLayout_4.setWidget(10, QFormLayout.FieldRole, self.totalSolubleFiberGLineEdit)

        self.totalDietaryFiberGLineEdit = QLineEdit(self.carbsFrame)
        self.totalDietaryFiberGLineEdit.setObjectName(u"totalDietaryFiberGLineEdit")
        self.totalDietaryFiberGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))
        self.totalDietaryFiberGLineEdit.setPlaceholderText('Recommended')

        self.formLayout_4.setWidget(8, QFormLayout.FieldRole, self.totalDietaryFiberGLineEdit)

        self.addedSugarsGLineEdit = QLineEdit(self.carbsFrame)
        self.addedSugarsGLineEdit.setObjectName(u"addedSugarsGLineEdit")
        self.addedSugarsGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))
        self.addedSugarsGLineEdit.setPlaceholderText('Recommended')

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.addedSugarsGLineEdit)

        self.totalSugarsGLineEdit = QLineEdit(self.carbsFrame)
        self.totalSugarsGLineEdit.setObjectName(u"totalSugarsGLineEdit")
        self.totalSugarsGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))
        self.totalSugarsGLineEdit.setPlaceholderText('Recommended')

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.totalSugarsGLineEdit)

        self.totalCarbohydratesGLineEdit = QLineEdit(self.carbsFrame)
        self.totalCarbohydratesGLineEdit.setObjectName(u"totalCarbohydratesGLineEdit")
        self.totalCarbohydratesGLineEdit.setPlaceholderText('Required')
        self.totalCarbohydratesGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.totalCarbohydratesGLineEdit)

        self.carbsLabel = QLabel(self.carbsFrame)
        self.carbsLabel.setObjectName(u"carbsLabel")
        self.carbsLabel.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.carbsLabel)


        self.gridLayout_4.addWidget(self.carbsFrame, 0, 0, 1, 1)

        self.fatsFrame = QFrame(self.scrollAreaWidgetContents)
        self.fatsFrame.setObjectName(u"fatsFrame")
        self.fatsFrame.setAutoFillBackground(True)
        self.fatsFrame.setFrameShape(QFrame.StyledPanel)
        self.formLayout_5 = QFormLayout(self.fatsFrame)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_4 = QLabel(self.fatsFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.saturatedFatGLabel = QLabel(self.fatsFrame)
        self.saturatedFatGLabel.setObjectName(u"saturatedFatGLabel")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.saturatedFatGLabel)

        self.totalUnsaturatedFatGLabel = QLabel(self.fatsFrame)
        self.totalUnsaturatedFatGLabel.setObjectName(u"totalUnsaturatedFatGLabel")

        self.formLayout_5.setWidget(6, QFormLayout.LabelRole, self.totalUnsaturatedFatGLabel)

        self.monounsaturatedFatGLabel = QLabel(self.fatsFrame)
        self.monounsaturatedFatGLabel.setObjectName(u"monounsaturatedFatGLabel")

        self.formLayout_5.setWidget(8, QFormLayout.LabelRole, self.monounsaturatedFatGLabel)

        self.polyunsaturatedFatGLabel = QLabel(self.fatsFrame)
        self.polyunsaturatedFatGLabel.setObjectName(u"polyunsaturatedFatGLabel")

        self.formLayout_5.setWidget(10, QFormLayout.LabelRole, self.polyunsaturatedFatGLabel)

        self.transFatGLabel = QLabel(self.fatsFrame)
        self.transFatGLabel.setObjectName(u"transFatGLabel")

        self.formLayout_5.setWidget(12, QFormLayout.LabelRole, self.transFatGLabel)

        self.cholestrolMgLabel = QLabel(self.fatsFrame)
        self.cholestrolMgLabel.setObjectName(u"cholestrolMgLabel")

        self.formLayout_5.setWidget(14, QFormLayout.LabelRole, self.cholestrolMgLabel)

        self.omega3FattyAcidGLabel = QLabel(self.fatsFrame)
        self.omega3FattyAcidGLabel.setObjectName(u"omega3FattyAcidGLabel")

        self.formLayout_5.setWidget(16, QFormLayout.LabelRole, self.omega3FattyAcidGLabel)

        self.omega6FattyAcidGLabel = QLabel(self.fatsFrame)
        self.omega6FattyAcidGLabel.setObjectName(u"omega6FattyAcidGLabel")

        self.formLayout_5.setWidget(18, QFormLayout.LabelRole, self.omega6FattyAcidGLabel)

        self.totalFatGLabel = QLabel(self.fatsFrame)
        self.totalFatGLabel.setObjectName(u"totalFatGLabel")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.totalFatGLabel)

        self.totalFatGLineEdit = QLineEdit(self.fatsFrame)
        self.totalFatGLineEdit.setObjectName(u"totalFatGLineEdit")
        self.totalFatGLineEdit.setPlaceholderText('Required')
        self.totalFatGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.totalFatGLineEdit)

        self.saturatedFatGLineEdit = QLineEdit(self.fatsFrame)
        self.saturatedFatGLineEdit.setObjectName(u"saturatedFatGLineEdit")
        self.saturatedFatGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))
        self.saturatedFatGLineEdit.setPlaceholderText('Recommended')

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.saturatedFatGLineEdit)

        self.totalUnsaturatedFatGLineEdit = QLineEdit(self.fatsFrame)
        self.totalUnsaturatedFatGLineEdit.setObjectName(u"totalUnsaturatedFatGLineEdit")
        self.totalUnsaturatedFatGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))
        self.totalUnsaturatedFatGLineEdit.setPlaceholderText('Recommended')

        self.formLayout_5.setWidget(6, QFormLayout.FieldRole, self.totalUnsaturatedFatGLineEdit)

        self.monounsaturatedFatGLineEdit = QLineEdit(self.fatsFrame)
        self.monounsaturatedFatGLineEdit.setObjectName(u"monounsaturatedFatGLineEdit")
        self.monounsaturatedFatGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_5.setWidget(8, QFormLayout.FieldRole, self.monounsaturatedFatGLineEdit)

        self.polyunsaturatedFatGLineEdit = QLineEdit(self.fatsFrame)
        self.polyunsaturatedFatGLineEdit.setObjectName(u"polyunsaturatedFatGLineEdit")
        self.polyunsaturatedFatGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_5.setWidget(10, QFormLayout.FieldRole, self.polyunsaturatedFatGLineEdit)

        self.transFatGLineEdit = QLineEdit(self.fatsFrame)
        self.transFatGLineEdit.setObjectName(u"transFatGLineEdit")
        self.transFatGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))
        self.transFatGLineEdit.setPlaceholderText('Recommended')

        self.formLayout_5.setWidget(12, QFormLayout.FieldRole, self.transFatGLineEdit)

        self.cholestrolMgLineEdit = QLineEdit(self.fatsFrame)
        self.cholestrolMgLineEdit.setObjectName(u"cholestrolMgLineEdit")
        self.cholestrolMgLineEdit.setPlaceholderText('Recommended')
        self.cholestrolMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_5.setWidget(14, QFormLayout.FieldRole, self.cholestrolMgLineEdit)

        self.omega3FattyAcidGLineEdit = QLineEdit(self.fatsFrame)
        self.omega3FattyAcidGLineEdit.setObjectName(u"omega3FattyAcidGLineEdit")
        self.omega3FattyAcidGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_5.setWidget(16, QFormLayout.FieldRole, self.omega3FattyAcidGLineEdit)

        self.omega6FattyAcidGLineEdit = QLineEdit(self.fatsFrame)
        self.omega6FattyAcidGLineEdit.setObjectName(u"omega6FattyAcidGLineEdit")
        self.omega6FattyAcidGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_5.setWidget(18, QFormLayout.FieldRole, self.omega6FattyAcidGLineEdit)

        self.gridLayout_4.addWidget(self.fatsFrame, 0, 2, 1, 1)

        self.vitaminsFrame = QFrame(self.scrollAreaWidgetContents)
        self.vitaminsFrame.setObjectName(u"vitaminsFrame")
        self.vitaminsFrame.setAutoFillBackground(True)
        self.vitaminsFrame.setInputMethodHints(Qt.ImhDigitsOnly)
        self.vitaminsFrame.setFrameShape(QFrame.StyledPanel)
        self.formLayout_7 = QFormLayout(self.vitaminsFrame)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_5 = QLabel(self.vitaminsFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.vitaminAIUIULabel = QLabel(self.vitaminsFrame)
        self.vitaminAIUIULabel.setObjectName(u"vitaminAIUIULabel")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.vitaminAIUIULabel)

        self.vitaminAREMcgLabel = QLabel(self.vitaminsFrame)
        self.vitaminAREMcgLabel.setObjectName(u"vitaminAREMcgLabel")

        self.formLayout_7.setWidget(4, QFormLayout.LabelRole, self.vitaminAREMcgLabel)

        self.vitaminARAEMcgLabel = QLabel(self.vitaminsFrame)
        self.vitaminARAEMcgLabel.setObjectName(u"vitaminARAEMcgLabel")

        self.formLayout_7.setWidget(6, QFormLayout.LabelRole, self.vitaminARAEMcgLabel)

        self.vitaminB1ThiaminMgLabel = QLabel(self.vitaminsFrame)
        self.vitaminB1ThiaminMgLabel.setObjectName(u"vitaminB1ThiaminMgLabel")

        self.formLayout_7.setWidget(8, QFormLayout.LabelRole, self.vitaminB1ThiaminMgLabel)

        self.vitaminB2RiboflavinMgLabel = QLabel(self.vitaminsFrame)
        self.vitaminB2RiboflavinMgLabel.setObjectName(u"vitaminB2RiboflavinMgLabel")

        self.formLayout_7.setWidget(10, QFormLayout.LabelRole, self.vitaminB2RiboflavinMgLabel)

        self.vitaminB3NiacinMgLabel = QLabel(self.vitaminsFrame)
        self.vitaminB3NiacinMgLabel.setObjectName(u"vitaminB3NiacinMgLabel")

        self.formLayout_7.setWidget(12, QFormLayout.LabelRole, self.vitaminB3NiacinMgLabel)

        self.vitaminB3NiacinEquivMgLabel = QLabel(self.vitaminsFrame)
        self.vitaminB3NiacinEquivMgLabel.setObjectName(u"vitaminB3NiacinEquivMgLabel")

        self.formLayout_7.setWidget(14, QFormLayout.LabelRole, self.vitaminB3NiacinEquivMgLabel)

        self.vitaminB6MgLabel = QLabel(self.vitaminsFrame)
        self.vitaminB6MgLabel.setObjectName(u"vitaminB6MgLabel")

        self.formLayout_7.setWidget(16, QFormLayout.LabelRole, self.vitaminB6MgLabel)

        self.vitaminB12McgLabel = QLabel(self.vitaminsFrame)
        self.vitaminB12McgLabel.setObjectName(u"vitaminB12McgLabel")

        self.formLayout_7.setWidget(18, QFormLayout.LabelRole, self.vitaminB12McgLabel)

        self.vitaminCMgLabel = QLabel(self.vitaminsFrame)
        self.vitaminCMgLabel.setObjectName(u"vitaminCMgLabel")

        self.formLayout_7.setWidget(20, QFormLayout.LabelRole, self.vitaminCMgLabel)

        self.vitaminDIUIULabel = QLabel(self.vitaminsFrame)
        self.vitaminDIUIULabel.setObjectName(u"vitaminDIUIULabel")

        self.formLayout_7.setWidget(22, QFormLayout.LabelRole, self.vitaminDIUIULabel)

        self.vitaminEAlphaTocoMgLabel = QLabel(self.vitaminsFrame)
        self.vitaminEAlphaTocoMgLabel.setObjectName(u"vitaminEAlphaTocoMgLabel")

        self.formLayout_7.setWidget(24, QFormLayout.LabelRole, self.vitaminEAlphaTocoMgLabel)

        self.folateMcgLabel = QLabel(self.vitaminsFrame)
        self.folateMcgLabel.setObjectName(u"folateMcgLabel")

        self.formLayout_7.setWidget(26, QFormLayout.LabelRole, self.folateMcgLabel)

        self.folateDFEMcgDFELabel = QLabel(self.vitaminsFrame)
        self.folateDFEMcgDFELabel.setObjectName(u"folateDFEMcgDFELabel")

        self.formLayout_7.setWidget(28, QFormLayout.LabelRole, self.folateDFEMcgDFELabel)

        self.vitaminKMcgLabel = QLabel(self.vitaminsFrame)
        self.vitaminKMcgLabel.setObjectName(u"vitaminKMcgLabel")

        self.formLayout_7.setWidget(30, QFormLayout.LabelRole, self.vitaminKMcgLabel)

        self.panothenicAcidMgLabel = QLabel(self.vitaminsFrame)
        self.panothenicAcidMgLabel.setObjectName(u"panothenicAcidMgLabel")

        self.formLayout_7.setWidget(32, QFormLayout.LabelRole, self.panothenicAcidMgLabel)

        self.vitaminAIUIULineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminAIUIULineEdit.setObjectName(u"vitaminAIUIULineEdit")
        self.vitaminAIUIULineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.vitaminAIUIULineEdit)

        self.vitaminAREMcgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminAREMcgLineEdit.setObjectName(u"vitaminAREMcgLineEdit")
        self.vitaminAREMcgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_7.setWidget(4, QFormLayout.FieldRole, self.vitaminAREMcgLineEdit)

        self.vitaminARAEMcgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminARAEMcgLineEdit.setObjectName(u"vitaminARAEMcgLineEdit")

        self.formLayout_7.setWidget(6, QFormLayout.FieldRole, self.vitaminARAEMcgLineEdit)

        self.vitaminB1ThiaminMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB1ThiaminMgLineEdit.setObjectName(u"vitaminB1ThiaminMgLineEdit")
        self.vitaminB1ThiaminMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_7.setWidget(8, QFormLayout.FieldRole, self.vitaminB1ThiaminMgLineEdit)

        self.vitaminB2RiboflavinMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB2RiboflavinMgLineEdit.setObjectName(u"vitaminB2RiboflavinMgLineEdit")
        self.vitaminB2RiboflavinMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_7.setWidget(10, QFormLayout.FieldRole, self.vitaminB2RiboflavinMgLineEdit)

        self.vitaminB3NiacinMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB3NiacinMgLineEdit.setObjectName(u"vitaminB3NiacinMgLineEdit")
        self.vitaminB3NiacinMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_7.setWidget(12, QFormLayout.FieldRole, self.vitaminB3NiacinMgLineEdit)

        self.vitaminB3NiacinEquivMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB3NiacinEquivMgLineEdit.setObjectName(u"vitaminB3NiacinEquivMgLineEdit")
        self.vitaminB3NiacinEquivMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_7.setWidget(14, QFormLayout.FieldRole, self.vitaminB3NiacinEquivMgLineEdit)

        self.vitaminB6MgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB6MgLineEdit.setObjectName(u"vitaminB6MgLineEdit")
        self.vitaminB6MgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_7.setWidget(16, QFormLayout.FieldRole, self.vitaminB6MgLineEdit)

        self.vitaminB12McgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB12McgLineEdit.setObjectName(u"vitaminB12McgLineEdit")
        self.vitaminB12McgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_7.setWidget(18, QFormLayout.FieldRole, self.vitaminB12McgLineEdit)

        self.vitaminCMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminCMgLineEdit.setObjectName(u"vitaminCMgLineEdit")
        self.vitaminCMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_7.setWidget(20, QFormLayout.FieldRole, self.vitaminCMgLineEdit)

        self.vitaminDIUIULineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminDIUIULineEdit.setObjectName(u"vitaminDIUIULineEdit")
        self.vitaminDIUIULineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_7.setWidget(22, QFormLayout.FieldRole, self.vitaminDIUIULineEdit)

        self.vitaminEAlphaTocoMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminEAlphaTocoMgLineEdit.setObjectName(u"vitaminEAlphaTocoMgLineEdit")
        self.vitaminEAlphaTocoMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_7.setWidget(24, QFormLayout.FieldRole, self.vitaminEAlphaTocoMgLineEdit)

        self.folateMcgLineEdit = QLineEdit(self.vitaminsFrame)
        self.folateMcgLineEdit.setObjectName(u"folateMcgLineEdit")
        self.folateMcgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_7.setWidget(26, QFormLayout.FieldRole, self.folateMcgLineEdit)

        self.folateDFEMcgDFELineEdit = QLineEdit(self.vitaminsFrame)
        self.folateDFEMcgDFELineEdit.setObjectName(u"folateDFEMcgDFELineEdit")
        self.folateDFEMcgDFELineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_7.setWidget(28, QFormLayout.FieldRole, self.folateDFEMcgDFELineEdit)

        self.vitaminKMcgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminKMcgLineEdit.setObjectName(u"vitaminKMcgLineEdit")
        self.vitaminKMcgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_7.setWidget(30, QFormLayout.FieldRole, self.vitaminKMcgLineEdit)

        self.panothenicAcidMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.panothenicAcidMgLineEdit.setObjectName(u"panothenicAcidMgLineEdit")
        self.panothenicAcidMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_7.setWidget(32, QFormLayout.FieldRole, self.panothenicAcidMgLineEdit)


        self.gridLayout_4.addWidget(self.vitaminsFrame, 2, 2, 1, 1)

        self.proteinsFrame = QFrame(self.scrollAreaWidgetContents)
        self.proteinsFrame.setObjectName(u"proteinsFrame")
        self.proteinsFrame.setAutoFillBackground(True)
        self.proteinsFrame.setFrameShape(QFrame.StyledPanel)
        self.formLayout_2 = QFormLayout(self.proteinsFrame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.proteinsFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.totalProteinGLabel = QLabel(self.proteinsFrame)
        self.totalProteinGLabel.setObjectName(u"totalProteinGLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.totalProteinGLabel)

        self.totalProteinGLineEdit = QLineEdit(self.proteinsFrame)
        self.totalProteinGLineEdit.setObjectName(u"totalProteinGLineEdit")
        self.totalProteinGLineEdit.setAlignment(Qt.AlignCenter)
        self.totalProteinGLineEdit.setPlaceholderText('Required')
        self.totalProteinGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.totalProteinGLineEdit)


        self.gridLayout_4.addWidget(self.proteinsFrame, 1, 2, 1, 1)

        self.otherNutrientsFrame = QFrame(self.scrollAreaWidgetContents)
        self.otherNutrientsFrame.setObjectName(u"otherNutrientsFrame")
        self.otherNutrientsFrame.setAutoFillBackground(True)
        self.otherNutrientsFrame.setFrameShape(QFrame.StyledPanel)

        self.formLayout_3 = QFormLayout(self.otherNutrientsFrame)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.caloriesKCalLabel = QLabel(self.otherNutrientsFrame)
        self.caloriesKCalLabel.setObjectName(u"caloriesKCalLabel")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.caloriesKCalLabel)

        self.moistureGLabel = QLabel(self.otherNutrientsFrame)
        self.moistureGLabel.setObjectName(u"moistureGLabel")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.moistureGLabel)

        self.caffeineMgLabel = QLabel(self.otherNutrientsFrame)
        self.caffeineMgLabel.setObjectName(u"caffeineMgLabel")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.caffeineMgLabel)

        self.cholineMgLabel = QLabel(self.otherNutrientsFrame)
        self.cholineMgLabel.setObjectName(u"cholineMgLabel")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.cholineMgLabel)

        self.alcoholGLabel = QLabel(self.otherNutrientsFrame)
        self.alcoholGLabel.setObjectName(u"alcoholGLabel")

        self.formLayout_3.setWidget(9, QFormLayout.LabelRole, self.alcoholGLabel)

        self.sugarAlcoholGLabel = QLabel(self.otherNutrientsFrame)
        self.sugarAlcoholGLabel.setObjectName(u"sugarAlcoholGLabel")

        self.formLayout_3.setWidget(11, QFormLayout.LabelRole, self.sugarAlcoholGLabel)

        self.caloriesKCalLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.caloriesKCalLineEdit.setObjectName(u"caloriesKCalLineEdit")
        self.caloriesKCalLineEdit.setPlaceholderText('Required')
        self.caloriesKCalLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.caloriesKCalLineEdit)

        self.moistureGLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.moistureGLineEdit.setObjectName(u"moistureGLineEdit")
        self.moistureGLineEdit.setPlaceholderText('Recommended')
        self.moistureGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.moistureGLineEdit)

        self.caffeineMgLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.caffeineMgLineEdit.setObjectName(u"caffeineMgLineEdit")
        self.caffeineMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.caffeineMgLineEdit)

        self.cholineMgLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.cholineMgLineEdit.setObjectName(u"cholineMgLineEdit")
        self.cholineMgLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.cholineMgLineEdit)

        self.alcoholGLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.alcoholGLineEdit.setObjectName(u"alcoholGLineEdit")
        self.alcoholGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_3.setWidget(9, QFormLayout.FieldRole, self.alcoholGLineEdit)

        self.sugarAlcoholGLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.sugarAlcoholGLineEdit.setObjectName(u"sugarAlcoholGLineEdit")
        self.sugarAlcoholGLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))

        self.formLayout_3.setWidget(11, QFormLayout.FieldRole, self.sugarAlcoholGLineEdit)

        self.label_6 = QLabel(self.otherNutrientsFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.gridLayout_4.addWidget(self.otherNutrientsFrame, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.addIngredientTabWidget.addTab(self.nutritionalsTab, "")
        self.documentationTab = QWidget()
        self.documentationTab.setObjectName(u"documentationTab")
        self.verticalLayout_7 = QVBoxLayout(self.documentationTab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.addIngredientSpecificDocumentsLabel = QLabel(self.documentationTab)
        self.addIngredientSpecificDocumentsLabel.setObjectName(u"addIngredientSpecificDocumentsLabel")
        self.addIngredientSpecificDocumentsLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.addIngredientSpecificDocumentsLabel)

        self.filesToBeUploadedLabel = QLabel(self.documentationTab)
        self.filesToBeUploadedLabel.setObjectName(u"filesToBeUploadedLabel")
        self.filesToBeUploadedLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.filesToBeUploadedLabel)

        self.filesToBeUploadedTableWidget = QTableWidget(self.documentationTab)
        if (self.filesToBeUploadedTableWidget.columnCount() < 3):
            self.filesToBeUploadedTableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.filesToBeUploadedTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.filesToBeUploadedTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.filesToBeUploadedTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.filesToBeUploadedTableWidget.setObjectName(u"filesToBeUploadedTableWidget")
        self.filesToBeUploadedTableWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.filesToBeUploadedTableWidget.setShowGrid(True)
        self.filesToBeUploadedTableWidget.setColumnCount(3)
        self.filesToBeUploadedTableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.filesToBeUploadedTableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.filesToBeUploadedTableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_7.addWidget(self.filesToBeUploadedTableWidget)

        self.widget_2 = QWidget(self.documentationTab)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.browseForFileBtn = QPushButton(self.widget_2)
        self.browseForFileBtn.setObjectName(u"browseForFileBtn")

        self.horizontalLayout_3.addWidget(self.browseForFileBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.removeFromTableBtn = QPushButton(self.widget_2)
        self.removeFromTableBtn.setObjectName(u"removeFromTableBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.removeFromTableBtn.sizePolicy().hasHeightForWidth())
        self.removeFromTableBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.removeFromTableBtn)

        self.clearAllFromTableBtn = QPushButton(self.widget_2)
        self.clearAllFromTableBtn.setObjectName(u"clearAllFromTableBtn")

        self.horizontalLayout_3.addWidget(self.clearAllFromTableBtn)


        self.verticalLayout_7.addWidget(self.widget_2)

        self.addIngredientTabWidget.addTab(self.documentationTab, "")
        self.groupsTab = QWidget()
        self.groupsTab.setObjectName(u"groupsTab")
        self.verticalLayout_6 = QVBoxLayout(self.groupsTab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.groupListLabel = QLabel(self.groupsTab)
        self.groupListLabel.setText("Check the categories that pertain to this ingredient")
        self.verticalLayout_6.addWidget(self.groupListLabel)
        self.groupListWidget = QListWidget(self.groupsTab)
        self.groupListWidget.setObjectName(u"groupListWidget")

        
        self.verticalLayout_6.addWidget(self.groupListWidget)

        self.addIngredientTabWidget.addTab(self.groupsTab, "")
        self.costTab = QWidget()
        self.costTab.setObjectName(u"costTab")
        self.verticalLayout_5 = QVBoxLayout(self.costTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.costTableWidget = QTableWidget(self.costTab)
        self.costTableWidget.setObjectName(u"costTableWidget")

        self.verticalLayout_5.addWidget(self.costTableWidget)

        self.addIngredientTabWidget.addTab(self.costTab, "")

        self.gridLayout.addWidget(self.addIngredientTabWidget, 0, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(addIngredientDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy3)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)
        self.retranslateUi(addIngredientDialog)
        self.buttonBox.accepted.connect(addIngredientDialog.accept)
        self.buttonBox.rejected.connect(addIngredientDialog.reject)

        ### CHANGES BEYOND QT ###############<--------------------------------------------
        self.addIngredientTabWidget.setCurrentIndex(0)
        self.percentYieldDoubleSpinBox.setValue(100)

        ### sets tab order 
        self.setTabOrder(self.totalCarbohydratesGLineEdit, self.totalSugarsGLineEdit)
        self.setTabOrder(self.totalSugarsGLineEdit, self.addedSugarsGLineEdit)
        self.setTabOrder(self.addedSugarsGLineEdit, self.totalDietaryFiberGLineEdit)
        self.setTabOrder(self.totalDietaryFiberGLineEdit, self.totalSolubleFiberGLineEdit)
        self.setTabOrder(self.totalSolubleFiberGLineEdit, self.monosaccharidesGLineEdit)
        self.setTabOrder(self.monosaccharidesGLineEdit, self.disaccharidesGLineEdit)
        self.setTabOrder(self.disaccharidesGLineEdit, self.otherCarbohydratesGLineEdit)
        self.setTabOrder(self.otherCarbohydratesGLineEdit, self.totalFatGLineEdit)
        self.setTabOrder(self.omega6FattyAcidGLineEdit, self.caloriesKCalLineEdit)
        self.setTabOrder(self.sugarAlcoholGLineEdit, self.totalProteinGLineEdit)
        self.setTabOrder(self.totalProteinGLineEdit, self.calciumMgLineEdit)
        self.setTabOrder(self.zincMgLineEdit ,self.vitaminAIUIULineEdit)

        # adds suggestions to input fields
        
        #self.buttonBox.accepted.connect(addIngredientDialog.accept)
    
        QMetaObject.connectSlotsByName(addIngredientDialog)
        # setupUi
    
    def setupLogic(self):

        # sets up signals
        self.browseForFileBtn.clicked.connect(lambda: self.browseFiles()) # lambda might not be right for this
        self.clearAllFromTableBtn.clicked.connect(lambda: self.filesToBeUploadedTableWidget.setRowCount(0)) # lambda might not be right for this
        self.vitaminAIUIULineEdit.textChanged.connect(self.toggleVitA) 
        self.vitaminAREMcgLineEdit.textChanged.connect(self.toggleVitA)
        self.vitaminARAEMcgLineEdit.textChanged.connect(self.toggleVitA)

        self.folateDFEMcgDFELineEdit.textChanged.connect(self.toggleFolate)
        self.folateMcgLineEdit.textChanged.connect(self.toggleFolate)

        # sets up autocompletion for user input 
        # VV adds suggestions for suppliers to general tab supplier box VV 
        with dbConnection('FormulaSchema').cursor() as cursor:
            cursor.execute('SELECT supplier_id, supplier_name FROM supplier')
            suppliers = cursor.fetchall()
            model = QStandardItemModel()
            completer = QCompleter()
            for supplier in suppliers:
                supplierItem = QStandardItem()
                name = str(supplier['supplier_name']).capitalize()
                supplierItem.setData(supplier, Qt.UserRole)
                supplierItem.setText(name)
                model.appendRow(supplierItem)
            completer.setModel(model)
            self.supplierComboBox.setCompleter(completer)
            self.supplierComboBox.setModel(model)
            self.supplierComboBox.setCurrentIndex(-1)

        # adds suggestions/autocomplete to common name line input box 
        with dbConnection('FormulaSchema').cursor() as cursor:
            cursor.execute('SELECT food_id, food_desc FROM food')
            cNameRows = cursor.fetchall()
            completer = QCompleter()
            completer.setCaseSensitivity(Qt.CaseInsensitive)
            completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
            completer.setMaxVisibleItems(10)
            model = QStandardItemModel()
            for cName in cNameRows:
                cNameItem = QStandardItem()
                cNameItem.setText(cName['food_desc'])
                cNameItem.setData(cName, Qt.UserRole)
                model.appendRow(cNameItem)
            completer.setModel(model)
            self.ingNameLineEdit.setCompleter(completer)

        # adds categories to categories list widgete
        with dbConnection('FormulaSchema').cursor() as cursor:
            self.categories = [{}]
            cursor.execute("SELECT category_name, category_id FROM category")
            for row in cursor.fetchall(): 
                category = str.title(row['category_name'])
                item = QListWidgetItem(category)
                item.setData(1, row['category_id']) # < not sure about the role, want to change to qt user role but not sure hwo it affects dependencies
                item.setFlags(item.flags()| Qt.ItemIsUserCheckable)
                item.setCheckState(Qt.Unchecked)
                self.groupListWidget.addItem(item)
            self.groupListWidget.sortItems(Qt.AscendingOrder)

    # clears all files from table
    def clearContentsWrapper(self): 
        self.filesToBeUploadedTableWidget.clearContents()

    # called when OK button pushed
    def accepted(self):
        self.accepted.connect(lambda: self.formSubmit())
        #self.rejected.connect(lambda: self.cancelEvent())
        #self.buttonBox.Box.rejected.connect(Ui_addIngredientDialog.rejected)

    # called when cancel button pushed
    #TODO
    def rejected(self):
        toClose = QMessageBox.question(self, "Confirm cancellation", "Are you sure you would like to cancel?", QMessageBox.Yes | QMessageBox.No)
        if toClose == QMessageBox.Yes:
            self.rejected.connect(addIngredientDialog.rejected)
        else:
            pass

    # opens file browsing dialog. Adds selected to upload table
    def browseFiles(self):
        self.fileNavigator = QFileDialog()
        self.fileNavigator.setFileMode(QFileDialog.AnyFile)
        self.fileNavigator.setFilter(QDir.Files)

        if self.fileNavigator.exec_(): 
            files = self.fileNavigator.selectedFiles()
            for file in files: 
                self.filesToBeUploadedTableWidget.insertRow(self.filesToBeUploadedTableWidget.rowCount())
                self.filesToBeUploadedTableWidget.setItem(self.filesToBeUploadedTableWidget.rowCount() - 1, 2, QTableWidgetItem(file))
                fileName = os.path.basename(file)
                date = datetime.now().date()
                self.filesToBeUploadedTableWidget.setItem(self.filesToBeUploadedTableWidget.rowCount() - 1, 0, QTableWidgetItem(fileName))
                self.filesToBeUploadedTableWidget.setItem(self.filesToBeUploadedTableWidget.rowCount() - 1, 1, QTableWidgetItem(str(date)))
        else:
            pass

    # called when submitting the form 
    def formSubmit(self):
        validated = self.validateNutrients()
        if not validated:
            return

        # validates successful connection with the database
        try:
            db = dbConnection('FormulaSchema')
        except ConnectionError:
            msg = QMessageBox()
            msg.setText('Connection to database unsuccessful. Please try again')
            msg.exec_()
            return
        else:
            # if database connection is successful, ensures all queries are valid and that all information gets added to database at the same time
            try: 
                with db.cursor() as cursor:
                    ingDesc = self.ingDescLineEdit.text()
                    # validates that user puts an ingredient description 
                    if not ingDesc:
                        msg = QMessageBox()
                        msg.setText('Must input an ingredient description on tab 1')
                        msg.exec_()
                        return
                    
                    # SUPPLIER #####
                    # validates that a supplier was inputted into combo box
                    if self.supplierComboBox.currentText():
                        supplierItem = self.supplierComboBox.currentData(Qt.UserRole)
                        if not supplierItem:# < probably need to doublecheck this
                            supplier = self.supplierComboBox.currentText()
                            cursor.execute('INSERT IGNORE INTO supplier(supplier_name) VALUES (%s)', (supplier,))
                            supplierID = db.insert_id()
                        elif supplierItem:
                            supplierID = supplierItem['supplier_id']
                            supplier = supplierItem['supplier_name']
                        
                        foodName = self.ingNameLineEdit.text()
                        itemCode = self.supplierIngredientNumberLineEdit.text()
                        ingStatement = self.ingredientStatementLineEdit.text()

                        cursor.execute('INSERT INTO supplier_food (food_id, specific_name, supplier_id, supplier_ing_item_code, ing_statement) VALUES (%s, %s, %s, %s, %s)', (foodID, foodName, itemCode, ingStatement))

                    percentYield = self.percentYieldDoubleSpinBox.value()

                    # FOOD GENERAL
                    # Adds the ingredient into database if the supplier_id and item code as a pair don't already exist in the database. If they do, finds the ingredient id and stores as lastIngID
                    ingRepeats = cursor.execute('SELECT food.food_id, food.food_desc, food.food_notes, supplier.supplier_id, supplier.supplier_name FROM food INNER JOIN supplier_food ON supplier_food.food_id = food.food_id INNER JOIN supplier ON supplier.supplier_id = supplier_food.supplier_id WHERE food.food_desc = (%s) AND supplier.supplier_id = (%s)', (ingDesc, supplierID))
                    repeatData = cursor.fetchall()

                    # if unique food based on food_desc AND supplier_id
                    if ingRepeats == 0:
                        cursor.execute('INSERT IGNORE INTO food(food_desc, food_notes, user_inputted, input_date) VALUES (%s, %s, %s, %s)', (ingDesc, self.notesLineEdit.text(), 1, date.today()))
                        foodID = db.insert_id()
                    else: 
                        foodID = repeatData[0]['food_id']
                        # could make this fetch all instead and have popup window for user to choose

                    # ALLERGENS inputs allergens  {'allergen': 'Dairy', 'id': 1, 'object': self.dairyCheckbox},
                    for allergen in self.allergenMap:
                        input = allergen['object']
                        if input.isChecked(): 
                            cursor.execute("INSERT INTO ing_allergens(ing_id, allergen) VALUES (%s, %s)", (foodID, allergen['allergen']))
                    
                    # CLAIMS inputs claims into database
                    for claim in self.claimMap:
                        box = claim['object']
                        if box.isChecked():
                            cursor.execute('INSERT INTO food_claim (food_id, claim) VALUES (%s, %s)', (foodID, claim['claim']))

                    # NUTRIENTS 
                    for nutrient in self.nutrientMap:
                        if nutrient['value']:
                            try:
                                value = float(nutrient['value'])
                                nutrientID = nutrient['nutrient_id']
                                factor = nutrient['factor']
                            except:
                                msg = QMessageBox()
                                msg.setText('Value for {} on nutritional tab is not in numerical format'.format(nutrient['nutrient_name']))
                                msg.exec_()
                                return
                            else:
                                weight = value * factor
                                cursor.execute('INSERT INTO food_nutrient (food_id, nutrient_id, nutrient_weight) VALUES (%s, %s, %s)', (foodID, nutrientID, weight))


                    # DOCUMENTS 
                    # NOT SURE IF TODO
                    '''for row in range(self.filesToBeUploadedTableWidget.rowCount()):
                        fileName = self.filesToBeUploadedTableWidget.itemAt(row, 0).text()
                        dateInputted = date.today()
                        filePath = self.filesToBeUploadedTableWidget.itemAt(row, 2).text()
                        cursor.execute('INSERT IGNORE INTO food_doc(food_id, doc_name, doc_file, upload_datetime) VALUES (%s, %s, %s, %s), (foodID, fileName, filePath, dateInputted))
                        
                    for row in range(self.groupListWidget.count()):
                        item = self.groupListWidget.item(row)
                        if item.checkState(Qt.Checked):
                            catID = self.groupListWidget.item(row).data(1)
                            cursor.execute('INSERT INTO food_category (food_id, category_id), (foodID, catID))'''
                        
            except ConnectionAbortedError:
                msg = QMessageBox()
                msg.setText('Something went wrong. Food ingredient was not added to database')
                msg.exec_()
                return
            else:
                # if data successfully inputted 
                ############>>>> cursor.commit() #<<<------- uncomment to make official
                msg = QMessageBox()
                msg.setText('Successfully added food ingredient to database')
                msg.exec_()
                # return?
    
    # ensures user does not input more than one measure for vitamin A
    def toggleVitA(self):

        if self.vitaminAIUIULineEdit.text() != '':
            self.vitaminARAEMcgLineEdit.setEnabled(False)
            self.vitaminARAEMcgLineEdit.setPlaceholderText('Disabled')
            self.vitaminAREMcgLineEdit.setEnabled(False)
            self.vitaminAREMcgLineEdit.setPlaceholderText('Disabled')
        elif self.vitaminARAEMcgLineEdit.text() != '':
            self.vitaminAIUIULineEdit.setEnabled(False)
            self.vitaminAIUIULineEdit.setPlaceholderText('Disabled')
            self.vitaminAREMcgLineEdit.setEnabled(False)
            self.vitaminAREMcgLineEdit.setPlaceholderText('Disabled')
        elif self.vitaminAREMcgLineEdit.text() != '':
            self.vitaminAIUIULineEdit.setEnabled(False)
            self.vitaminAIUIULineEdit.setPlaceholderText('Disabled')
            self.vitaminARAEMcgLineEdit.setEnabled(False)
            self.vitaminARAEMcgLineEdit.setPlaceholderText('Disabled')
        else:
            self.vitaminAIUIULineEdit.setEnabled(True)
            self.vitaminAIUIULineEdit.setPlaceholderText('')
            self.vitaminARAEMcgLineEdit.setEnabled(True)
            self.vitaminARAEMcgLineEdit.setPlaceholderText('')
            self.vitaminAREMcgLineEdit.setEnabled(True)
            self.vitaminAREMcgLineEdit.setPlaceholderText('')
    
    # ensures user does not input more than one measure for folate
    def toggleFolate(self):
        if self.folateDFEMcgDFELineEdit.text() != '':
            self.folateMcgLineEdit.setEnabled(False)
            self.folateMcgLineEdit.setPlaceholderText('Disabled')
        elif self.folateMcgLineEdit.text() != '':
            self.folateDFEMcgDFELineEdit.setEnabled(False)
            self.folateDFEMcgDFELineEdit.setPlaceholderText('Disabled')
        else:
            self.folateDFEMcgDFELineEdit.setEnabled(True)
            self.folateDFEMcgDFELineEdit.setPlaceholderText('')
            self.folateMcgLineEdit.setEnabled(True)
            self.folateMcgLineEdit.setPlaceholderText('')

    def validateNutrients(self):
        # required inputs are calories, total fat, total protein, total carbs 

        # NOTE
        # omega3 + omega6 is a polyunsat fat 
        # sugar alcohols are not considered carbs
        # sugars are monosaccharides and disaccharides

        carbs = self.totalCarbohydratesGLineEdit.text()
        fats = self.totalFatGLineEdit.text()
        proteins = self.totalFatGLineEdit.text()
        calories = self.caloriesKCalLineEdit.text()
        alcohol = self.alcoholGLineEdit.text()
        sugarAlcohols = self.sugarAlcoholGLineEdit.text()
        water = self.moistureGLineEdit.text()
        totalSugar = self.totalSugarsGLineEdit.text()
        addedSugar = self.addedSugarsGLineEdit.text()
        totalDietaryFiber = self.totalDietaryFiberGLineEdit.text()
        totalSolubleFiber = self.totalSolubleFiberGLineEdit.text()
        monosaccharides = self.monosaccharidesGLineEdit.text()
        disaccharides = self.disaccharidesGLineEdit.text()
        otherCarbs = self.otherCarbohydratesGLineEdit.text()
        totalUnsatFat = self.totalUnsaturatedFatGLineEdit.text()
        totalSatFat = self.saturatedFatGLineEdit.text()
        monounsatFat = self.monounsaturatedFatGLineEdit.text()
        polyunsatFat = self.polyunsaturatedFatGLineEdit.text()
        transFat = self.transFatGLineEdit.text()
        omega3 = self.omega3FattyAcidGLineEdit.text()
        omega6 = self.omega6FattyAcidGLineEdit.text()

        # water
        if water != '':
            water = float(water)
        else:
            water = 0
        # alcohol
        if alcohol != '':
            alcohol = float(alcohol)
        else:
            alcohol = 0
        # sugar alcohol
        if sugarAlcohols != '':
            sugarAlcohols = float(sugarAlcohols)
        else:
            sugarAlcohols = 0
        # total sugar
        if totalSugar != '':
            totalSugar = float(totalSugar)
        else:
            totalSugar = 0
        # added sugar
        if addedSugar != '':
            addedSugar = float(addedSugar)
        else:
            addedSugar = 0
        # total dietary fiber
        if totalDietaryFiber != '':
            totalDietaryFiber = float(totalDietaryFiber)
        else:
            totalDietayrFiber = 0
        # total soluble fiber
        if totalSolubleFiber != '':
            totalSolubleFiber = float(totalSolubleFiber)
        else:
            totalSolubleFiber = 0
        # monosaccharides
        if monosaccharides != '':
            monosaccharides = float(monosaccharides)
        else:
            monosaccharides = 0
        # disaccharides
        if disaccharides != '':
            disaccharides = float(disaccharides)
        else:
            disaccharides = 0
        # other carbs
        if otherCarbs != '':
            otherCarbs = float(otherCarbs)
        else:
            otherCarbs = 0
        # total unsaturated fat 
        if totalUnsatFat != '':
            totalUnsatFat = float(totalUnsatFat)
        else:
            totalUnsatFat = 0
        # total saturated fat 
        if totalSatFat != '':
            totalSatFat = float(totalSatFat)
        else:
            totalSatFat = 0
        # monounsaturated fats
        if monounsatFat != '':
            monounsatFat = float(monounsatFat)
        else:
            monounsatFat = 0
        # polyunsaturated fats
        if polyunsatFat != '':
            polyunsatFat = float(polyunsatFat)
        else:
            polyunsatFat = 0   
        # trans fat 
        if transFat != '':
            transFat = float(transFat)
        else:
            transFat = 0
        # omega 3
        if omega3 != '':
            omega3 = float(omega3)
        else:
            omega3 = 0
        # omega 6 
        if omega6 != '':
            omega6 = float(omega6)
        else:
            omega6 = 0


        # validates the mandatory inputs
        if carbs != '':
            carbs = float(carbs)
        else:
            msg = QMessageBox()
            msg.setText('Input required in total carbohydates box on nutritionals tab')
            self.totalCarbohydratesGLineEdit.setFocus()
            msg.exec_()
            return False
        if fats != '':
            fats = float(fats)
        else:
            msg = QMessageBox()
            msg.setText('Input required in total fats box on nutritionals tab')
            self.totalFatGLineEdit.setFocus()
            msg.exec_()
            return False
        if proteins != '':
            proteins = float(proteins)
        else:
            msg = QMessageBox()
            msg.setText('Input required in total proteins box on nutritionals tab')
            self.totalProteinGLineEdit.setFocus()
            msg.exec_()
            return False
        if calories != '':
            calories = float(calories)
        else:
            msg = QMessageBox()
            msg.setText('Input required in calories box on nutritionals tab')
            self.caloriesKCalLineEdit.setFocus()
            msg.exec_()
            return False
            


        # Logic
        # checks that calories are validated in relation to major calorie-contributing nutrients
        if (proteins * 4) + (fats * 9) + (carbs * 4) + (alcohol * 7) + (sugarAlcohols * 4) > calories:
            msg = QMessageBox()
            msg.setText('Calories are lower than expected given entered macronutrients')
            self.caloriesKCalLineEdit.setFocus()
            msg.exec_()
            return False

        # checkse that nutrient weights are validated in relation to per-weight
        perWeight = self.perGramsSpinBox.value()
        if proteins + fats + carbs + alcohol + sugarAlcohols + water > perWeight:
            msg = QMessageBox()
            msg.setText('Invalid input. Nutrient weights are greater than the reference weight')
            self.perGramsSpinBox.setFocus()
            msg.exec_()
            return False 
         
        # if added sugars are higher than total sugar
        if addedSugar > totalSugar and totalSugar != 0:
            msg = QMessageBox()
            msg.setText('Added sugar cannot be greater than the total sugar')
            self.totalSugarsGLineEdit.setFocus()
            msg.exec_()
            return False
        
        # checks mono/disaccharide inconsistency with total sugar if total sugar is inputted
        if monosaccharides + disaccharides > totalSugar and totalSugar != 0:
            msg = QMessageBox()
            msg.setText('The total sugar content cannot be less than the sum of monosaaccharide and disaccharide content')
            self.totalSugarsGLineEdit.setFocus()
            msg.exec_()
            return False
        
        # checks all carbs in relation to total carbs
        if max(totalSugar, monosaccharides + disaccharides) + totalDietaryFiber + totalSolubleFiber + otherCarbs > carbs:
            msg = QMessageBox()
            msg.setText('Inputted carbohydrates are greater than the total carbohydrates')
            msg.exec_()
            return False

        # checks polyunsaturated fats are not inconsistent
        if omega3 + omega6 > polyunsatFat and polyunsatFat != 0:
            msg = QMessageBox()
            msg.setText('Inconsistent input for polyunsaturated fat. Omega-3 and Omega-6 are higher than the total')
            self.totalUnsaturatedFatGLineEdit.setFocus()
            msg.exec_()
            return False

        # checks that total unsaturated fat isnt lower than sum of constituents
        if monounsatFat + polyunsatFat > totalUnsatFat and totalUnsatFat != 0:
            msg = QMessageBox()
            msg.setText('Inconsistent input for unsaturated fats. Monunsaturated and Polyunsaturated fat content cannot be higher than the total Unsaturated Fat Content')
            self.totalUnsaturatedFatGLineEdit.setFocus()
            msg.exec_()
            return False
        
        # checks that total fat is not less than sum of its constituents 
        if totalSatFat + max(totalUnsatFat, monounsatFat + polyunsatFat, monounsatFat + omega3 + omega6) + transFat > fats:
            msg = QMessageBox()
            msg.setText('Total fats cannot be less than the sum of the inputted fats')
            msg.exec_()
            return False
        
        # returns True if all error checking has passed 
        return True
        
    def retranslateUi(self, addIngredientDialog):
        self.ingDescLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Ingredient Description", None))
        self.ingNameLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Specific Name", None))
        self.ingNameLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Common Name (if applicable)", None))
        self.ingNameLineEdit.setPlaceholderText(QCoreApplication.translate("addIngredientDialog", u"ie. Cellulose Gum", None))
        self.supplierLabel_2.setText(QCoreApplication.translate("addIngredientDialog", u"Supplier (if applicable)", None))
        self.supplierIngIDLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Supplier Ingredient Number (if applicable)", None))
        self.percentYieldIfApplicableLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Percent Yield (if applicable)", None))
        self.supplierLabel.setText("")
        self.ingredientStatementLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Ingredient Statement", None))
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
        self.optionalLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Optional", None))
        self.perLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Per ", None))
        self.gramsLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Grams", None))
        self.checkDataBtn.setText(QCoreApplication.translate("addIngredientDialog", u"Check Data", None))
        self.generateNFPPushBtn.setText(QCoreApplication.translate("addIngredientDialog", u"Generate NFP", None))
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
        self.label_4.setText(QCoreApplication.translate("addIngredientDialog", u"Fats", None))
        self.saturatedFatGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Total Saturated Fat (g)", None))
        self.totalUnsaturatedFatGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Total Unsaturated Fat (g)", None))
        self.monounsaturatedFatGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Monounsaturated Fat (g)", None))
        self.polyunsaturatedFatGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Polyunsaturated Fat (g)", None))
        self.transFatGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Trans Fat (g)", None))
        self.cholestrolMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Cholestrol (mg)", None))
        self.omega3FattyAcidGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Omega 3 Fatty Acid (g)", None))
        self.omega6FattyAcidGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Omega 6 Fatty Acid (g)", None))
        self.totalFatGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Total Fat (g)", None))
        self.label_5.setText(QCoreApplication.translate("addIngredientDialog", u"Vitamins", None))
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
        self.panothenicAcidMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Vitamin B5/Panothenic Acid (mg)", None))
        self.label_2.setText(QCoreApplication.translate("addIngredientDialog", u"Proteins", None))
        self.totalProteinGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Total Protein (g)", None))
        self.caloriesKCalLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Calories (kCal)", None))
        self.moistureGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Moisture (g)", None))
        self.caffeineMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Caffeine (mg)", None))
        self.cholineMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Choline (mg)", None))
        self.alcoholGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Alcohol (g)", None))
        self.sugarAlcoholGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Sugar Alcohol (g)", None))
        self.label_6.setText(QCoreApplication.translate("addIngredientDialog", u"Other Nutrients", None))
        self.addIngredientTabWidget.setTabText(self.addIngredientTabWidget.indexOf(self.nutritionalsTab), QCoreApplication.translate("addIngredientDialog", u"Nutritionals", None))
        self.addIngredientSpecificDocumentsLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Add Ingredient Specific Documents To Be Uploaded", None))
        self.filesToBeUploadedLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Double Click File Name to Edit", None))
        ___qtablewidgetitem = self.filesToBeUploadedTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("addIngredientDialog", u"File Name", None));
        ___qtablewidgetitem1 = self.filesToBeUploadedTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("addIngredientDialog", u"Upload Date", None));
        ___qtablewidgetitem2 = self.filesToBeUploadedTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("addIngredientDialog", u"File Path", None));
        self.browseForFileBtn.setText(QCoreApplication.translate("addIngredientDialog", u"Browse Files", None))
        self.removeFromTableBtn.setText(QCoreApplication.translate("addIngredientDialog", u"Remove File", None))
        self.clearAllFromTableBtn.setText(QCoreApplication.translate("addIngredientDialog", u"Clear Files", None))
        self.addIngredientTabWidget.setTabText(self.addIngredientTabWidget.indexOf(self.documentationTab), QCoreApplication.translate("addIngredientDialog", u"Documentation", None))
        self.addIngredientTabWidget.setTabText(self.addIngredientTabWidget.indexOf(self.groupsTab), QCoreApplication.translate("addIngredientDialog", u"Groups", None))
        self.addIngredientTabWidget.setTabText(self.addIngredientTabWidget.indexOf(self.costTab), QCoreApplication.translate("addIngredientDialog", u"Cost", None))
        pass
    # retranslateUi




'''app = QApplication(sys.argv)
gui = addIngredientDialog()
gui.show()
sys.exit(app.exec_())'''