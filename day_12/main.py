### number guessing game ###
import random

from day_12.art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print(logo)
print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


def set_difficulty():
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def get_random_number():
    return random.randint(1, 100)


def game():
    answer = get_random_number()
    remaining_guesses = set_difficulty()

    still_guessing = True
    while still_guessing:

        print(f"You have {remaining_guesses} attempts remaning to guess the number")
        guess = int(input("Make a guess: "))

        if remaining_guesses > 1:
            if guess > answer:
                print("Too high")
            elif guess < answer:
                print("Too low")
            elif guess == answer:
                print("you did it!")
                still_guessing = False
            remaining_guesses = remaining_guesses - 1
        else:
            still_guessing = False
            print(f"The number was {answer}")


game()
