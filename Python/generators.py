def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums)

# The above code to a generator
def square_nums(nums):
    for i in nums:
        yield (i*i)

my_nums = square_nums([1, 2, 3, 4, 5])

# A generator function holds only one value at a time which is why we use a for loop or use -
# print(next(num))
for num in my_nums:
    print(num)

# Above code using list comprehension
my_nums1 = (x*x for x in [1,2,3,4,5])

# for num in my_nums1:
#     print(num)

# Printing the result by converting result from a generator function to a list
my_nums1 = (x*x for x in [1,2,3,4,5])
print(list(my_nums1))