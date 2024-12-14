import turtle
import time
import sys
import random
from ball import Ball
from paddle import Paddle
from obstacles import Obstacle
from interface import Interface


class Game:
    def __init__(self):
        # Normal setup
        turtle.listen()
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.screen = turtle.Screen()
        self.screen.setup(1000, 800)  # screen size = 1000x800
        self.screen.bgcolor("black")  # set background color

        # This is the reason why I make ball class a child of turtle class. I don't want to type self.ball.ball.method()
        self.ball = Ball()
        self.vx = 1.5
        self.vy = 1.5

        # Same reason with ball.py
        self.paddle = Paddle()

        self.obstacles = []  # A list to store obstacles ID created from for loop
        # Start generate obstacles and put it in list
        for y in range(275, 260, -30):  # original (270, 200)
            for x in range(300, 350, 70):  # (-350, 400)
                self.obstacles.append(Obstacle(x, y))

        self.hit_count = 0
        self.spawn_delay = 0.1
        self.last_spawn = time.time()

        # introduce interface class
        self.ui = Interface()
        self.scores = 0
        self.level = 1
        self.lives = 3  # set how many lives you want
        self.highest_scores = 0  # variable for highest score
        self.running = False

    # Start ui
    def menu(self):
        self.ui.show_menu()
        self.screen.onkey(self.start_game, "space")

    def start_game(self):
        self.ui.menu.clear()
        self.ui.draw_border()
        self.ui.show_in_game_stats(self.scores, self.lives, self.level)
        self.run()

    def new_game(self):
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
        for y in range(275, 260, -30):  # original (270, 200)
            for x in range(300, 350, 70):  # (-350, 400)
                self.obstacles.append(Obstacle(x, y))
        self.paddle.goto(0, -250)

        # Restart game by running the game loop
        self.run()

    def level_up(self):
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
        for y in range(275, 260, -30):  # original (270, 200)
            for x in range(300, 350, 70):  # (-350, 400)
                self.obstacles.append(Obstacle(x, y))

        # Reset paddle position
        self.paddle.goto(0, -250)

        # Restart game by running the game loop
        self.run()

    @staticmethod
    def end_game():
        print("See you next time :)")
        sys.exit()

    # check wall bounce in xcor
    def check_wall_collision_x(self):
        if self.ball.xcor() > 390:
            self.ball.setx(390)
            self.ball.bounce_off_xcor()
            self.hit_count += 1

        if self.ball.xcor() < -390:  # Check wall bounce
            self.ball.setx(-390)
            self.ball.bounce_off_xcor()  # Change parameter to opposite
            self.hit_count += 1
        self.add_random_obstacle()

    # check wall bounce in ycor
    def check_wall_collision_y(self):
        if self.ball.ycor() > 287:  # Check wall bounce top side
            self.ball.sety(287)
            self.ball.bounce_off_ycor()  # Change direction of vx to opposite
            self.hit_count += 1
        self.add_random_obstacle()

    # check paddle bounce
    def check_paddle_bounce(self):
        if -240 < self.ball.ycor() < -230 and \
                self.paddle.xcor() - 50 < self.ball.xcor() < self.paddle.xcor() + 50:
            self.ball.sety(-231)
            self.ball.bounce_off_ycor()  # Change direction of vy to opposite
            self.hit_count += 1
        self.add_random_obstacle()

    # check obstacle bounce
    def check_obstacles_collision(self):
        for obstacle in self.obstacles:
            if obstacle.isvisible() and \
                    obstacle.ycor() - 10 < self.ball.ycor() < obstacle.ycor() + 10 and \
                    obstacle.xcor() - 35 < self.ball.xcor() < obstacle.xcor() + 35:
                obstacle.hideturtle()  # Hide the obstacle that's hit by the ball
                self.obstacles.remove(obstacle)  # Remove hit obstacle ID
                self.ball.bounce_off_ycor()  # Change direction of vy to opposite
                self.scores += 100
                self.hit_count += 1
        self.add_random_obstacle()

    def add_random_obstacle(self):
        if self.hit_count == 10:
            current_time = time.time()
            if current_time - self.last_spawn >= self.spawn_delay:
                self.hit_count = 0
                self.last_spawn = current_time
                x = random.randint(-350, 350)
                y = random.randint(0, 200)
                new_obstacle = Obstacle(x, y)
                self.obstacles.append(new_obstacle)

    # check if the ball hit the bottom screen border (pass the paddle or no)
    def check_lose_life(self):
        if self.ball.ycor() < -287:
            self.lives -= 1  # if hit -1 live
            # restart the game
            self.ball.goto(0, 0)
            self.ball.vx = self.vy
            self.ball.vy = self.vx

    def check_game_pass(self):
        return len(self.obstacles) == 0

    # check live = 0
    def check_game_over(self):
        return self.lives == 0

    # run the program
    def run(self):
        while True:

            # ball starts to move
            self.ball.move()

            # put check collisions functions
            self.check_wall_collision_x()  # check bounce wall in xcor
            self.check_wall_collision_y()  # check bounce wall in ycor
            self.check_paddle_bounce()  # check bounce with paddle
            self.check_obstacles_collision()  # check bounce with obstacles
            self.check_lose_life()  # check whether the ball drop below paddle or no

            # after check everything update game stats
            self.ui.update_in_game_stats(self.scores, self.lives, self.level)

            if self.check_game_pass():
                self.level_up()

            # check if live = 0 if so, end the game (break the loop)
            if self.check_game_over():
                # check if score higher then highest
                if self.scores > self.highest_scores:
                    self.highest_scores = self.scores

                # kills everything
                self.ball.hideturtle()
                self.paddle.hideturtle()
                for obstacle in self.obstacles:
                    obstacle.hideturtle()
                self.ui.stats.clear()
                self.ui.show_game_over(self.scores, self.highest_scores)
                break

            turtle.update()  # update screen so turtle doesn't crash

            # This is here to slow down the ball, if this sleep timer does not exist,
            # ball speed will reach the speed of light (not really, and yes, it's a bug and I don't know how to fix it)
            # It seems like this happened due to the obstacles list for loop, loops faster when there's less item
            # and every time the loop is lessened the ball speed increases
            time.sleep(0.001)

        self.screen.onkey(self.new_game, "r")
        self.screen.onkey(self.end_game, "q")


a = Game()
a.menu()
turtle.done()
