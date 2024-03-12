from art import logo

print(logo)


def clear_screen():
    print("\n" * 100)


def find_highest_bidder():
    highest_bid = 0
    winner = ""
    for key in bids:
        if int(bids[key]) > highest_bid:
            highest_bid = int(bids[key])
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bidding_finished = False

bids = {}

while not bidding_finished:
    name = input("what is your name?\n")
    bid = input("What is your bid?\n$")
    bids[name] = bid

    another_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if another_bid == "no":
        bidding_finished = True
    else:
        clear_screen()

find_highest_bidder()
