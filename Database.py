import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', passwd='', database='python_database')
mycursor = conn.cursor()
mycursor.execute('select Name from test where Subject = "AVG TH + PR" && Attendance < 75')
for i in mycursor:
    print(i)