# Day 1 - Question 1
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line
seq = []
for number in range(2000, 3200):

    if (number % 7 == 0) and (number % 5 != 0):
        seq.append(number)
# print(seq)

# Got right third try. Had to change function into a simple for loop and put list outside of for loop


# Day 1 - Question 2
# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

fact_num = int(input())

fact = 1

for number in range(1, fact_num + 1):
    fact = fact * number

# print(fact)
# Needed the help of the solution. Have to declare variable outside of loop and use a range with the input number +1(Because range does not include the end number, thefore add 1 in order to include it)

# Day 1 - Question 3
# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

n = int(input())
output = {}


for i in range(1, n+1):
    output[i] = i * i

print(output)

# Didnt have too much of an idea what was going on except that I needed a loop and the range. Very simple but couldnt figure the logic out
