import turtle
from ball import Ball
from paddle import Paddle


class Game:
    def __init__(self):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.screen = turtle.Screen()
        self.screen.setup(1000, 800)
        self.screen.bgcolor("black")
        self.draw_border()
        self.ball = Ball()
        self.paddle = Paddle()

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
            turtle.update()
            self.ball.move()
            self.ball.wall_bounce_horizontal()
            self.ball.wall_bounce_vertical()
            if (self.ball.ycor() > -240 and self.ball.ycor() < -230) and \
                    (self.paddle.xcor() - 50 < self.ball.xcor() < self.paddle.xcor() + 50):
                self.ball.sety(-230)
                self.ball.paddle_bounce()

a = Game()
a.run()
