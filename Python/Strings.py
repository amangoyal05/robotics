# Using a variable to hold a string
message = 'Hello World'
print(message)

# snake_case naming
my_message = 'Hello World again using snake_case'
print(my_message)

# Handling '' issues - Suppose we want to print Bobby's World. If we do print('Bobby's World), it will give an error.
message = 'Bobby\'s World'
print(message)

message = "Bobby's World"
print(message)

# Printing multiple lines
long_message = """Bobby's World was a 
good cartoon in the 1990s"""
print(long_message)

# String functions
message = 'Hello World'
print(len(message))     # Length of the string