import random
from turtle import Turtle, Screen

tim = Turtle()
# tim.shape("turtle")
tim.shape("turtle")
tim.color("red")


def square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)


def dashed_line():
    for i in range(50):
        if i % 2 == 0:
            tim.penup()
        else:
            tim.pendown()
        tim.forward(10)


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


def draw_shapes():
    for shape_side_n in range(3, 11):
        change_color()
        draw_shape(shape_side_n)


def random_walk():
    dirs = [0, 90, 180, 360]
    tim.pensize(15)
    tim.speed(10)
    for _ in range(200):
        direction = random.choice(dirs)
        change_color()
        tim.setheading(direction)
        tim.forward(30)

def spirograph(size_of_gap):

    tim.speed(10)
    for _ in range(int(360 / size_of_gap)):
        change_color()
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)



screen = Screen()

# square()
# dashed_line()
# draw_shapes()
# random_walk()
spirograph(5)
screen.exitonclick()
