# Comparisons
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

if True:
    print('Conditional was True.')

if False:
    print('Conditional was False.')

language = 'Java'

if language == 'Python':
    print('Language is Python.')

elif language == 'Java':
    print('Language is Java.')

else:
    print('No match')

# Boolean Operators
# and
# or
# not

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')

else:
    print('Bad Credentials')

if user == 'Admin' or logged_in:
    print('Admin Page')

else:
    print('Bad Credentials')

if not logged_in:
    print('Please Log In')

else:
    print('Welcome')

a = [1,2,3]
b = [1,2,3]

print(id(a))
print(id(b))
print(a is b)                   # The output is False since a and b are stored in different memory locations

c = a
print(id(c))
print(a is c)

# False Values:
#     False
#     None
#     Zero of any numeric type
#     Any empty sequence. For example, '', (), [].
#     Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaulated to True')
else:
    print('Evaulated to False')

condition = None
if condition:
    print('Evaulated to True')
else:
    print('Evaulated to False')

condition = 0
if condition:
    print('Evaulated to True')
else:
    print('Evaulated to False')

condition = 10
if condition:
    print('Evaulated to True')
else:
    print('Evaulated to False')

condition = []
if condition:
    print('Evaulated to True')
else:
    print('Evaulated to False')

condition = 'Test'
if condition:
    print('Evaulated to True')
else:
    print('Evaulated to False')

condition = {}
if condition:
    print('Evaulated to True')
else:
    print('Evaulated to False')