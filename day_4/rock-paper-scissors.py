import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
options = [rock, paper, scissors]
player = int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors\n"))

if player >= 3 or player < 0:
    print("invalid number")
else:
    print(f"{options[player]}")
    computer = random.randint(0, 2)
    print(f"computer chose:\n{options[computer]}")

    if player == 0 and computer == 2:
        print("you win!")
    elif computer == 0 and player == 2:
        print("you lose")
    elif computer > player:
        print("you lose")
    elif player > computer:
        print("you win")
    elif player == computer:
        print("it's a tie")