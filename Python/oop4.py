# Inheritance

class Employee:

    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

emp_1 = Employee('Test', 'Employee', 50000)
dev_1 = Developer('Aman', 'Goyal', 50000, 'Python')
dev_2 = Developer('Test', 'Developer', 60000, 'Java')

# print(help(Developer))

print(dev_1.pro_lang)
print(dev_2.email)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(dev_2.pay)
dev_2.apply_raise()
print(dev_2.pay)

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.print_emps()

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Manager))
