import turtle


class Interface(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)

    def draw_border(self):
        turtle.penup()
        turtle.color("white")
        turtle.pensize(5)
        turtle.goto(-400, -300)
        turtle.pendown()
        turtle.goto(-400, 300)
        turtle.goto(400, 300)
        turtle.goto(400, -300)
        turtle.goto(-400, -300)


