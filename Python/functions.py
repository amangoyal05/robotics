# def - stands for definition
# hello_func - function name
# () - hold the parameters
# pass - allows to define a function without any code in it for the time being. This prevents errors.
def hello_func():
    pass

print(hello_func)       # This will print the location where the function is stored.
print(hello_func())     # This will execute the function

def hello():
    return "Hello Function!"

# DRY (Don't Repeat Yourself) - use functions or variables to repeat something. don't do it manually.
print(hello().upper())

def hello1(greeting):
    return f'{greeting} Function.'

print(hello1('Hi'))

# Function with a default value for the parameter
def hello1(greeting, name='You'):
    return f'{greeting}, {name}.'

print(hello1('Morning'))
print(hello1('Morning', 'Aman'))

# *args - allows to accept an arbitrary number of positional arguments
# *kwargs - allows to accept an arbitrary number of keyword arguments
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name = 'John', age = 22)

# Passing a list and a dictionary as an argument and telling the function which is args and which is kwargs
def student_info1(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info1(*courses, **info)


""" This is a docstring used for documentation purpose """
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2017))
print(days_in_month(2017, 2))