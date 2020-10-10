from MySQLdb import _mysql as mysql

def connectDB():
  
    db = mysql.connect(host='localhost',
                       user='root',
                       passwd='Pj@bW1!G1-4'
    )
    return db

'''
  def connectDB(self):
        try:
            db = mysql.connect(host='localhost',
                            user='root',
                            passwd='Pj@bW1!G1-4'
                            )
            QMessageBox.about(self, 'Connection', 'Database Connection Successful')
            print('It Worked!')  # verification
            return db
        except:
            QMessageBox.about(self, 'Connection', 'Database Connection Failed')
            print('It failed')
            #sys.exit(1)

            '''