import turtle
import random


class Obstacle(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color(random.choice(["peru", "cyan", "gold1", "olivedrab", "blue", "pink"]))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.goto(x, y)
