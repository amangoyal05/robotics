import logging
import employee

# There are five levels of logging, namely - 

# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
# Default level of logging - Warning. This means it will ignore Debug and Info
# https://docs.python.org/3/library/logging.html

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def add(x ,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result =  x / y
    except ZeroDivisionError:
        # logger.error('Tried to divide by zero')
        logger.exception('Tried to divide by zero')
    else:
        return result
    
num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
logger.debug(f'Add: {num_1} + {num_2} = {add_result}')

sub_result = subtract(num_1, num_2)
logger.debug(f'Sub: {num_1} - {num_2} = {sub_result}')

mul_result = multiply(num_1, num_2)
logger.debug(f'Mul: {num_1} * {num_2} = {mul_result}')

div_result = divide(num_1, num_2)
logger.debug(f'Div: {num_1} / {num_2} = {div_result}')