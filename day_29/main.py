from tkinter import *

window = Tk()
window.title("Password Manager")

canvas = Canvas(window, width=500, height=500)
lock_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=1)
website_entry = Entry()
website_entry.grid(row=1, column=2)

user_label = Label(text="Email/Username")
user_label.grid(row=2, column=1)
user_entry = Entry()
user_entry.grid(row=2, column=2)

password_label = Label(text="Password")
password_label.grid(row=3, column=1)
password_entry = Entry()
password_entry.grid(row=3, column=2)
password_generate_button = Button(text="Generate Password")
password_generate_button.grid(row=3, column=3)

add_button = Button(text="Add")
add_button.grid(row=4, column=1)

window.mainloop()
