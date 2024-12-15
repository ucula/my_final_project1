import turtle


class Paddle(turtle.Turtle):
    """
    A class for creating functioning paddle that can move left and right
    """
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -250)
        self.shape("square")
        self.color("white")
        self.shapesize(0.5, 5)
        self.screen.listen()
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeypress(self.move_right, "Right")

    def move_left(self):
        self.setx(max(self.xcor() - 70, -350))

    def move_right(self):
        self.setx(min(self.xcor() + 70, 350))