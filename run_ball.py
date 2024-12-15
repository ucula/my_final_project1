import turtle
import time
import sys
import random
from ball import Ball
from paddle import Paddle
from obstacles import Obstacle
from interface import Interface


class Game:
    """
    Put all classes together creating a functioning pong game
    """
    def __init__(self):
        turtle.listen()
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.screen = turtle.Screen()
        self.screen.setup(1000, 800)
        self.screen.bgcolor("black")
        self.vx = 1.5
        self.vy = 1.5
        self.ball = Ball()
        self.paddle = Paddle()
        self.ui = Interface()
        self.obstacles = []
        self.scores = 0
        self.level = 1
        self.lives = 3
        self.hit_count = 0
        self.last_spawn = time.time()
        self.highest_scores = 0
        for y in range(270, 200, -30):
            for x in range(-350, 400, 70):
                self.obstacles.append(Obstacle(x, y))

    def menu(self):
        # Show menu when player first run the program and wait for space bar response
        self.ui.show_menu()
        self.screen.onkey(self.start_game, "space")

    def start_game(self):
        self.ui.menu.clear()
        self.ui.draw_border()
        self.ui.show_in_game_stats(self.scores, self.lives, self.level)
        self.run()

    def new_game(self):
        # Reset all player stats(variables) and run the game again
        self.scores = 0
        self.level = 1
        self.lives = 3
        self.vx = 1.5
        self.vy = 1.5
        self.ui.menu.clear()
        self.ball = Ball()
        self.paddle = Paddle()
        self.ball.goto(0, 0)
        self.ui.stats.clear()
        for obstacle in self.obstacles:
            obstacle.hideturtle()
        self.obstacles.clear()
        for y in range(270, 200, -30):  # original (270, 200)
            for x in range(-350, 400, 70):  # (-350, 400)
                self.obstacles.append(Obstacle(x, y))
        self.paddle.goto(0, -250)
        self.run()

    def level_up(self):
        """
        Increases the value of some variables such as level and the speed of the ball
        and re-position ball/paddle and obstacles
        """
        self.level += 1
        self.vx += 0.5
        self.vy += 0.5
        self.ball.hideturtle()
        self.paddle.hideturtle()
        self.ui.menu.clear()
        self.ball = Ball(self.vx, self.vy)
        self.paddle = Paddle()
        self.ball.goto(0, 0)
        self.ui.stats.clear()
        for obstacle in self.obstacles:
            obstacle.hideturtle()
        self.obstacles.clear()
        for y in range(270, 200, -30):  # original (270, 200)
            for x in range(-350, 400, 70):  # (-350, 400)
                self.obstacles.append(Obstacle(x, y))
        self.paddle.goto(0, -250)

    @staticmethod
    def end_game():
        # This is here to be used with onkey turtle methods
        print("See you next time :)")
        sys.exit()

    def check_collisions(self):
        # Check for collisions on every single surfaces
        if self.ball.xcor() > 390:
            self.ball.setx(390)
            self.ball.bounce_x()
            self.hit_count += 1

        if self.ball.xcor() < -390:
            self.ball.setx(-390)
            self.ball.bounce_x()
            self.hit_count += 1
        self.add_random_obstacle()

        if self.ball.ycor() > 287:
            self.ball.sety(287)
            self.ball.bounce_y()
            self.hit_count += 1
        self.add_random_obstacle()

        if -240 < self.ball.ycor() < -230 and \
                self.paddle.xcor() - 50 < self.ball.xcor() < self.paddle.xcor() + 50:
            self.ball.sety(-231)
            self.ball.bounce_y()
            self.hit_count += 1
        self.add_random_obstacle()

        for obstacle in self.obstacles:
            if obstacle.isvisible() and \
                    obstacle.ycor() - 10 < self.ball.ycor() < obstacle.ycor() + 10 and \
                    obstacle.xcor() - 35 < self.ball.xcor() < obstacle.xcor() + 35:
                obstacle.hideturtle()
                self.obstacles.remove(obstacle)
                self.ball.bounce_y()
                self.scores += 100
                self.hit_count += 1
        self.add_random_obstacle()

    def add_random_obstacle(self):
        # Adds in a random obstacles for every 10 times the ball bounces
        if self.hit_count == 10:
            current_time = time.time()
            if current_time - self.last_spawn >= 0.1:
                self.hit_count = 0
                self.last_spawn = current_time
                x = random.randint(-350, 350)
                y = random.randint(0, 200)
                new_obstacle = Obstacle(x, y)
                self.obstacles.append(new_obstacle)

    def check_lose_life(self):
        # Check for if the ball hits the bottom of the border
        if self.ball.ycor() < -287:
            self.lives -= 1  # if hit -1 live
            # restart the game
            self.ball.goto(0, 0)
            self.ball.vx = self.vy
            self.ball.vy = self.vx

    def check_game_pass(self):
        return len(self.obstacles) == 0

    def check_game_over(self):
        return self.lives == 0

    def run(self):
        while True:
            self.ball.move()
            self.check_collisions()
            self.check_lose_life()
            self.ui.update_in_game_stats(self.scores, self.lives, self.level)
            if self.check_game_pass():
                self.level_up()
            if self.check_game_over():
                self.highest_scores = max(self.highest_scores, self.scores)
                self.ball.hideturtle()
                self.paddle.hideturtle()
                for obstacle in self.obstacles:
                    obstacle.hideturtle()
                self.ui.stats.clear()
                self.ui.show_game_over(self.scores, self.highest_scores)
                break
            turtle.update()
            """
            This is here because when tested my pc if there's no time.sleep the ball will very very fast 
            making it unplayable for me, but when tested on my friends' pc with time.sleep the ball runs
            very slow. (I don't know if it's a bug or no)
            """
            time.sleep(0.001)

        self.screen.onkey(self.new_game, "r")
        self.screen.onkey(self.end_game, "q")


a = Game()
a.menu()
turtle.done()
