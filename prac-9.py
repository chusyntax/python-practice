# classmethods ~ Used to create methods in classes

class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        if(self.membership):
            self.name = name
            self.age = age

    def run(self):
        print('run')

    def shout(self):
        print(f'My name is {self.name}!')

    @classmethod
    def adding_numbers(cls, num1, num2):  # The first parameter has to be cls
        return cls("teddy", num1+num2)

# We van use classmethods without instanciation
# Classmethods can also be used to instantiate objects

# @staticmethod does the same thing, but you dont have access to cls

# Classical OOP - use classes to create an OOP Paradigm


# The four Pillars of OOP

# 1) Encapsulation
# The binding of functions and data that manipulate that data. You encapsulate into one big object to keep everything together so that pthers can interat with
# The data and functions are called the attributes
# Functions can act upon the data
# Used to package things up and create a blueprint

# 2) Abstraction
# Hiding/abstracting away information and giving access to only what is neccessary. Everything else is hidden
# In Python, we connot create private variables, so we use _ in the beginning by convention
# This is to indicate the attribute or method is private

# 3) Inheritance
# Allows objects to take on the properties of exsisting objects ~ You can inherit classes
# For inheritance, put the parent class in the parameters of the object that wants to inherit the attribute
# Helps in keeiping code DRY
# Classes that inherit are called children classes or sub classes or derived classes
# ininstance~ To check if something is an instance
# isinstance(instance,Class)

# Everything in python falls under the object instance  ~ Thats where all the methods come from
# Every class has (object) in its parameters by default
