import my_module as mm
from my_module import find_index, test                  # Importing a particular function from a module
# from my_module import *                               # Imports everything from my_module (not recommended)
import sys
sys.path.append('C:/Users/AMAN/OneDrive/Desktop/')       # Adding a path to the existing list of paths. This is not the best solution. Instead set the environment variable.

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')
print(index)

index = find_index(courses, 'Physics')
print(index)
print(test)

print(sys.path)                                         # List of paths

# Standard Libraries
import random
import math
import datetime
import calendar
import os
import antigravity

random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(rads)

sine = math.sin(rads)
print(sine)

today = datetime.date.today()
print(today)

print(calendar.isleap(2023))
print(calendar.isleap(2020))

print(os.getcwd())                                        # getcwd - get current working directory
print(os.__file__)