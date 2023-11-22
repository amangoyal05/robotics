from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 155, 255)
white = Color(255, 255, 255)
print(color)
print(color[1])
print(color.blue)
print(white)

# namedtuples are better than tuples as they are more readable. In above example, we are able to access the values easily and on printing 
# the entire tuple, we get labels assigned to each value.
# namedtuple are also better than dictionary because they are immutable. Using a dictionary also requires more code.
# Example - 
# color = {'red': 55, 'green': 155, 'blue': 255}
# white = {'red': 255, 'green': 255, 'blue': 255}
# This requires more coding