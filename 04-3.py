"""
4-03 More advanced sorting examples.
"""

import random

# 4-03-1 Easily create a shuffled list of numbers
data = list(range(10))
random.shuffle(data)
print("shuffled data:", data)
#shuffled data: [9, 1, 5, 2, 4, 6, 7, 3, 0, 8]

# 4-03-2 Sort the list of numbers
data.sort()
print("ascending sort:", data)
# ascending sort: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

data.sort(reverse=True)
print("descending sort:", data)
# descending sort: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 4-03-3 Create a list of tuples
datatups = [(item, random.randrange(3, 15)) for item in data]
print("data tuples:", datatups)
# data tuples: [(9, 11), (8, 6), (7, 13), (6, 8), (5, 9), (4, 7), (3, 14), (2, 9), (1, 8), (0, 3)]

# 4-03-4 Sort the list
datatups.sort()
print("sorted data tuples:", datatups)
# sorted data tuples: [(0, 10), (1, 7), (2, 10), (3, 14), (4, 6), (5, 14), (6, 13), (7, 13), (8, 13), (9, 4)]

datatups.sort(key=lambda pair: pair[1])
print("sorted by second item:", datatups)
# sorted by second item: [(3, 4), (4, 4), (9, 5), (0, 6), (5, 7), (2, 8), (8, 8), (6, 9), (7, 11), (1, 13)]

datatups.sort(key=lambda pair: pair[0] * pair[1], reverse=True)
print("sorted by product:", datatups)
# sorted by product: [(6, 12), (7, 10), (5, 13), (8, 8), (9, 4), (3, 11), (4, 8), (2, 10), (1, 3), (0, 11)]

# 4-03-5 Shuffle it again
random.shuffle(datatups)
print("shuffled tuples:", datatups)
# shuffled tuples: [(4, 13), (8, 7), (9, 8), (1, 13), (5, 9), (0, 3), (2, 6), (3, 5), (7, 8), (6, 9)]

# 4-03-6 Use sorted to sort the list
newdata = sorted(datatups, key=lambda pair: pair[1], reverse=True)

print("tuples after sorted:", datatups)
# tuples after sorted: [(9, 5), (4, 6), (3, 14), (5, 14), (2, 5), (0, 6), (8, 7), (6, 8), (7, 5), (1, 6)]

print("returned from sorted:", newdata)
# returned from sorted: [(3, 14), (5, 14), (6, 8), (8, 7), (4, 6), (0, 6), (1, 6), (9, 5), (2, 5), (7, 5)]
