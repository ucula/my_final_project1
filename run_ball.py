import turtle
import time
from ball import Ball
from paddle import Paddle
from obstacles import Obstacle
from interface import Interface


class Game:
    def __init__(self):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.screen = turtle.Screen()
        self.screen.setup(1000, 800)  # screen size = 1000x800
        self.screen.bgcolor("black")

        # This is the reason why I make ball class a child of turtle class. I don't want to type self.ball.ball.method()
        self.ball = Ball()
        self.paddle = Paddle()
        self.obstacles = []
        for y in range(275, 185, -30):
            for x in range(-350, 401, 70):
                self.obstacles.append(Obstacle(x, y))
        self.ui = Interface()
        self.scores = 0
        self.level = 1
        self.lives = 5
        self.highest_scores = 0
        self.running = True

    def set_up_ui(self):
        self.ui.draw_border()
        self.ui.show_menu()
        self.ui.show_in_game_stats(self.scores, self.lives, self.level)

    def check_wall_collision_x(self):
        if self.ball.xcor() > 390 or self.ball.xcor() < -390:  # Check wall bounce
            self.ball.bounce_off_xcor()  # Change parameter to opposite

    def check_wall_collision_y(self):
        if self.ball.ycor() > 287:  # Check wall bounce top side
            self.ball.bounce_off_ycor()  # Change direction of vx to opposite

    def check_paddle_bounce(self):
        if -240 < self.ball.ycor() < -230 and \
                self.paddle.xcor() - 50 < self.ball.xcor() < self.paddle.xcor() + 50:
            self.ball.bounce_off_ycor()  # Change direction of vy to opposite

    def check_obstacles_collision(self):
        for obstacle in self.obstacles:
            if obstacle.isvisible() and \
                    obstacle.ycor() - 10 < self.ball.ycor() < obstacle.ycor() + 10 and \
                    obstacle.xcor() - 35 < self.ball.xcor() < obstacle.xcor() + 35:
                obstacle.hideturtle()  # Hide the obstacle if it's already hit by the ball
                self.obstacles.remove(obstacle)  # Remove hit obstacle ID
                self.ball.bounce_off_ycor()  # Change direction of vy to opposite

    def start_new_life(self):
        self.ball.goto(0, 0)
        self.ball.vx = 1.5
        self.ball.vy = 1.5
        self.paddle.goto(0, -250)

    def check_lose_life(self):
        if self.ball.ycor() < -287:
            self.lives -= 1
            self.start_new_life()

    def check_game_over(self):
        if self.lives == 0:
            return True
        else:
            return False

    # run the program
    def run(self):
        self.set_up_ui()
        while self.running:
            # ball starts to move
            self.ball.move()
            self.check_wall_collision_x()
            self.check_wall_collision_y()
            self.check_paddle_bounce()
            self.check_obstacles_collision()
            self.check_lose_life()
            self.ui.update_in_game_stats(self.scores, self.lives, self.level)
            if self.check_game_over():
                if self.scores > self.highest_scores:
                    self.highest_scores = self.scores
                break
            turtle.update()  # update screen

            # This is here to slow down the ball, if this sleep timer does not exist,
            # ball speed will reach the speed of light
            time.sleep(0.001)


a = Game()
a.run()
turtle.done()
