import time
from turtle import Screen
from snake import Snake

# create snake body with 3 squares
# move the snake so it's walways movng forward
# control the snake so it moves

# next day
# detect collision with the food and double in size
# create score board
# detect collision with the wall -game over
# detect collision with tail - game over

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("my snake game")
screen.tracer(0)


snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



screen.exitonclick()
