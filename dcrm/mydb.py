import pymysql

dataBase = pymysql.connect(
    host='localhost',
    user='root',
    passwd='Giuschil@040291',
    database='crm'
)

cursorObject = dataBase.cursor()
cursorObject.execute("show databases;")

dataBase.close()
