import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:')                   # In-memory database. Gives a database that lives in RAM. Is good for testing as it provides a new database everytime.
# conn = sqlite3.connect('employee.db')              # Storing db in a file

c = conn.cursor()

# Creating a table
c.execute("""CREATE TABLE employees(
            first text,
            last text,
            pay integer      
            )""")

def insert_emp(emp):
    with conn:                                      # Since we are using context manager, we do not need to commit
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last = :last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                  WHERE first = :first and last = :last""",
                {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first and last = :last",
                  {'first': emp.first, 'last': emp.last})

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.pay)

# Adding data to the table
# c.execute("INSERT INTO employees VALUES ('Aman', 'Goyal', 50000)")
# c.execute("INSERT INTO employees VALUES ('Naman', 'Goyal', 70000)")

# Passing values that we may get from an end user (Don't use string formatting as it will break the database and eventually the entire code)
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# conn.commit()

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
# conn.commit()
# Querying the database
# c.execute("SELECT * FROM employees WHERE last = ?", ('Goyal',))

# c.fetchone()                                         # Fetches only 1 result
# c.fetchmany(num)                                     # Fetches as many records as we pass as argument
# c.fetchall()                                         # Fetches all the records as a list
# print(c.fetchall())

# c.execute("SELECT * FROM employees WHERE last = :last", {'last': 'Doe'})
# print(c.fetchall())

# conn.commit()                                         # Commits the changes

conn.close()