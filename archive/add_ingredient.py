# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_ingredient.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

## TODO: ADD CALORIES 

from PyQt5.QtCore import QSize, QObject, Qt, QCoreApplication, QMetaObject, QDir, QRect
from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout, QGridLayout, QWidget, QTabWidget, QFormLayout, QFrame, QLabel, QCheckBox, QLineEdit, QSpinBox, QPushButton, QDialog, QCompleter, QComboBox, QDoubleSpinBox, QAbstractSpinBox, QHBoxLayout, QListWidget, QTableWidget, QDialogButtonBox, QFileDialog, QScrollArea, QSpacerItem, QTableWidgetItem

from helpers import connectDB, displayNFP

class addIngredientDialog(QDialog):

    def __init__(self):
        super(addIngredientDialog, self).__init__()
        self.setupUi(self)
        self.db = connectDB()
        self.addSignals()

        self.allergenMap = [
            {'allergen': 'Dairy', 'object': self.dairyCheckbox},
            {'allergen': 'Eggs', 'object': self.eggCheckbox},
            {'allergen': 'Fish', 'object': self.fishCheckbox},
            {'allergen': 'Shellfish', 'object': self.shellfishCheckbox},
            {'allergen': 'Tree Nuts', 'object': self.treeNutsCheckbox},
            {'allergen': 'Peanuts', 'object': self.peanutsCheckbox},
            {'allergen': 'Wheat', 'object': self.wheatCheckbox},
            {'allergen': 'Soy', 'object': self.soyCheckbox},
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
            },
            {
                "nutrient_name": "Calories", 
                "nutrient_id": 54, 
                "value": self.caloriesKCalLineEdit.text(),
                "weight_id": "kCal"
            },
            {
                "nutrient_name": "Calories from Fat", 
                "nutrient_id": 55, 
                "value": self.caloriesFromFatKCalLineEdit.text(),
                "weight_id": "kCal"
            },
            {
                "nutrient_name": "Calories from SatFat", 
                "nutrient_id": 56, 
                "value": self.caloriesFromSatFatKCalLineEdit.text(),
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
        self.addIngredientTabWidget.setCurrentIndex(0)
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

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.ingredientNameLabel)

        self.ingredientNameLineEdit = QLineEdit(self.generalFrame1)
        self.ingredientNameLineEdit.setObjectName(u"ingredientNameLineEdit")
        self.ingredientNameLineEdit.setMinimumSize(QSize(300, 0))
        self.ingredientNameLineEdit.setPlaceholderText(u"ie. Pre-Hydrated\u00ae Ticalose\u00ae CMC 15 Powder")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ingredientNameLineEdit)

        self.commonNameLabel = QLabel(self.generalFrame1)
        self.commonNameLabel.setObjectName(u"commonNameLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.commonNameLabel)

        self.commonNameLineEdit = QLineEdit(self.generalFrame1)
        self.commonNameLineEdit.setObjectName(u"commonNameLineEdit")
        self.commonNameLineEdit.setMinimumSize(QSize(300, 0))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.commonNameLineEdit)

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
        self.perGramsSpinBox.setSingleStep(10)
        self.perGramsSpinBox.setValue(100)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 937, 1525))
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

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.calciumMgLineEdit)

        self.chromiumMcgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.chromiumMcgLineEdit.setObjectName(u"chromiumMcgLineEdit")

        self.formLayout_6.setWidget(4, QFormLayout.FieldRole, self.chromiumMcgLineEdit)

        self.copperMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.copperMgLineEdit.setObjectName(u"copperMgLineEdit")

        self.formLayout_6.setWidget(6, QFormLayout.FieldRole, self.copperMgLineEdit)

        self.fluorideMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.fluorideMgLineEdit.setObjectName(u"fluorideMgLineEdit")

        self.formLayout_6.setWidget(8, QFormLayout.FieldRole, self.fluorideMgLineEdit)

        self.iodineMcgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.iodineMcgLineEdit.setObjectName(u"iodineMcgLineEdit")

        self.formLayout_6.setWidget(10, QFormLayout.FieldRole, self.iodineMcgLineEdit)

        self.ironMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.ironMgLineEdit.setObjectName(u"ironMgLineEdit")

        self.formLayout_6.setWidget(12, QFormLayout.FieldRole, self.ironMgLineEdit)

        self.magnesiumMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.magnesiumMgLineEdit.setObjectName(u"magnesiumMgLineEdit")

        self.formLayout_6.setWidget(14, QFormLayout.FieldRole, self.magnesiumMgLineEdit)

        self.manganeseMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.manganeseMgLineEdit.setObjectName(u"manganeseMgLineEdit")

        self.formLayout_6.setWidget(16, QFormLayout.FieldRole, self.manganeseMgLineEdit)

        self.molybdenumMcgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.molybdenumMcgLineEdit.setObjectName(u"molybdenumMcgLineEdit")

        self.formLayout_6.setWidget(18, QFormLayout.FieldRole, self.molybdenumMcgLineEdit)

        self.phosphorusMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.phosphorusMgLineEdit.setObjectName(u"phosphorusMgLineEdit")

        self.formLayout_6.setWidget(20, QFormLayout.FieldRole, self.phosphorusMgLineEdit)

        self.potassiumMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.potassiumMgLineEdit.setObjectName(u"potassiumMgLineEdit")

        self.formLayout_6.setWidget(22, QFormLayout.FieldRole, self.potassiumMgLineEdit)

        self.seleniumMcgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.seleniumMcgLineEdit.setObjectName(u"seleniumMcgLineEdit")

        self.formLayout_6.setWidget(24, QFormLayout.FieldRole, self.seleniumMcgLineEdit)

        self.sodiumMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.sodiumMgLineEdit.setObjectName(u"sodiumMgLineEdit")

        self.formLayout_6.setWidget(26, QFormLayout.FieldRole, self.sodiumMgLineEdit)

        self.zincMgLineEdit = QLineEdit(self.mineralsFrame_2)
        self.zincMgLineEdit.setObjectName(u"zincMgLineEdit")

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

        self.formLayout_4.setWidget(16, QFormLayout.FieldRole, self.otherCarbohydratesGLineEdit)

        self.disaccharidesGLineEdit = QLineEdit(self.carbsFrame)
        self.disaccharidesGLineEdit.setObjectName(u"disaccharidesGLineEdit")

        self.formLayout_4.setWidget(14, QFormLayout.FieldRole, self.disaccharidesGLineEdit)

        self.monosaccharidesGLineEdit = QLineEdit(self.carbsFrame)
        self.monosaccharidesGLineEdit.setObjectName(u"monosaccharidesGLineEdit")

        self.formLayout_4.setWidget(12, QFormLayout.FieldRole, self.monosaccharidesGLineEdit)

        self.totalSolubleFiberGLineEdit = QLineEdit(self.carbsFrame)
        self.totalSolubleFiberGLineEdit.setObjectName(u"totalSolubleFiberGLineEdit")

        self.formLayout_4.setWidget(10, QFormLayout.FieldRole, self.totalSolubleFiberGLineEdit)

        self.totalDietaryFiberGLineEdit = QLineEdit(self.carbsFrame)
        self.totalDietaryFiberGLineEdit.setObjectName(u"totalDietaryFiberGLineEdit")

        self.formLayout_4.setWidget(8, QFormLayout.FieldRole, self.totalDietaryFiberGLineEdit)

        self.addedSugarsGLineEdit = QLineEdit(self.carbsFrame)
        self.addedSugarsGLineEdit.setObjectName(u"addedSugarsGLineEdit")

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.addedSugarsGLineEdit)

        self.totalSugarsGLineEdit = QLineEdit(self.carbsFrame)
        self.totalSugarsGLineEdit.setObjectName(u"totalSugarsGLineEdit")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.totalSugarsGLineEdit)

        self.totalCarbohydratesGLineEdit = QLineEdit(self.carbsFrame)
        self.totalCarbohydratesGLineEdit.setObjectName(u"totalCarbohydratesGLineEdit")

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

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.totalFatGLineEdit)

        self.saturatedFatGLineEdit = QLineEdit(self.fatsFrame)
        self.saturatedFatGLineEdit.setObjectName(u"saturatedFatGLineEdit")

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.saturatedFatGLineEdit)

        self.totalUnsaturatedFatGLineEdit = QLineEdit(self.fatsFrame)
        self.totalUnsaturatedFatGLineEdit.setObjectName(u"totalUnsaturatedFatGLineEdit")

        self.formLayout_5.setWidget(6, QFormLayout.FieldRole, self.totalUnsaturatedFatGLineEdit)

        self.monounsaturatedFatGLineEdit = QLineEdit(self.fatsFrame)
        self.monounsaturatedFatGLineEdit.setObjectName(u"monounsaturatedFatGLineEdit")

        self.formLayout_5.setWidget(8, QFormLayout.FieldRole, self.monounsaturatedFatGLineEdit)

        self.polyunsaturatedFatGLineEdit = QLineEdit(self.fatsFrame)
        self.polyunsaturatedFatGLineEdit.setObjectName(u"polyunsaturatedFatGLineEdit")

        self.formLayout_5.setWidget(10, QFormLayout.FieldRole, self.polyunsaturatedFatGLineEdit)

        self.transFatGLineEdit = QLineEdit(self.fatsFrame)
        self.transFatGLineEdit.setObjectName(u"transFatGLineEdit")

        self.formLayout_5.setWidget(12, QFormLayout.FieldRole, self.transFatGLineEdit)

        self.cholestrolMgLineEdit = QLineEdit(self.fatsFrame)
        self.cholestrolMgLineEdit.setObjectName(u"cholestrolMgLineEdit")

        self.formLayout_5.setWidget(14, QFormLayout.FieldRole, self.cholestrolMgLineEdit)

        self.omega3FattyAcidGLineEdit = QLineEdit(self.fatsFrame)
        self.omega3FattyAcidGLineEdit.setObjectName(u"omega3FattyAcidGLineEdit")

        self.formLayout_5.setWidget(16, QFormLayout.FieldRole, self.omega3FattyAcidGLineEdit)

        self.omega6FattyAcidGLineEdit = QLineEdit(self.fatsFrame)
        self.omega6FattyAcidGLineEdit.setObjectName(u"omega6FattyAcidGLineEdit")

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

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.vitaminAIUIULineEdit)

        self.vitaminAREMcgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminAREMcgLineEdit.setObjectName(u"vitaminAREMcgLineEdit")

        self.formLayout_7.setWidget(4, QFormLayout.FieldRole, self.vitaminAREMcgLineEdit)

        self.vitaminARAEMcgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminARAEMcgLineEdit.setObjectName(u"vitaminARAEMcgLineEdit")

        self.formLayout_7.setWidget(6, QFormLayout.FieldRole, self.vitaminARAEMcgLineEdit)

        self.vitaminB1ThiaminMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB1ThiaminMgLineEdit.setObjectName(u"vitaminB1ThiaminMgLineEdit")

        self.formLayout_7.setWidget(8, QFormLayout.FieldRole, self.vitaminB1ThiaminMgLineEdit)

        self.vitaminB2RiboflavinMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB2RiboflavinMgLineEdit.setObjectName(u"vitaminB2RiboflavinMgLineEdit")

        self.formLayout_7.setWidget(10, QFormLayout.FieldRole, self.vitaminB2RiboflavinMgLineEdit)

        self.vitaminB3NiacinMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB3NiacinMgLineEdit.setObjectName(u"vitaminB3NiacinMgLineEdit")

        self.formLayout_7.setWidget(12, QFormLayout.FieldRole, self.vitaminB3NiacinMgLineEdit)

        self.vitaminB3NiacinEquivMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB3NiacinEquivMgLineEdit.setObjectName(u"vitaminB3NiacinEquivMgLineEdit")

        self.formLayout_7.setWidget(14, QFormLayout.FieldRole, self.vitaminB3NiacinEquivMgLineEdit)

        self.vitaminB6MgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB6MgLineEdit.setObjectName(u"vitaminB6MgLineEdit")

        self.formLayout_7.setWidget(16, QFormLayout.FieldRole, self.vitaminB6MgLineEdit)

        self.vitaminB12McgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminB12McgLineEdit.setObjectName(u"vitaminB12McgLineEdit")

        self.formLayout_7.setWidget(18, QFormLayout.FieldRole, self.vitaminB12McgLineEdit)

        self.vitaminCMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminCMgLineEdit.setObjectName(u"vitaminCMgLineEdit")

        self.formLayout_7.setWidget(20, QFormLayout.FieldRole, self.vitaminCMgLineEdit)

        self.vitaminDIUIULineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminDIUIULineEdit.setObjectName(u"vitaminDIUIULineEdit")

        self.formLayout_7.setWidget(22, QFormLayout.FieldRole, self.vitaminDIUIULineEdit)

        self.vitaminEAlphaTocoMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminEAlphaTocoMgLineEdit.setObjectName(u"vitaminEAlphaTocoMgLineEdit")

        self.formLayout_7.setWidget(24, QFormLayout.FieldRole, self.vitaminEAlphaTocoMgLineEdit)

        self.folateMcgLineEdit = QLineEdit(self.vitaminsFrame)
        self.folateMcgLineEdit.setObjectName(u"folateMcgLineEdit")

        self.formLayout_7.setWidget(26, QFormLayout.FieldRole, self.folateMcgLineEdit)

        self.folateDFEMcgDFELineEdit = QLineEdit(self.vitaminsFrame)
        self.folateDFEMcgDFELineEdit.setObjectName(u"folateDFEMcgDFELineEdit")

        self.formLayout_7.setWidget(28, QFormLayout.FieldRole, self.folateDFEMcgDFELineEdit)

        self.vitaminKMcgLineEdit = QLineEdit(self.vitaminsFrame)
        self.vitaminKMcgLineEdit.setObjectName(u"vitaminKMcgLineEdit")

        self.formLayout_7.setWidget(30, QFormLayout.FieldRole, self.vitaminKMcgLineEdit)

        self.panothenicAcidMgLineEdit = QLineEdit(self.vitaminsFrame)
        self.panothenicAcidMgLineEdit.setObjectName(u"panothenicAcidMgLineEdit")

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

        self.caloriesFromSatFatKCalLabel = QLabel(self.otherNutrientsFrame)
        self.caloriesFromSatFatKCalLabel.setObjectName(u"caloriesFromSatFatKCalLabel")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.caloriesFromSatFatKCalLabel)

        self.caloriesFromFatKCalLabel = QLabel(self.otherNutrientsFrame)
        self.caloriesFromFatKCalLabel.setObjectName(u"caloriesFromFatKCalLabel")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.caloriesFromFatKCalLabel)

        self.moistureGLabel = QLabel(self.otherNutrientsFrame)
        self.moistureGLabel.setObjectName(u"moistureGLabel")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.moistureGLabel)

        self.caffeineMgLabel = QLabel(self.otherNutrientsFrame)
        self.caffeineMgLabel.setObjectName(u"caffeineMgLabel")

        self.formLayout_3.setWidget(9, QFormLayout.LabelRole, self.caffeineMgLabel)

        self.cholineMgLabel = QLabel(self.otherNutrientsFrame)
        self.cholineMgLabel.setObjectName(u"cholineMgLabel")

        self.formLayout_3.setWidget(11, QFormLayout.LabelRole, self.cholineMgLabel)

        self.alcoholGLabel = QLabel(self.otherNutrientsFrame)
        self.alcoholGLabel.setObjectName(u"alcoholGLabel")

        self.formLayout_3.setWidget(13, QFormLayout.LabelRole, self.alcoholGLabel)

        self.sugarAlcoholGLabel = QLabel(self.otherNutrientsFrame)
        self.sugarAlcoholGLabel.setObjectName(u"sugarAlcoholGLabel")

        self.formLayout_3.setWidget(15, QFormLayout.LabelRole, self.sugarAlcoholGLabel)

        self.caloriesKCalLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.caloriesKCalLineEdit.setObjectName(u"caloriesKCalLineEdit")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.caloriesKCalLineEdit)

        self.caloriesFromSatFatKCalLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.caloriesFromSatFatKCalLineEdit.setObjectName(u"caloriesFromSatFatKCalLineEdit")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.caloriesFromSatFatKCalLineEdit)

        self.caloriesFromFatKCalLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.caloriesFromFatKCalLineEdit.setObjectName(u"caloriesFromFatKCalLineEdit")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.caloriesFromFatKCalLineEdit)

        self.moistureGLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.moistureGLineEdit.setObjectName(u"moistureGLineEdit")

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.moistureGLineEdit)

        self.caffeineMgLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.caffeineMgLineEdit.setObjectName(u"caffeineMgLineEdit")

        self.formLayout_3.setWidget(9, QFormLayout.FieldRole, self.caffeineMgLineEdit)

        self.cholineMgLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.cholineMgLineEdit.setObjectName(u"cholineMgLineEdit")

        self.formLayout_3.setWidget(11, QFormLayout.FieldRole, self.cholineMgLineEdit)

        self.alcoholGLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.alcoholGLineEdit.setObjectName(u"alcoholGLineEdit")

        self.formLayout_3.setWidget(13, QFormLayout.FieldRole, self.alcoholGLineEdit)

        self.sugarAlcoholGLineEdit = QLineEdit(self.otherNutrientsFrame)
        self.sugarAlcoholGLineEdit.setObjectName(u"sugarAlcoholGLineEdit")

        self.formLayout_3.setWidget(15, QFormLayout.FieldRole, self.sugarAlcoholGLineEdit)

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

        self.addDocsHeaderWidget = QWidget(self.documentationTab)
        self.addDocsHeaderWidget.setObjectName(u"addDocsHeaderWidget")
        self.addDocsHeaderWidget.setAutoFillBackground(False)
        self.horizontalLayout_2 = QHBoxLayout(self.addDocsHeaderWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.addDocsHeaderWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.label_3 = QLabel(self.addDocsHeaderWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.addToUploadBtn = QPushButton(self.addDocsHeaderWidget)
        self.addToUploadBtn.setObjectName(u"addToUploadBtn")

        self.horizontalLayout_2.addWidget(self.addToUploadBtn)

        self.verticalLayout_7.addWidget(self.addDocsHeaderWidget)

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
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(addIngredientDialog)
        self.buttonBox.accepted.connect(addIngredientDialog.accept)
        self.buttonBox.rejected.connect(addIngredientDialog.reject)

        ### CHANGES BEYOND QT ###############<--------------------------------------------
        self.addIngredientTabWidget.setCurrentIndex(0)
        # adds suggestions to input fields
        self.addSuggestions()
        
        self.buttonBox.accepted.connect(addIngredientDialog.accept)
    
        QMetaObject.connectSlotsByName(addIngredientDialog)
    # setupUi
    
    def addSignals(self):
        self.browseForFileBtn.clicked(self.browseFiles())
        
    

    # called at the end of setupUi
    def addSuggestions(self): 
        # adds suggestions for suppliers to general tab supplier box
        with connectDB().cursor() as cursor: 
            cursor.execute("SELECT supplier_name FROM supplier")
            allSuppliers = cursor.fetchall()
            for supplierRow in allSuppliers:
                self.supplierComboBox.addItem(supplierRow[0])
        
        # adds suggestions/autocomplete to common name line input box 
        with connectDB().cursor() as cursor:
            cursor.execute("SELECT ing_common_name FROM ingredient")
            cNameRows = [row[0] for row in cursor.fetchall()]
            completer = QCompleter(cNameRows)
            completer.setCaseSensitivity(Qt.CaseInsensitive)
            completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
            completer.setMaxVisibleItems(10)
            self.commonNameLineEdit.setCompleter(completer)

    # called when button pushed
    def accepted(self):
        self.accepted.connect(lambda: self.formSubmit())
        self.buttonBox.Box.rejected.connect(Ui_addIngredientDialog.rejected)

    def browseFiles(self):
        self.fileNavigator = QFileDialog()
        self.fileNavigator.setFileMode(QFileDialog.AnyFile)
        self.fileNavigator.setFilter(QDir.Files)

        if self.fileNavigator.exec_(): 
            fileName = self.fileNavigator.selectedFile()
            #self.fileNavigator.
            
        else:
            pass
    
    def formSubmit(self): # NEED TO FIX

        db = connectDB()
        try: 
            with db.cursor() as cursor:   
                    cName = self.commonNameLineEdit.text()
                    supplier = self.supplierComboBox.currentText()
                    sName = self.ingredientNameLineEdit.text()
                    itemCode = self.supplierIngredientNumberLineEdit.text()
                    
                    # inputs supplier into supplier table unless if it doesn't exist. Otherwise, gets the supplier id and saves in variable lastSupplierID
                    sameSupplierCount = cursor.execute("SELECT supplier_id, supplier_name FROM supplier WHERE supplier_name = (%s)", (supplier,))
                    if  sameSupplierCount == 0: 
                        cursor.execute("INSERT IGNORE INTO supplier(supplier_name) VALUES (%s)", (supplier,))
                        lastSupplierID  = db.insert_id()
                    else: 
                        lastSupplierID = cursor.fetchone()[0]
                        cursor._clear_result()

                    # Adds the ingredient into database if the supplier_id and item code as a pair don't already exist in the database. If they do, finds the ingredient id and stores as lastIngID
                    sameSpecificName = cursor.execute("SELECT * FROM ingredient WHERE supplier_id = (%s) AND supplier_ing_item_code = (%s)", (lastSupplierID, itemCode))
                    if sameSpecificName == 0:
                        cursor.execute("INSERT IGNORE INTO ingredient(ing_common_name, supplier_id, ing_specific_name, supplier_ing_item_code, ingredient_statement, notes) VALUES (%s, %s, %s, %s, %s, %s)", (cName, lastSupplierID, sName, itemCode, self.ingredientStatementLineEdit.text(), self.notesLineEdit.text()))
                        lastIngID = db.insert_id()
                    else: 
                        cursor.execute("SELECT * FROM ingredient WHERE ing_common_name = (%s) AND supplier_id = (%s)", (cName, lastSupplierID))
                        lastIngID = cursor.fetchone()[0]

                        # could make this fetch all instead and have popup window for user to choose 
                        #lastIngID = cursor.fetchAll()
                    #cursor.commit()

            # Adds information from nutrients tab into database
            with db.cursor() as cursor:
                perGrams = self.perGramsSpinBox.value()
                for nutrient in nutrientMap: 
                    if nutrient['value']: 
                        cursor.execute("INSERT INTO ing_nutrient(ing_id, nutrient_id, nutrient_weight, per_weight) VALUES (%s, %s, %s, %s)", (lastIngID, nutrient['nutrient_id'], nutrient['value'], perGrams,))
                #cursor.commit()

            # Adds allergens into database
            with db.cursor() as cursor: 
                for allergen in allergenMap:
                    input = allergen['object']
                    if input.isChecked(): 
                        cursor.execute("INSERT INTO ing_allergens(ing_id, allergen) VALUES (%s, %s)", (lastIngID, allergen['allergen']))
                #cursor.commit()  

            # inserts claims into database
            with db.cursor() as cursor: 
                for claim in claimMap: 
                    box = claim['object']
                    if box.isChecked(): 
                        cursor.execute("INSERT INTO ing_claims(ing_id, claim) VALUES (%s, %s)", (lastIngID, claim['claim']))

                #cursor.commit()       
            print('Everything went right')
        except: 
            print('something went wrong')

    def retranslateUi(self, addIngredientDialog):
        self.ingredientNameLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Specific Name", None))
        self.commonNameLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Common Name (if applicable)", None))
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
        self.panothenicAcidMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Panothenic Acid (mg)", None))
        self.label_2.setText(QCoreApplication.translate("addIngredientDialog", u"Proteins", None))
        self.totalProteinGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Total Protein (g)", None))
        self.caloriesKCalLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Calories (kCal)", None))
        self.caloriesFromSatFatKCalLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Calories from SatFat (kCal)", None))
        self.caloriesFromFatKCalLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Calories from Fat (kCal)", None))
        self.moistureGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Moisture (g)", None))
        self.caffeineMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Caffeine (mg)", None))
        self.cholineMgLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Choline (mg)", None))
        self.alcoholGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Alcohol (g)", None))
        self.sugarAlcoholGLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Sugar Alcohol (g)", None))
        self.label_6.setText(QCoreApplication.translate("addIngredientDialog", u"Other Nutrients", None))
        self.addIngredientTabWidget.setTabText(self.addIngredientTabWidget.indexOf(self.nutritionalsTab), QCoreApplication.translate("addIngredientDialog", u"Nutritionals", None))
        self.addIngredientSpecificDocumentsLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Add Ingredient Specific Documents", None))
        self.label.setText(QCoreApplication.translate("addIngredientDialog", u"Save As", None))
        self.label_3.setText(QCoreApplication.translate("addIngredientDialog", u"File Path", None))
        self.browseForFileBtn.setText(QCoreApplication.translate("addIngredientDialog", u"Browse Files", None))
        self.addToUploadBtn.setText(QCoreApplication.translate("addIngredientDialog", u"Add To Upload List", None))
        self.filesToBeUploadedLabel.setText(QCoreApplication.translate("addIngredientDialog", u"Files To Be Uploaded", None))
        ___qtablewidgetitem = self.filesToBeUploadedTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("addIngredientDialog", u"File Name", None));
        ___qtablewidgetitem1 = self.filesToBeUploadedTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("addIngredientDialog", u"Upload Date", None));
        ___qtablewidgetitem2 = self.filesToBeUploadedTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("addIngredientDialog", u"File Path", None));
        self.removeFromTableBtn.setText(QCoreApplication.translate("addIngredientDialog", u"Remove File", None))
        self.clearAllFromTableBtn.setText(QCoreApplication.translate("addIngredientDialog", u"Clear Files", None))
        self.addIngredientTabWidget.setTabText(self.addIngredientTabWidget.indexOf(self.documentationTab), QCoreApplication.translate("addIngredientDialog", u"Documentation", None))
        self.addIngredientTabWidget.setTabText(self.addIngredientTabWidget.indexOf(self.groupsTab), QCoreApplication.translate("addIngredientDialog", u"Groups", None))
        self.addIngredientTabWidget.setTabText(self.addIngredientTabWidget.indexOf(self.costTab), QCoreApplication.translate("addIngredientDialog", u"Cost", None))
        pass
    # retranslateUi



