# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulaSetupDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import pymysql

sys.path.append('../pjrd')
from helpers import test
from formulaEditor import formulaEditorDialog

class formulaSetupDialog(QDialog):

    def __init__(self):
        super(formulaSetupDialog, self).__init__()
        self.setupUi(self)
        self.setupLogic()

    def setupUi(self, formulaSetupDialog):
        if not formulaSetupDialog.objectName():
            formulaSetupDialog.setObjectName(u"formulaSetupDialog")
        formulaSetupDialog.resize(672, 419)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(formulaSetupDialog.sizePolicy().hasHeightForWidth())
        formulaSetupDialog.setSizePolicy(sizePolicy)
        formulaSetupDialog.setMaximumSize(QSize(678, 419))
        self.verticalLayout = QVBoxLayout(formulaSetupDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dialogHeaderLabel = QLabel(formulaSetupDialog)
        self.dialogHeaderLabel.setObjectName(u"dialogHeaderLabel")
        font = QFont()
        font.setPointSize(13)
        self.dialogHeaderLabel.setFont(font)
        self.dialogHeaderLabel.setAutoFillBackground(True)
        self.dialogHeaderLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dialogHeaderLabel)

        self.line_2 = QFrame(formulaSetupDialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.headerFrame = QFrame(formulaSetupDialog)
        self.headerFrame.setObjectName(u"headerFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy1)
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.revisionPromptLabel = QLabel(self.headerFrame)
        self.revisionPromptLabel.setObjectName(u"revisionPromptLabel")

        self.horizontalLayout_2.addWidget(self.revisionPromptLabel)

        self.headerRadioBtnContainer = QWidget(self.headerFrame)
        self.headerRadioBtnContainer.setObjectName(u"headerRadioBtnContainer")
        self.horizontalLayout = QHBoxLayout(self.headerRadioBtnContainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.newFormulaRadioBtn = QRadioButton(self.headerRadioBtnContainer)
        self.newFormulaRadioBtn.setObjectName(u"newFormulaRadioBtn")

        self.horizontalLayout.addWidget(self.newFormulaRadioBtn)

        self.revisionRadioBtn = QRadioButton(self.headerRadioBtnContainer)
        self.revisionRadioBtn.setObjectName(u"revisionRadioBtn")

        self.horizontalLayout.addWidget(self.revisionRadioBtn)


        self.horizontalLayout_2.addWidget(self.headerRadioBtnContainer)


        self.verticalLayout.addWidget(self.headerFrame)

        self.bodyContainerWidget = QWidget(formulaSetupDialog)
        self.bodyContainerWidget.setObjectName(u"bodyContainerWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.bodyContainerWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.newFormulaContainerFrame = QFrame(self.bodyContainerWidget)
        self.newFormulaContainerFrame.setObjectName(u"newFormulaContainerFrame")
        self.newFormulaContainerFrame.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_3 = QVBoxLayout(self.newFormulaContainerFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formulaContainerLabel = QLabel(self.newFormulaContainerFrame)
        self.formulaContainerLabel.setObjectName(u"formulaContainerLabel")
        self.formulaContainerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.formulaContainerLabel)

        self.formulaNamePromptLabel = QLabel(self.newFormulaContainerFrame)
        self.formulaNamePromptLabel.setObjectName(u"formulaNamePromptLabel")

        self.verticalLayout_3.addWidget(self.formulaNamePromptLabel)

        self.formulaNameLineEdit = QLineEdit(self.newFormulaContainerFrame)
        self.formulaNameLineEdit.setObjectName(u"formulaNameLineEdit")

        self.verticalLayout_3.addWidget(self.formulaNameLineEdit)

        self.categoryLabel1 = QLabel(self.newFormulaContainerFrame)
        self.categoryLabel1.setObjectName(u"categoryLabel1")

        self.verticalLayout_3.addWidget(self.categoryLabel1)

        self.newCategoryComboBox = QComboBox(self.newFormulaContainerFrame)
        self.newCategoryComboBox.setObjectName(u"newCategoryComboBox")
        self.newCategoryComboBox.setEditable(True)

        self.verticalLayout_3.addWidget(self.newCategoryComboBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_4.addWidget(self.newFormulaContainerFrame)

        self.revisionContainerFrame = QFrame(self.bodyContainerWidget)
        self.revisionContainerFrame.setObjectName(u"revisionContainerFrame")
        self.revisionContainerFrame.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_2 = QVBoxLayout(self.revisionContainerFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.revisionContainerLabel = QLabel(self.revisionContainerFrame)
        self.revisionContainerLabel.setObjectName(u"revisionContainerLabel")
        self.revisionContainerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.revisionContainerLabel)

        self.categoryLabel2 = QLabel(self.revisionContainerFrame)
        self.categoryLabel2.setObjectName(u"categoryLabel2")

        self.verticalLayout_2.addWidget(self.categoryLabel2)

        self.revisionCategoryComboBox = QComboBox(self.revisionContainerFrame)
        self.revisionCategoryComboBox.setObjectName(u"revisionCategoryComboBox")
        self.revisionCategoryComboBox.setEditable(False)
        self.revisionCategoryComboBox.setInsertPolicy(QComboBox.NoInsert)

        self.verticalLayout_2.addWidget(self.revisionCategoryComboBox)

        self.revisedFormulaPromptLabel = QLabel(self.revisionContainerFrame)
        self.revisedFormulaPromptLabel.setObjectName(u"revisedFormulaPromptLabel")

        self.verticalLayout_2.addWidget(self.revisedFormulaPromptLabel)

        self.formulasToDateComboBox = QComboBox(self.revisionContainerFrame)
        self.formulasToDateComboBox.setObjectName(u"formulasToDateComboBox")
        self.formulasToDateComboBox.setEditable(True)
        self.formulasToDateComboBox.setInsertPolicy(QComboBox.NoInsert)

        self.verticalLayout_2.addWidget(self.formulasToDateComboBox)

        self.previousVersionLabel = QLabel(self.revisionContainerFrame)
        self.previousVersionLabel.setObjectName(u"previousVersionLabel")

        self.verticalLayout_2.addWidget(self.previousVersionLabel)

        self.previousVersionPlaceholderLabel = QLabel(self.revisionContainerFrame)
        self.previousVersionPlaceholderLabel.setObjectName(u"previousVersionPlaceholderLabel")

        self.verticalLayout_2.addWidget(self.previousVersionPlaceholderLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)


        self.horizontalLayout_4.addWidget(self.revisionContainerFrame)


        self.verticalLayout.addWidget(self.bodyContainerWidget)

        self.buttonBox = QDialogButtonBox(formulaSetupDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(formulaSetupDialog)
        self.buttonBox.accepted.connect(formulaSetupDialog.accept)
        self.buttonBox.rejected.connect(formulaSetupDialog.close)

        
        #####

        self.revisionContainerFrame.setDisabled(True)
        self.newFormulaContainerFrame.setDisabled(True)
        ###
        self.revisionRadioBtn.toggled.connect(self.newFormulaContainerFrame.setDisabled)
        self.revisionRadioBtn.toggled.connect(self.revisionContainerFrame.setEnabled)
        self.newFormulaRadioBtn.toggled.connect(self.revisionContainerFrame.setDisabled)
        self.newFormulaRadioBtn.toggled.connect(self.newFormulaContainerFrame.setEnabled)



        QMetaObject.connectSlotsByName(formulaSetupDialog)
    # setupUi

    def retranslateUi(self, formulaSetupDialog):
        formulaSetupDialog.setWindowTitle(QCoreApplication.translate("formulaSetupDialog", u"Setup", None))
        self.dialogHeaderLabel.setText(QCoreApplication.translate("formulaSetupDialog", u"Formula Setup", None))
        self.revisionPromptLabel.setText(QCoreApplication.translate("formulaSetupDialog", u"Is this a revision of a previous formula, or an entirely new formula?", None))
        self.newFormulaRadioBtn.setText(QCoreApplication.translate("formulaSetupDialog", u"New Formula", None))
        self.revisionRadioBtn.setText(QCoreApplication.translate("formulaSetupDialog", u"Revision", None))
        self.formulaContainerLabel.setText(QCoreApplication.translate("formulaSetupDialog", u"New Formula", None))
        self.formulaNamePromptLabel.setText(QCoreApplication.translate("formulaSetupDialog", u"What is the new formula name?", None))
        self.categoryLabel1.setText(QCoreApplication.translate("formulaSetupDialog", u"Category", None))
        self.revisionContainerLabel.setText(QCoreApplication.translate("formulaSetupDialog", u"Revision", None))
        self.categoryLabel2.setText(QCoreApplication.translate("formulaSetupDialog", u"Category", None))
        self.revisedFormulaPromptLabel.setText(QCoreApplication.translate("formulaSetupDialog", u"Select formula to be revised", None))
        self.previousVersionLabel.setText(QCoreApplication.translate("formulaSetupDialog", u"Previous Version", None))
        self.previousVersionPlaceholderLabel.setText("")
    # retranslateUi

    def setupLogic(self):
    
        self.map = {}
        # EXAMLE MAP
            # self.map {
                # 'bowl': {
                    # 'category_id': int
                    # 'model': QStandardItemModel
                    # 'completer': QCompleter
                    # },
            # }   

        # 0: create all categories model, all categories completer
        # A: puts category_name, category_id, catSpecific model, catSpecific completer --> map
        # B: category_name, category_id --------------------------------->  category item
        # B: map(category_name) --> catSpecific model, catSpecific completer --> category item
        # C: category item ----------------------------------------------> all categories model
        # D: all categories model --> all categories completer -----------> category combobox, revision combobox
        # E: formula_name, formula_id --> formula item -------------------> catSpecific model
        # E: category_name --> map(category_name) ------------------------> catSpecific model 

        # creates self.map to model and completer for each type of formula category
        # inputs models into category comboboxes for autocompletion and datamapping
        with pymysql.connect(host='localhost', user='root', password='Pj@bW1!G1-4', database='FormulaSchema', cursorclass=pymysql.cursors.DictCursor).cursor() as cursor:

            ############################## 0
            # instantiates new completer for the category combo box
            allCatCompleter = QCompleter()
            # instantiates new model for the category combo box 
            allCatModel = QStandardItemModel()
            ############################# /0

            # gets category name and id from database
            cursor.execute('SELECT DISTINCT category_name, category.category_id FROM formula INNER JOIN category ON formula.category_id = category.category_id')
            categories = cursor.fetchall()
            
            # category = {'category_name': 'bowl'}
            for category in categories:
                name = category['category_name']

                ######################### A --------> map 
                self.map[name] = {}  
                self.map[name]['category_id'] = category['category_id']
                self.map[name]['model'] = QStandardItemModel()
                self.map[name]['completer'] = QCompleter()
                ########################## /A

                ########################## B
                categoryItem = QStandardItem()
                categoryItem.setText(name.capitalize())
                # Qt.UserRole - category id
                categoryItem.setData(self.map[name]['category_id'], Qt.UserRole) 
                # Qt.UserRole + 1 - category name
                categoryItem.setData(name, Qt.UserRole + 1)
                # Qt.UserRole + 2 - category completer for past formulas that are part of category
                categoryItem.setData(self.map[name]['completer'], Qt.UserRole + 2)
                # Qt.userRole + 3 - category formulas model that stores formula specific data (id, name, etc)
                categoryItem.setData(self.map[name]['model'], Qt.UserRole + 3)
                ############################ /B

                ############################ C
                allCatModel.appendRow(categoryItem)
                ############################ /C

            ################################ D
            allCatCompleter.setCompletionMode(QCompleter.InlineCompletion)
            allCatCompleter.setModel(allCatModel)
            self.newCategoryComboBox.setModel(allCatModel)
            self.newCategoryComboBox.setCompleter(allCatCompleter)
            self.newCategoryComboBox.setCurrentIndex(-1)
            self.revisionCategoryComboBox.setModel(allCatModel)
            #self.revisionCategoryComboBox.setCompleter(allCatCompleter)
            self.revisionCategoryComboBox.setCurrentIndex(-1)
            ################################ /D

            ################################ E
            # adds formula information to the category model that it is applied to 
            cursor.execute('SELECT formula_id, formula_name, category_name, category.category_id FROM formula INNER JOIN category ON formula.category_id = category.category_id')
            results = cursor.fetchall()
            for result in results:
                category = result['category_name']
                formulaItem = QStandardItem()
                formulaItem.setText(result['formula_name'])
                formulaItem.setData(result['formula_id'], Qt.UserRole)
                self.map[category]['model'].appendRow(formulaItem)
            ################################ /E

        self.revisionCategoryComboBox.currentIndexChanged.connect(self.comboBoxUpdate)

    def comboBoxUpdate(self, isUpdated=False):
        if isUpdated is False:
            isUpdated = True
            return
        text = self.revisionCategoryComboBox.itemData(self.revisionCategoryComboBox.currentIndex(), Qt.UserRole + 1)
        completer = self.map[text]['completer']
        model = self.map[text]['model']
        completer.setModel(model)
        completer.setCompletionMode(QCompleter.PopupCompletion)
        completer.setMaxVisibleItems(50)
        self.formulasToDateComboBox.setCompleter(completer)
        self.formulasToDateComboBox.setModel(model)
        self.formulasToDateComboBox.setCurrentIndex(-1)

    # TODO 
    def updatePlaceholderLabels(self):
        with pymysql.connect(host='localhost', user='root', password='Pj@bW1!G1-4', database='FormulaSchema', cursorclass=pymysql.cursors.DictCursor) as cursor:
            pass
        
    # called form accept
    def accept(self):
        # error checking
        if self.revisionRadioBtn.isChecked() is False and self.newFormulaRadioBtn.isChecked() is False:
            msg = QMessageBox()
            msg.setText('Please indicate whether this formula is new or a revision/iteration')
            msg.exec_()
            return
        else:
            isRevision = self.revisionRadioBtn.isChecked()

            if isRevision is False:
                # if the formula is new but no name was inputted
                if self.formulaNameLineEdit.text() == '' or self.formulaNameLineEdit.text() is None:
                    msg = QMessageBox()
                    msg.setText('Input a formula name to continue')
                    msg.exec_()
                    return

                # if everything goes right
                else:
                    name = self.formulaNameLineEdit.text()
                    formulaEditor = formulaEditorDialog(isRevision, formulaName = name)
                    formulaEditor.exec_()
                    self.close()

            else:
                # if formula is a revision, but no previous formula was chosen
                if self.formulasToDateComboBox.currentIndex() == -1:
                    msg = QMessageBox()
                    msg.setText('Select a previous formula that you are revising')
                    msg.exec_()
                    return

                # if everything goes right
                else:
                    prevID = self.formulasToDateComboBox.currentData(Qt.UserRole)
                    prevName = self.formulasToDateComboBox.currentText()
                    formulaEditor = formulaEditorDialog(isRevision,formulaName = prevName, prevRevisionID =  'prevID') #<<<< debug
                    formulaEditor.exec_()
                    self.close()
                    

'''app = QApplication(sys.argv)
gui = formulaSetupDialog()
gui.show()
sys.exit(app.exec_())
#test(formulaSetupDialog)'''