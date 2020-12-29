# -*- coding: utf-8 -*-

#########################################################################
## Form generated from reading UI file 'add_ingredient.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
#########################################################################

import os, sys
sys.path.append('../pjrd')
from datetime import date, datetime
from typing import NoReturn
#from pjrd.helpers import TimedMessageBox

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pymysql import Connection
from pjrd.helpers import dbConnection

os.environ['QT_MAC_WANTS_LAYER'] = '1' 
# TODO for later
# add a text box where you can paste in copied nutritionals from some table or pdf. The textbox would recognize the change and scan over the lines and autofill the data

class addIngredientDialog(QDialog):

    def __init__(self, mainWindow, openIngredientID: int=None):
        super(addIngredientDialog, self).__init__()
        self.mainWindow = mainWindow
        self.setupUi(self)
        self.setupLogic()
        self.isEdit = False
    
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
        self.nutrientMap = {
            659: {
                'name': 'Added Sugars',
                'object': self.addedSugarsGLineEdit,
                'factor': 1
            }, 
            221: {
                'name': 'Alcohol',
                'object': self.alcoholGLineEdit,
                'factor': 1
            },
            262: {
                'name': "Caffeine",
                'object': self.caffeineMgLineEdit,
                'factor': 1
            }, 
            301:  {
                'name': 'Calcium',
                'object': self.calciumMgLineEdit,
                'factor': .001
            }, 
            601: {
                'name': 'Cholestrol',
                'object': self.cholestrolMgLineEdit,
                'factor': .001
            }, 
            421: {
                'name': 'Choline',
                'object': self.cholineMgLineEdit,
                'factor': .001
            }, 
            654: {
                'name': 'Chromium',
                'object': self.chromiumMcgLineEdit,
                'factor': .000001
            }, 
            312: {
                'name': 'Copper',
                'object': self.copperMgLineEdit,
                'factor': .001
            }, 
            649: {
                'name': 'Disaccharides',
                'object': self.disaccharidesGLineEdit,
                'factor': 1
            }, 
            652: {
                'name': 'Fluoride',
                'object': self.fluorideMgLineEdit,
                'factor': .001
            }, 
            417: {
                'name': 'Folate',
                'object': self.folateMcgLineEdit,
                'factor': .000001
            }, 
            435: {
                'name': 'Folate - DFE',
                'object': self.folateDFEMcgDFELineEdit,
                'factor': .000001
            }, 
            655: {
                'name': 'Iodine',
                'object': self.iodineMcgLineEdit,
                'factor': .000001
            }, 
            303: {
                'name': 'Iron',
                'object': self.ironMgLineEdit,
                'factor': .001
            }, 
            651: {
                'name': 'Magnesium',
                'object': self.magnesiumMgLineEdit,
                'factor': .001
            }, 
            255: {
                'name': 'Moisture',
                'object': self.moistureGLineEdit,
                'factor': 1
            },
            657: {
                'name': 'Molybdenum',
                'object': self.molybdenumMcgLineEdit,
                'factor': .000001
            }, 
            1: {
                'name': 'Monosaccharides',
                'object': self.monosaccharidesGLineEdit,
                'factor': 1
            }, 
            645: {
                'name': 'Monounsaturated Fat',
                'object': self.monounsaturatedFatGLineEdit,
                'factor': 1
            }, 
            660: {
                'name': 'Omega-3',
                'object': self.omega3FattyAcidGLineEdit,
                'factor': 1
            }, 
            661: {
                'name': 'Omega-6',
                'object': self.omega6FattyAcidGLineEdit,
                'factor': 1
            }, 
            662: {
                'name': 'Other Carbohydrates',
                'object': self.otherCarbohydratesGLineEdit,
                'factor': 1
            }, 
            658: {
                'name': 'Panothenic Acid',
                'object': self.panothenicAcidMgLineEdit,
                'factor': .001
            }, 
            305: {
                'name': 'Phosphorus',
                'object': self.phosphorusMgLineEdit,
                'factor': .001
            }, 
            646: {
                'name': 'Polyunsaturated Fat',
                'object': self.polyunsaturatedFatGLineEdit,
                'factor': 1
            }, 
            306: {
                'name': 'Potassium',
                'object': self.potassiumMgLineEdit,
                'factor': .001
            }, 
            606: {
                'name': 'Saturated Fat',
                'object': self.saturatedFatGLineEdit,
                'factor': 1
            }, 
            317: {
                'name': 'Selenium',
                'object': self.seleniumMcgLineEdit,
                'factor': .000001
            }, 
            307: {
                'name': 'Sodium',
                'object': self.sodiumMgLineEdit,
                'factor': .001
            }, 
            647: {
                'name': 'Sugar Alcohol',
                'object': self.sugarAlcoholGLineEdit,
                'factor': 1
            }, 
            205: {
                'name': 'Total Carbs',
                'object': self.totalCarbohydratesGLineEdit,
                'factor': 1
            }, 
            291: {
                'name': 'Total Dietary Fiber',
                'object': self.totalDietaryFiberGLineEdit,
                'factor': 1
            }, 
            204: {
                'name': 'Total Fat',
                'object': self.totalFatGLineEdit,
                'factor': 1
            },
            203: {
                'name': 'Total Protein',
                'object': self.totalProteinGLineEdit,
                'factor': 1
            },
            648: {
                'name': 'Total Soluble Fiber',
                'object': self.totalSolubleFiberGLineEdit,
                'factor': 1
            },
            269: {
                'name': 'Total Sugars',
                'object': self.totalSugarsGLineEdit,
                'factor': 1
            }, 
            663: {
                'name': 'Total Unsat Fat',
                'object': self.totalUnsaturatedFatGLineEdit,
                'factor': 1
            }, 
            664: {
                'name': 'Total Trans Fat',
                'object': self.transFatGLineEdit,
                'factor': 1
            }, 
            320: {
                'name': 'Vitamin A RAE',
                'object': self.vitaminARAEMcgLineEdit,
                'factor': .00001
            }, 
            404: {
                'name': 'Vitamin b1/thiamin',
                'object': self.vitaminB1ThiaminMgLineEdit,
                'factor': .001
            }, 
            418: {
                'name': 'Vitamin b12',
                'object': self.vitaminB12McgLineEdit,
                'factor': .000001
            }, 
            405: {
                'name': 'Vitamin b2/Riboflavin',
                'object': self.vitaminB2RiboflavinMgLineEdit,
                'factor': .001
            }, 
            406: {
                'name': 'Vitamin b3/niacin',
                'object': self.vitaminB3NiacinMgLineEdit,
                'factor': .001
            }, 
            415: {
                'name': 'Vitamin b6',
                'object': self.vitaminB6MgLineEdit,
                'factor': .001
            }, 
            401: {
                'name': 'Vitamin C',
                'object': self.vitaminCMgLineEdit,
                'factor': .001
            },
            328: {
                'name': 'Vitamin D',
                'object': self.vitaminDIUIULineEdit,
                'factor': .001
            }, 
            323: {
                'name': 'Vitamin E/Alpha-Tocopherol',
                'object': self.vitaminEAlphaTocoMgLineEdit,
                'factor': .001
            }, 
            430: {
                'name': 'Vitamin K',
                'object': self.vitaminKMcgLineEdit,
                'factor': 0.000001
            }, 
            309: {
                'name': 'Zinc',
                'object': self.zincMgLineEdit,
                'factor': .001
            }, 
            208: {
                'name': 'Calories',
                'object': self.caloriesKCalLineEdit,
                'factor': 1
            }
        }

        if openIngredientID is not None:
            self.openFromExisting(openIngredientID)
            self.isEdit = True # helps to differentiate the database access whether the ingredient is new, or existing
            self.id = openIngredientID
        else:
            self.isEdit = False

    # opens the ingredient dialog with the 
    def openFromExisting(self, id):

        with dbConnection('FormulaSchema').cursor() as cursor:
            cursor.execute('SELECT food.food_desc, food.food_notes, food.ing_statement, food.percent_yield, supplier_food.specific_name, supplier_food.supplier_ing_item_code, supplier.supplier_id, supplier.supplier_name FROM food LEFT JOIN supplier_food ON supplier_food.food_id = food.food_id LEFT JOIN supplier ON supplier.supplier_id = supplier_food.supplier_id WHERE food.food_id = %s', (id,))
            result = cursor.fetchone()

            # sets the general information
            self.ingDescLineEdit.setText(result['food_desc'])
            if result['food_notes'] is not None:
                self.notesLineEdit.setText(result['food_notes'])
            if result['ing_statement'] is not None:
                self.ingredientStatementLineEdit.setText(result['ing_statement'])
            if result['supplier_name'] is not None:
                comboBoxIndex = self.supplierComboBox.findData(result['supplier_id'], Qt.UserRole, Qt.MatchFlag.MatchExactly)
                self.supplierComboBox.setCurrentIndex(comboBoxIndex)
            if result['supplier_ing_item_code'] is not None:
                self.supplierIngredientNumberLineEdit.setText(result['supplier_ing_item_code'])
            if result['percent_yield'] is not None:
                self.percentYieldDoubleSpinBox.setValue(result['percent_yield'])
            if result['specific_name'] is not None:
                self.ingNameLineEdit.setText(result['specific_name'])

            # bad design 
            # sets the allergens and claims
            cursor.execute('SELECT claim FROM food_claim WHERE food_id = %s', (id,))
            claims = cursor.fetchall()
            for claim in claims:
                value = claim['claim']
                for dictionary in self.claimMap:
                    if dictionary['claim'] == value:
                        checkbox = dictionary['object']
                        checkbox.setChecked(True)
    
            # sets the allergens to their existing position
            cursor.execute('SELECT allergen_id, allergen FROM food_allergen WHERE food_id = %s', (id,))
            allergens = cursor.fetchall()
            for allergen in allergens:
                for dictionary in self.allergenMap:
                    if dictionary['id'] == allergen['allergen_id']:
                        checkbox = dictionary['object']
                        checkbox.setChecked(True)

            cursor.execute('SELECT nutrient_id, nutrient_weight_g_per_100g FROM food_nutrient WHERE food_id = %s', (id,))
        
            nutrients = cursor.fetchall()
            for nutrient in nutrients:
                nutrientID = nutrient['nutrient_id']
                lineEdit = self.nutrientMap.get(nutrientID)['object']
                lineEdit.setText(str(nutrient['nutrient_weight_g_per_100g']))

        self.ingDescLineEdit.clearFocus()


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
        self.ingDescLineEdit.setPlaceholderText(u"Prehydrated Cellulose Gum Powder")
        self.ingDescLineEdit.clearFocus()

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ingDescLineEdit)

        self.ingNameLabel = QLabel(self.generalFrame1)
        self.ingNameLabel.setObjectName(u"ingNameLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.ingNameLabel)

        self.ingNameLineEdit = QLineEdit(self.generalFrame1)
        self.ingNameLineEdit.setObjectName(u"ingNameLineEdit")
        self.ingNameLineEdit.setMinimumSize(QSize(300, 0))
        self.ingNameLineEdit.setPlaceholderText(u"ie. Pre-Hydrated\u00ae Ticalose\u00ae CMC 15 Powder")

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
        self.percentYieldDoubleSpinBox.setValue(100)
        self.percentYieldDoubleSpinBox.setDecimals(0)
        self.percentYieldDoubleSpinBox.setRange(1, 1000)

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

        self.autoFillTextEdit = QTextEdit(self.nutritionalsTab)
        self.autoFillTextEdit.setPlaceholderText('This feature is still being developed. Will autofill the below line inputs based by scanning the input here. Paste any copied information')
        self.verticalLayout_3.addWidget(self.autoFillTextEdit)

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
        self.buttonBox.accepted.connect(self.formSubmit)
        self.buttonBox.rejected.connect(addIngredientDialog.reject)

        ### CHANGES BEYOND QT ###############<--------------------------------------------
        self.addIngredientTabWidget.setCurrentIndex(0)
        

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
        self.browseForFileBtn.clicked.connect(lambda: self.browseFiles()) 
        # lambda might not be right for this

        self.checkDataBtn.clicked.connect(self.validateNutrients)
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
                name = str(supplier['supplier_name']).title()
                #supplierItem.setData(supplier, Qt.UserRole)
                supplierItem.setData(supplier['supplier_id'], Qt.UserRole)
                supplierItem.setText(name)
                model.appendRow(supplierItem)
            completer.setModel(model)
            self.supplierComboBox.setCompleter(completer)
            self.supplierComboBox.setModel(model)
            self.supplierComboBox.setCurrentIndex(-1)

    # clears all files from table
    def clearContentsWrapper(self): 
        self.filesToBeUploadedTableWidget.clearContents()

    # called when OK button pushed
    def accepted(self):
        submit = QMessageBox.question(self, 'Confirm Submission', 'Are you ready to submit?', QMessageBox.Yes|QMessageBox.No)
        if submit == QMessageBox.Yes:
            self.formSubmit()

    def rejected(self):
        toClose = QMessageBox.question(self, "Confirm Cancellation", "Are you sure you would like to cancel?", QMessageBox.Yes | QMessageBox.No)
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

    def autofillNutritionals(self):
        pass
    # called when submitting the form 
    def formSubmit(self):
        submit = QMessageBox.question(self, 'Confirm Submission', 'Are you ready to submit?', QMessageBox.Yes|QMessageBox.No)
        if submit != QMessageBox.Yes:
            return

        if not self.validateNutrients():
            print('Input not valid')
            return

        if self.validatedInput() is False:
            return

        try:
            db = dbConnection('FormulaSchema')
        except ConnectionError:
            msg = QMessageBox()
            msg.setText('Connection to database unsuccessful. Ingredient unsuccessfully added')
            msg.exec_()
            return

        try: 
            with db.cursor() as cursor:

                ingDesc = self.ingDescLineEdit.text()
            
                # SUPPLIER 
                # validates that a supplier was inputted into combo box
                if self.supplierComboBox.currentText():
                    supplierID = self.supplierComboBox.currentData(Qt.UserRole)
                    if not supplierID:
                        cursor.execute('INSERT IGNORE INTO supplier(supplier_name) VALUES (%s)', (self.supplierComboBox.currentText().title(),))
                        supplierID = db.insert_id()
                    else:
                        
                        supplier = self.supplierComboBox.currentText()
                        #supplier = supplierItem['supplier_name']
                else: 
                    supplierID = None

                foodName = self.ingNameLineEdit.text()
                if self.supplierIngredientNumberLineEdit.text() != '':
                    itemCode = self.supplierIngredientNumberLineEdit.text()
                else:
                    itemCode = None
                if self.ingredientStatementLineEdit.text() != '':
                    ingStatement = self.ingredientStatementLineEdit.text()
                else:
                    ingStatement = None
                
                
                percentYield = self.percentYieldDoubleSpinBox.value()
            
                # food table 
                if self.isEdit is True:
                    cursor.execute('UPDATE food SET food_desc = %s, food_notes = %s, user_inputted = %s, input_date = %s, percent_yield = %s, ing_statement = %s WHERE food_id = %s', (ingDesc, self.notesLineEdit.text(), True, date.today(), percentYield, ingStatement, self.id))
                else:
                    cursor.execute('INSERT IGNORE INTO food(food_desc, food_notes, user_inputted, input_date, percent_yield, ing_statement, is_ingredient, is_formula) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (ingDesc, self.notesLineEdit.text(), True, date.today(), percentYield, ingStatement, True, False))
                    self.id = db.insert_id()

                # supplier_food table
                if supplierID is None:
                    if self.isEdit is True:
                        cursor.execute('DELETE FROM supplier_food WHERE food_id = %s', (self.id,))
                    else:
                        pass
                else:
                    if self.isEdit is True:
                        cursor.execute('UPDATE supplier_food SET specific_name = %s, supplier_id = %s, supplier_ing_item_code = %s WHERE food_id = %s', (foodName, supplierID, itemCode, self.id))
                    else:
                        cursor.execute('INSERT INTO supplier_food (food_id, specific_name, supplier_id, supplier_ing_item_code) VALUES (%s, %s, %s, %s)', (self.id, foodName, supplierID, itemCode))

                # allergens table
                # allergen map  {'allergen': 'Dairy', 'id': 1, 'object': self.dairyCheckbox},
                if self.isEdit is True:
                    cursor.execute('DELETE FROM food_allergen WHERE food_id = %s', (self.id,))
                for allergen in self.allergenMap:
                    input = allergen['object']
                    if input.isChecked(): 
                        cursor.execute("INSERT INTO food_allergen(food_id, allergen_id, allergen) VALUES (%s, %s, %s)", (self.id, allergen['id'], allergen['allergen']))
                
                # food_claim table
                if self.isEdit is True:
                    cursor.execute('DELETE FROM food_claim WHERE food_id = %s', (self.id,))
                for claim in self.claimMap:
                    box = claim['object']
                    if box.isChecked():
                        cursor.execute('INSERT INTO food_claim (food_id, claim) VALUES (%s, %s)', (self.id, claim['claim']))

                # food_nutrient table
                if self.isEdit is True:
                    cursor.execute('DELETE FROM food_nutrient WHERE food_id = %s', (self.id,))
                perWeight = self.perGramsSpinBox.value()
                for id, nutrient in self.nutrientMap.items():
                    if nutrient['object'].text():
                        try:
                            value = float(nutrient['object'].text())
                            factor = nutrient['factor']
                        except:
                            msg = QMessageBox()
                            msg.setText('Value for {} on nutritional tab is not in numerical format'.format(nutrient['nutrient_name']))
                            msg.exec_()
                            return
                        else:
                            weight = ((value/perWeight) * 100) * factor
                            cursor.execute('INSERT INTO food_nutrient (food_id, nutrient_id, nutrient_weight_g_per_100g) VALUES (%s, %s, %s)', (self.id, id, weight))
                    
        except ConnectionAbortedError:
            msg = QMessageBox()
            msg.setText('Something went wrong. Food ingredient was not added to database')
            msg.exec_()
            return

        else:
            db.commit()
            msg = QMessageBox()
            if self.isEdit is True:
                msg.setText('Successfully updated the ingredient information')
            else:
                msg.setText('Successfully added the new ingredient to the database')
            msg.exec_()
            self.mainWindow.refreshListWidget()
            self.close()
            return
     
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

    def validateNutrients(self, requested: bool=None):
        # required inputs are calories, total fat, total protein, total carbs 

        # NOTE
        # omega3 + omega6 is a polyunsat fat 
        # sugar alcohols are not considered carbs
        # sugars are monosaccharides and disaccharides

        # carbohydrate validation
        if self.totalCarbohydratesGLineEdit.text():
            carbs = float(self.totalCarbohydratesGLineEdit.text())
        else:
            msg = QMessageBox()
            msg.setText('Input required in Total Carbohydates box on Nutritionals tab')
            self.totalCarbohydratesGLineEdit.setFocus()
            msg.exec_()
            return False
        
        # fat validation
        if self.totalFatGLineEdit.text():
            fats = float(self.totalFatGLineEdit.text())
        else:
            msg = QMessageBox()
            msg.setText('Input required in Total Fats box on Nutritionals tab')
            self.totalFatGLineEdit.setFocus()
            msg.exec_()
            return False
        
        # protein validation
        if self.totalProteinGLineEdit.text():
            proteins = float(self.totalProteinGLineEdit.text())
        else:
            msg = QMessageBox()
            msg.setText('Input required in Total Proteins box on Nutritionals tab')
            self.totalProteinGLineEdit.setFocus()
            msg.exec_()
            return False

        # calories validation
        if self.caloriesKCalLineEdit.text():
            calories = float(self.caloriesKCalLineEdit.text())
        else:
            msg = QMessageBox()
            msg.setText('Input required in Calories box on Nutritionals tab')
            self.caloriesKCalLineEdit.setFocus()
            msg.exec_()
            return False
            
        if not self.alcoholGLineEdit.text():
            alcohol = 0
        else: 
            alcohol = float(self.alcoholGLineEdit.text())
        
        if not self.sugarAlcoholGLineEdit.text():
            sugarAlcohols = 0
        else:
            sugarAlcohols = float(self.sugarAlcoholGLineEdit.text())
        
        if not self.moistureGLineEdit.text():
            water = 0
        else: 
            water = float(self.moistureGLineEdit.text())
        
        if not self.totalSugarsGLineEdit.text():
            totalSugar = 0
        else:
            totalSugar = float(self.totalSugarsGLineEdit.text())
        
        if not self.addedSugarsGLineEdit.text():
            addedSugar = 0
        else:
            addedSugar = float(self.addedSugarsGLineEdit.text())

        if not self.totalDietaryFiberGLineEdit.text():
            totalDietaryFiber = 0
        else:
            totalDietaryFiber = float(self.totalDietaryFiberGLineEdit.text())

        if not self.totalSolubleFiberGLineEdit.text():
            totalSolubleFiber = 0
        else:
            totalSolubleFiber = float(self.totalSolubleFiberGLineEdit.text())

        if not self.monosaccharidesGLineEdit.text():
            monosaccharides = 0
        else:
            monosaccharides = float(self.monosaccharidesGLineEdit.text())

        if not self.disaccharidesGLineEdit.text():
            disaccharides = 0
        else:
            disaccharides = float(self.disaccharidesGLineEdit.text())

        if not self.otherCarbohydratesGLineEdit.text():
            otherCarbs = 0
        else:
            otherCarbs = float(self.otherCarbohydratesGLineEdit.text())

        if not self.totalUnsaturatedFatGLineEdit.text():
            totalUnsatFat = 0
        else:
            totalUnsatFat = float(self.totalUnsaturatedFatGLineEdit.text())
      
        if not self.saturatedFatGLineEdit.text():
            totalSatFat = 0
        else:
            totalSatFat = float(self.saturatedFatGLineEdit.text())

        if not self.monounsaturatedFatGLineEdit.text():
            monounsatFat = 0
        else:
            monounsatFat = float(self.monounsaturatedFatGLineEdit.text())

        if not self.polyunsaturatedFatGLineEdit.text():
            polyunsatFat = 0
        else:
            polyunsatFat = float(self.polyunsaturatedFatGLineEdit.text())
        
        if not self.transFatGLineEdit.text():
            transFat = 0
        else:
            transFat = float(self.transFatGLineEdit.text())
        
        if not self.omega3FattyAcidGLineEdit.text():
            omega3 = 0
        else:
            omega3 = float(self.omega3FattyAcidGLineEdit.text())
    
        if not self.omega6FattyAcidGLineEdit.text():
            omega6 = 0
        else:
            omega6 = float(self.omega6FattyAcidGLineEdit.text())

        # Logic
        '''if calories/self.perGramsSpinBox.value() > .05:
            # checks that calories are validated in relation to major calorie-contributing nutrients
            # 10% buffer applied
            if (proteins * 4) + (fats * 9) + (carbs * 4) + (alcohol * 7) > calories * 1.1:
                msg = QMessageBox()
                msg.setText('Calories are lower than expected given entered macronutrients')
                self.caloriesKCalLineEdit.setFocus()
                msg.exec_()
                return False'''

        # checkse that nutrient weights are validated in relation to per-weight
        # 10% buffer applied
        perWeight = self.perGramsSpinBox.value()
        if proteins + fats + carbs + alcohol + water > perWeight * 1.1:

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
        
        if requested is True:
            msg = QMessageBox()
            msg.setText('Looks good')
            msg.exec_()
        # returns True if all error checking has passed 
        return True
        
    def retranslateUi(self, addIngredientDialog):
        self.ingDescLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Ingredient Description", None))
        self.ingNameLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Ingredient Name", None))
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
        #self.addIngredientTabWidget.setTabText(self.addIngredientTabWidget.indexOf(self.groupsTab), QCoreApplication.translate("addIngredientDialog", u"Groups", None))
        #self.addIngredientTabWidget.setTabText(self.addIngredientTabWidget.indexOf(self.costTab), QCoreApplication.translate("addIngredientDialog", u"Cost", None))
        pass
    # retranslateUi

    # validates all the user input before committing to database
    def validatedInput(self):
        if self.ingDescLineEdit.text() is None:
            msg = QMessageBox()
            msg.setText('Must input an ingredient description on tab 1')
            msg.exec_()
            return False
        
        




'''app = QApplication(sys.argv)
gui = addIngredientDialog()
gui.show()
sys.exit(app.exec_())'''