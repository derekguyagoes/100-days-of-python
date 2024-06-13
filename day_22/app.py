import time
from turtle import Screen, Turtle

from day_22.Paddle import Paddle
from ball import Ball
from day_22.scoreboard import Scoreboard

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
divider.goto(0, 800)

rightPaddle = Paddle(350)
leftPaddle = Paddle(-350)

screen.listen()
screen.onkey(rightPaddle.go_up, "Up")
screen.onkey(rightPaddle.go_down, "Down")
screen.onkey(leftPaddle.go_up, "w")
screen.onkey(leftPaddle.go_down, "s")

ball = Ball()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with right paddle
    if (ball.distance(rightPaddle) < 50 and ball.xcor() > 320 or
            ball.distance(leftPaddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    #detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
