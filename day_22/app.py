from turtle import Screen, Turtle


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

paddle = Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color("white")
paddle.penup()
paddle.goto(350, 0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()