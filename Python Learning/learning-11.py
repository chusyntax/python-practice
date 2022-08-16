# Functional Programming

# About seperation of concerns
# Also seperating data and functions
# They have an emphisis on simplicity where data and functions are concerned
# Functions operate on well definded data structures
# Goal- Mka code clean and extendable, keep code dry, keep code memory efficient

# Pure Functions
# Pure functions are more of a guideline than an absolute
# Rule 1- Given same input, will always return the same output
# Rule 2 - A function should not produce side effects i.e FUnction uses variable that is out of its scope

# new_list = [] #Thsi would also be interacting with the outside world

from functools import reduce


def multiply_2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    # Has side effects because print interacts with the outside world
    return print(new_list)


multiply_2([1, 2, 3])

# Map

# first param - function (action)
# second param - iterable (what we want to take action upon)
# In order for us to view map, we need to turn it into a list first - or else we will just get the memory location


def multiply_4(number):
    return number*4


print(list(map(multiply_4, [1, 2, 6])))

# Map calls the function
# It runs the function, loops through all tiems in terable then returns new map object that we need to convert into a list
# Map doesnt have side effects
# You get bac the same number of items

# Filter

# You could get less items back
# Filter method tries to recieve a boolean value
# Prints out what is true after function runs
# Filter accepts function signature and runs the function on each item(iterable)
# Also creates a new list


def only_odd(filt):
    return filt % 2 != 0


print(list(filter(only_odd, [1, 2, 3])))

# Zip

# You need two or more lists or iterables
# Needs to be in a list function in order to be printed out and read
# Takes items in the same index and adds them together in a tuple
# Does not modify the original

list_1 = [2, 35, 5]
list_2 = [5, 7, 1]

print(list(zip(list_1, list_2)))

# Reduce

# Reduces the iterable to a single
# Not a built in function ~ Must be imported from functools


#reduce(function, sequence/data,initial)
# It accumulates numbers then returns one single number

def accumulator(acc, item):
    # First item is the first item from the list, acc will default to zero
    return acc + item
# For the next pass through, whatever wass returned before will be the acc


# We dont need to print with the list method
print(reduce(accumulator, list_1, 0))


# Exercise

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalized(string):
    return string.upper()


print(list(map(capitalized, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

my_numbers.sort()
print(list(zip(my_numbers, my_strings)))


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def over_50(li):
    return li > 50


print(list(filter(over_50, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

print(reduce(accumulator, (scores + my_numbers)))

# Lambda Expressions

# They are one time anonymous functions that you dont need to run more than once
# Because they are used once, they dont need a name
# Lambda param: action(param)

# takes an item from 'scores' and multiplies it by two then automatically returns it
print(list(map(lambda item: item*2, scores)))

# 146-Exercise: Lambda Expressions

# Square

square_list = [5, 4, 3]

print(list(map(lambda square: square**2, square_list)))

# List Sorting

sorting_list = [(0, 2), (4, 3), (9, 9), (10, -1)]

# To iterate over each tuple. X is going to be the second value in the tuple
sorting_list.sort(key=lambda x: x[1])


# Comprehensions

# This can be done on lists, sets and dictionaries
# A Quick way to create list, sets or dicts instead of looping or appending items

#Lists =  [param for param in iterable]
# First char can be how we want to act upon each item, like in Lambda
comp_list = [char for char in 'hello']
comp_list2 = [number for number in range(0, 100)]
comp_list3 = [number*2 for number in range(0, 100)]
comp_list4 = [number**2 for number in range(0, 100) if number % 2 == 0]

print(comp_list)
print(comp_list2)
print(comp_list3)
print(comp_list4)

#Sets = {param for param in iterable}
comp_set = {char for char in 'hello'}
comp_set2 = {number for number in range(0, 100)}
comp_set3 = {number*2 for number in range(0, 100)}

# Dictionaries

# First create simple dictionary in order for looping to work

simple_dict = {
    'a': 1,
    'b': 2
}

comp_dict = {key: value**2 for key, value in simple_dict.items()}

print(comp_dict)

# If you dont have keys and want to make the iterables the keys
comp_dict2 = {num: num**2 for num in [1, 2, 3]}
print(comp_dict2)


# 149-Exercise: Comprehensions

prac_list = ['a', 'b', 'c', 'd', 'd', 'n', 'n']

# count() is a method that tells us how many times an item appears in a list
duplicates = list(set([dup for dup in prac_list if prac_list.count(dup) > 1]))


print(duplicates)
