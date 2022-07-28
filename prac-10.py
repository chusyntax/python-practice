# Super

# If you want to call the __init__ method of a parent class in a child class, use (name of parent ).__init__(self, method you want to call)
# you can also use super() ~ Refers to the super class/class above
# With super(), you dont need to pass in self
# super.__init__(email)

# Introspection
# The ability to determine the type of an object at runtime
# Runtime- when the code is running
# dir() ~ Gives all methods and attributes an instance or class has

# Dunder Methods
# Inherited from base object class
# Dunder methods can be modified

# __call__ ~ Allows us to call functions with ()

# Classes can get as many parent classes as they need
# All you need to do is pass the class the object should inherit in the parameters
# you need to initialize/inherit  the parent clases functions with their parameters in the subclass (use .__init__)

# Method Resolution Order

class A():
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)  # prints out 1

# mro() ~ Methods that shows order of class
# Checks classes in ascending order
# MRO uses the algorithm Depth FIrst Search
