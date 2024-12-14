import turtle
import random


class Ball(turtle.Turtle):  # Make this class a child of turtle class, there's a reason why I do this
    def __init__(self):
        super().__init__()  # Implement all turtle methods in
        self.shape('circle')
        self.color('red')
        self.penup()  # No more line from ball_turtle
        self.vx = random.choice([-1.5, 1.5])  # Set the initial ball speed of xcor(increasing this value will make the game harder to play)
        self.vy = 1.5  # Set the initial ball speed of ycor(increasing this value will make the game harder to play)

    # How this works is I tell the turtle to go to (the current cords + given parameter(how fast it can move))
    def move(self):
        self.goto(self.xcor() + self.vx, self.ycor() + self.vy)

    # Change direction of the ball in xcor
    def bounce_off_xcor(self):
        self.vx = -self.vx + random.uniform(-0.1, 0.1)

    # Change direction of the ball in ycor
    def bounce_off_ycor(self):
        self.vy = -self.vy + random.uniform(-0.1, 0.1)

    def setcolor(self):
        self.color('blue')
