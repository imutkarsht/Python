# Python program to demonstrate Map, filter and reduce in python
from functools import reduce

# Map

l = [1, 2, 3, 4, 5, 6, 7]

newl = list(map(lambda x: x * x * x, l))
print(newl)

# Filter

newnewl = list(filter(lambda x: x > 2, l))
print(newnewl)

# Reduce

sum = reduce(lambda a, b: a + b, l)
print(sum)