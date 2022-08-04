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
