Activate venv 
source venv/bin/activate

bin is for storing executable files. could be hte project itself 

pyside2-uic mainwindow.ui > ui_mainwindow.py



class formulaEditorDialog(QDialog):
    
    def __init__(self):
        super(formulaEditorDialog, self).__init__()
        self.setupUi(self)
        self.setupSuggestions()
    
    def setupSuggestions(self):
        db = connectDB()
        with db.cursor() as cursor:
            cursor.execute("SELECT category_id, category_name FROM formula_category")
            allCategories = cursor.fetchall()
            for category in allCategories:
                name = category[1]
                id = category[0]
                index = self.categoryComboBox.currentIndex()

                
        