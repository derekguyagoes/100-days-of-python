import random

from day_14.art import *
from game_data import data as data

print(logo)


def get_a_thing(first):
    candidate = random.choice(data)

    while first == candidate:
        candidate = random.choice(data)
    return candidate


champion = random.choice(data)
challenger = get_a_thing(champion)

print(f"Compare A: {champion["name"]} a {champion["description"]} from {champion["country"]}")
print(vs)
print(f"Against B: {challenger["name"]} a {challenger["description"]} from {challenger["country"]}")
guess = input("Who has more followers? Choose 'A' or 'B': ")

if guess == 'A':
    if champion["follower_count"] > challenger["follower_count"]:
        print("correct a > b")
    else:
        print("wrong b < a")
else:
    if challenger["follower_count"] > champion["follower_count"]:
        print("correct b>a")
    else:
        print("wrong b < a")
