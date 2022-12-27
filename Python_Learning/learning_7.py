# Walrus Operator
# Assigns values to variables as part of a larger expression
# Use it in an expression when something is being evaluated

a = 'helloooooooooo'

if ((n := Len(a)) > 10):
    # Remeber the extra pair of brackets because we eant to evaluate it first

    print(f"too long {len(a)} elements")


# Assigning the variable n whatever the outcome of (len(a)) is


# Scope
# Scope- What variables do I have access to

# Global scope - anything has access to it
# local scope - If the variable is created in a function, it is not apart of the global scope and cannot be accesssed outside the function
# The onyl time you create a new scope is when you define a function

# PYTHON Interperator functioning

# 1- start with local scope
# 2 - iS there a parent for the local scope ~ goes up one level
# 3 - Goes to global
# 4 - Built in python functions


# Parameters are considered local as we can use them inside a function but not outside them

# Global
# use the global variable to access a global variable for use in a function
total = 0


def count():
    global total
    total += 1
    return total


# Instead of acessing global variables in this way which may become complicated, use Dependancy Injection
# Put the variable in tthe parameters

def count2(total):
    total += 1
    return total


print(count(total))

# nonlocal
# Used when you want to use a variable that is not local but also not global ~ For parent local
# nonlocal keyword, when newly reassigned localy, modifies the original


# Why not have all variables global?

# Computers have limited resources, creating all variables as global can use up a lot of them and cause crashes
# When creating a variable, the variavle creates a new 'bookshelf' (location in memory)
# but when modifying it changing it, it doesnt create a new 'bookshelf'
# once a function is done, the python interperator destroys it in memory ~ gragage collection -
#  so that those variables within the function dont take up memory
print("hello")
