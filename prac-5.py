#For Loops

#uses the keyword "for"
#Iterable~ Something that is able to get looped over
#For Loops allow us to iterate over anything that has a collection of items
#You can nest loops in loops

for item in (1,2,3,4,5):
    print(item)

#Iterables
# 
#Iterable -> List, dict, set, tuple, string and range  
#Iterate -> One by one check each item in a collection

user = {
    'name': 'Chu',
    'age': 90,
    'can_swim': True
}

for key,value in user.items():
    print(key,value) #method to get all keys and values not as tuples

for item in user.keys(): #method to get all keys
    print(item)

for item in user.values():#method to get all values
    print(item)    

#212~ Exercise
#counter

my_list = [1,2,3,4,5,6,7,8,9,10]

total = 0 #The counter needed to be out here because if it was in the loop, it would be set to 0 every time

for item in my_list:
    
    total = total + item
    #If you put the print here, it will get looped over as well in the code block
print(total)    

# Range 
# Returns an object that produces a sequence of integers from start to stop by step.
for number in range(0,10,2):
    print(number)
for _ in range(10,0,-1):
    print(_)
#If you want to do something in reverse, add a -1

for ql in range(2):
    print(list(range(10)))#Quick way to create a list with integers

#Enumertate
#takes in an iterable object and returns an index counter

for i,char in enumerate(list(range(100))):
    if char == 50:
        print(f'Char 50 is {i}')

#While Loop
#while condition:
    #do something


i=0
while i <50: #Will create an infinite loop
    print("Nothing")
    break#Stops code from running again

while i<50:
    print(i)
    i+=1

#We can break out of a while loop if a condition can be turned into false    
   
