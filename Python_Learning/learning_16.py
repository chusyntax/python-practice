# File I/O ~ Input/Output

# open - used to read and write files

# my_file = open('test.txt')

# print(my_file.read())  # You can only read a file once
# # Done so that the cursor moves back to the start and you can read a file again
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)

# my_file.readline()  # Reads one line. Use multiple and it will show the next lines
# my_file.readlines()  # Shows all the lines in a list format

# my_file.close() # Should do this so that the file closes and you can use it in some other part of the program


# mode="r" ~ Read mode
# mode = "w" ~Write mode ~ Treats the file as if it is empty ~ Alo creates a new file if it doesnt exist
# mode="r+" ~ Read and write ~ Overwrites as cursor goes to the beginning
# mode="a" Append to the end

# with open('test.txt', mode="a") as my_file:  # Like this, you dont need to close the file
#     # In order to not break what we had prevoisly, use mode="a" ~ Append mode
#     text = my_file.write("New text in the file from Python :) lol")

# print(text)

#     NB!!! Make sure that you are in the right folder when trying to use open.
#     Also, when it comes to working with files and folders in Python, Make sure that they are named in snake_case with no spaces!!!

# cd .. ~ Goes up one directory
# When you copy the entire file path, that is the absolute file path.
# You can also use relative file path as it is much more simple
# ./ ~ From the current folder
# ../  Goes up one folder

# File I/O can also be used in try and except blocks

try:
    with open('test.txt', mode="a") as my_file:

        text = my_file.write("New text in the file from Python :) lol")

except FileNotFoundError as err:
    print("file does not exist")
    raise err

except IOError as err:
    print("IO Error")
    raise err
