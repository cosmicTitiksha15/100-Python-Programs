# A basic console game against the computer using the random module.

import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    get_choices = {'computer_choice' : computer_choice, 'user_choice' : user_choice}
    return get_choices

def check_win(user, computer):
    if user == computer:
        output = "It's a tie!"
        score = 0
    elif user == 'rock':
        if computer == 'scissors':
            output = "You win! Rock beats scissors."
            score = 1
        else:
            output = "You lose! Paper beats rock."
            score = 0
    elif user == 'paper':
        if computer == 'rock':
            output = "You win! Paper beats rock."
            score = 1
        else:
            output = "You lose! Scissors beats paper."
            score = 0
    elif user == 'scissors':
        if computer == 'paper':
            output = "You win! Scissors beats paper."
            score = 1
        else:
            output = "You lose! Rock beats scissors."
            score = 0
    print(output)
    return score

# Ask the user how many rounds they want to play, with error handling for invalid input
try:
    trials = int(input("How many rounds do you want to play? "))
except ValueError:
    print("Please enter a valid number. Defaulting to 3 rounds.")
    trials = 3
score = 0
count = 0
for match in range(trials):
    count += 1
    choice = get_user_choice()
    try:
        score += check_win(choice['user_choice'], choice['computer_choice'])
    except UnboundLocalError:
        print("Please enter either 'rock', 'paper', or 'scissors'.")
        print("You will be scored 0 for this round.")
        continue

# Comment based on the final score
if score == 0:
    comment = 'Oh- Auch! You lost all rounds.'
elif score < count / 2:
    comment = "Better luck next time!"
elif score == count:
    comment = "Aha! Perfect score."
else:
    comment = "Not bad! You did well."

# Final score output
print(f"You scored {score} out of {count}. {comment}")