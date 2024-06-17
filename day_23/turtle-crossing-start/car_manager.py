import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
BOTTOM = -500


class CarManager:
    def __init__(self):
        self.cars = []

        for _ in range(10):
            new_car = Car()
            self.cars.append(new_car)



class Car(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(500, BOTTOM)
