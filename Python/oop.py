# Object-Oriented Programming
# Why classes - They allow to logically group data and functions in a way that is easy to reuse and also easy to build upon
# attribute - data associated with a class
# method - function associated with a class

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('Aman', 'Goyal', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(Employee.fullname(emp_2))