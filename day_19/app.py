from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_right():
    tim.setheading(tim.heading() - 10)


def turn_left():
    tim.setheading(tim.heading() + 10)


def clear_and_centered():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(key="w", fun=move_forwards)

screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_right)
screen.onkey(key="d", fun=turn_left)
screen.onkey(key="c", fun=clear_and_centered)

screen.exitonclick()
