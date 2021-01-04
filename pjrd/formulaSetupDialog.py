# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulaSetupDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
import os


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

sys.path.append('../pjrd')
from pjrd.helpers import test, dbConnection
from pjrd.formulaEditor import formulaEditorDialog

os.environ['QT_MAC_WANTS_LAYER'] = '1' 

class formulaSetupDialog(QDialog):

    def __init__(self, mainWindow):
        super(formulaSetupDialog, self).__init__()
        self.mainWindow = mainWindow
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
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.close)




        #self.buttonBox.accepted.connect(formulaSetupDialog.accept)
        #self.buttonBox.rejected.connect(formulaSetupDialog.close)

        ##
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
        """
        -----------------------------
            Purpose:
                -  Event setup, QModel data fill
            Arguments:
                -  None
            Return Value:
                -  None
        """
        # creates the item models for the category boxes
        categoryModel = QStandardItemModel()
        with dbConnection('FormulaSchema').cursor() as cursor:
            cursor.execute('SELECT DISTINCT category_name, category.category_id FROM formula INNER JOIN category ON formula.formula_category_id = category.category_id')
            categories = cursor.fetchall()
            for category in categories:
                categoryItem = QStandardItem()
                categoryItem.setText(category['category_name'])
                categoryItem.setData(category, Qt.UserRole)
                categoryModel.appendRow(categoryItem)
        self.newCategoryComboBox.setModel(categoryModel)
        self.revisionCategoryComboBox.setModel(categoryModel)
        self.revisionCategoryComboBox.setCurrentIndex(-1)

        # signal setup
        self.revisionCategoryComboBox.currentIndexChanged.connect(self.comboBoxUpdate)
        self.formulasToDateComboBox.currentIndexChanged.connect(self.updatePlaceholderLabel)

    def comboBoxUpdate(self):
        """
        -----------------------------
            Purpose:
                -  Signal setup 
            Arguments:
                -  None
            Return Value:
                -  None
        """
        
        revisionComboboxSelection = self.revisionCategoryComboBox.itemData(self.revisionCategoryComboBox.currentIndex(), Qt.UserRole)
        if revisionComboboxSelection is None:
            return
        else:
            categoryID = revisionComboboxSelection['category_id']
        if categoryID is None:
            return
        prevFormulasModel = QStandardItemModel()

        blankItem = QStandardItem()
        blankItem.setText('SELECT')
        blankItem.setEditable(False)
        blankItem.setData(0, Qt.UserRole)
        prevFormulasModel.appendRow(blankItem)

        # fills the data from 
        with dbConnection('FormulaSchema').cursor() as cursor:
            cursor.execute('SELECT formula.formula_id, formula_name, formula.version_number, formula.formula_category_id, formula.version_of_id, category.category_name, category.category_id FROM formula LEFT JOIN category ON category.category_id = formula.formula_category_id WHERE formula.formula_category_id = %s', (categoryID,))
            formulas = cursor.fetchall()
            for formula in formulas:
                formulaItem = QStandardItem()
                formulaItem.setText(formula['formula_name'].title())
                formulaItem.setData(formula, Qt.UserRole)
                prevFormulasModel.appendRow(formulaItem)
        self.formulasToDateComboBox.setModel(prevFormulasModel)    

    # updates the version number label 
    def updatePlaceholderLabel(self):
        """
        -----------------------------
            Purpose:
                -  Updates the version number label
            Arguments:
                -  None
            Return Value:
                -  None
        """
        
        itemData = self.formulasToDateComboBox.itemData(self.formulasToDateComboBox.currentIndex(), Qt.UserRole)
        if itemData == 0 or itemData is None:
            return
        versionNumber = itemData['version_number']
        if versionNumber:
            self.previousVersionPlaceholderLabel.setText(str(versionNumber))
        else:
            self.previousVersionPlaceholderLabel.setText('None')

    # form accept
    def accept(self):
        """
        -----------------------------
            Purpose:
                -  Method for calling the Formula Editor window 
            Arguments:
                -  None
            Return Value:
                -  None
        """

        # if neither new formula or revision is indicated, throws an error message and returns
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
                    name = self.formulaNameLineEdit.text().title()
                    formulaEditor = formulaEditorDialog(self.mainWindow, formulaName = name, revision = False, category = self.newCategoryComboBox.currentText())
                    self.close()
                    formulaEditor.exec_()
            else:
                # if formula is a revision, but no previous formula was chosen
                if self.formulasToDateComboBox.currentIndex() == -1:
                    msg = QMessageBox()
                    msg.setText('Select a previous formula that you are revising')
                    msg.exec_()
                    return
                # if everything goes right
                else:
                    prevID = self.formulasToDateComboBox.currentData(Qt.UserRole)['version_number']
                    prevName = self.formulasToDateComboBox.currentText().title()
                    #if isRevision is False:
                    formulaEditor = formulaEditorDialog(self.mainWindow, formulaName = prevName, revision = isRevision, prevRevisionID = prevID, category = self.revisionCategoryComboBox.currentText())
                        
                    formulaEditor.exec_()
                    self.close()
                    
'''
app = QApplication(sys.argv)
gui = formulaSetupDialog(app)
gui.show()
sys.exit(app.exec_())
#test(formulaSetupDialog)'''