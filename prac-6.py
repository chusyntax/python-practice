#Functions

#def- used to define a function

def say_hello():
    print('hello')

say_hello()  #Brakets are needed in order to run the code
#Functions allow us to keep our code DRY and make it reusable

#The brakets are called the parameters/aruguments
#they are able to be used inside a function as variables

#Arguments are used as the actual values we provide to a function
#Arguments~Used when we create/call/invoke a function

#Parameters are the names of the variables we use
#Parameters~Used when we define a function
#eg say_hello(Thabo, Smile)

#positional arguments need to be in the exact order in order to function and execute properly

#keyword arguments
#say_hello(emoji="Smile", name="Chu") ~> Often bad practice
#Lets you know the parameters exactly
#Make sure arguments are in order

#Default parameters
def say_goodbye(name="Chu", emoji="Angry face"):
    print(f'hi {name} youre {emoji} today')

say_goodbye()    
    
    
     #If your'e not able to get the arguments, use the defaults


#Return

#Functions need to return something or else they automatically return None

def addition(num1, num2):
    return num1 + num2 #Exit out of function and return 

print(addition(10,3))   

#Functions either return some sort od value/data type, or doesnt return anything but modifies something
#A function should do one thing really well and/or return something ~ Its good practice
#Retuen function automatically exits a function


#Methods have to be owned by something (on the left)
#They are owned by an object or data type
#They are avaiilable as soon as you use the dot (.)
#Methods are built into objects and data types


#Docstring

#adds info about a function
#For comments and definitions

# def test(a):
#     '''
#     info: This is extra info describing the function
    
#     '''

    
#help(test)



#*Args and **Kwargs
#Arguments and Keyword arguments

#def super_func(*args): #adding a star allows function to accept any number of positional arguments
    #return sum(args)

#print(super_func(1,2,3,4,5)) 

#Keyword arguments allow us to create any number of keyword arguments that then return a dictionary {num1: 5}

def superior_func(*ar, **kwargs):
     total = 0
     for items in kwargs.values():
          total += items
     return sum(ar) + total

print(superior_func(1,2,3, number1=50, number2=20))

#Rule: params, *args, default params, **kwargs


#Exercise on 229: Highest Even
#Find highest even number in a list

def highest_even(li):
    evens = [] #First create empty array that will be populated with the looped items which will be the even numbers
    for items in li:
        if items % 2 ==0:
            evens.append(items)
    return max(evens) #max retuens the highest value(Built in function)

print(highest_even([1,3,5,7,11,20,40]))    



  
