# Decorators with arguments

def prefix_decorator(prefix):
    def decorator_func(original_function):
        def wrapper_func(*args, **kwargs):
            print(prefix, 'Executed Before ', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed After', original_function.__name__)
            return result
        return wrapper_func
    return decorator_func

@prefix_decorator('TESTING:')
def display_info(name, age):
    print(f'Display ran with arguments ({name}, {age})')

display_info('John', 25)
display_info('Travis', 30)