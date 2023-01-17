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

#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:

#34,67,55,33,12,98
#Then, the output should be:

#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')


li = input().split(',')
t = tuple(li)
print(li)
print(t)
