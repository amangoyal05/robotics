# iterable - something that can be looped over.

nums = [1, 2, 3]

for num in nums:
    print(num)

# How do we know if something is iterable?
# If something is iterable, it will have the __iter__ method
    
print(dir(nums))

# iterator - an object with a state so that it remembers where it is during iteration.
# iterators get next value through __next__ method. nums does not have any __next__ method printed in the terminal when using dir(nums), ergo it is not an iterator.

# i_nums = nums.__iter__()
i_nums = iter(nums)              # The above and this statement are the same
print(dir(i_nums))
print(i_nums)
print(next(i_nums))

# next(i_nums) prints the next element in i_nums and throws an error when the complete list gets exhausted 
# For loop does the same thing. It changes the data structure to a iterator and then prints the next element. It handles the error automatically.

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break

# Iterators can only go forward. To start from beginning, create a new iterator.
    
class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current
    
nums = MyRange(1, 10)

print(next(nums))

# Generators are a type of iterator only. Let's create a generator for the above task.

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


nums1 = my_range(1, 10)

for num in nums1:
    print(num)

# Iterators don't need to end.
# The following is an infinite loop
def my_range1(start):
    current = start
    while True:
        yield current
        current += 1


nums2 = my_range1(1)

for num in nums2:
    print(num)