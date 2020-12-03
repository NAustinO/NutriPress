# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirmAddDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys, os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
sys.path.append(sys.path.append('../pjrd'))
from helpers import dbConnection, TimedMessageBox
from pjrd.helperClasses import Ingredient, UnitOfMeasure, FormulaIngredient


class confirmationDialog(QDialog):

    def __init__(self, root, ingredient: Ingredient):
        self.ingredient = ingredient
        super(confirmationDialog, self).__init__()
        self.root = root
        self.setupUi(self)
        self.setupFromSearchResultsDialog(ingredient)
        self.setupLogic()

    '''
    CALLED: called during setup of the dialog (__init__())
    '''
    def setupUi(self, confirmationDialog):
        if not confirmationDialog.objectName():
            confirmationDialog.setObjectName(u"confirmationDialog")
        confirmationDialog.resize(500, 333)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(confirmationDialog.sizePolicy().hasHeightForWidth())
        confirmationDialog.setSizePolicy(sizePolicy)
        confirmationDialog.setMaximumSize(QSize(500, 333))
        confirmationDialog.setSizeGripEnabled(False)
        self.verticalLayout = QVBoxLayout(confirmationDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(confirmationDialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.HLine)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.headerLabel = QLabel(self.frame_3)
        self.headerLabel.setObjectName(u"headerLabel")
        self.headerLabel.setAutoFillBackground(True)
        self.headerLabel.setAlignment(Qt.AlignCenter)
        self.headerLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.headerLabel)

        self.containerFrame = QFrame(self.frame_3)
        self.containerFrame.setObjectName(u"containerFrame")
        self.containerFrame.setAutoFillBackground(True)
        self.formLayout = QFormLayout(self.containerFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(self.containerFrame)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.nameLabel)

        self.namePlaceholderLabel = QLabel(self.containerFrame)
        self.namePlaceholderLabel.setObjectName(u"namePlaceholderLabel")
        

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.namePlaceholderLabel)

        self.specificNameLabel = QLabel(self.containerFrame)
        self.specificNameLabel.setObjectName(u"specificNameLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.specificNameLabel)

        self.specificNamePlaceholderLabel = QLabel(self.containerFrame)
        self.specificNamePlaceholderLabel.setObjectName(u"specificNamePlaceholderLabel")
        

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.specificNamePlaceholderLabel)

        self.supplierLabel = QLabel(self.containerFrame)
        self.supplierLabel.setObjectName(u"supplierLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.supplierLabel)

        self.supplierPlaceholderLabel = QLabel(self.containerFrame)
        self.supplierPlaceholderLabel.setObjectName(u"supplierPlaceholderLabel")
        

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.supplierPlaceholderLabel)

        self.supplierCodeLabel = QLabel(self.containerFrame)
        self.supplierCodeLabel.setObjectName(u"supplierCodeLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.supplierCodeLabel)

        self.supplierCodePlaceholderLabel = QLabel(self.containerFrame)
        self.supplierCodePlaceholderLabel.setObjectName(u"supplierCodePlaceholderLabel")
        

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.supplierCodePlaceholderLabel)

        self.label_7 = QLabel(self.containerFrame)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.weightLineEdit = QLineEdit(self.containerFrame)
        self.weightLineEdit.setObjectName(u"weightLineEdit")
        self.weightLineEdit.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.weightLineEdit.setPlaceholderText("Numbers only")
        self.weightLineEdit.setFocusPolicy(Qt.StrongFocus)
       

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.weightLineEdit)

        self.label_6 = QLabel(self.containerFrame)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.unitComboBox = QComboBox(self.containerFrame)
        self.unitComboBox.setObjectName(u"unitComboBox")
        self.unitComboBox.setMaxVisibleItems(15)
        self.unitComboBox.setEditable(True)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.unitComboBox)


        self.verticalLayout_2.addWidget(self.containerFrame)


        self.verticalLayout.addWidget(self.frame_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelPushBtn = QPushButton(confirmationDialog)
        self.cancelPushBtn.setObjectName(u"cancelPushBtn")
        self.cancelPushBtn.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout.addWidget(self.cancelPushBtn)

        self.okPushBtn = QPushButton(confirmationDialog)
        self.okPushBtn.setObjectName(u"okPushBtn")
        self.okPushBtn.setFocusPolicy(Qt.StrongFocus)

        self.horizontalLayout.addWidget(self.okPushBtn)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.setTabOrder(self.weightLineEdit, self.unitComboBox)
        self.setTabOrder(self.unitComboBox, self.cancelPushBtn)
        self.setTabOrder(self.cancelPushBtn, self.okPushBtn)
        
        self.retranslateUi(confirmationDialog)

        QMetaObject.connectSlotsByName(confirmationDialog)

        ##################
        self.weightLineEdit.setValidator(QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+")))
    # setupUi

    '''
    CALLED: called during setup of the dialog (setupUi())
    '''
    def retranslateUi(self, confirmationDialog):
        confirmationDialog.setWindowTitle(QCoreApplication.translate("confirmationDialog", u"Confirm", None))
        self.headerLabel.setText(QCoreApplication.translate("confirmationDialog", u"Please confirm the ingredient and specify the weight added to the formula", None))
        self.nameLabel.setText(QCoreApplication.translate("confirmationDialog", u"Ingredient Name", None))
        self.namePlaceholderLabel.setText("")
        self.specificNameLabel.setText(QCoreApplication.translate("confirmationDialog", u"Specific Name", None))
        self.specificNamePlaceholderLabel.setText("")
        self.supplierLabel.setText(QCoreApplication.translate("confirmationDialog", u"Supplier", None))
        self.supplierPlaceholderLabel.setText("")
        self.supplierCodeLabel.setText(QCoreApplication.translate("confirmationDialog", u"Supplier Code", None))
        self.supplierCodePlaceholderLabel.setText("")
        self.label_7.setText(QCoreApplication.translate("confirmationDialog", u"Weight", None))
        self.label_6.setText(QCoreApplication.translate("confirmationDialog", u"Unit", None))
        self.cancelPushBtn.setText(QCoreApplication.translate("confirmationDialog", u"Cancel", None))
        self.okPushBtn.setText(QCoreApplication.translate("confirmationDialog", u"Ok", None))
    # retranslateUi

    '''
    CALLED: called during setup of the dialog (__init__())
    PURPOSE: links the events and signal/slots
    '''
    def setupLogic(self):
        # sets up signals
        self.okPushBtn.clicked.connect(self.submit)
        self.cancelPushBtn.clicked.connect(self.cancelEvent)

        # setup events
        self.installEventFilter(self)

        # setup unit of measure combobox completer and data
        with dbConnection('FormulaSchema').cursor() as cursor:
            completer = QCompleter()
            model = QStandardItemModel()
            cursor.execute('SELECT unit_id, unit_name, unit_symbol, conversion_factor, conversion_offset FROM unit WHERE unit_class = "mass" ORDER BY conversion_factor ASC')
            uoms = cursor.fetchall()
            for uom in uoms:
                unit = UnitOfMeasure(uom['unit_id'], uom['unit_name'], uom['conversion_factor'], uom['conversion_offset'], uom['unit_symbol'])
                unit.setText('{unitName} ({unitSymbol})'.format(unitName=uom['unit_name'], unitSymbol = uom['unit_symbol']))
                model.appendRow(unit)
            completer.setModel(model)
            completer.setCompletionMode(QCompleter.InlineCompletion)
            self.unitComboBox.setCompleter(completer)
            self.unitComboBox.setModel(model)
            self.unitComboBox.setCurrentIndex(-1)

    '''
    CALLED: called during setup of the dialog (__init__())
    PURPOSE: Takes in the food dictionary data that is passed when creating the confirmationDialog. Inputs the relevant information to placeholder labels in order to remind user of their choice
    '''
    def setupFromSearchResultsDialog(self, ingredient: Ingredient):

        # ingredient name label
        self.namePlaceholderLabel.setText(ingredient.desc)  

        # update specific name if exists
        if ingredient.specificName is None:
            self.specificNamePlaceholderLabel.setText('-')
        else:
            self.specificNamePlaceholderLabel.setText(ingredient.specificName)

        # update supplier name if exists
        if ingredient.supplierName is None:
            self.supplierPlaceholderLabel.setText('-')
        else:
            self.supplierPlaceholderLabel.setText(ingredient.supplierName)

        # update supplier item code if exists
        if ingredient.supplierItemCode is None:
            self.supplierCodePlaceholderLabel.setText('-')
        else:
            self.supplierCodePlaceholderLabel.setText(ingredient.supplierItemCode)
   
    '''# event filter to listen for return button '''
    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress and source == self and event.key() == Qt.Key_Return: 
            self.submit()
            return True
        return False

    '''
    PURPOSE: submits the form, adds the data and fills to the formula editor table.
    CALLED: from eventFilter(), when okPushBtn.clicked (setupLogic()) 
    ON SUCCESS: closes the confirmation dialog, allowing another addition
    '''
    def submit(self):
        # validates for float input and that is a unit from box is chosen
        if self.validatedInput() is False:
            return

        # if validated
        else:
            unit = self.unitComboBox.currentData(Qt.UserRole)
            if unit is None:
                return
        
            # adds information to dictionary
            self.ingredient.inputWeight = float(self.weightLineEdit.text())
            self.ingredient.unit = unit
            '''self.ingredient['weight_in_g'] = (weight + unit['conversion_offset']) * unit['conversion_factor']''' # TODO This will potentially cause problems for (IU for VIT A in unit table)

            self.root.formula.addIngredient(self.ingredient)

            #updates the table widget in the formula editor window
            rowCount = self.root.ingTabFormulaTableWidget.rowCount()
            rowIndex = self.root.ingTabFormulaTableWidget.rowCount() - 1
            if rowCount == 0:
                rowIndex = 0
            itemWithData = QTableWidgetItem()
            itemWithData.setData(Qt.UserRole, self.ingredient)
            itemWithData.setText(self.ingredient.desc)
            self.root.ingTabFormulaTableWidget.insertRow(rowIndex)
            self.root.ingTabFormulaTableWidget.setItem(rowIndex, 0, itemWithData)
            self.root.ingTabFormulaTableWidget.setItem(rowIndex, 2, QTableWidgetItem(self.weightLineEdit.text()))
            self.root.ingTabFormulaTableWidget.setItem(rowIndex, 3, QTableWidgetItem(self.unitComboBox.currentText()))
            self.root.ingTabFormulaTableWidget.setItem(rowIndex, 4, QTableWidgetItem(self.supplierPlaceholderLabel.text()))
            self.root.ingTabFormulaTableWidget.update()
            self.root.refresh()
            self.root.update()

            # popup window with timer to confirm successful addition
            msg = TimedMessageBox(timeout = 3)
            msg.setText('Successfully added ingredient. You can add another or return to editor')
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            self.close()
            msg.exec_()
 
    '''
    PURPOSE: validates the user input
    RETURN: Returns true if user input is validated, returns false if not valid
    '''
    # returns true if the user input for this window is valid, otherwise returns false
    def validatedInput(self):
        try:
            weight = float(self.weightLineEdit.text()) #TODO error handling
        except ValueError:
            msg = QMessageBox()
            msg.setText("Weight of ingredient must be a number")
            msg.exec_()
            return False
        else:
            if (self.unitComboBox.currentIndex() == -1):
                msg = QMessageBox()
                msg.setText("Must choose a unit")
                msg.exec_()
                return False
            return True
        
    
    '''
    PURPOSE: Event handler to confirm whether the user wants to exit the dialog without adding the ingredient to the formula
    Calls a message box, allowing user to confirm before exiting
    '''
    def cancelEvent(self):
        confirm = QMessageBox().question(self, 'Confirm cancellation', 'Are you sure you want to cancel?', QMessageBox.Yes|QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.close()
