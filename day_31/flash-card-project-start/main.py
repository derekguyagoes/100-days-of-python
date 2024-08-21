from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

window = Tk()
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="title", font=TITLE_FONT, fill="black")
canvas.create_text(400, 263, text="word", font=WORD_FONT, fill="black")
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_back = PhotoImage(file="./images/card_back.png")
pass_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=pass_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)

window.mainloop()
