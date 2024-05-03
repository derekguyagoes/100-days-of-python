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

segment = []

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new = Snake(position)

    segment.append(new)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segment) - 1, 0, -1):
        new_x = segment[seg_num - 1].xcor()
        new_y = segment[seg_num - 1].ycor()
        segment[seg_num].goto(new_x, new_y)
    segment[0].forward(20)

screen.exitonclick()
