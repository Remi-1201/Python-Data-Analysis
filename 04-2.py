"""
04-2 Lambda & creating and using anonymous functions.
"""

import random

# 04-2-1 Easily create a list of numbers
data = list(range(10))
print("range data:", data)
# range data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def square(val):
    return val ** 2

# 04-2-2 Square all numbers in the list
squares = list(map(square, data))
print("squares:", squares)
# squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 04-2-3 Double all numbers in the list
doubles = list(map(lambda num: num * 2, data))
print("doubles:", doubles)
# doubles: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 04-2-4 Create a list of random numbers (list comprehension)
randnums = [random.randrange(2, num+3) for num in range(10)]
print("random numbers:", randnums)
# random numbers: [2, 2, 3, 2, 3, 6, 4, 6, 6, 10]

# 04-2-5 Create a list of tuples
tups = list(map(lambda num1, num2: (num1, num2), data, randnums))
print("tuples:", tups)
# tuples: [(0, 2), (1, 2), (2, 3), (3, 2), (4, 3), (5, 6), (6, 4), (7, 6), (8, 6), (9, 10)]

# 04-2-6 Create a list of the min values in the tuples
mins = list(map(lambda pair: min(pair[0], pair[1]), tups))
print("minimums:", mins)
# minimums: [0, 1, 2, 2, 3, 5, 4, 6, 6, 9]

# 04-2-7 Create a list only of tuples where the second item is less than the first
newtups = list(filter(lambda pair: pair[1] < pair[0], tups))
print("filtered:", newtups)
# filtered: [(3, 2), (4, 3), (6, 4), (7, 6), (8, 6)]
