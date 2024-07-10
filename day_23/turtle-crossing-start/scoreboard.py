FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level: {self.score}", align="center", font=(FONT))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
