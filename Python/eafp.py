# Duck Typing and Easier to Ask Forgiveness Than Permission (EAFP)

class Duck:
    
    def quack(self):
        print('Quack', 'quack')
    
    def fly(self):
        print('Flap', 'flap')

class Person:

    def quack(self):
        print("I'm Quacking Like a Duck!")
    
    def fly(self):
        print("I'm Flapping my Arms!")


# def quack_and_fly(thing):
#     # Not Duck-Typed (Non-Pythonic)
#     # if isinstance(thing, Duck):
#     thing.quack()
#     thing.fly()
#     # else:
#     # print("This has to be a Duck!")

#     print()


# def quack_and_fly(thing):
#     # Look Before You Leave (Non-Pythonic)
#     if hasattr(thing, 'quack'):
#         if callable(thing.quack):
#             thing.quack()

#     if hasattr(thing, 'fly'):
#         if callable(thing.fly):
#             thing.fly()

#     print()

def quack_and_fly(thing):
    # EAFP (Pythonic)
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

    print()

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

# Another example
# person = {'name': 'Jess', 'age': 23, 'job': 'Programmer'}
person = {'name': 'Jess', 'age': 23}

# LBYL (Non-Pythonic)
# if 'name' in person and 'age' in person and 'job' in person:
#     print(f"I'm {person['name']}. I'm {person['age']} years old and I am a {person['job']}")
# else:
#     print('Missing some keys')

# EAFP (Pythonic)
try:
    print(f"I'm {person['name']}. I'm {person['age']} years old and I am a {person['job']}")
except KeyError as e:
    print(f"Missing {e} key")


my_list = [1, 2, 3, 4, 5]

# Non-Pythonic
# if len(my_list) >= 6:
#     print(my_list[5])
# else:
#     print('That index does not exist')

# Pythonic
try:
    print(my_list[5])
except IndexError:
    print('That index does not exist')


import os

my_file = 'test_file.txt'

# Race Condition
# if os.access(my_file, os.R_OK):
#     with open(my_file) as f:
#         print(f.read())

# else:
#     print('File can not be accessed')

# Non-Race Condition
try:
    f = open(my_file)
except IOError as e:
    print('File can not be accessed')
else:
    with f:
        print(f.read())