import pymysql
import sys

from PyQt5.QtWidgets import QTextBrowser
from PyQt5.QtCore import QUrl, QDir
from PyQt5 import QtWebEngineWidgets, QtWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView


from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

sys.path.append('/pjrd')


def dbConnection(database: str):
    connection = pymysql.connect(host='localhost', user='root', password='Pj@bW1!G1-4', database=database, cursorclass=pymysql.cursors.DictCursor)
    return connection

def displayNFP():
    webEngineView = QWebEngineView()
    webEngineView.run
    #filePath = 'pjrd/static/templates/nfp.html'
    #with open('pjrd/static/templates/nfp.html', 'r') as f:
     #   html = f.read()
    #url = QUrl.fromLocalFile(QUrl('pjrd/static/templates/nfp.html')
    #webEngineView.load(QUrl.fromLocalFile(filePath))
    html = "<h1>Hello, World</h1>"
    webEngineView.setHtml(html)
    webEngineView.resize(800, 800)
    return webEngineView


# called to test if the window works
def test(window):
    app = QApplication(sys.argv)
    gui = window()
    gui.show()
    sys.exit(app.exec_())

# TODO
# creates window of nutrition facts panel when called
def displayNFP():
    pass
    '''sourceHTML = QUrl('pjrd/static/templates/nfp.html')
    
    textBrowser = QTextBrowser()
    textBrowser.setOpenExternalLinks(True)
    textBrowser.setSource(sourceHTML)
    #textBrowser.setStyleSheet(stylesheetURL)
    #textBrowser.setSearchPaths()
    return textBrowser'''

class TimedMessageBox(QMessageBox):
    
    def __init__(self, autoClose=True, timeout=2):
        ##### must call when inheriting a base class in order to gain access to everything
        super(TimedMessageBox, self).__init__()
        self.timeout = timeout
        self.autoClose = autoClose
        
    def showEvent(self, showEvent):
        self.currentTimer = 0
        if self.autoClose:
            self.startTimer(1000)
    
    def timerEvent(self, timerEvent):
        self.currentTimer += 1
        if self.currentTimer >= self.timeout:
            self.done(0)

            
