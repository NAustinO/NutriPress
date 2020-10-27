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
from helpers import test

class formulaSetupDialog(QDialog):

    def __init__(self):
        super(formulaSetupDialog, self).__init__()
        self.setupUi(self)

    def setupUi(self, formulaSetupDialog):
        if not formulaSetupDialog.objectName():
            formulaSetupDialog.setObjectName(u"formulaSetupDialog")
        formulaSetupDialog.resize(678, 419)
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
        self.gridLayout = QGridLayout(self.newFormulaContainerFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formulaContainerLabel = QLabel(self.newFormulaContainerFrame)
        self.formulaContainerLabel.setObjectName(u"formulaContainerLabel")
        self.formulaContainerLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.formulaContainerLabel, 0, 0, 1, 1, Qt.AlignTop)

        self.formulaNameLineEdit = QLineEdit(self.newFormulaContainerFrame)
        self.formulaNameLineEdit.setObjectName(u"formulaNameLineEdit")

        self.gridLayout.addWidget(self.formulaNameLineEdit, 3, 0, 1, 1)

        self.formulaNamePromptLabel = QLabel(self.newFormulaContainerFrame)
        self.formulaNamePromptLabel.setObjectName(u"formulaNamePromptLabel")

        self.gridLayout.addWidget(self.formulaNamePromptLabel, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.newFormulaContainerFrame)

        self.revisionContainerFrame = QFrame(self.bodyContainerWidget)
        self.revisionContainerFrame.setObjectName(u"revisionContainerFrame")
        self.revisionContainerFrame.setFrameShape(QFrame.StyledPanel)
        self.gridLayout_2 = QGridLayout(self.revisionContainerFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.previousVersionLabel = QLabel(self.revisionContainerFrame)
        self.previousVersionLabel.setObjectName(u"previousVersionLabel")

        self.gridLayout_2.addWidget(self.previousVersionLabel, 4, 0, 1, 1)

        self.revisionContainerLabel = QLabel(self.revisionContainerFrame)
        self.revisionContainerLabel.setObjectName(u"revisionContainerLabel")
        self.revisionContainerLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.revisionContainerLabel, 0, 0, 1, 2)

        self.revisedFormulaPromptLabel = QLabel(self.revisionContainerFrame)
        self.revisedFormulaPromptLabel.setObjectName(u"revisedFormulaPromptLabel")

        self.gridLayout_2.addWidget(self.revisedFormulaPromptLabel, 2, 0, 1, 1)

        self.formulasToDateComboBox = QComboBox(self.revisionContainerFrame)
        self.formulasToDateComboBox.setObjectName(u"formulasToDateComboBox")

        self.gridLayout_2.addWidget(self.formulasToDateComboBox, 3, 0, 1, 1)

        self.differencesPrompt = QLabel(self.revisionContainerFrame)
        self.differencesPrompt.setObjectName(u"differencesPrompt")

        self.gridLayout_2.addWidget(self.differencesPrompt, 7, 0, 1, 1)

        self.differencesTextEdit = QTextEdit(self.revisionContainerFrame)
        self.differencesTextEdit.setObjectName(u"differencesTextEdit")

        self.gridLayout_2.addWidget(self.differencesTextEdit, 8, 0, 1, 1)

        self.previousVersionPlaceholderLabel = QLabel(self.revisionContainerFrame)
        self.previousVersionPlaceholderLabel.setObjectName(u"previousVersionPlaceholderLabel")

        self.gridLayout_2.addWidget(self.previousVersionPlaceholderLabel, 5, 0, 1, 1)


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
        self.previousVersionLabel.setText(QCoreApplication.translate("formulaSetupDialog", u"Previous Version", None))
        self.revisionContainerLabel.setText(QCoreApplication.translate("formulaSetupDialog", u"Revision", None))
        self.revisedFormulaPromptLabel.setText(QCoreApplication.translate("formulaSetupDialog", u"Select formula to be revised", None))
        self.differencesPrompt.setText(QCoreApplication.translate("formulaSetupDialog", u"Differences from previous version (optional)", None))
        self.previousVersionPlaceholderLabel.setText("")
    # retranslateUi



test(formulaSetupDialog)