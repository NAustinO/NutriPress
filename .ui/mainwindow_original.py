# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1114, 985)
        MainWindow.setMinimumSize(QSize(500, 500))
        icon = QIcon()
        icon.addFile(u"../pjrd/static/media/pjgraphiclogo.png", QSize(), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAddRecipe = QAction(MainWindow)
        self.actionAddRecipe.setObjectName(u"actionAddRecipe")
        self.actionAddIngredient = QAction(MainWindow)
        self.actionAddIngredient.setObjectName(u"actionAddIngredient")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        self.mainWindowWidget = QWidget(MainWindow)
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
        self.label = QLabel(self.leftNavBarWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 16))
        self.label.setMaximumSize(QSize(100, 100))
        self.label.setPixmap(QPixmap(u"../pjrd/static/media/pjgraphiclogo.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

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

        self.verticalLayout_3.addWidget(self.quickAddIngrBtn)

        self.quickAddDocBtn = QPushButton(self.leftNavBarWidget)
        self.quickAddDocBtn.setObjectName(u"quickAddDocBtn")

        self.verticalLayout_3.addWidget(self.quickAddDocBtn)

        self.pushButton_4 = QPushButton(self.leftNavBarWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_3.addWidget(self.pushButton_4)

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

        MainWindow.setCentralWidget(self.mainWindowWidget)
        self.menubar = QMenuBar(MainWindow)
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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.menuAdd.menuAction())
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menuAdd.addAction(self.actionAddRecipe)
        self.menuAdd.addAction(self.actionAddIngredient)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pressed Juicery R&D", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Meta+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionAddRecipe.setText(QCoreApplication.translate("MainWindow", u"Recipe", None))
        self.actionAddIngredient.setText(QCoreApplication.translate("MainWindow", u"Ingredient", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label.setText("")
        self.loginStatus.setText(QCoreApplication.translate("MainWindow", u"You are logged in as: ______", None))
        self.quickSearchBtn.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.quickAddLabel.setText(QCoreApplication.translate("MainWindow", u"Quick Add", None))
        self.quickAddFormulaBtn.setText(QCoreApplication.translate("MainWindow", u"Formula", None))
        self.quickAddIngrBtn.setText(QCoreApplication.translate("MainWindow", u"Ingredient", None))
        self.quickAddDocBtn.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.quickOpenLabel.setText(QCoreApplication.translate("MainWindow", u"Quick Open/Edit", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAdd.setTitle(QCoreApplication.translate("MainWindow", u"Add", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuDatabase.setTitle(QCoreApplication.translate("MainWindow", u"Database", None))
    # retranslateUi

