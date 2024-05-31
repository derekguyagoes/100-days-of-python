import time
from turtle import Screen, Turtle

from day_22.Paddle import Paddle
from ball import Ball

# pong
# screate teh screen divider in the middle
# two paddles
# ball moving
# detect wall colliison
# detect collision with paddle
# detect when paddle misses
# 2 player scores

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("pong")
screen.tracer(0)

divider = Turtle()
# divider.penup()
divider.goto(0, -780)
divider.color("white")
divider.goto(0,800)

rightPaddle = Paddle(350)
leftPaddle = Paddle(-350)

screen.listen()
screen.onkey(rightPaddle.go_up, "Up")
screen.onkey(rightPaddle.go_down, "Down")
screen.onkey(leftPaddle.go_up, "w")
screen.onkey(leftPaddle.go_down, "s")

ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()