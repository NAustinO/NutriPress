# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirmAddDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from helpers import connectDB

class confirmationDialog(object):

    def __init__(self):
        super(confirmationDialog, self).__init__()
        self.setupUi(self)

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
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

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

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.weightLineEdit)

        self.label_6 = QLabel(self.containerFrame)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.unitComboBox = QComboBox(self.containerFrame)
        self.unitComboBox.setObjectName(u"unitComboBox")
        self.unitComboBox.setEditable(False)
        self.unitComboBox.setMaxVisibleItems(15)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.unitComboBox)


        self.verticalLayout_2.addWidget(self.containerFrame)


        self.verticalLayout.addWidget(self.frame_3)

        self.buttonBox = QDialogButtonBox(confirmationDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(confirmationDialog)
        self.buttonBox.accepted.connect(confirmationDialog.accept)
        self.buttonBox.rejected.connect(confirmationDialog.reject)

        QMetaObject.connectSlotsByName(confirmationDialog)
    # setupUi

    def retranslateUi(self, confirmationDialog):
        confirmationDialog.setWindowTitle(QCoreApplication.translate("confirmationDialog", u"Confirm", None))
        self.label.setText(QCoreApplication.translate("confirmationDialog", u"Please confirm the ingredient and specify the weight added to the formula", None))
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
    # retranslateUi

