import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.vx = 0.25  # set the initial ball speed of xcor
        self.vy = 0.25  # set the initial ball speed of ycor

    def move(self):
        self.goto(self.xcor() + self.vx, self.ycor() + self.vy)

    def wall_bounce_horizontal(self):
        # Check for collisions with the walls
        if self.xcor() > 390:
            self.setx(390)
            self.vx *= -1

        if self.xcor() < -390:
            self.setx(-390)
            self.vx *= -1

    def wall_bounce_vertical(self):
        if self.ycor() > 290:
            self.sety(290)
            self.vy *= -1

    def paddle_bounce(self):
        self.vy = -self.vy