'''
    def formSubmit(self): # NEED TO FIX
        db = connectDB()
        try: 
            # Adds information from general tab into database
            with db.cursor() as cursor:   
                    cName = self.ingNameLineEdit.text()
                    supplier = self.supplierComboBox.currentText()
                    sName = self.ingDescLineEdit.text()
                    itemCode = self.supplierIngredientNumberLineEdit.text()
                    
                    # inputs supplier into supplier table unless if it doesn't exist. Otherwise, gets the supplier id and saves in variable lastSupplierID
                    sameSupplierCount = cursor.execute("SELECT supplier_id, supplier_name FROM supplier WHERE supplier_name = (%s)", (supplier,))
                    if  sameSupplierCount == 0: 
                        cursor.execute("INSERT IGNORE INTO supplier(supplier_name) VALUES (%s)", (supplier,))
                        lastSupplierID  = db.insert_id()
                    else: 
                        lastSupplierID = cursor.fetchone()[0]
                        cursor._clear_result()

                    # Adds the ingredient into database if the supplier_id and item code as a pair don't already exist in the database. If they do, finds the ingredient id and stores as lastIngID
                    sameSpecificName = cursor.execute("SELECT * FROM ingredient WHERE supplier_id = (%s) AND supplier_ing_item_code = (%s)", (lastSupplierID, itemCode))
                    if sameSpecificName == 0:
                        cursor.execute("INSERT IGNORE INTO ingredient(ing_common_name, supplier_id, ing_specific_name, supplier_ing_item_code, ingredient_statement, notes) VALUES (%s, %s, %s, %s, %s, %s)", (cName, lastSupplierID, sName, itemCode, self.ingredientStatementLineEdit.text(), self.notesLineEdit.text()))
                        lastIngID = db.insert_id()
                    else: 
                        cursor.execute("SELECT * FROM ingredient WHERE ing_common_name = (%s) AND supplier_id = (%s)", (cName, lastSupplierID))
                        lastIngID = cursor.fetchone()[0]

                        # could make this fetch all instead and have popup window for user to choose 
                        #lastIngID = cursor.fetchAll()
                    #cursor.commit()

            # Adds information from nutrients tab into database
            with db.cursor() as cursor:
                perGrams = self.perGramsSpinBox.value()
                for nutrient in nutrientMap: 
                    if nutrient['value']: 
                        cursor.execute("INSERT INTO ing_nutrient(ing_id, nutrient_id, nutrient_weight, per_weight) VALUES (%s, %s, %s, %s)", (lastIngID, nutrient['nutrient_id'], nutrient['value'], perGrams,))
                #cursor.commit()

            # Adds allergens into database
            with db.cursor() as cursor: 
                for allergen in allergenMap:
                    input = allergen['object']
                    if input.isChecked(): 
                        cursor.execute("INSERT INTO ing_allergens(ing_id, allergen) VALUES (%s, %s)", (lastIngID, allergen['allergen']))
                #cursor.commit()  

            # inserts claims into database
            with db.cursor() as cursor: 
                for claim in claimMap: 
                    box = claim['object']
                    if box.isChecked(): 
                        cursor.execute("INSERT INTO ing_claims(ing_id, claim) VALUES (%s, %s)", (lastIngID, claim['claim']))

                #cursor.commit()       
            
            # inserts ingredient documents into database
            with db.cursor() as cursor:
                for row in range(self.filesToBeUploadedTableWidget.rowCount()):
                    fileName = self.filesToBeUploadedTableWidget.itemAt(row, 0).text()
                    fileName
                    date = self.filesToBeUploadedTableWidget.itemAt(row, 1).text()
                    filePath = self.filesToBeUploadedTableWidget.itemAt(row, 2).text()
                    cursor.execute("INSERT IGNORE INTO ing_docs(ing_id, doc_name, doc_file, upload_date) VALUES (%s, %s, %s, %s)", (lastIngID, fileName, filePath, date))

            # inserts ingredient categores into database
            with db.cursor() as cursor:
                for row in range(self.groupListWidget.count()):
                    item = self.groupListWidget.item(row)
                    if item.checkState(Qt.Checked):
                        catID = self.groupListWidget.item(row).data(1)
                        cursor.execute("INSERT INTO ing_category(ing_id, category_id) VALUES (%s, %s)", (lastIngID, catID))
                    else:
                        pass

            print('Everything went right')

        except: 
            print('something went wrong')
        else:
            print('THIS DOESN"T NEED FIXING')'''