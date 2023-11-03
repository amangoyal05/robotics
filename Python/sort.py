# List
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li)

print('Sorted Variable:\t', s_li)
print('Original Variable:\t', li)

li.sort()
print('Sorted Variable:\t', li)

s_li = sorted(li, reverse=True)

print('Sorted Variable:\t', s_li)

li.sort(reverse=True)
print('Sorted Variable:\t', li)

# Tuple
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)

s_tup = sorted(tup)

print('Sorted Variable:\t', s_tup)
print('Original Variable:\t', tup)

# Dictionary
di = {'name': 'Aman', 'job': 'programming', 'age': None, 'os': 'Window'}

s_di = sorted(di)

print('Sorted Variable:\t', s_di)
print('Original Variable:\t', di)

# Sorting on criteria other than ascending and descending
li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)
print(s_li)

from operator import attrgetter

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return f'({self.name}, {self.age}, ${self.salary})'
    
e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

# def e_sort(emp):
#     return emp.name

s_employees = sorted(employees, key=attrgetter('name'), reverse = True)

print(s_employees)