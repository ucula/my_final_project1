import turtle
import random


class Obstacle(turtle.Turtle):  # Make this class a child of turtle class, there's a reason why I do this ()
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color(random.choice(["peru", "cyan", "gold1", "olivedrab", "blue", "pink"]))  # Obstacle colors
        self.speed(0)
        self.shapesize(stretch_wid=1, stretch_len=3)  # set shape of obstacles
        self.penup()
        self.goto(x, y)
