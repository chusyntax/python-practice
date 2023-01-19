# Question 4
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:

inp = int(input())


def tup_list(inp):
    inp.list()
    tuple(inp)
    return inp


tup_list()

# Didnt really figure this one out. Correct solution is doewn below
# lst = input().split(',')  # the input is being taken as string and as it is string it has a built in
# method name split. ',' inside split function does split where it finds any ','
# and save the input as list in lst variable

# tpl = tuple(lst)          # tuple method converts list to tuple

# print(lst)
# print(tpl)

# Question 5

#Define a class which has at least two methods:

#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

class IOstring():
    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())

xx = IOstring()
xx.get_string()
xx.print_string()