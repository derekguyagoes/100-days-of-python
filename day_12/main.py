### number guessing game ###
import random

from day_12.art import logo

print(logo)
print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

remaining_guesses = 0

if difficulty == "easy":
    remaining_guesses = 10
else:
    remaining_guesses = 5

da_number = random.randint(1, 100)

still_guessing = True
while still_guessing:

    print(f"You have {remaining_guesses} attempts remaning to guess the number")
    guess = ""
    guess = int(input("Make a guess: "))

    if remaining_guesses > 1:
        if guess > da_number:
            print("Too high")
        elif guess < da_number:
            print("Too low")
        elif guess == da_number:
            print("you did it!")
            still_guessing = False
        remaining_guesses = remaining_guesses - 1
    else:
        still_guessing = False
        print(f"The number was {da_number}")
