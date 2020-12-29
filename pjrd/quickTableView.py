
import sys, os

sys.path.append('../pjrd')
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from pjrd.helperClasses import CustomTableModel


# Fixes compatibility bug with mac big sur and pyqt
os.environ['QT_MAC_WANTS_LAYER'] = '1'

class QuickTableView(QDialog):

    def __init__(self, model: CustomTableModel = None, label: str = None, note :str = ''):
        super(QuickTableView, self).__init__()
        self.setupUi(self, label, note)
        self.setupLogic()
        if model is not None:
            self.setTableModel(model)

    def setupUi(self, Dialog, label: str = None, note: str = ''):
        if not Dialog.objectName():
            Dialog.setObjectName(u"quickTableView")
        Dialog.resize(900, 700)
        self.verticalLayout_1 = QVBoxLayout(Dialog)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")

        self.headerLabel = QLabel()
        self.headerLabel.setText(label)

        self.verticalLayout_1.addWidget(self.headerLabel)

        self.subHeaderLabel = QLabel()
        self.subheaderFont = QFont()
        self.subheaderFont.setPointSize(10)
        self.subHeaderLabel.setFont(self.subheaderFont)
        self.subHeaderLabel.setText('')

        self.verticalLayout_1.addWidget(self.subHeaderLabel)

        self.noteLabel = QLabel()
        self.noteFont = QFont()
        self.noteFont.setPointSize(10)
        self.noteLabel.setFont(self.noteFont)
        self.noteLabel.setText(note)
        self.verticalLayout_1.addWidget(self.noteLabel)

        self.tableView = QTableView()

        self.tableView.horizontalHeader().setSizeAdjustPolicy(QHeaderView.AdjustToContents)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalLayout_1.addWidget(self.tableView)

        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.verticalLayout_1.addWidget(self.buttonBox)

        QMetaObject.connectSlotsByName(Dialog)

    def setupLogic(self):
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.accept)

    def accept(self):
        self.close()
        
    def setTableModel(self, model: CustomTableModel):
        self.tableView.setModel(model)
    
    def setHeaderLabel(self, header: str):
        self.headerLabel.setText(header)

    def setSubheaderLabel(self, header: str):
        self.subHeaderLabel.setText(header)


