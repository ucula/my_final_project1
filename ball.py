import turtle
import random


class Ball(turtle.Turtle):
    """
    A class for initializing a ball object with initial velocity of vx and vy
    """
    def __init__(self, vx, vy):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.vx = vx
        self.vy = vy

    def move(self):
        self.goto(self.xcor() + self.vx, self.ycor() + self.vy)

    def bounce_x(self):
        # Reverses the ball direction and adds a bit of velocity change
        self.vx = -self.vx + random.uniform(-0.1, 0.1)

    def bounce_y(self):
        # Reverses the ball direction and adds a bit of velocity change
        self.vy = -self.vy + random.uniform(-0.1, 0.1)