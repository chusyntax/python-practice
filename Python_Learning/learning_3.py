#Dictionary ~ Unordered key:value pairs. Basically an object. Can also have lists, booleans and numbers
#Dictionaries hold more information

dictionary ={
    'a':1,
    'b':2,
    'c':3
}
#Dictionary keys have to be immutable(Cannot change) ~ No list or dictionary as keys
#keys must be unique (or previous value will be overridden)

dictionary2 ={
    11:1,
    'a':2,
    True:3
}

###NB! I've discovered a little gotcha by myself###
#If earlier in your dictionary you declare 1 as a key then later declare True as a variable, the True overrides the 1 

print(dictionary2.get(1)) #.get is a method that can help you get a value and if it doesnt exsist, returns None and doesnt stop program
print(dictionary2.get('age', 25)) #second parameter sets the default is the key value pair does not exsist
#print('i' in 'hi')
#print(11 in dictionary2.keys()) #checks if key is there
#print(3 in dictionary2.values()) #checks if value is there
#dictionary2.clear()#Empties dictionary
print(dictionary2)
dictionary2.pop('a') #removes the key:value pair but returns item
print(dictionary.popitem())#pops a random item
dictionary.update({'age': 69}) #updates exsisting key:value pair or creates new one if it doesnt exsist
print(dictionary)

#Tuples ~ used when you dont want to change values and makes code more predictable
#less flexible than list
#faster than lists
#basically immutable list
#tuples can be used as keys in lists
my_tuple = (1,1,2,3,4,5)
print(my_tuple.count(1))#returns how many times thet value occurs
print(my_tuple.index(2))#returns the index of the item in brackets

#Sets
#unorderede collections of unique objects
my_set = {1,2,3,4,5}
my_set2 = {1,2,3,4,5,5}# cannot be any duplicates in a set
my_set.add(100)#adds to the list

#make list into a set
list_to_set = [1,2,2,3,4,5,5]
print(set(list_to_set))#removes duplicate values


print(1 in my_set)#check in value exsists in set
print(list(my_set))#turns set into list

new_set= my_set.copy()#makes duplicate of set

my_set.clear()#clears set

my_set.difference(my_set2)#finds difference between sets
my_set.discard(5)#removes item from set
my_set.difference_update(my_set2)#removes all elements of a another set from this set
my_set.intersection(my_set2)#prints out what is the same in both sets. Shorthand ~ print(my_set & my_set2)
my_set.isdisjoint(my_set2)#checks if they have anything in common. Prints out a boolean value. 
my_set.union(my_set2)# returns a new set with the sets joined together with no duplicates. Shorthand ~ (my_set | my_set2)
my_set.issubset(my_set2)# Checks if all of the set is in the set within the brakets. Reutrns boolean
my_set2.issuperset(my_set) # Opposite of issubset. Returns boolean 