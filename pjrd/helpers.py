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

# returns the connection only. Must use connection.cursor() to execute queries
def connectDB():
    connection = pymysql.connect(host='localhost', user='root', password='Pj@bW1!G1-4', database='sys')#cursorclass=pymysql.cursors.DictCursor)
    return connection

def isUniqueQuery(query):
    db = connectDB()
    cursor = db.cursor()
    result = cursor.execute(query)
    if result:
        return False

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


'''
def displayNFP():
    sourceHTML = QUrl('pjrd/static/templates/nfp.html')
    
    textBrowser = QTextBrowser()
    textBrowser.setOpenExternalLinks(True)
    textBrowser.setSource(sourceHTML)
    #textBrowser.setStyleSheet(stylesheetURL)
    #textBrowser.setSearchPaths()
    return textBrowser

'''