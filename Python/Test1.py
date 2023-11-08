# Write a Python function that takes a string as input and returns the reversed version of that string.

message = input("Please enter something: ")
print(message[::-1])

# Given a string, write a Python program to count the number of vowels in it.
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
count = 0
for i in message:
    if i in vowel:
        count += 1

print(count)

# Calculate the result of the expression (3 * 4 + 7) / 2 and print it.
print(float((3*4+7)/2))

# Create a list of integers from 1 to 5. Write Python code to add the number 6 to the end of the list.
nums = [1,2,3,4,5]
nums.append(6)
print(nums)

# Define a tuple containing the days of the week. Access the third element of the tuple.
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(days_of_week[2])

# Create a dictionary with the following key-value pairs: "name" - "John", "age" - 30, "city" - "New York". Print the value associated with the key "age".
diction = {"name": "John", "age": "30", "city": "New York"}
print(diction["age"])

# Write a Python program to check if a given number is even or odd. Take the number as input from the user and print the result.
num = int(input("Please enter a number (Odd-Even): "))
if num%2 == 0:
    print("It is even.")
else:
    print("It is odd.")

# Write a Python program to print the numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)

# Use a while loop to find and print the first 5 even numbers.
even_numbers = []
num = 2

while len(even_numbers) < 5:
    even_numbers.append(num)
    num += 2

for even in even_numbers:
    print(even)
    
# 10. Write a Python function that takes two numbers as input and returns their sum.
def sum_func(a,b):
    return a+b

def main():
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    result = sum_func(num1, num2)
    print("The sum is: ",result)

main()

# Define a function that calculates the factorial of a given number.
def factorial(number):
    result = 1
    for i in range(1, number+1):
        result *= i
    return result

factorial_num = int(input("Enter a number: "))
answer = factorial(factorial_num)
print("The factorial is: ",answer)

# Create a string that contains the following variables: name = "Alice", age = 25, city = "London". Use string formatting to create a message like "Alice is 25 years old and lives in London."
name = "Alice"
age = 25
city = "London"
print(f"{name} is {age} years old and lives in {city}.")

# Create a text file named "sample.txt" and write the text "Hello, World!" to it. Then, read the contents of the file and print them.
with open("sample.txt", 'w') as f:
    f.seek(0)
    f.write("Hello, World!")