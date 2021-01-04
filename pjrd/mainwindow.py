# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'self.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
import os

sys.path.append('../pjrd')
from pjrd.mainSearch import MainSearch
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *


#from addIngredient import addIngredientDialog
from pjrd.helpers import dbConnection
from pjrd.add_ingredient import addIngredientDialog
from pjrd.formulaSetupDialog import formulaSetupDialog
from pjrd.formulaEditor import formulaEditorDialog
os.environ['QT_MAC_WANTS_LAYER'] = '1' 

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi()
        self.setupLogic()
        try:
            self.db = dbConnection('FormulaSchema')
        except:
            QMessageBox.about(self, 'Connection', 'Database Connection Failed')
        else:
            QMessageBox.about(self, 'Connection', 'Database Connection Successful')
        self.refreshListWidget()
        
    def setupLogic(self):
        """
        -----------------------------
            Purpose:
                - Event/signal setup
            Arguments:
                - None
            Return Value:
                - None
        """
        self.quickAddFormulaBtn.clicked.connect(self.addFormula)
        self.searchBtn.clicked.connect(self.search)
        self.searchLine.installEventFilter(self)
        self.quickFormulaAccess.installEventFilter(self)
        self.quickFormulaAccess.itemDoubleClicked.connect(self.listItemClicked)
  
    # when called, opens the new ingredient dialog
    def addIngEvent(self):
        """
        -----------------------------
            Purpose:
                - Opens the new ingredient dialog when called
            Arguments:
                - None
            Return Value:
                - None
        """
        widget = addIngredientDialog(self)
        widget.show()
        widget.exec_()
    
    # opens the new new formula setup dialog
    def addFormula(self):
        """
        -----------------------------
            Purpose:
                - Opens the new formula editor when called
            Arguments:
                - None
            Return Value:
                - None
        """
        widget = formulaSetupDialog(self)
        widget.show()
        widget.exec_()

    # overrides standard event filter
    def eventFilter(self, source, event):
        """
        -----------------------------
            Purpose:
                - Overloads eventFilter method for QDialog
                - Listens for the return key to be pressed to call the open method
            Arguments:
                - source: the QWidget in focus when the event is handled
                - event: the QEvent object that specifies the type of event
            Return Value:
                - Returns True if successfully handles the event
                - Returns False if unsuccessful
        """
        # search event
        if (event.type() == QEvent.KeyPress and source is self.searchLine and event.key() == Qt.Key_Return):
            if self.searchLine.text() is None:
                return False
            else:
                self.search()
                return True 
        return super(Ui_MainWindow, self).eventFilter(source, event)

    # slot that listens for a double click on the listwidget
    def listItemClicked(self):
        """
        -----------------------------
            Purpose:
                - The method is called to open the item
            Arguments:
                - None
            Return Value:
                - None
        """
        toOpen = self.quickFormulaAccess.currentItem().data(Qt.UserRole)
        description = self.quickFormulaAccess.currentItem().text()
        id = toOpen['foodID']
        type = toOpen['type']
        msg = QMessageBox()
        if type == 'ingredient':
            msg.setText('Now opening the ingredient to make edits')
            msg.exec_()
            self.open(description, foodIdToOpen=id, type=type)
        else:
            formulaID = toOpen['formulaID']
            msg.setText('Now opening the formula to make edits')
            msg.exec_()
            self.open(description, foodIdToOpen=id, formulaIdToOpen=formulaID, type=type)
        return

    # refreshes the list widget. Called when a new ingredient or formula is added
    def refreshListWidget(self):
        """
        -----------------------------
            Purpose:
                - Autofills the list widget with items. Mostly called after adding an ingredient or formula to the database
            Arguments:
                - None
            Return Value:
                - None
        """
        self.quickFormulaAccess.clear()
        with dbConnection('FormulaSchema').cursor() as cursor:
            results = cursor.execute('SELECT food.food_id, food.food_desc, food.input_date FROM food WHERE food.user_inputted = %s and food.food_id NOT IN (SELECT food_id FROM formula) ORDER BY food_desc ASC', (True,))
            results = cursor.fetchall()
            for result in results:
                item = QListWidgetItem()
                itemData = {
                    'foodID': result['food_id'],
                    'type': 'ingredient'
                }
                item.setText(result['food_desc'].title() + ' (Ingredient)')
                item.setBackground(Qt.green)
                item.setData(Qt.UserRole, itemData)
                self.quickFormulaAccess.addItem(item)
    
            results = cursor.execute('SELECT food.food_id, formula.formula_id, formula.formula_name, food.input_date FROM food INNER JOIN formula ON food.food_id = formula.food_id WHERE user_inputted = %s ORDER BY formula_name ASC', (True))
            results = cursor.fetchall()
            for result in results:
                item = QListWidgetItem()
                itemData = {
                    'foodID': result['food_id'],
                    'formulaID': result['formula_id'],
                    'type': 'formula'
                }
                item.setText(result['formula_name'].title() + ' (Formula)')
                item.setTextColor(Qt.white)
                item.setBackground(Qt.darkGreen)
                item.setData(Qt.UserRole, itemData)
                self.quickFormulaAccess.addItem(item)

    # slot for opening the search window
    def search(self):
        """ 
        -----------------------------
            Purpose:
                - Slot for opening the search window upon the signal 
            Arguments:
                - None
            Return Value:
                - None
        """
        if self.searchLine.text() == '':
            return
        widget = MainSearch(self, self.searchLine.text())
        widget.show()
        widget.exec_()

    # opens the formula editor or ingredient dialog based on the type of item selected
    def open(self, description, foodIdToOpen: int=None, formulaIdToOpen: int=None, type: str=None):
        """
        -----------------------------
            Purpose:
                - Opens the formula editor/ingredient dialog of an existing item based on the params passed in 
            Arguments:
                - description: The name of the item (formula name or ingredient name)
                - foodIdToOpen: The unique foodID of the item to open
                - formulaIdToOpen: The unique formulaId to open
                - type: string that indicates what type of item it is to open (Can be either "formula" or "ingredient") 
            Return Value:
                - None
        """
        if foodIdToOpen is None:
            return
        if type == 'ingredient':
            widget = addIngredientDialog(self, foodIdToOpen)
            widget.show()
            widget.exec_()
            return
        elif type == 'formula':
            widget = formulaEditorDialog(self, formulaName=description, openFormulaID=formulaIdToOpen, corrFoodID=foodIdToOpen)
            widget.show()
            widget.exec_()
            return

    # event handler that validates the users input to close the window and exit the program
    def closeEvent(self, event):
        """
        -----------------------------
            Purpose:
                - Event handler that validates the users input before closing the window and exiting the program
            Arguments:
                - event: the QEvent object passed
            Return Value:
                - None
        """
        toClose = QMessageBox.question(self, 'Confirm Exit', 'Exit Program?', QMessageBox.Yes | QMessageBox.No)
        if toClose == QMessageBox.Yes:
            self.close()
        else:
            return

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"self")
        self.resize(1114, 985)
        self.setMinimumSize(QSize(500, 500))
        icon = QIcon()
        icon.addFile(u"pjrd/static/media/hpMyPlate.png", QSize(), QIcon.Normal, QIcon.On)
        self.setWindowIcon(icon)
    
        self.actionExit = QAction(self)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAddRecipe = QAction(self)
        self.actionAddRecipe.setObjectName(u"actionAddRecipe")
        self.actionAddRecipe.triggered.connect(self.addFormula)

        self.actionAddIngredient = QAction(self)
        self.actionAddIngredient.triggered.connect(self.addIngEvent)
        self.actionAddIngredient.setObjectName(u"actionAddIngredient")
    
        self.actionOpen = QAction(self)
        self.actionOpen.setObjectName(u"actionOpen")
        #self.actionOpen.triggered.connect(self.search)

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

        self.welcomeFrame = QFrame(self.tab)
        
        self.verticalLayout2 = QVBoxLayout(self.welcomeFrame)
        self.welcomeFrame.setLayout(self.verticalLayout2)
        self.welcomeFrame.setMaximumHeight(150)
        
        self.welcomeHeader = QLabel(self.tab)
        self.welcomeHeader.setText('Welcome to my Nutrition Database and Assistant Program')
        self.welcomeHeader.setAlignment(Qt.AlignCenter)
        self.welcomeHeaderFont = QFont()
        self.welcomeHeaderFont.setPointSize(22)
        self.welcomeHeaderFont.setBold(True)
        self.welcomeHeader.setFont(self.welcomeHeaderFont)
        self.welcomeHeader.setStyleSheet("QLabel { background-color: white}")
        self.verticalLayout2.addWidget(self.welcomeHeader)

        self.verticalLayout.addWidget(self.welcomeFrame)

        self.welcomeBody = QFrame(self.tab)
        self.bodyLayout = QVBoxLayout(self.welcomeBody)
        self.welcomeBody.setLayout(self.bodyLayout)

        self.welcomeBodyLabel = QLabel(self.welcomeBody)
        self.welcomeBodyLabel.setText('This program is designed as a tool to assist with recipe development.  It allows: <ul> <li>Storage of ingredient ratios and helps document different versions of recipes that are improved upon</li> <li>Estimate the nutritional information of their recipe, without outsourcing to a lab for analytical testing</li> <li>Upload custom or supplier specific ingredients to ensure more accurate nutrition estimations</li> </ul> Finally, formulas stored in this program can be used as components of entire meals or diets simply by using the component as an ingredient in another formula. <br><br> To begin, click on the buttons to the left.')
        self.welcomeBodyLabel.setStyleSheet("QLabel { background-color: white}")
        self.welcomeBodyLabel.setContentsMargins(20, 10, 20, 10)
        self.bodyFont = QFont()
        self.bodyFont.setPointSize(16)
        self.welcomeBodyLabel.setFont(self.bodyFont)
        self.welcomeBodyLabel.setWordWrap(True)
        self.bodyLayout.addWidget(self.welcomeBodyLabel)
        self.verticalLayout.addWidget(self.welcomeBody)


        #self.tabTableView = QTableView(self.tab)
        #self.verticalLayout.addWidget(self.tabTableView)

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
        self.leftNavBarWidget.setMinimumWidth(250)
        self.leftNavBarWidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_3 = QVBoxLayout(self.leftNavBarWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.pjLogoHeader = QLabel(self.leftNavBarWidget)
        self.pjLogoHeader.setObjectName(u'pjLogoLoginHeader')
        self.pjLogoHeader.setMinimumSize(QSize(0, 16))
        self.pjLogoHeader.setMaximumSize(QSize(100, 100))
        self.pjLogoHeader.setPixmap(QPixmap(u'pjrd/static/media/icon.png'))
        self.pjLogoHeader.setScaledContents(True)
        self.verticalLayout_3.addWidget(self.pjLogoHeader, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.loginHeader = QLabel(self.leftNavBarWidget)
        self.loginHeader.setWordWrap(True)
        self.loginHeader.setObjectName(u"loginHeader")
        self.loginHeader.setMinimumSize(QSize(0, 16))
        self.loginHeader.setMaximumSize(QSize(100, 100))
        self.loginHeader.setPixmap(QPixmap(u"../pjrd/static/media/icon.png"))
        self.loginHeader.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.loginHeader, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.loginStatus = QLabel(self.leftNavBarWidget)
        self.loginStatus.setObjectName(u"loginStatus")
        self.loginStatus.setText('You are logged in')
        self.loginStatus.setWordWrap(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.loginStatus.sizePolicy().hasHeightForWidth())
        self.loginStatus.setSizePolicy(sizePolicy2)
        self.loginStatus.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.loginStatus)

        self.searchLine = QLineEdit(self.leftNavBarWidget)
        self.searchLine.setObjectName(u"searchLine")

        self.verticalLayout_3.addWidget(self.searchLine)

        self.searchBtn = QPushButton(self.leftNavBarWidget)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setText('Search')

        self.verticalLayout_3.addWidget(self.searchBtn)

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

        self.listAccessHeaderLabel = QLabel(self.leftNavBarWidget)
        self.listAccessHeaderLabel.setObjectName(u"listAccessHeaderLabel")
        self.listAccessHeaderLabel.setAlignment(Qt.AlignCenter)
        self.listAccessHeaderLabel.setText('Double click to access')

        self.verticalLayout_3.addWidget(self.listAccessHeaderLabel)

        self.quickFormulaAccess = QListWidget(self.leftNavBarWidget)
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
       
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())

        self.menubar.setNativeMenuBar(False)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuAdd.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.actionExit.triggered.connect(self.closeEvent)  ####### <----------------- Does not work properly
        self.menuFile.addSeparator()
        self.menuAdd.addAction(self.actionAddRecipe)
        self.menuAdd.addAction(self.actionAddIngredient)

        # adds shortcuts
        self.actionOpen.setShortcut('Ctrl+O')
        self.actionExit.setShortcut('Ctrl+Q')

        self.retranslateUi()

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("self", u"Nutrition Assistant", None))
        self.actionExit.setText(QCoreApplication.translate("self", u"Quit", None))
        #if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("self", u"Meta+Q", None))
        #endif // QT_CONFIG(shortcut)
        self.actionAddRecipe.setText(QCoreApplication.translate("self", u"Recipe", None))
        self.actionAddIngredient.setText(QCoreApplication.translate("self", u"Ingredient", None))
        self.actionOpen.setText(QCoreApplication.translate("self", u"Open", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("self", u"Welcome", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("self", u"Tab 2", None))
        self.loginHeader.setText("")
        self.searchLine.setPlaceholderText(QCoreApplication.translate("self", u"Search", None))
        self.quickAddLabel.setText(QCoreApplication.translate("self", u"Quick Add", None))
        self.quickAddFormulaBtn.setText(QCoreApplication.translate("self", u"Formula", None))
        self.quickAddIngrBtn.setText(QCoreApplication.translate("self", u"Ingredient", None))
        self.menuFile.setTitle(QCoreApplication.translate("self", u"File", None))
        self.menuAdd.setTitle(QCoreApplication.translate("self", u"Add", None))

    # retranslateUi

app = QApplication(sys.argv)
gui = Ui_MainWindow()
gui.show()
sys.exit(app.exec_())
