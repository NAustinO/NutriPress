# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys, os

sys.path.append('../pjrd')
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from pjrd.add_ingredient import addIngredientDialog

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi()

    def connectDB(self):
        try:
            db = mysql.connect(host='localhost',
                            user='root',
                            passwd='Pj@bW1!G1-4'
                            )
            QMessageBox.about(self, 'Connection', 'Database Connection Successful')
            print('It Worked!')  # verification
            return db
        except: 
            QMessageBox.about(self, 'Connection', 'Database Connection Failed')
            print('It failed')
            #sys.exit(1)


    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Ui_MainWindow")
        self.resize(1114, 985)
        self.setMinimumSize(QSize(500, 500))
        icon = QIcon()
        icon.addFile(u"pjrd/static/media/pjgraphiclogo.png", QSize(), QIcon.Normal, QIcon.On)
        self.setWindowIcon(icon)
        # main window widget

        mainWindowWidget = QWidget(self)
        mainWindowWidget.setObjectName(u'mainWindowWidget')
        mainWindowWidgetSizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        mainWindowWidgetSizePolicy.setHorizontalStretch(0)
        mainWindowWidgetSizePolicy.setVerticalStretch(0)
        mainWindowWidgetSizePolicy.setHeightForWidth(mainWindowWidget.sizePolicy().hasHeightForWidth())
        mainWindowWidget.setSizePolicy(mainWindowWidgetSizePolicy)

        self.gridLayout = QGridLayout(mainWindowWidget)

        self.gridLayout.setObjectName(u"mainWindowGridLayout")

        mainTabWidget = QTabWidget(mainWindowWidget)
        mainTabWidget.setObjectName('mainWindowTabWidget')
        self.tab = QWidget()
        self.tab.setObjectName(u"tab1")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        # self.mdiArea = QMdiArea(self.tab)
        # self.mdiArea.setObjectName(u"mdiArea")
        # self.verticalLayout.addWidget(self.mdiArea)
        # self.tabWidget.addTab(self.tab, 'MMI')
        # self.tab_2 = QWidget()
        # self.tab_2.setObjectName(u"tab_2")
        #self.widget = QWidget(self.tab_2)
        # self.widget.setObjectName(u"widget")
        #self.widget.setGeometry(QRect(0, 0, 1051, 931))
        #sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        #self.widget.setSizePolicy(sizePolicy)
        #self.tabWidget.addTab(self.tab_2, 'Free')

        self.gridLayout.addWidget(mainTabWidget, 0, 1, 1, 1)

        homeNavBarWidget = QWidget(mainWindowWidget)
        homeNavBarWidget.setObjectName(u'homeNavBarWidget')

        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(homeNavBarWidget.sizePolicy().hasHeightForWidth())

        homeNavBarWidget.setSizePolicy(sizePolicy1)

        homeNavBarWidget.setMaximumSize(QSize(200, 16777215))

        homeNavBarWidget.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_3 = QVBoxLayout(homeNavBarWidget)

        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        pjLogoLoginHeader = QLabel(homeNavBarWidget)
        pjLogoLoginHeader.setObjectName(u'pjLogoLoginHeader')
        pjLogoLoginHeader.setMinimumSize(QSize(0, 16))
        pjLogoLoginHeader.setMaximumSize(QSize(100, 100))
        pjLogoLoginHeader.setPixmap(QPixmap(u'pjrd/static/media/pjgraphiclogo.png'))
        pjLogoLoginHeader.setScaledContents(True)

        self.verticalLayout_3.addWidget(pjLogoLoginHeader, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        loginHeader = QLabel(homeNavBarWidget)
        loginHeader.setObjectName(u'loginHeader')
        loginHeader.setText('You are logged in as: USER EMAIL HERE')
        loginHeader.setWordWrap(True)
        loginHeaderSizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        loginHeaderSizePolicy.setHorizontalStretch(0)
        loginHeaderSizePolicy.setVerticalStretch(0)
        loginHeaderSizePolicy.setHeightForWidth(loginHeader.sizePolicy().hasHeightForWidth())
        loginHeader.setSizePolicy(loginHeaderSizePolicy)
        loginHeader.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(loginHeader)

        quickSearchBtn = QLineEdit(homeNavBarWidget)
        quickSearchBtn.setObjectName(u'quickSearchBtn')
        quickSearchBtn.setPlaceholderText('Search')

        self.verticalLayout_3.addWidget(quickSearchBtn)

        self.verticalSpacer_2 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        quickAddHeader = QLabel(homeNavBarWidget)
        quickAddHeader.setText('Quick Add Access')
        quickAddHeader.setObjectName(u'quickAddHeader')
        self.verticalLayout_3.addWidget(quickAddHeader, 0, Qt.AlignHCenter)

        quickAddFormulaBtn = QPushButton(homeNavBarWidget)
        quickAddFormulaBtn.setText('Add Formula')
        quickAddFormulaBtn.setObjectName(u'quickAddFormulaBtn')
        quickAddFormulaBtn.setFlat(False)

        self.verticalLayout_3.addWidget(quickAddFormulaBtn)

        quickAddIngrBtn = QPushButton(homeNavBarWidget)
        quickAddIngrBtn.setText('Add Ingredient')
        quickAddIngrBtn.setObjectName(u'quickAddIngrBtn')
        self.verticalLayout_3.addWidget(quickAddIngrBtn)

        quickAddDocBtn = QPushButton(homeNavBarWidget)
        quickAddDocBtn.setText('Add Documentation')
        quickAddDocBtn.setObjectName(u'quickAddDocBtn')
        self.verticalLayout_3.addWidget(quickAddDocBtn)

        quickAddScoreBtn = QPushButton(homeNavBarWidget)
        quickAddScoreBtn.setText('Add Formula Scoring')
        quickAddScoreBtn.setObjectName(u'quickAddScoreBtn')
        self.verticalLayout_3.addWidget(quickAddScoreBtn)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.quickOpenHeader = QLabel(homeNavBarWidget)
        self.quickOpenHeader.setText('Double-Tap to Open Formula')
        self.quickOpenHeader.setObjectName(u'quickOpenHeader')
        self.quickOpenHeader.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.quickOpenHeader)

        self.quickFormulaAccess = QListView(homeNavBarWidget)
        self.quickFormulaAccess.setObjectName(u'quickFormulaAccess')
        self.quickFormulaAccess.setMouseTracking(True)
        self.verticalLayout_3.addWidget(self.quickFormulaAccess)

        self.gridLayout.addWidget(homeNavBarWidget, 0, 0, 2, 1)

        self.setCentralWidget(mainWindowWidget)

        # creates menubar object
        menuBar = self.menuBar()
        menuBar.setObjectName(u'menubar')
        menuBar.setGeometry(QRect(0, 0, 1114, 22))

        # sets menuBar object to mainWindow class menubar attribute
        self.setMenuBar(menuBar)

        # adds menus to menubar
        fileMenu = menuBar.addMenu('&File')
        editMenu = menuBar.addMenu('&Edit')
        viewMenu = menuBar.addMenu('&View')
        databaseMenu = menuBar.addMenu('&Database')

        # sets object names for menubar objects
        fileMenu.setObjectName(u'fileMenu')
        editMenu.setObjectName(u'editMenu')
        viewMenu.setObjectName(u'viewMenu')
        databaseMenu.setObjectName(u'databaseMenu')

        # adds actions to file Menu
        addMenu = fileMenu.addMenu('&Add')
        exitAction = fileMenu.addAction('&Exit')
        openAction = fileMenu.addAction('&Open')
        saveAction = fileMenu.addAction('&Save')
        logoutAction = fileMenu.addAction('&Log Out')
        exitAction.triggered.connect(self.closeEvent)
        fileMenu.addAction(exitAction)
        addFormulaAction = addMenu.addAction('&Add Formula')
        addIngredientAction = addMenu.addAction('&Add Ingredient')

        ############################addIngredientAction.triggered.connect()


        # adds shortcuts
        saveAction.setShortcut('Ctrl+S')
        openAction.setShortcut('Ctrl+O')
        exitAction.setShortcut('Ctrl+Q')

        # menubar settings
        menuBar.setNativeMenuBar(False)

        # status bar
        statusBar = QStatusBar(self)
        statusBar.setObjectName(u'statusBar')
        self.setStatusBar(statusBar)
        exitAction.setStatusTip('Exits the application')

        fileMenu.addSeparator()

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Ui_MainWindow", u"Pressed Juicery R&D", None))
        self.actionExit.setText(QCoreApplication.translate("Ui_MainWindow", u"Quit", None))
        # if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("Ui_MainWindow", u"Meta+Q", None))
        #endif // QT_CONFIG(shortcut)
        self.actionAddRecipe.setText(QCoreApplication.translate("Ui_MainWindow", u"Recipe", None))
        self.actionAddIngredient.setText(QCoreApplication.translate("Ui_MainWindow", u"Ingredient", None))
        self.actionOpen.setText(QCoreApplication.translate("Ui_MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("Ui_MainWindow", u"Save", None))
        self.actionLogout.setText(QCoreApplication.translate("Ui_MainWindow", u"Logout", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Ui_MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Ui_MainWindow", u"Tab 2", None))
        self.label.setText("")
        self.loginStatus.setText(QCoreApplication.translate("Ui_MainWindow", u"You are logged in as: ______", None))
        self.quickSearchBtn.setPlaceholderText(QCoreApplication.translate("Ui_MainWindow", u"Search", None))
        self.quickAddLabel.setText(QCoreApplication.translate("Ui_MainWindow", u"Quick Add", None))
        self.quickAddFormulaBtn.setText(QCoreApplication.translate("Ui_MainWindow", u"Formula", None))
        self.quickAddIngrBtn.setText(QCoreApplication.translate("Ui_MainWindow", u"Ingredient", None))
        self.quickAddDocBtn.setText(QCoreApplication.translate("Ui_MainWindow", u"Documentation", None))
        self.pushButton_4.setText(QCoreApplication.translate("Ui_MainWindow", u"PushButton", None))
        self.quickOpenLabel.setText(QCoreApplication.translate("Ui_MainWindow", u"Quick Open/Edit", None))
        self.menuFile.setTitle(QCoreApplication.translate("Ui_MainWindow", u"File", None))
        self.menuAdd.setTitle(QCoreApplication.translate("Ui_MainWindow", u"Add", None))
        self.menuEdit.setTitle(QCoreApplication.translate("Ui_MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("Ui_MainWindow", u"View", None))
        self.menuDatabase.setTitle(QCoreApplication.translate("Ui_MainWindow", u"Database", None))

        ###### call helper functions 
        self.retranslateUi()
        self.tabWidget.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(self)

    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.question(
                                                self,
                                                'Confirm exit',
                                                'Exit program?',
                                                QtWidgets.QMessageBox.Yes |
                                                QtWidgets.QMessageBox.No
        )
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            pass

  


def connectDB(Ui_MainWindow):
    try:
        db = mysql.connect(host='localhost',
                           user='root',
                           passwd='Pj@bW1!G1-4'
        )
        print('It Worked!')  # verification
        QMessageBox.about(Ui_MainWindow, 'Connection', 'Database Connection Successful')
        return db
    except:
        QMessageBox.about(Ui_MainWindow, 'Connection', 'Database Connection Failed')
        print('It failed')
        # sys.exit(1)

