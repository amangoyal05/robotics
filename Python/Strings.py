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

# Accessing characters of the string
print(message[6])       # Printing W

# Accessing only Hello
print(message[0:5])     # 0 is inclusive and 5 is exclusive. 
print(message[:5])
print(message[6:])

print(message.lower())  # Lower case everything
print(message.upper())  # Upper case everytyhing

# Counting a certain number of word/alphabet
print(message.count('Hello'))
print(message.count('l'))

# Finding a certain alphabet/word
print(message.find('World'))    # Answer is 6 because World starts at 6
print(message.find('l'))
print(message.find('z'))        # Gives -1 as it does not exist

# Replacing
new_message = message.replace('World', 'Universe')
print(new_message)

# Adding/Concatenating strings
greeting = 'Hello'
name = 'Aman'
# message = greeting + ' ' + name + '. Welcome!'
# print(message)

# + is useful for small sentences. But for longer sentences, we will use another method.
# We will use formatted strings
message = f'{greeting}, {name}. Welcome!'
print(message)

# Getting all the attributes, methods and functions we can use
print(dir(name))

print(help(str))        #help(str.lower) will give information about lower function