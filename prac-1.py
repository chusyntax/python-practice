print (type('hello world'))

first_name = "Chu" #assigns to a variable
last_name = "Theko"
full_name = first_name + " " + last_name

print(full_name)

print(type(str(int(10)))) #Type Conversion

weather = "It\'s \"kind of\" sunny today " #Escape Sequence "Whatever comes after the backslash is a string"
#\t adds tab
#\n new line
print(weather)

print(f"my name is {first_name} and my surname is {last_name}") #formatted strings ~ f string

si = "01234567"
print(si[0:5:2]) #String Indexes ~ [Start:Stop:Stepover]
print(si[::-1]) #reverses the order
#Strings are immutable(cannot be chnaged). The only way it can be  changed is by completely reassigning
#String methods ~ .replace('','') .capitalize(), .format, .upper()

#Boolean- True and False
#0=false, 1=true
print(bool(9))

birth_year = input("what year were you born?")

age = 2022 - int(birth_year) #type conversion is needed in order to do mathematical opertions

print(f" You are {age} years old")

