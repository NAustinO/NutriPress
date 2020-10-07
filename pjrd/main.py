
import sys
from PyQt5 import QtWidgets, QtGui  # , QtCore, QtNetwork
from PyQt5.QtWidgets import *

from MySQLdb import _mysql as msql

# note that Window.connectDB contains a hard-coded password

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(200, 200, 800, 800)  # (xpos, ypos, width, height)
        self.setWindowTitle("Pressed Juicery R&D")
        self.setWindowIcon(QtGui.QIcon('pjlogo.png'))   # not working
        self.initUI()

    def initUI(self):
        self.createMenus()
        self.home()

    def connectDB(self):
        try:
            db = msql.connect(
                              host='localhost',
                              user='root',
                              passwd='Pj@bW1!G1-4'  # <----------
                             )
            QMessageBox.about(self, 'Connection',
                              'Database Connection Successful')
            print('It worked!')  # verification
        except:
            QMessageBox.about(self, 'Connection', 'Database Connection Failed')
            print('failed')
            # sys.exit(1)

    # Creates the menu bar for home page
    def createMenus(self):
        self.statusBar()
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)
    

        fileMenu = menuBar.addMenu('&File')
        editMenu = menuBar.addMenu('&Edit')

        exitAction = QtWidgets.QAction('&Quit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exits application')
        exitAction.triggered.connect(self.closeEvent)

        fileMenu.addAction(exitAction)

        menuBar.addMenu('&View')
        menuBar.addMenu('&Database')

    def home(self):
        self.centralWidget = QtWidgets(Window)
        self.centralWidget.setObjectName(u'mainWidget')
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.)
        self.gridLayout = QGridLayout()

        layout.addWidget()
        self.connectDB()
        btn = QtWidgets.QPushButton("Quit", self)
        btn.move(50, 50)
        btn.clicked.connect(self.closeEvent)








        self.show()

    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.question(self,
                                               'Confirm exit',
                                               'Exit program?',
                                               QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            pass



# def checkAuthentication():

def main():

    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':

    main()
