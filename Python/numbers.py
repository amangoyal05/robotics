num = 3
pi = 3.14
# checking the data type of a variable
print(type(num))
print(type(pi))

# Arithmetic Operators:
# Addition:       3 + 2     = 5
# Subtraction:    3 - 2     = 1
# Multiplication: 3 * 2     = 6
# Division:       3 / 2     = 1.5
# Floor Division: 3 // 2    = 1
# Exponent:       3 ** 2    = 9
# Modulus:        3 % 2     = 1

# Order of operations is same as maths

num = 1

num += 1        # Can replace + with other operators
print(num)

print(abs(-3))
print(round(3.75, 1))

# Comparison Operators:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <=2

num_1 = 3
num_2 = 2

print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)


num_1 = '100'
num_2 = '200'

print(num_1 + num_2)

# We will cast num_1 and num_2 from String to Integers
num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)