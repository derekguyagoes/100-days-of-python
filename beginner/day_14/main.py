import random

from beginner.day_14.art import *
from game_data import data as data
from helpers import clear_screen

print(logo)


def get_a_thing(first):
    candidate = random.choice(data)

    while first == candidate:
        candidate = random.choice(data)
    return candidate


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"


keep_playing = True
score = 0
champion = random.choice(data)

while keep_playing:

    challenger = get_a_thing(champion)

    print(f"Compare A: {champion["name"]} a {champion["description"]} from {champion["country"]}")
    print(vs)
    print(f"Against B: {challenger["name"]} a {challenger["description"]} from {challenger["country"]}")
    guess = input("Who has more followers? Choose 'A' or 'B': ").upper()

    is_correct = check_answer(guess, champion["follower_count"], challenger["follower_count"])

    if is_correct:
        score += 1
        print(f"correct a > b current score: {score}")
        clear_screen()
    else:
        keep_playing = False
        print(f"wrong b < a final score: {score}")
