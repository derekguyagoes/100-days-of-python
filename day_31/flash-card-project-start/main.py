from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

window = Tk()
window.title("Flash Card Project")
window.config(padx=50, pady=50)

canvas = Canvas(width=800, height=800, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas.create_image(526, 800, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

title_label = Label(text="title", font=TITLE_FONT)
title_label.grid(row=0, column=0)

word_label = Label(text="word", font=WORD_FONT)
word_label.grid(row=0, column=1)

pass_image = PhotoImage(file="./images/wrong.png")
pass_button = Button(image=pass_image)
pass_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image)
right_button.grid(row=1, column=1)

window.mainloop()
