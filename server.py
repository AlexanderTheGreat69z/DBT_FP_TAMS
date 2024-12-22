import mysql.connector
import os

mydb = mysql.connector.connect(
    host        = "localhost",
    user        = "root",
    password    = "b!Nu$21042005",
    database    = "Binusantara"
)
cursor = mydb.cursor()

def getTableNames():
    return  ['customer', 'staff', 'tour', 'destination', 'tourdest', 'booking', 'flight', 'flightbooking']

def selectTable(name:str):
    table_name = name.lower().capitalize()
    cursor.execute(f"SELECT * FROM {table_name}")
    return cursor.fetchall()

def setStaffSalary(id, salary):
    if int(salary) > 100000000:
        cursor.execute("UPDATE Staff SET staff_salary = %s WHERE staffID = %s", (salary, id))
        mydb.commit()
        print(f"set {id} salary to {str(salary)}")
    print(selectTable('staff'))

def hireStaff(id, fname, lname, email, phoneNo, sex, salary):
    val = (id, fname, lname, email, phoneNo, sex, salary)
    cursor.execute("INSERT INTO Staff VALUES (%s, %s, %s, %s, %s, %s, %s)", val)
    mydb.commit()
    print(f'Hired {fname} {lname} as new Staff!')
    print(selectTable('staff'))
    
def fireStaff(id):
    cursor.execute("DELETE FROM Staff WHERE staffID = %s", [id])
    mydb.commit()
    print(f'Fired a staff')
    print(selectTable('staff'))