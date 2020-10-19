import sys 
from PyQt5.QtWidgets import QApplication
from mainWindow import Ui_MainWindow


from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

sys.path.append('../pjrd')

def main():
    app = QApplication(sys.argv)
    gui = Ui_MainWindow()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()