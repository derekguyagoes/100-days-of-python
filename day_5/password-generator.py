# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = 4  # int(input("How many letters would you like in your password?\n"))
nr_symbols = 2  # int(input(f"How many symbols would you like?\n"))
nr_numbers = 2  # int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_password = ""
for x in range(1, nr_letters + 1):
    easy_password += random.choice(letters)

for x in range(1, nr_symbols + 1):
    easy_password += random.choice(symbols)

for x in range(1, nr_numbers + 1):
    easy_password += random.choice(numbers)

print(easy_password)
hard_password_list = list(easy_password)

hp = random.choices(hard_password_list, k=len(hard_password_list))
print(''.join(hp))

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
