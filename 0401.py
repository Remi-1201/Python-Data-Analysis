"""
4-1 Example code to sort sequences
"""

import random

# 4-1-1 Easily create a list of numbers
data = list(range(10))
print("range data:", data)
# range data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 4-1-2 Randomly shuffle those numbers
random.shuffle(data)
print("shuffled data:", data)
# shuffled data: [7, 2, 9, 5, 8, 4, 1, 0, 3, 6]

# 4-1-3 Sort the list of numbers
data.sort()
print("sorted data:", data)
# sorted data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 4-1-4 Shuffle it again
random.shuffle(data)
print("shuffled data:", data)
# shuffled data: [0, 4, 6, 1, 9, 8, 3, 7, 5, 2]

# 4-1-5 Use sorted to sort the list
newdata = sorted(data)

print("data after sorted:", data)
# data after sorted: [0, 4, 6, 1, 9, 8, 3, 7, 5, 2]

print("returned from sorted:", newdata)
# returned from sorted: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 4-1-6 Convert to a tuple
datatup = tuple(data)
print("data tuple:", datatup)
# data tuple: (0, 4, 6, 1, 9, 8, 3, 7, 5, 2)

# 4-1-7 Sort the tuple of numbers
# datatup.sort()

print("tuple after sort:", datatup)
# tuple after sort: (0, 4, 6, 1, 9, 8, 3, 7, 5, 2)

# 4-1-8 Use sorted to sort the tuple
newdatatup = sorted(datatup)
print("returned from sorted:", newdatatup)
# returned from sorted: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 4-1-9 Create a dictionary of squares (dictionary comprehension)
datamap = {key: key ** 2 for key in datatup}
print("data dictionary:", datamap)
# data dictionary: {6: 36, 2: 4, 8: 64, 9: 81, 0: 0, 5: 25, 1: 1, 3: 9, 4: 16, 7: 49}

# 4-1-10 Use sorted to sort the dictionary
sortmap = sorted(datamap)
print("returned from sorted:", sortmap)
# returned from sorted: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
