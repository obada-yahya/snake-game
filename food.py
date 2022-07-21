from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")
        self.penup()
        self.goto(100, 100)
        self.color("Blue")

    def respawn(self):
        self.goto(randint(-320, 320), randint(-260, 260))
