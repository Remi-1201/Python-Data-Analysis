"""
1 - Create a list nested_list consisting of five empty lists
"""

nested_list = [[], [], [], [], []]

# Tests
print(nested_list) # [[], [], [], [], []]

"""
2 - Create a list nested_list of length 5 whose items 
are themselves lists consisting of 3 zeros
"""

nested_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Tests
print(nested_list)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]] 

"""
3 - Create a list zero_list consisting of 3 zeroes using a list comprehension 
"""
 
zero_list = [0 for dummy_idx in range(3)]
 
nested_list = [[0 for dummy_idx1 in range(3)] for dummy_idx2 in range(5)]

# Tests
print(zero_list)
print(nested_list)
 
#[0, 0, 0]
#[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

"""
4 - Select a specific item in a nested list
"""

# Define a nested list of lists
nested_list = [[col + 5 * row for col in range(2)] for row in range(3)]
print(nested_list) #[[0, 1], [5, 6], [10, 11]]

# Add code to print out the item in this nested list with value 5
print(nested_list[1][0]) #5

"""
5 - Analyze a reference issue involving a nested list
"""

# Create a nested list
zero_list = [0, 3, 0]
nested_list = []
for dummy_idx in range(3):
     nested_list.append(list(zero_list)) 
print(nested_list)
    
# Update an entry 
nested_list[2][1] = 10
print(nested_list)

"""
6 - Create a list list_dicts of 5 empty dictionaries
"""
list_dicts = [{}, {}, {}, {}, {}]

# Tests
print(list_dicts) # [{}, {}, {}, {}, {}] 

"""
7 - Write a function dict_copies(my_dict, num_copies) that 
returns a list consisting of num_copies copies of my_dict
"""
 
def dict_copies(my_dict, num_copies): 
    answer = []
    for idx in range(num_copies):
        answer.append(dict(my_dict))
    return answer

# Tests
print(dict_copies({}, 0)) #[]
print(dict_copies({}, 1)) #[{}]
print(dict_copies({}, 2)) #[{}, {}]

test_dict = dict_copies({'a' : 1, 'b' : 2}, 2)
print(test_dict)
#[{'a': 1, 'b': 2}, {'b': 2, 'a': 1}]

# Check for reference problem
test_dict[1]["a"] = 3
print(test_dict)
#[{'b': 2, 'a': 1}, {'b': 2, 'a': 3}]

# Note that you have a reference issue if the last line of output is
#[{'a': 3, 'b': 2}, {'b': 2, 'a': 3}]

"""
8 - Write a function make_dict_lists(length) 
that returns a dictionary whose keys are in range(length) 
and whose corresponding values are lists of zeros with length matching the key
"""
 
def make_dict_lists(length):
 
    list_dicts = {}
    for idx in range(length):
        list_dicts[idx] = [0] * idx
    return list_dicts

# Tests
print(make_dict_lists(0)) #{}
print(make_dict_lists(1)) #{0: []}
print(make_dict_lists(5)) #{3: [0, 0, 0], 0: [], 4: [0, 0, 0, 0], 1: [0], 2: [0, 0]}

"""
9 - Create a dictionary grade_table whose keys are provided
student names and values are associated list of grades
"""

# Add code here
grade_table = {"Joe" : [100, 98, 100, 13],
              "Scott" : [75, 59, 89, 77],
              "John" : [86, 84, 91, 78]}

# Tests
print(grade_table["Joe"]) #[100, 98, 100, 13]
print(grade_table["Scott"]) #[75, 59, 89, 77]
print(grade_table["John"]) #[86, 84, 91, 78]

"""
10 - Create a function make_grade_table(names, grades_list) 
whose keys are the names in names and whose values are the
lists of grades in grades
"""
 
def make_grade_table(name_list, grades_list):
 
    grade_table = {}
    for name, grades in zip(name_list, grades_list):
        grade_table[name] = grades
    return grade_table
        
# Tests
print(make_grade_table([], [])) #{}

name_list = ["Joe", "Scott", "John"]
grades_list = [100, 98, 100, 13], [75, 59, 89, 77],[86, 84, 91, 78] 
print(make_grade_table(name_list, grades_list))

#{'Scott': [75, 59, 89, 77], 'John': [86, 84, 91, 78], 'Joe': [100, 98, 100, 13]}

"""
11 - Quiz
"""
NUM_ROWS = 5
NUM_COLS = 9

# construct a matrix
my_matrix = {}
for row in range(NUM_ROWS):
    row_dict = {}
    for col in range(NUM_COLS):
        row_dict[col] = row * col
    my_matrix[row] = row_dict
    
print(my_matrix)
#{1: {1: 1, 2: 2, 4: 4, 7: 7, 3: 3, 5: 5, 8: 8, 6: 6, 0: 0}, 4: {5: 20, 7: 28, 2: 8, 6: 24, 1: 4, 3: 12, 8: 32, 0: 0, 4: 16}, 2: {0: 0, 4: 8, 5: 10, 8: 16, 6: 12, 3: 6, 1: 2, 7: 14, 2: 4}, 0: {8: 0, 1: 0, 4: 0, 3: 0, 7: 0, 6: 0, 5: 0, 0: 0, 2: 0}, 3: {2: 6, 6: 18, 4: 12, 0: 0, 7: 21, 5: 15, 1: 3, 8: 24, 3: 9}}
 
# print the matrix
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        print(my_matrix[row][col], end = " ")
    print()
    
""" 
0 0 0 0 0 0 0 0 0 
0 1 2 3 4 5 6 7 8 
0 2 4 6 8 10 12 14 16 
0 3 6 9 12 15 18 21 24 
0 4 8 12 16 20 24 28 32 
"""
