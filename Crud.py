import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="faizan"
)

cur = conn.cursor()
'''
def create_database():
    cur.execute("CREATE DATABASE faizan")
create_database()    
'''
def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS emp (eno INT AUTO_INCREMENT PRIMARY KEY, ename VARCHAR(255), age INT, salary INT)")

create_table()



print("1. Insert data")
print("2. Update data")
print("3. Delete data")
print("4. Show   data")

ch = int(input("Enter your choice: "))

if ch == 1:
    def insert_user(ename, age, salary):
        sql = "INSERT INTO emp (ename, age, salary) VALUES (%s, %s, %s)"
        val = (ename, age, salary)
        cur.execute(sql, val)
        conn.commit()

    ename = input("Enter the employee name: ")
    age = int(input("Enter the employee's age: "))
    salary = int(input("Enter the employee's salary: "))
    insert_user(ename, age, salary)

elif ch == 2:
    def update_employee(eno, ename, age, salary):
        sql = "UPDATE emp SET ename = %s, age = %s, salary = %s WHERE eno = %s"
        val = (ename, age, salary, eno)
        cur.execute(sql, val)
        conn.commit()

    eno = int(input("Enter the id of the employee to update: "))
    ename = input("Enter the updated name: ")
    age = int(input("Enter the updated age: "))
    salary = int(input("Enter the updated salary: "))
    update_employee(eno, ename, age, salary)

elif ch == 3:
    def delete(eno):
        sql = "DELETE FROM emp WHERE eno = %s"
        val = (eno,)
        cur.execute(sql, val)
        conn.commit()

    eno = int(input("Enter the id of the employee to delete: "))
    delete(eno)
elif ch == 4:
    sql="SELECT * FROM emp"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)   

cur.close()
conn.close()
