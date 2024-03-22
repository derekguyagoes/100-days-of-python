import random

from day_14.art import *
from game_data import data as data

print(logo)


def get_a_thing(first):
    candidate = random.choice(data)

    while first == candidate:
        candidate = random.choice(data)
    return candidate


keep_playing = True
score = 0
champion = random.choice(data)

while keep_playing:

    challenger = get_a_thing(champion)

    print(f"Compare A: {champion["name"]} a {champion["description"]} from {champion["country"]}")
    print(vs)
    print(f"Against B: {challenger["name"]} a {challenger["description"]} from {challenger["country"]}")
    guess = input("Who has more followers? Choose 'A' or 'B': ").upper()

    if guess == 'A':
        if champion["follower_count"] > challenger["follower_count"]:
            score += 1
            print(f"correct a > b current score: {score}")
        else:
            keep_playing = False
            print(f"wrong b < a final score: {score}")

    elif guess == 'B':
        if challenger["follower_count"] > champion["follower_count"]:
            print(f"correct b>a current score: {score}")
            score += 1
            champion = challenger
        else:
            keep_playing = False
            print(f"wrong b < a final score: {score}")
    else:
        print("bad input, exiting")
        keep_playing = False
