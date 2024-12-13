import turtle
import ball
import paddle


class Game:
    def __init__(self):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.screen = turtle.Screen()
        self.screen.setup(1000, 800)
        self.screen.bgcolor("black")
        self.draw_border()
        self.ball = ball.Ball()
        self.paddle = paddle.Paddle()

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

    def run(self):
        while True:
            self.screen.update()


a = Game()
a.run()
