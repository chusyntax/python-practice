# Decorators

# Decorators supercharge our function
# They hace the @ sign and wording after
# Fuctions are first class citizens ~ They can be passed around like variables

# Higher Order Function
# It can either be a function that accepts another function in its parameters
# OR
# A functioin that returns another function

# Decorators can add extra functionality (superboost) to other functions


# This is the Decorator Pattern
from time import time  # Using a module


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("***")  # Not part if the pattern
        func(*args, **kwargs)
        print("***")  # Not part if the pattern
    return wrap_func
# Decorators should use this format
# *args and **kwargs makes the decorator flexible


@my_decorator
def hello():
    print("hello")


hello()

# If a function that will be using the decorators has arguments, use *args and **kwargs and that will sort it out


def preformance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()  # Time returns a value in seconds
        print(f'Function took {t2-t1} s')
        return result
    return wrapper
# This is a way to compare functions and can help you make functions faster and more optimized


@preformance
def long_time():
    for i in range(100):
        i*5


long_time()

# Exerice: @Authenticated ~ 156

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': False
}


def authenticated(fn):
    def wrapped(*args, **kwargs):
        if 'valid':
            fn(*args, **kwargs)
    return wrapped
# Sort of worked

# Right answer:
# if args[0]['valid']: #0 is refering to the first argument which would be the key
#        return fn(*args, **kwargs)


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
