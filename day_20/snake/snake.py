from turtle import Turtle

LEFT = 180

RIGHT = 0

DOWN = 270

UP = 90

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # super().__init__(shape='square')
        #
        # self.position = position
        # self.color("white")
        # self.penup()
        # self.goto(position)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new = Turtle("square")
            new.color("white")
            new.penup()
            new.goto(position)

            self.segments.append(new)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
