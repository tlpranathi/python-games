# Tic Tac Toe

# function to print board
def display_board(board):
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[7] + " | " + board[8] + " | " + board[9])


# function to take player input
def player_input():
    # returns tuple (player1, player2)
    choice = " "
    while choice != "x" and choice != "o":
        choice = input("player 1 - do you want to be X or O? ").lower()
    if choice == "x":
        return "x", "o"
    else:
        return "o", "x"


# function to update board after player input
# choice = x or o
# position - 1 to 9
def update_board(board, choice, position):

    board[position] = choice


# function to check winner that takes in a board and choice
def check_winner(board, choice):

    return board[1] == board[2] == board[3] == choice or board[4] == board[5] == board[6] == choice or board[7] == board[8] == board[9] == choice or board[1] == board[4] == board[7] == choice or board[2] == board[5] == board[8] == choice or board[3] == board[6] == board[9] == choice or board[1] == board[5] == board[9] == choice or board[3] == board[5] == board[7] == choice


# function to decide which player goes first
import random


def first_turn():
    turn1 = random.randint(1, 2)
    if turn1 == 1:
        return "player 1"
    else:
        return "player 2"


# function that returns boolean to check for an empty position
def check_board(board, position):

    return board[position] == " "


# function to check if board is full
def check_fullboard(board):
    for i in range(1, 10):
        if check_board(board, i):
            return False
    return True


# function that asks for players next position and also checks if the position is empty
def player_choice(board):
    position = 0
    while position not in range(1, 10) or not check_board(board, position):
        position = int(input("choose a position(1-9): "))
    return position


# function to play again
def play_again():
    replay = input("do you want to play again?(y/n): ").lower()
    return replay == "y"


# main
print("Tic Tac Toe")
while True:
    # testboard to display positions
    testboard = [0, "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    display_board(testboard)

    # empty game board
    board1 = [" "]*10

    # tuple unpacking
    player1, player2 = player_input()

    # returns string "player 1" or "player 2"
    turn = first_turn()
    print(turn + " will go first")

    game = True
    while game:
        # player 1
        if turn == "player 1":
            # show board
            display_board(board1)

            # choose a position
            position = player_choice(board1)

            # place choice in the position
            update_board(board1, player1, position)

            # to clear screen
            print("\n"*100)

            # check if player has won
            if check_winner(board1, player1):
                display_board(board1)
                print("Player 1 has won!!!")
                game = False

            # check if game is a tie
            else:
                if check_fullboard(board1):
                    display_board(board1)
                    print("the game is a tie!!")
                    game = False

                # no tie/ no win >>> next players turn
                else:
                    turn = "player 2"

        # player 2
        else:
            # show board
            display_board(board1)

            # choose a position
            position = player_choice(board1)

            # place choice in the position
            update_board(board1, player2, position)

            # to clear screen
            print("\n"*100)

            # check if player has won
            if check_winner(board1, player2):
                display_board(board1)
                print("Player 2 has won!!!")
                game = False

            # check if game is a tie
            else:
                if check_fullboard(board1):
                    display_board(board1)
                    print("the game is a tie!!")
                    game = False

                # no tie/ no win >>> next players turn
                else:
                    turn = "player 1"

    # want to play again?????
    if not play_again():
        break




































