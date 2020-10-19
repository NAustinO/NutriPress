from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


sys.path.append('../pjrd')
from pjrd.helpers import displayNFP


class testWindow(QWidget):

    def __init__(self):
        super(testWindow, self).__init__()
        layout = QVBoxLayout()
        self.button = QPushButton('Test')
        layout.addWidget(self.button)

        nfp = displayNFP()
        layout.addWidget(nfp)
        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    gui = testWindow()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()