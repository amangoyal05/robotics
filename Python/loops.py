# for LOOPS
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

# break - helps to breakout of the loop
# continue - moves on to the next iteration of the loop

# Suppose we are looking for a number. We find that and wish to exit the loop
for num in nums:
    print(num)
    if num == 3:
        print('Found!')
        break

# What if we want to ignore a value and not break out of the loop
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

# Nested Loops
for num in nums:
    for letter in 'abc':
        print(num, letter)

# range
for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

#  while LOOPS - They will continue looping until we reach a condition that is False
x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

x = 0
# Infinite Loop
while True:
    print(x)
    x += 1