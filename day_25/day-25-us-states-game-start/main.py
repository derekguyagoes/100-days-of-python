import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("u.s. states game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
turtle.penup()

data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="Which state do you want to play?",
    ).title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        if answer_state in guessed_states:
            print("you've already guessed that")
        else:
            state_data = data[data.state == answer_state]
            guessed_states.append(answer_state)
            t.goto(state_data.x.item(), state_data.y.item())

            t.write(answer_state)
