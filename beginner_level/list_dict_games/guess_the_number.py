# The computer picks a random number, and the user has to guess it with "higher/lower" hints.
import random

# function to check the user's guess against the computer's number and provide hints
def guess_the_number(guess):
    output = False
    if guess == number:
        output = True
    elif guess < number:
        if number - guess >= 10:
            print("Add 10 or more.")
        else:
            print("Add a single digit number")
    else:
        if guess - number >= 10:
            print("Subtract 10 or more.")
        else:            
            print("Subtract a single digit number.")
    return output

# Start of the program
print("The number lies between 1 and 100.")
number = random.randint(1, 100)
print(number)
trials = 0

while True:
    trials += 1
    try:
        guess = int(input("Enter your guess: "))
        output = guess_the_number(guess)
    except ValueError:
        print("Please enter an integer.")
        continue
    if output == True:
        break

print(f"You took {trials} trials to guess the number.")