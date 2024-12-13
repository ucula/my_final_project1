import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.vx = 1.5  # set the initial ball speed of xcor
        self.vy = 1.5  # set the initial ball speed of ycor

    # how this works is I tell the turtle to go to (the current cords + given parameter(how fast it can move))
    def move(self):
        self.goto(self.xcor() + self.vx, self.ycor() + self.vy)

    def wall_bounce_horizontal(self):
        # Check for collisions with the walls
        if self.xcor() > 390:
            self.setx(390)
            self.vx = -self.vx

        if self.xcor() < -390:
            self.setx(-390)
            self.vx = -self.vx

    def wall_bounce_vertical(self):
        if self.ycor() > 290:
            self.sety(290)
            self.vy = -self.vy

        if self.ycor() < -290:
            self.sety(-290)
            self.vy = -self.vy

    def paddle_bounce(self):
        self.vy = -self.vy

    def obstacle_bounce(self):
        self.vy = -self.vy
