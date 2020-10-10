
import sys
import bycrypt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout, QLabel, QWidget, QApplication, QPushButton, QMessageBox, QLineEdit
from MySQLdb import _mysql as msql

class loginForm(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Login')
        self.resize(500, 150)

        layout = QGridLayout()

        usernameLabel = QLabel('Username')
        self.inputUsername = QLineEdit()
        self.inputUsername.setPlaceholderText('Please enter your Pressed email')

        layout.addWidget(usernameLabel, 0, 0)
        layout.addWidget(self.inputUsername, 0, 1)

        passwordLabel = QLabel('Password')
        self.inputPassword = QLineEdit()
        self.inputPassword.setPlaceholderText('Please enter your unique assigned password')
        layout.addWidget(passwordLabel, 1, 0)
        layout.addWidget(self.inputPassword, 1, 1)

        loginButton = QPushButton('Login')
        layout.addWidget(loginButton, 2, 1)
        #loginButton.clicked.connect()

        self.setLayout(layout)

    
    # def authenticate(email, password):
     #  hashed = 

#def checkAuthenticated(): 
    

app = QApplication(sys.argv)
form = loginForm()
form.show()
sys.exit(app.exec_())

