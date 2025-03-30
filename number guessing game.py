def game():
    print("$$$$#### NUMBER GUESSING GAME ####$$$$")
    int1 = int(input("enter lower bound - "))
    int2 = int(input("enter upper bound (make sure the difference is more than 500 to really challenge yourself!!!) - "))
    print("\nyou have only 7 chances to guess the number")

    import random
    mynum = random.randrange(int1, int2)



    for i in range(1, 8):
        guess = int(input("guess a number - "))
        if guess != mynum:
            if guess > mynum and guess < mynum+4:
                print("your guess is a little higher than the number!!! (its only 3 numbers more/less than what I'm thinking!!)")
            elif guess < mynum and guess > mynum-4:
                print("your guess is a little lower than the number!!! (its only 3 numbers more/less than what I'm thinking!!)")
            elif guess > mynum:
                print("you guessed too high!!!")
            elif guess < mynum:
                print("you guessed too low!!!")

        if guess == mynum:
            print("\nCONGRATULATIONS")
            if i == 1:
                print("you guessed the number in", i, "chance")
            else:
                print("you guessed the number in", i, "chances")
            break

    if guess != mynum:
        print("\nYOU LOSE")
        print("the number was", mynum)


game()