# OOP


# Everything in Python is an object
# Objects have methods and attributes you xcan access with dot
# OOP is a paraadigm ~ A way to structure code in a way that is still organised
# In Python you can create your own data type by using the keyword class ~ First letter is capitalised and uses camel case

class BigObject:
    pass


obj1 = BigObject()

# The class = The blueprint of what we want to create - Basic attributes and properties
# Classes are then instantiated and create different instances


class PlayerCharacter:
    membership = True  # Class Object attribute

    def __init__(self, name, age):  # Constructor
        if(self.membership):  # Need to use self.
            # if(PlayerCharacter.membership): #Can aalso be used like this
            self.name = name  # For self.name to equal whatever the parameter name is
            self.age = age

    def run(self):
        print('run')

    def shout(self):
        print(f'My name is {self.name}!')
        # Cannot do PlayerCharacter.name because name is not a class object attribute

# Two underscores = Dunder method


# FIrst parameter of class should always be self

# Remeber that when a function doesnt returrn anyhing, we get None
# Class Object Attributes - Static values ~ Used when there will be no change
# Cllass object attribute is something that doesnt change across different instances ~ Can be accessed without using self.
# One needs to use self. for function parameters

# __init__ can be used to add different controls and safeguards to make sure we recieve the right data type in order to create the object

# Cat Exercise


class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat("Tom", 18)
cat2 = Cat("Timmy", 19)
cat3 = Cat("Blxkie", 20)


def oldest_cat(*args):
    return max(args)


print(
    f'the oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old')
