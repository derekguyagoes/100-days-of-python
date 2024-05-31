from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.width = 20
        self.height = 20
        self.setx(0)
        self.sety(0)
        self.color('white')
        self.shape('circle')
        self.penup()

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
