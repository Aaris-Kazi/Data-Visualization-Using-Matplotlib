import mysql.connector

def td():
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='python_database')
        cursor = conn.cursor()
        cursor.execute('select Name from test where Subject ="AVG TH + PR" && Attendance < 75')
        print('\t\tDefaulter:\n')
        for i in cursor:
            print(i)
        conn.close()
    except mysql.connector.Error as err:
        print('Could not Establish the connection:{}'.format(err))
def td1():
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='python_database')
        cursor = conn.cursor()
        cursor.execute('select Name from test where Subject ="AVG TH + PR" && Attendance < 75')
        rows = cursor.fetchall()
        return rows
        
    except mysql.connector.Error as err:
        print('Could not Establish the connection:{}'.format(err))

def td2():
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='python_database')
        cursor = conn.cursor()
        cursor.execute('select * from test')
        rows = cursor.fetchall()
        return rows
    except mysql.connector.Error as err:
        print('Could not Establish the connection:{}'.format(err))
    

def td3(x):
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='python_database')
        cursor = conn.cursor()
        cursor.execute('select * from test')
        rows = cursor.fetchall()
        return rows
    except mysql.connector.Error as err:
        print('Could not Establish the connection:{}'.format(err))