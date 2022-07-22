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
