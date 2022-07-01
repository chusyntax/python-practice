# username = input("What is your name?")
# password = input("What is your password?")
# password_length = len(password)
# hidden_password = len(password) * '*'


# print(f"Hey {username}, your password {hidden_password} is {password_length} characters long")

#Lists(data structure - container around data that had pros and cons) ~ ordered sequence of objects that can be of any type (almost same as array)

li1 = [1,2,3,4,5]
li2 = [1,2.5,'list', True, False]

print(len(li2))
print(len(li2[2]))
#lists are mutable
#list slicing creates a new list

amazon_cart = [
    'pen',
    'paper',
    'highlater',
    'sharpener'
]
amazon_cart[0] = 'book'
new_cart = amazon_cart[:] #copys list
new_cart[0] = "earphones"
print(new_cart)
print(amazon_cart)

#Matrix~ Way to describe 2D list ~ [[]]
matrix =[
    [1,0,1],
    [1,0,1],
    [1,0,1]
    
    ]
#Lists
#Some List methods dont return values, they change the list you give it
basket=[1,2,3,4,5]  
basket.append(100) #list method (NB! List mothods dont create new copies of the list. Must do method first before trying to 
#create new list)~ add
basket.insert(4,200) #adds item at specified index
basket.extend([300,400])#adds an interable (a list to the end of the exsisting list)

basket.pop()#removes what at end of list
basket.pop(1)#removes item in the given index
basket.remove(5)#give value you want to remove
#basket.clear()#removes everything in a list


print(basket.index(200))#(value,start,stop)
print(200 in basket) # in checks if value is there, returns a boolean value(Used on strings as well)
print(basket.count(1)) #how many times a value occurs
basket.sort() #sorts the list
sorted(basket) #creates new copy and sorts it
basket.copy() #copies list and returns the list
basket.reverse()#reverses list
#combining sort then reverse reverses the list in order
new_basket= basket
print(new_basket)  

print(list(range(1,100))) #range generates a list. range(start,stop)


new_sentance = " ".join(["I", "am", "a", "programmer"]) #joins all the iterables with what was declared before
#(Combines lists into a string)
print(new_sentance)

#list unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(other)