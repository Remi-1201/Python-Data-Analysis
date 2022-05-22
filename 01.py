"""
1/ Initialize a dictionary my_dict to be empty
"""

# Add code here
my_dict = {}

# 1/ Tests
print(type(my_dict)) #<class 'dict'>
print(my_dict) #{} 

"""
2/ Create a dictionary my_dict that contains 
two specified value/pairs 
"""

# Add code here
my_dict = {"Joe" : 1, "Scott" : 2}

# An alternative approach
#my_dict = {}
#my_dict["Joe"] = 1
#my_dict["Scott"] = 2

# 2/ Tests
print(type(my_dict)) #<class 'dict'>
print(my_dict["Joe"]) #1
print(my_dict["Scott"]) #2
print(my_dict) #{'Scott': 2, 'Joe': 1} 

"""
3/ Add the specified key/value pair to an
existing dictionary my_dict
"""

# Initialize dictionary
my_dict = {"Joe" : 1, "Scott" : 2}

# Add key/value pair "John" : 3
my_dict["John"] = 3

# 3/ Tests
print(type(my_dict)) #<class 'dict'>
print(my_dict["Joe"]) #1
print(my_dict["Scott"]) #2
print(my_dict["John"]) #3
print(my_dict) #{'Scott': 2, 'John': 3, 'Joe': 1} 

"""
4/ Template - Write an expression that determines whether
a key is in a dictionary
"""

my_dict = {"Joe" : 1, "Scott" : 2, "John" : 3}
print("Joe" in my_dict) #True
print("John" in my_dict) #True
print("Stephen" in my_dict) #False

"""
5/ Write a function is_empty(my_dict) that
returns True if a dictionary is empty and False otherwise
"""

def is_empty(my_dict): 
    
    return len (my_dict) == 0

# Testing code
print(is_empty({})) #True
print(is_empty({0 : 1})) #False
print(is_empty({"Joe" : 1, "Scott" : 2})) #False 

"""
6/ Write a function value_sum(my_dict) that
returns the sum of the values in a dictionary
"""

def value_sum(my_dict): 
    
    value_sum = 0
    for key in my_dict:
        value_sum += my_dict[key]
    return value_sum

# Testing code
print(value_sum({})) #0
print(value_sum({0 : 1})) #1
print(value_sum({"Joe" : 1, "Scott" : 2, "John" : 4})) #7 

"""
7/ Write a function make_dict(key_value_list) that
takes a list of tuples (key, value) and returns a 
dictionary with these keys and values
"""

def make_dict(key_value_list):

    answer = {}
    for key, value in key_value_list:
        answer[key] = value
    return answer 
  
print(make_dict([])) #{}
print(make_dict([(0, 1)])) #{0: 1}
print(make_dict([("Joe", 1), ("Scott", 2), ("John", 4)])) 
#{'John': 4, 'Joe': 1, 'Scott': 2}

"""
8/ Using substitution ciphers to encrypt and decrypt plain text
"""
 
CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}

def encrypt(phrase, cipher_dict):
    
    answer = ""
    for letter in phrase:
        answer += cipher_dict[letter]
	return answer
 
print("Output for part 1") # Output for part 1
print(encrypt("pig", CIPHER_DICT)) #vif
print(encrypt("hello world", CIPHER_DICT)) #hunnybtygnd
print()

"""
9/ Using substitution ciphers to encrypt and decrypt plain text
# Part 2 - Compute an inverse substitution cipher that decrypts
# an encrypted phrase
"""

def make_decipher_dict(cipher_dict):
    """
    Take a cipher dictionary and return the cipher
    dictionary that undoes the cipher
    """    
    decipher_dict = {}
    for letter in cipher_dict:
        decipher_dict[cipher_dict[letter]]=[letter]
    return decipher_dict

DECIPHER_DICT = make_decipher_dict(CIPHER_DICT)

# Tests - note that applying encrypting with the cipher and decipher dicts
# should return the original results

print("Output for part 2") # Output for part 2 - note order of items in dictionary is not important
print(DECIPHER_DICT)
#{'p': 'f', 'n': 'l', 'm': 'a', 'i': 'i', 'd': 'd', 'x': 'k', 'b': ' ', 'l': 'v', 'f': 'g', 'o': 's', 'u': 'e', 'a': 'n', 'c': 'y', 'r': 'q', 'e': 'z', 'k': 'c', 'w': 'm', 'g': 'r', 'y': 'o', ' ': 't', 'h': 'h', 'v': 'p', 'j': 'x', 'q': 'u', 't': 'w', 's': 'b', 'z': 'j'}
print(encrypt(encrypt("pig", CIPHER_DICT), DECIPHER_DICT)) #pig
print(encrypt(encrypt("hello world", CIPHER_DICT), DECIPHER_DICT))	#hello world
print()

 



