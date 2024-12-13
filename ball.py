import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.setheading(270)
        self.vx = 1
        self.vy = 1
