# ROCK PAPER SCISSORS
import random

# function to get valid integer
def get_valid_integer(question):
    while True:
        try:
            number =  int(input(question))
            if number > 0:
                return number
            else:
                print("please enter a positive number")
        except ValueError:
            print("enter a valid number")

# function to get valid choice without wasting rounds
def get_valid_choice(question):
    while True:
        user_choice = input(question).lower()
        if user_choice in ["r", "p", "s"]:
            return user_choice
        else:
            print("Invalid choice, choose r, p, or s.")

# function to display scores
def display_scores(user_score, computer_score):
    print("your score: {0} | computer's score: {1}".format(user_score, computer_score))

# function to play again
def play_again():
    while True:
        replay = input("do you want to play again? (y/n): ").lower()
        if replay in ["y", "n"]:
            return replay == "y"
        else:
            print("Invalid input, choose y or n.")

# game definition
def game():
    # dictionary for game logic instead of multiple if-elif conditions
    game_choices = {"r": "rock", "p": "paper", "s": "scissors"}
    winning_combinations = {"r": "s", "p": "r", "s": "p"}

    rounds = get_valid_integer("\nhow many rounds do you want to play?: ")

    user_score = 0
    computer_score = 0

    for _ in range(rounds):
        user_choice = get_valid_choice("\nrock, paper, or scissors (r/p/s): ")

        computer_choice = random.choice(list(game_choices.keys()))
        print("computer chose >>>>>>>>>> {} ".format(game_choices[computer_choice]))

        if computer_choice == user_choice:
            print("\nTie!!")
        elif winning_combinations[user_choice] == computer_choice:
            print("\nYou win this round!!")
            user_score += 1
        else:
            print("\nComputer wins this round")
            computer_score += 1

        display_scores(user_score, computer_score)

    if computer_score > user_score:
        print("\n<<<<< COMPUTER WINS >>>>>")
    elif computer_score < user_score:
        print("\n<<<<< YOU WIN >>>>>")
    else:
        print("\nTIE GAME!!!")


# Main

print("\nROCK PAPER SCISSORS: YOU vs COMPUTER")
print("RULES:\n~ Rock beats Scissors\n~ Paper beats Rock\n~ Scissors beat Paper")

while True:
    game()
    if not play_again():
        break





