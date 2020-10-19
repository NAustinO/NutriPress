# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'self.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QCoreApplication, Qt, QMetaObject, QSize, QRect
from PyQt5.QtWidgets import QSizePolicy, QAction, QMenu, QMdiArea, QVBoxLayout, QGridLayout, QWidget, QFrame, QLabel, QCheckBox, QLineEdit, QSpinBox, QPushButton, QListView, QSpacerItem, QApplication, QMainWindow, QStatusBar, QTabWidget, QMessageBox, QDialog, QMenuBar, QComboBox

from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *


#from addIngredient import addIngredientDialog
from helpers import connectDB
from add_ingredient import addIngredientDialog

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi()
        try:
            self.db = connectDB()
        except:
            QMessageBox.about(self, 'Connection', 'Database Connection Failed')
        else:
            QMessageBox.about(self, 'Connection', 'Database Connection Successful')
  
    def addIngEvent(self):
        widget = addIngredientDialog()
        widget.show()
        widget.exec_()

    def closeEvent(self, event):

        toClose = QMessageBox.question(self, 'Confirm Exit', 'Exit Program?', QMessageBox.Yes | QMessageBox.No)
        if toClose == QMessageBox.Yes:
            print('Exited the program')
            event.accept()
        else:
            event.ignore()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"self")
        self.resize(1114, 985)
        self.setMinimumSize(QSize(500, 500))
        icon = QIcon()
        icon.addFile(u"pjrd/static/media/pjgraphiclogo.png", QSize(), QIcon.Normal, QIcon.On)
        self.setWindowIcon(icon)
    
        self.actionExit = QAction(self)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAddRecipe = QAction(self)
        self.actionAddRecipe.setObjectName(u"actionAddRecipe")
        self.actionAddIngredient = QAction(self)
        self.actionAddIngredient.setObjectName(u"actionAddIngredient")
        self.actionOpen = QAction(self)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(self)
        self.actionSave.setObjectName(u"actionSave")
        self.actionLogout = QAction(self)
        self.actionLogout.setObjectName(u"actionLogout")
        self.mainWindowWidget = QWidget(self)
        self.mainWindowWidget.setObjectName(u"mainWindowWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWindowWidget.sizePolicy().hasHeightForWidth())
        self.mainWindowWidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.mainWindowWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.mainWindowWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mdiArea = QMdiArea(self.tab)
        self.mdiArea.setObjectName(u"mdiArea")

        self.verticalLayout.addWidget(self.mdiArea)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.widget = QWidget(self.tab_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1051, 931))
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

        self.leftNavBarWidget = QWidget(self.mainWindowWidget)
        self.leftNavBarWidget.setObjectName(u"leftNavBarWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftNavBarWidget.sizePolicy().hasHeightForWidth())
        self.leftNavBarWidget.setSizePolicy(sizePolicy1)
        self.leftNavBarWidget.setMaximumSize(QSize(200, 16777215))
        self.leftNavBarWidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_3 = QVBoxLayout(self.leftNavBarWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.pjLogoHeader = QLabel(self.leftNavBarWidget)
        self.pjLogoHeader.setObjectName(u'pjLogoLoginHeader')
        self.pjLogoHeader.setMinimumSize(QSize(0, 16))
        self.pjLogoHeader.setMaximumSize(QSize(100, 100))
        self.pjLogoHeader.setPixmap(QPixmap(u'pjrd/static/media/pjgraphiclogo.png'))
        self.pjLogoHeader.setScaledContents(True)
        self.verticalLayout_3.addWidget(self.pjLogoHeader, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.loginHeader = QLabel(self.leftNavBarWidget)
        self.loginHeader.setText(u'You are logged in as: USER EMAIL HERE')
        self.loginHeader.setWordWrap(True)
        self.loginHeader.setObjectName(u"loginHeader")
        self.loginHeader.setMinimumSize(QSize(0, 16))
        self.loginHeader.setMaximumSize(QSize(100, 100))
        self.loginHeader.setPixmap(QPixmap(u"../pjrd/static/media/pjgraphiclogo.png"))
        self.loginHeader.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.loginHeader, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.loginStatus = QLabel(self.leftNavBarWidget)
        self.loginStatus.setObjectName(u"loginStatus")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.loginStatus.sizePolicy().hasHeightForWidth())
        self.loginStatus.setSizePolicy(sizePolicy2)
        self.loginStatus.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.loginStatus)

        self.quickSearchBtn = QLineEdit(self.leftNavBarWidget)
        self.quickSearchBtn.setObjectName(u"quickSearchBtn")

        self.verticalLayout_3.addWidget(self.quickSearchBtn)

        self.verticalSpacer_2 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.quickAddLabel = QLabel(self.leftNavBarWidget)
        self.quickAddLabel.setObjectName(u"quickAddLabel")

        self.verticalLayout_3.addWidget(self.quickAddLabel, 0, Qt.AlignHCenter)

        self.quickAddFormulaBtn = QPushButton(self.leftNavBarWidget)
        self.quickAddFormulaBtn.setObjectName(u"quickAddFormulaBtn")
        self.quickAddFormulaBtn.setFlat(False)

        self.verticalLayout_3.addWidget(self.quickAddFormulaBtn)

        self.quickAddIngrBtn = QPushButton(self.leftNavBarWidget)
        self.quickAddIngrBtn.setObjectName(u"quickAddIngrBtn")
        self.quickAddIngrBtn.clicked.connect(self.addIngEvent)

        self.verticalLayout_3.addWidget(self.quickAddIngrBtn)

        self.quickAddDocBtn = QPushButton(self.leftNavBarWidget)
        self.quickAddDocBtn.setObjectName(u"quickAddDocBtn")

        self.verticalLayout_3.addWidget(self.quickAddDocBtn)

        self.quickAddScoreBtn = QPushButton(self.leftNavBarWidget)
        self.quickAddScoreBtn.setObjectName(u"quickAddScoreBtn")

        self.verticalLayout_3.addWidget(self.quickAddScoreBtn)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.quickOpenLabel = QLabel(self.leftNavBarWidget)
        self.quickOpenLabel.setObjectName(u"quickOpenLabel")
        self.quickOpenLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.quickOpenLabel)

        self.quickFormulaAccess = QListView(self.leftNavBarWidget)
        self.quickFormulaAccess.setObjectName(u"quickFormulaAccess")
        self.quickFormulaAccess.setMouseTracking(True)

        self.verticalLayout_3.addWidget(self.quickFormulaAccess)


        self.gridLayout.addWidget(self.leftNavBarWidget, 0, 0, 2, 1)

        self.setCentralWidget(self.mainWindowWidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1114, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAdd = QMenu(self.menuFile)
        self.menuAdd.setObjectName(u"menuAdd")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuDatabase = QMenu(self.menubar)
        self.menuDatabase.setObjectName(u"menuDatabase")
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menubar.setNativeMenuBar(False)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.menuAdd.menuAction())
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addAction(self.actionExit)
        self.actionExit.triggered.connect(self.closeEvent)  ####### <----------------- Does not work properly
        self.menuFile.addSeparator()
        self.menuAdd.addAction(self.actionAddRecipe)
        self.menuAdd.addAction(self.actionAddIngredient)

        # adds shortcuts
        self.actionSave.setShortcut('Ctrl+S')
        self.actionOpen.setShortcut('Ctrl+O')
        self.actionExit.setShortcut('Ctrl+Q')

        self.retranslateUi()

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("self", u"Pressed Juicery R&D", None))
        self.actionExit.setText(QCoreApplication.translate("self", u"Quit", None))
        #if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("self", u"Meta+Q", None))
        #endif // QT_CONFIG(shortcut)
        self.actionAddRecipe.setText(QCoreApplication.translate("self", u"Recipe", None))
        self.actionAddIngredient.setText(QCoreApplication.translate("self", u"Ingredient", None))
        self.actionOpen.setText(QCoreApplication.translate("self", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("self", u"Save", None))
        self.actionLogout.setText(QCoreApplication.translate("self", u"Logout", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("self", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("self", u"Tab 2", None))
        self.loginHeader.setText("")
        self.loginStatus.setText(QCoreApplication.translate("self", u"You are logged in as: ______", None))
        self.quickSearchBtn.setPlaceholderText(QCoreApplication.translate("self", u"Search", None))
        self.quickAddLabel.setText(QCoreApplication.translate("self", u"Quick Add", None))
        self.quickAddFormulaBtn.setText(QCoreApplication.translate("self", u"Formula", None))
        self.quickAddIngrBtn.setText(QCoreApplication.translate("self", u"Ingredient", None))
        self.quickAddDocBtn.setText(QCoreApplication.translate("self", u"Documentation", None))
        self.quickAddScoreBtn.setText(QCoreApplication.translate("self", u"Add Formula Scoring", None))
        self.quickOpenLabel.setText(QCoreApplication.translate("self", u"Quick Open/Edit", None))
        self.menuFile.setTitle(QCoreApplication.translate("self", u"File", None))
        self.menuAdd.setTitle(QCoreApplication.translate("self", u"Add", None))
        self.menuEdit.setTitle(QCoreApplication.translate("self", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("self", u"View", None))
        self.menuDatabase.setTitle(QCoreApplication.translate("self", u"Database", None))
    # retranslateUi

