############### Blackjack Project #####################
import random

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################


# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []


def start():
    global user_cards
    global computer_cards
    user_cards = []
    computer_cards = []
    for x in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


def calculate_score(c):
    score = sum(c)
    if score == 21 and len(c) == 2:
        return 0  # blackjack
    if 11 in c and score > 21:
        c.remove(11)
        c.append(1)
        score = sum(c)

    return score


def clear_screen():
    print("\n" * 100)


def compare(user_score, computer_score):
    # If the computer and user both have the same score, then it's a draw.
    if user_score == computer_score:
        print('draw')
        # If the computer has a blackjack (0), then the user loses.
    elif computer_score == 0:
        print('dealer blackjack')
        # If the user has a blackjack (0), then the user wins.
    elif user_score == 0:
        print("user blackjack")
    # If the user_score is over 21, then the user loses.
    elif user_score > 21:
        print('user bust')
    # If the computer_score is over 21, then the computer loses.
    elif computer_score > 21:
        print("dealer bust")
    # If none of the above, then the player with the highest score wins.
    else:
        if user_score > computer_score:
            print("user wins")
        else:
            print("dealer wins")


game_over = False
start()

while not game_over:
    print(user_cards)
    print(computer_cards)

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    if user_score == 0 or computer_score == 0:
        game_over = True
    elif user_score == 21:
        game_over = True
    else:
        player_wants_more_cards = input("do you want another card? hit/stand: ")
        if player_wants_more_cards == "hit":
            user_cards.append(deal_card())
        elif player_wants_more_cards == "stand":
            while computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)
            compare(user_score, computer_score)
            if input("do you want to play again? yes/no") == "yes":
                clear_screen()
                start()
            else:
                game_over = True
