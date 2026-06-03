# Generate a random number between 1 and 6 on command. 
import random

# random.randint(a, b) returns a random integer N such that a <= N <= b.

def roll_dice():
    return random.randint(1, 6)

while True:
    query = input("Roll the dice? (y/n): ").strip().lower()
    if query == 'y':
        result = roll_dice()
        print(f"You rolled a {result}.")
    elif query == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Please enter 'y' or 'n'.")