import turtle


class Paddle(turtle.Turtle):  # Make this class a child of turtle class, there's a reason why I do this ()
    def __init__(self):
        super().__init__()  # I do this because I don't want to type self.paddle.(Method)
        self.penup()
        self.goto(0, -250)  # the initial spot for the paddle (x, y)
        self.shape("square")
        self.color("white")  # set the color of the paddle
        self.shapesize(0.5, 5)  # set width and length of the paddle
        self.control()

    # tell the paddle to move to the left
    def move_left(self):
        x = self.xcor()
        x -= 70  # set how far the paddle can move to the left
        if x < -350:  # check if it goes over border, if not, do the following methods
            x = -350
        self.setx(x)

    # move the paddle to move to the right
    def move_right(self):
        x = self.xcor()
        x += 70  # set how far the paddle can move to the right
        if x > 350:  # check if it goes over border, if not, do the following methods
            x = 350
        self.setx(x)

    # assign keys to move paddle
    def control(self):
        self.screen.listen()
        self.screen.onkeypress(self.move_left, "Left")  # assign "Left key" to the move left function
        self.screen.onkeypress(self.move_right, "Right")  # assign "Right key" to the move right function
