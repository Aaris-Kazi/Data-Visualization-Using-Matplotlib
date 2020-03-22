import mysql.connector

def td():
    conn = mysql.connector.connect(host='localhost', user='root', password='', database='python_database')

    cursor = conn.cursor()
    cursor.execute('select Name from test where Subject ="AVG TH + PR" && Attendance < 75')
    print('\t\tDefaulter:\n')
    for i in cursor:
        print(i)
