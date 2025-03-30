# COMPUTER READS YOUR MIND
print("I'm going to READ YOUR MIND.")

def get_valid_input(question, valid_answer):
    # function to get valid input
    while True:
        user_input = input(question).lower()
        if user_input in valid_answer:
            return user_input
        else:
            print(f"Invalid input. Please enter any of the following: {", ".join(valid_answer)}")


def get_valid_integer(question):
    # function to get valid number
    while True:
        try:
            return int(input(question))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def computer_guess(lower_bound, upper_bound):
    # game definition
    print(f"\nThink of a number between {lower_bound} and {upper_bound}.")

    import time
    time.sleep(2)

    while lower_bound <= upper_bound:
        #  while loop to repeat until correct number is guessed
        # first guess is midpoint of the given range
        guess = (lower_bound + upper_bound) // 2
        print(f"My guess is: {guess}")

        # user response must be among h, l and c
        response = get_valid_input("Is the guess too low(L), is it too high(H) or is it correct(C): ", ["l", "h", "c"])

        # next guess should be adjusted acc to user's input

        # if the guess was lower, lower_bound is updated to guess + 1
        if response == "l":
            if guess == upper_bound:
                print("\nYou can't fool me")
            else:
                lower_bound = guess + 1

            # next guess is midpoint of (guess + 1, upper_bound)

        # if the guess was higher, upper_bound is updated to guess - 1
        elif response == "h":
            if guess == lower_bound:
                print("\nYou can't fool me")
            else:
                upper_bound = guess - 1
            # next guess is midpoint of (lower_bound, guess - 1)

        elif response == "c":
            print("YAY! I GOT IT")
            break




# upper and lower bound must be integers
lower_bound = get_valid_integer("\nEnter the lower bound: ")
upper_bound = get_valid_integer("Enter the upper bound: ")

while lower_bound >= upper_bound:
    # upper bound must be greater than lower bound
    print("\nUpper bound must be greater than the lower bound")
    upper_bound = get_valid_integer("Enter the upper bound: ")

computer_guess(lower_bound, upper_bound)

while True:
    play_again = input("do you want to play again?\nyes/no - ").lower()
    if play_again == "yes":
        computer_guess(lower_bound, upper_bound)
    else:
        break






















