# List and Tuples allow us to work with sequential data
# Sets are unordered collection of values with no duplicates

# LISTS
courses = ['History', 'Maths', 'Physics', 'CompSci']
courses_1 = ['History', 'Maths', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
print(courses)
print(len(courses))
print(courses[-1])
print(courses[0:2])

courses.append('Art')           # Adding a new value to list
courses.insert(0, 'English')    # Inserting a new value at a specific index

print(courses)

courses_1.insert(0, courses_2)  
print(courses_1)
print(courses_1[0])

# Inserting a list to another list will create nested list. 
# However, if we want to add values from one list to another list, we will use 'extend'
courses_1.extend(courses_2)
print(courses_1)

courses.remove('Maths')
print(courses)

courses.pop()                   # Removes last value from list like a stack
print(courses)

popped = courses.pop()
print(popped)
print(courses)

courses_1.remove(courses_1[0])
print(courses_1)

courses_1.reverse()
print(courses_1)

courses_1.sort()            # Sorting in ascending order
print(courses_1)

nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums)

courses_1.sort(reverse=True)
print(courses_1)

nums.sort(reverse=True)
print(nums)

# Sorting the list without altering the original list
sorted_courses = sorted(courses_1)
print(sorted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

# Finding index of a value in list
print(courses_1.index('CompSci'))

# Checking if a value exists in the list
print('Economics' in courses_1)
print('Maths' in courses_1)

for index, item in enumerate(courses, start=1):         # enumerate accesses the index and the value
    print(index, item)

# Joining list items and returning them as a string
course_str = ', '.join(courses_1)

print(course_str)

# Turning a string into a list
new_list = course_str.split(', ')

print(new_list)

# Mutable - can be edited. Lists are mutable
# Immutable - can not be edited. Tuples are immutable

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Physics', 'Compsci', 'Math'}
# The order may change after printing again and again. This is because
# sets do not care about the order of the items. They throw away duplicates.
print(cs_courses)
# Sets are best for membership tests. List and Tuples are also good but Sets are optimized for this.
print('Math' in cs_courses)

art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# Empty Lists
empty_list = []
empty_list = list[]

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}          # This isn't right! It's a dict
empty_set = set()       # Only method to create empty set