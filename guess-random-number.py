import random

def guess_random_number(tries):
    mynumber = random.randint(0,10)
    guess = 0
    print("Welcome to the guessing game")
    print("Guess a Number between 1 - 10")
    while tries != 0 and guess != mynumber:
        print("Your Guess: ")
        guess = int(input())
        if guess == mynumber:
            print("You're Right")
            return
        if guess != mynumber:
            tries -= 1
            print("Try again!")
            print("You have " + str(tries) + " tries left")
    while tries == 0:
        print("No more guesses! You Lose")
        print("Hahahahahahahaha")
        break
guess_random_number(5)