# Dictionaries are key-value pairs. Similar to hash maps and associative arrays in other languages.
# Think of it as a real dictionary. You have word (key) : meaning (value)

student = {'name':'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)
print(student['name'])

# We can also use integers as key
print(student.get('name'))
print(student.get('phone'))         # This won't give an error on accessing a key that does not exist. It will return None. We can set to some other default value as well.
print(student.get('phone', 'Not Found'))

# Adding enteries to dictionary
student['phone'] = '555-55555'
print(student)

# Updating the value of a key
student['name'] = 'Aman'
print(student)

# Updating multiple values and adding new key value pair to a dictionary
student.update({'name': 'John', 'age': 23, 'address': 'XYZ'})
print(student)

# Deleting key value pair from a dictionary
del student['address']
print(student)

# Or delete using pop method to delete as well as get the deleted value
phone = student.pop('phone')
print(student)
print(phone)

# Check the length of the dictionary
print(len(student))

print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key, value in student.items():
    print(key,': ', value)