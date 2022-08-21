# Modules
# Everytime you add a new packages, youre adding more code to your project, meaning the project gets heavier and heavier.
# Libraries are good when what you need is time consuming and you dont have the expertise in that area

from array import array
import datetime
from collections import Counter, defaultdict, OrderedDict  # Specialized data types
import pyjokes

# If there are spaces use underscore and nothing in capital (snake case)
# Use import to import files
# __main__ is given to the single file we are running
# Python is very useful for external modules and packages
# To import one thing, use from "filename" import "" ~ More explicit

# import learning_14
# import random

# print(learning_14)

# print(random.randint(1, 20))

# #In order to give something an alias, use the keyword 'as'
# import random as some_new

# 175 Exercise ~ Guessing Game

# 1. Generate number 1-10
# from random import randint

# ran_num = randint(1, 10)

# # 2. Input from user

#  3. Check that input is betweeen 1-10
# while True:
#     try:
#         # Must be in the try block
#        # user_ans = int(input("Guess a number between 1-10 "))
#         if 0 < user_ans < 11:
#             if user_ans == ran_num:
#                 print("You won!")
#                 break
#         else:
#             print("Number has to be from 1-10")
#     except ValueError:
#         print("Enter a number")


# 4. Check if number is right guess, otherwise guess again


# PIP install

joke = pyjokes.get_joke('en', 'all')

print(joke)


li = [1, 2, 3, 4, 5, 5, 6, 7]

# Creates a counter object that keeps track how many times an item occurs in an iterable
print(Counter(li))


# Default dictionary will give us a value if something doesnt exist
# for defaultdict, first item should be callable or none
dictionary = defaultdict(
    lambda: "No such key in this dictionary", {'a': 1, 'b': 2})

print(dictionary['2'])

# Ordered Dictionary retains the order that you insert in a dictionary

d = OrderedDict()
d['a'] = 1
d['b'] = 2

print(d)

#               #NB!!  Python has made dictionaries ordered by default now, no need to use OrderedDict           #


# Datetime module - Allows us to maniipulate date values
print(datetime.time())  # time(hours,minutes,seconds)


# Lists are dynamic
# Arrays take up less memory and preform faster
# They set how much memorty they can use in a machine
# Needs typecode  ~ What type of data its going to hold
# i ~ signed int typecode

arr = array('i', [1, 2, 3])
print(arr[0])


# Debugging

# Act of removing or fixing errors/bugs in programs
# Use linting
# Use IDE/ Editor
# Read errors
# pdb ~ Python debugger
# import pdp and use set_trace()
