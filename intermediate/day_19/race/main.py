import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="make your bet", prompt="which will win the race? enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
all_turtles = []

y = 0

for _ in range(0, 6):
    n = Turtle(shape="turtle")
    n.penup()
    n.color(random.choice(colors))
    n.goto(x=-230, y=y)
    y = y + 20
    all_turtles.append(n)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color}")
            else:
                print(f"You've lost! {winning_color}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
