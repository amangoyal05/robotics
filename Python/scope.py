'''
LEGB
Local - Variables inside a function
Enclosing - Variables inside Local Scope of an Enclosing function
Global - Variables defined at the top level of a module
Built-in - Variables pre-defined
Python checks the scope of the variable in the order LEGB
'''

x = 'global x'

def test():
    x = 'local x'
    y = 'local y'
    print(x)
    print(y)

test()
print(x)

# The function above printed 'local x' when print(x) was executed inside the function.
# In order to make the variable inside the function global, we perform the following.
def test1():
    global x
    x = 'local x'
    y = 'local y'
    print(x)
    print(y)

test1()
print(x)

def test2(z):               # z can only be used inside the function 'test2'
    print(z)

test2('local z')

# Built-in functions
import builtins

print(dir(builtins))

m = min([5, 1, 4, 2, 3])
print(m)

# Python allows to override built-in functions. Take care of that.
def min():
    pass

# m = min([5, 1, 4, 2, 3])              # This will give an error as Python will look at our function definition of min which takes 0 arguments

# Enclosing

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)
    
    inner()
    print(x)

outer()

def outer1():
    x = 'outer x'

    def inner1():
        nonlocal x
        x = 'inner x'
        print(x)
    
    inner1()
    print(x)

outer1()