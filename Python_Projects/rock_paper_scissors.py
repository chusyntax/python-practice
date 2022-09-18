import random

user_score = 0
comp_score = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit:  ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)

    comp_choice = options[random_number]
    # rock = 0, paper = 1, scissors = 2
    print("Computer picked", comp_choice)

    if user_input == 'rock' and comp_choice == 'scissors':
        print("You won!")
        user_score += 1

    elif user_input == 'paper' and comp_choice == 'scissors':
        print("You won!")
        user_score += 1

    elif user_input == 'rock' and comp_choice == 'scissors':
        print("You won!")
        user_score += 1

    else:
        print("The computer won!")
        comp_score += 1


print(
    f"Thank you for playing! You won {user_score} times while the computer won {comp_score} times")
print("Goodbye")
