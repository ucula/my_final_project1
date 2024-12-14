import turtle
import random


class Ball(turtle.Turtle):
    def __init__(self, vx=1.5, vy=1.5):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.vx = vx
        self.vy = vy

    def move(self):
        self.goto(self.xcor() + self.vx, self.ycor() + self.vy)

    def bounce_off_xcor(self):
        self.vx = -self.vx + random.uniform(-0.1, 0.1)

    def bounce_off_ycor(self):
        self.vy = -self.vy + random.uniform(-0.1, 0.1)
