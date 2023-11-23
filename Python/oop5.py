# Special (magic) methods - __methodName__ (__ - Dunder)

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

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

# __str__ is called before __repr__. __repr__ is the fallback function of __str__

emp_1 = Employee('Aman', 'Goyal', 50000)
emp_2 = Employee('Test', 'Developer', 60000)

print(emp_1)

print(repr(emp_1))
print(emp_1)

print(emp_1.__repr__())
print(emp_1.__str__())

print(1+2)                  # It uses a special function __add__ to add

print(int.__add__(1,2))
print(str.__add__('a', 'b'))

print(emp_1 + emp_2)        # Uses the __add__ defined by us in the Employee class

print(len('test'))

print('test'.__len__())

print(len(emp_1))