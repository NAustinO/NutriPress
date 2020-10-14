import pymysql

def connectDB():
    connection = pymysql.connect(host='localhost', user='root', password='Pj@bW1!G1-4', database='sys')#cursorclass=pymysql.cursors.DictCursor)
    return connection

def isUniqueQuery(query):
    db = connectDB()
    cursor = db.cursor()
    result = cursor.execute(query)
    if result:
        return False
