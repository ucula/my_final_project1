import turtle


class Interface:
    def __init__(self):
        turtle.speed(0)
        # assign turtle to each of the function
        self.border = turtle.Turtle()  # Make a turtle for each method
        self.menu = turtle.Turtle()  # Make a turtle for each method
        self.stats = turtle.Turtle()  # Make a turtle for each method
        self.width = 800
        self.height = 600

    # draw border for the game 800x600 size
    def draw_border(self):
        self.border.hideturtle()
        self.border.penup()
        self.border.color("white")
        self.border.pensize(5)
        self.border.goto(-self.width // 2, -self.height // 2)
        self.border.pendown()
        for _ in range(2):
            self.border.forward(self.width)
            self.border.left(90)
            self.border.forward(self.height)
            self.border.left(90)

    # show begin menu before playing the game
    def show_menu(self):
        self.menu.hideturtle()
        self.menu.penup()
        self.menu.color("white")
        self.menu.goto(0, 100)
        self.menu.write("Welcome to Brick Breaker Game!", align="center", font=("Arial", 24, "bold"))
        self.menu.goto(0, 50)
        self.menu.write("Press spacebar to start!", align="center", font=("Arial", 16, "normal"))

    # show lives, scores and level in-game
    def show_in_game_stats(self, score=0, lives=3, level=1):
        self.stats.hideturtle()
        self.stats.clear()
        self.stats.penup()
        self.stats.color("white")
        self.stats.goto(-400, 320)
        self.stats.write(f"Score: {score}  Lives: {lives}  Level: {level}", font=("Arial", 16, "bold"))

    # update in-game stats
    def update_in_game_stats(self, score, lives, level):
        self.show_in_game_stats(score, lives, level)

    # show game_over ui when lives reach 0
    def show_game_over(self, score, highest):
        self.stats.hideturtle()
        self.menu.hideturtle()
        self.menu.penup()
        self.menu.color("white")
        self.menu.goto(0, 0)
        self.menu.write(f"Game Over! Final Score: {score}, Highest Score: {highest}",
                        align="center", font=("Arial", 24, "bold"))
        self.menu.goto(0, -30)
        self.menu.write("Press 'r' to restart", align="center", font=("Arial", 16, "normal"))
        self.menu.goto(0, -60)
        self.menu.write("Press 'q' to quit", align="center", font=("Arial", 16, "normal"))
