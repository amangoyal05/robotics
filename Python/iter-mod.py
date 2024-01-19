import itertools, operator

counter = itertools.count()

data = [100, 200, 300, 400]

# Combines two iterables and zip them together
daily_data = list(zip(itertools.count(), data))

print(daily_data)

counter1 = itertools.count(start = 5, step = 5)
print(next(counter1))
print(next(counter1))
print(next(counter1))

counter1 = itertools.count(start = 5, step = -2.5)
print(next(counter1))
print(next(counter1))
print(next(counter1))
print(next(counter1))


# zip_longest zips the values according to the longest list and when the smaller list gets exhausted, it uses None instead.
daily_data = list(itertools.zip_longest(range(10), data))
print(daily_data)

# cycle returns an iterator that goes on forever, that is, it keeps cycling over the values.
cycler = itertools.cycle([1, 2, 3])
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))

cycler = itertools.cycle(('On', 'Off'))
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))


# Repeat takes in some input and repeats it indefinitely
repeater = itertools.repeat(2)
print(next(repeater))
print(next(repeater))
print(next(repeater))
print(next(repeater))

repeater = itertools.repeat(2, times = 3)           # times will allow the value to be repeated n times only. After that it will throw StopIteration error
print(next(repeater))
print(next(repeater))
print(next(repeater))
# print(next(repeater))

# map takes a function and then takes iterables to pass as values to that function until the shortest list of arguments is exhausted
squares = list(map(pow, range(10), itertools.repeat(2)))
print(squares)

# starmap is similar as map but instead of taking iterables as arguments, it takes arguments that are already paired as tuples
squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2), (3, 2)])
print(list(squares))

# Permutations and Combinations
letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Aman', 'Nicole']

result = itertools.combinations(letters, 2)

for item in result:
    print(item)

result = itertools.permutations(letters, 2)
print("Permutations: ")
for item in result:
    print(item)

result = itertools.product(numbers, repeat = 4)
print("Result with repeatitions: ")

for item in result:
    print(item)

result = itertools.combinations_with_replacement(numbers, 4)
print("Result with repeatitions using Combinations: ")
for item in result:
    print(item)

# chain allows to chain together iterables. It will go through 1st iterable until it gets exhausted and then moves to the next iterable.
chained = itertools.chain(letters, numbers, names)
print(list(chained))

# islice allows to slice an iterator. This is helpful as we do not need to save values to a list and then slice it. We can directly use islice for that and save memory.
sliced = itertools.islice(range(10), 1, 5, 2)

for item in sliced:
    print(item)

# Files are iterators themselves.
with open("test1.log", "r") as f:
    header = itertools.islice(f, 3)
    
    for line in header:
        print(line, end='')

# compress
selectors = [True, True, False, True]

result = itertools.compress(letters, selectors)

for item in result:
    print(item)


def lt_2(n):
    if n < 2:
        return True
    return False

result = filter(lt_2, numbers)
for item in result:
    print(item)

# filterfalse gives values that return false instead of true
result = itertools.filterfalse(lt_2, numbers)
for item in result:
    print(item)

# dropwhile will drop values from an iterable until one of the value returns true. after finding first true, it returns the iterable after that
numbers = [0, 1, 2, 3, 2, 1, 0]
result = itertools.dropwhile(lt_2, numbers)

for item in result:
    print(item)

# takewhile is the opposite of this. It will return values until a value is false. After that it will stop returning values.
result = itertools.takewhile(lt_2, numbers)

for item in result:
    print(item)

# accumulate takes an iterable and returns a sum of each item it sees. It uses addition by default but we can use other operations as well.
result = itertools.accumulate(numbers)

for item in result:
    print(item)

numbers = [1, 2, 3, 2, 1, 0]
result = itertools.accumulate(numbers, operator.mul)

for item in result:
    print(item)

# groupby will go through an iterator and group the values based on a certain key. Then it will return a stream of tuples.
people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

def get_state(person):
    return person['state']

person_group = itertools.groupby(people, get_state)
for key, group in person_group:
    print(key, len(list(group)))
    for person in group:
        print(person)
    print()

# groupby expects the value to be sorted. In the above example, all the values are sorted according to the state.
    
# tee is used for replicating iterators. Do not use the original iterator after replicating it.
copy1, copy2 = itertools.tee(person_group)