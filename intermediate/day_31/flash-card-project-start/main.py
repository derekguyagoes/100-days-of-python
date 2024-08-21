import os.path
import random
from time import sleep

import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

if os.path.exists("data/words_to_learn.csv"):
    data = pandas.read_csv("data/words_to_learn.csv")
else:
    data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")
current_card = {}


def update_file():
    try:
        with open("data/words_to_learn.csv", "w") as file:
            pandas.DataFrame(to_learn).to_csv(file, index=False)
    except FileNotFoundError:
        with open("data/words_to_learn.csv", "w") as file:
            pandas.DataFrame(to_learn).to_csv(file, index=False)


def new_card(known=False):
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, new_card)

    if known:
        to_learn.remove(current_card)
        update_file()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


window = Tk()
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="title", font=TITLE_FONT, fill="black")
card_word = canvas.create_text(400, 263, text="word", font=WORD_FONT, fill="black")
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

pass_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=pass_image, highlightthickness=0, command=new_card)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
# command=lambda: func("See this worked!")
right_button = Button(
    image=right_image, highlightthickness=0, command=lambda: new_card(known=True)
)
right_button.grid(row=1, column=1)

new_card()
window.mainloop()
