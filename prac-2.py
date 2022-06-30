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