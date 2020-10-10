import sys 
from PyQt5.QtWidgets import QApplication
from mainWindow import Ui_MainWindow


sys.path.append('../pjrd')

def main():
    app = QApplication(sys.argv)
    gui = Ui_MainWindow()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()