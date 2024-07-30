import turtle

import pandas as pd

screen = turtle.Screen()
screen.title("u.s. states game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
turtle.penup()

data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
correct_states = []

while True:
    turtle.goto(0, 0)
    answer_state = screen.textinput(
        title=f"{len(correct_states)}/50 States Correct",
        prompt="Which state do you want to play?",
    ).title()

    if answer_state in all_states:
        if answer_state in correct_states:
            print("you've already guessed that")
        else:
            correct_states.append(answer_state)
            x = data[data["state"] == answer_state].x.item()
            y = data[data["state"] == answer_state].y.item()

            turtle.goto(x, y)

            turtle.write(answer_state)

turtle.mainloop()
