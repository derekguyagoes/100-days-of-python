from turtle import Turtle


class Snake(Turtle):
    def __init__(self, position):
        super().__init__(shape='square')

        self.position = position
        self.color("white")
        self.penup()
        self.goto(position)

    def move_forwards(self):
        self.forward(10)

    def move_backwards(self):
        self.backward(10)

    def turn_right(self):
        self.setheading(self.heading() - 10)

    def turn_left(self):
        self.setheading(self.heading() + 10)

    def clear_and_centered(self):
        self.clear()
        self.penup()
        self.home()
        self.pendown()

    # screen.onkey(key="w", fun=move_forwards)
    #
    # screen.onkey(key="s", fun=move_backwards)
    # screen.onkey(key="a", fun=turn_right)
    # screen.onkey(key="d", fun=turn_left)
    # screen.onkey(key="c", fun=clear_and_centered)