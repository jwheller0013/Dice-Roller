# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#
from random import randrange


def roll_dice ():
    yes = True
    while yes == True:
        numberOfDice = input("How many dice would you like to roll? \n")
        # results = []
        for i in range(int(numberOfDice)):
            x= int(randrange(1,7))
            results.append(x)
        print(results)
        playAgain = input("Roll more?\n")
        if playAgain == "No":
            yes = False

results = []
roll_dice()