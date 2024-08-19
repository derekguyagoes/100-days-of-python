import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# Password Generator Project


def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def add():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("Error", f"Please fill all fields missing:")
    else:
        # reading old data
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                # updating old with new
                data.update(new_data)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search():
    website_to_find = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            try:
                found = data[website_to_find]
                messagebox.showinfo(
                    title=website_to_find,
                    message=f"Email: {found['email']}\n Password: {found['password']}",
                )
            except KeyError:
                messagebox.showinfo(message=f"{website_to_find} not found")
    except FileNotFoundError:
        messagebox.showinfo(message="data file not found")


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)
website_search_button = Button(text="Search", width=13, command=search)
website_search_button.grid(row=1, column=2)

user_label = Label(text="Email/Username")
user_label.grid(row=2, column=0)
user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "go@example.com")

password_label = Label(text="Password")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
password_generate_button = Button(text="Generate Password", command=generate_password)
password_generate_button.grid(row=3, column=2)

add_button = Button(text="Add", command=add, width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
