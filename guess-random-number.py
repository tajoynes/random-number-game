import random

# def guess_random_number(tries):
#     mynumber = random.randint(0,10)
#     guess = 0
#     print("Welcome to the guessing game")
#     print("Guess a Number between 1 - 10")
#     while tries != 0 and guess != mynumber:
#         print("Your Guess: ")
#         guess = int(input())
#         if guess == mynumber:
#             print("You're Right")
#             return
#         if guess != mynumber:
#             tries -= 1
#             print("Try again!")
#             print("You have " + str(tries) + " tries left")
#     while tries == 0:
#         print("No more guesses! You Lose")
#         print("Hahahahahahahaha")
#         break
# guess_random_number(5)

def guess_random_number_linear(tries):
    comp_number = random.randint(0,10)
    print("Welcome to the guessing game")
    print("The program number is......" + str(comp_number))
    print("---------------------------------")
    for t in range(tries):
        guess_number = random.randint(0,10)
        if guess_number == comp_number:
            print("The Computer's guess was...." + str(guess_number))
            print("You're Right")
            print("---------------------------------")
            return
        if guess_number != comp_number:
            tries -= 1
            print("The Computer's guess was...." + str(guess_number))
            print("Try again!")
            print("You have " + str(tries) + " tries left")
            print("---------------------------------")
        if tries == 0:
            print("No more tries left... You Suck")
            print("HAhaHa HaHAha")
            print("---------------------------------")
            return
guess_random_number_linear(5)
