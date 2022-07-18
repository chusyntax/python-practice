#Conditional logic

#else only runs if the if block evaluates to false
#elif (else if) runs if the if statement returns false
#else is a catch all ~ If previous conditions are not met, it will run
#one if and one else but multiple elif
#and keywords says that both conditions must be met/true

is_old = True
is_licensed = False

if is_old and is_licensed:
    print('You can drive')

else:
    print('You may not drive')

#and empy string '' and a zero 0 are falsey values while others are truthy

#Ternary Operator ~ Conditional Expression

# condition_if_true if condition else condition_if_false

is_friend = True
can_message = "You can message me" if is_friend else "You cannot message me"

print(can_message)

#Short Circuiting
#makes programs more fast and efficient
#with and and or keywords


# Logical Operators
#<, >, ==, <=, >=, and, or, not(gives us the opposite), !

#208 ~ Exercise
is_magician = True
is_expert = False

if is_magician and is_expert:
    print("you are a master magician")
elif is_magician and not(is_expert):
    print("Atleast you're getting there")
elif not(is_magician):
    print("You need magic powers")
    

#Double equal checks for equality of value
#The 'is' keyword checks if the two values have the same location in memory (has to be exact same thing)
#Doesnt work with lists as list are data structures and are always created in new locations
# is will print out false for any data structure





