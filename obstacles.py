import turtle
import random


class Obstacle(turtle.Turtle):
    """
    A class for creating and drawing variety of colourful obstacles
    """
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(["peru", "cyan", "gold1", "olivedrab", "blue", "pink"]))
        self.shapesize(1, 3)
        self.goto(x, y)
