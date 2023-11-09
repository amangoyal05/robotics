# List Comprehension
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Let us see how a normal for loop will look like
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# Doing the same thing using list comprehension
my_list1 = [n for n in nums]
print(my_list1)

my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

my_list1 = []
my_list1 = [n*n for n in nums]
print(my_list1)

my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
print(my_list)

my_list1 = []
my_list1 = [n for n in nums if n%2 == 0]
print(my_list1)

my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)

my_list1 = []
my_list1 = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list1)

# Dictionary Comprehension
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
dic = list(zip(names, heros))
print(dic)

my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

my_dict1 = {name: hero for name, hero in zip(names, heros)}
print(my_dict1)

# If name is not equal to Peter
my_dict1 = {}
my_dict1 = {name: hero for name, hero in zip(names, heros) if name!='Peter'}
print(my_dict1)

# Set Comprehension
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 6, 7, 8, 7, 9, 9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

my_set1 = {n for n in nums}
print(my_set1)

# Generator Expressions

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def gen_func(nums):
    for n in nums:
        yield(n*n)

my_gen = gen_func(nums)

for i in my_gen:
    print(i)

# Using comprehension

my_gen1 = (n*n for n in nums)

for i in my_gen1:
    print(i)