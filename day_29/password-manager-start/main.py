from tkinter import *


def add():
    # writes to file
    # website | username | password
    pass


def generate():
    # generates password
    # prints to screen
    # copies to clipboard
    pass


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

user_label = Label(text="Email/Username")
user_label.grid(row=2, column=0)
user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
password_generate_button = Button(text="Generate Password", command=generate)
password_generate_button.grid(row=3, column=2)

add_button = Button(text="Add", command=add, width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
