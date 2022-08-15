# Generators

# ALlow is to generate a sequence of values over time
# They can pause and resume functions
# Generators are also iterable
# Generators are created by fuctions
# Instead of returning, generators use yield
# Yield pauses the function and comes back to it when next is called
# Yield keyword makes it a generator. Only keeps the most recent data iin memory
# Next can be called as many times as we want and until the range expires
# Generators are also fast and preformant
# This is because generators allow us to only hold the most recent data in memory and not use up to many recources

def generator_function(num):
    for i in range(num):
        yield i


for item in generator_function(10):
    print(item)

# iter() function can allow us to use the next function on an iterable

# 166 - Exercise: Fibonacci Numbers


def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


for num in fib(20):
    print(num)
