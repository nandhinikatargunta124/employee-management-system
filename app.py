import mysql.connector
from datetime import date

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",
    database="employee_management"
)

cursor = db.cursor()

def add_employee(name, email, department, salary, joining_date):
    query = """
    INSERT INTO employees (name, email, department, salary, joining_date)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (name, email, department, salary, joining_date))
    db.commit()
    print("Employee added successfully")

def view_employees():
    cursor.execute("SELECT * FROM employees")
    for row in cursor.fetchall():
        print(row)

add_employee("Rahul", "rahul@gmail.com", "IT", 40000, date.today())
view_employees()
