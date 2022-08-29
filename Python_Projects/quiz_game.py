print("Welcome to the computer quiz!")

# Input asks user to start typing in the console
# Inside input is called the prompt. Also, whatever is typed will be stored in this variable
playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()  # Function that immediately quits the Python program

print("Great lets play!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("You are correct!")
    score += 1
else:
    print("Incorrect!")


# We can use the same variable again and again

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("You are correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("You are correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("You are correct!")
    score += 1
else:
    print("Incorrect!")

if score == 1:
    print(f"You got one question right")
    print("Thats 25% :(")

else:
    print(f"You got {score} questions right!")
    print(f"That is {score/4 * 100} %. ")
