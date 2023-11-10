import random

# random generates a random number between [0, 1)
value = random.random()
print(value)

value = random.uniform(1, 10)
print(value)

# Random integers
value = random.randint(1, 6)            # 1 and 6 are inclusive
print(value)

# choice picks a random value from a list of values
greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
value = random.choice(greetings)
print(value + ', Aman!')

# choices picks k random values from a list
# weights is used to specificy the chances of selecting a value from the list. For eg - Red has 18 out of 38 chance of randomly being selected.
colors = ['Red', 'Black', 'Green']
result = random.choices(colors, weights=[18, 18, 2], k=10)
print(result)

# Shuffling values
deck = list(range(1, 53))
random.shuffle(deck)
print(deck)

# sample - selects k unique value
hand = random.sample(deck, k=5)
print(hand)