# Regular Expressions

# Useful for validation
# Also useful for finding things
# Use import re
# Regex gives us an output as a match object
# Use regex101.com to test regex patterns
# Regex in brackets () are called capturing groups
# . means 'followed by anything'
# For refernce and study, use https://www.w3schools.com/python/python_regex.asp

# import re

# string = "Hey hello everyone"

# print(re.search('hello', string))

# pattern = re.compile('hello')  # Allows us to give a pattern to use

# a = pattern.search(string)  # Finsd the piece of the string
# b = pattern.findall(string)  # Finds alll instances of the match.
# # Exact match. In order for it to return, it has to be the exact same
# c = pattern.fullmatch(string)
# # Finds the match, doesnt matter what comes afterwords
# d = pattern.match(string)

# pattern2 = re.compile(r'[A-Za-z0-9$%#@]{7,}[0-9]')  # the r is for raw string
# password = "dodmjhjdw3"

# check = pattern2.fullmatch(password)  # Use fullsearch for this

# print(check)

# No need to to fully learn regex. You can copy paste patterns from internet and tweak them to your liking

# {8,} ~ Atleast that manh characters long


# For testing

def do_stuff(num=0):
    try:
        if num:
            return int(num)+5
        else:
            return 'please enter number'
    except ValueError as err:
        return err
