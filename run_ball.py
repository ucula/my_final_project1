import turtle
import time
from ball import Ball
from paddle import Paddle
from obstacles import Obstacle


class Game:
    def __init__(self):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.screen = turtle.Screen()
        self.screen.setup(1000, 800)
        self.screen.bgcolor("black")

        # initialize the game with ball, paddle, border and create all obstacles
        self.draw_border()
        self.ball = Ball()
        self.paddle = Paddle()
        self.obstacles = []
        for y in range(275, 185, -30):
            for x in range(-350, 401, 70):
                self.obstacles.append(Obstacle(x, y))

        self.levels = 1

    # draw border
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

    # run the program
    def run(self):
        while True:
            # ball starts to move
            self.ball.move()

            # Implement the wall bounce check method
            self.ball.wall_bounce_horizontal()
            self.ball.wall_bounce_vertical()


            #  check paddle bounce
            if -240 < self.ball.ycor() < -230 and (self.paddle.xcor() - 70 < self.ball.xcor() < self.paddle.xcor() + 70):
                self.ball.sety(-230)
                self.ball.paddle_bounce()

            # check obstacle bounce
            for obstacle in self.obstacles:
                if (obstacle.isvisible() and (obstacle.ycor() - 10 < self.ball.ycor() < obstacle.ycor() + 10)
                        and obstacle.xcor() - 35 < self.ball.xcor() < obstacle.xcor() + 35):
                    obstacle.hideturtle()  # hide the obstacle if it's already hit by the ball
                    self.obstacles.remove(obstacle)  # remove hit obstacle id
                    self.ball.obstacle_bounce()

            # check game over
            if self.ball.ycor() < -287:
                break

            turtle.update()  # update screen

            # This is here to slow down the ball, if this sleep timer does not exist,
            # ball speed will reach the speed of light
            time.sleep(0.001)


a = Game()
a.run()
