###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random
import turtle
from turtle import Turtle, Screen

import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


# print(rgb_colors)

def get_random_color():
    cat = random.choice(rgb_colors)
    tim.pencolor((cat[0], cat[1], cat[2]))


tim = Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
turtle.colormode(255)
tim.setheading(225)
tim.forward(400)
tim.setheading(0)
tim.dot(20, random.choice(rgb_colors))

screen = Screen()
screen.screensize(100, 100)

x = tim.xcor()
y = tim.ycor()

for _ in range(10):

    tim.goto(x, y)
    for _ in range(10):
        get_random_color()
        tim.pendown()
        tim.dot(20, random.choice(rgb_colors))
        tim.penup()
        tim.forward(50)
    y += 50

screen.exitonclick()
