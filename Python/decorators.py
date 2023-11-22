# Decorator - Function that takes another function as an argument, adds some functionality and returns another function without altering the source code of the original function that we passed

def decorator_func(original_function):
    def wrapper_func(*args, **kwargs):
        print(f'Wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_func


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'Call Method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)
    
# @decorator_func
@decorator_class
def display():
    print('Display Function ran')

# @decorator_func
@decorator_class
def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')

display()
display_info('John', 25)