# Error Handling

# Exceptions crash programs

# Syntax error- Not standard Python syntax
# Name error - Naming is wrong
# Index error - Could be because list index is out of range
# Key error -  For keys that dont exist in a Dictionary
# Zero division error - Error because you are dividing by zero
# Error handling allows the script to continue running even if there are errors
# Error handling can be done with try and except

while True:
    try:
        age = int(input("What is your age? "))
        10/age

    except ValueError as err:  # In this block, you can give in what type of error ypu want to handle
       # If anything in the try block errors out, do/say something
        print(f"Please enter a number. Specific error is: {err}")

    except ZeroDivisionError:
       # Can have multiple except blocks
        print("Please enter an age higher than 0")

    else:  # We put this at the end. Triggers if there is no error
        print("Thank you")
        break

    finally:  # Runs at the end when everything else has ran
        print("All done!")


# Try, except, else block can be used anywhere
# Good practise is to catch errors based on the specific exception
# Also using keywords with 'as' and printing it out can print out the specific error
# If you want to use the error object, print it out using an f string
# You can also wrap errors together using brackets. You can handle multiple errors the same way
# Finally will run at the end of everything regardless of any errors a well

# Using raise "Name of error"() also works, but if you use raise, you must remove the exception

# Errors are unavoidable. A programmer must be able to anticipate bugs/errors and handle thme properly in programs
