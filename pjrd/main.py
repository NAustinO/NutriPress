import sys, os
os.environ['QT_MAC_WANTS_LAYER'] = '1'
sys.path.append('../pjrd')

from pjrd.mainwindow import Ui_MainWindow
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *


def main():
    app = QApplication(sys.argv)
    gui = Ui_MainWindow()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()