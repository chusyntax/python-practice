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
    
    
     #If youre not able to get the arguments, use the defaults