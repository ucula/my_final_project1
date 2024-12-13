import turtle
import random

class Obstacle(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color(random.choice(["peru", "cyan", "gold1", "olivedrab"]))
        self.speed(0)
        self.shapesize(stretch_wid=1, stretch_len=3.2)
        self.penup()
        self.goto(x, y)
