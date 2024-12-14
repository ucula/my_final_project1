import turtle


class Interface:
    def __init__(self):
        turtle.speed(0)
        self.border = turtle.Turtle()
        self.menu = turtle.Turtle()
        self.stats = turtle.Turtle()
        self.width = 800
        self.height = 600

    def draw_border(self):
        """Draw the border of the game."""
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

    def show_menu(self):
        self.menu.hideturtle()
        self.menu.penup()
        self.menu.color("white")
        self.menu.goto(0, 100)
        self.menu.write("Welcome to Brick Breaker Game!", align="center", font=("Arial", 24, "bold"))

    def show_in_game_stats(self, score, lives, level):
        self.stats.hideturtle()
        self.stats.clear()
        self.stats.penup()
        self.stats.color("white")
        self.stats.goto(-400, 320)
        self.stats.write(f"Score: {score}  Lives: {lives}  Level: {level}", font=("Arial", 16, "bold"))

    def show_game_over(self, score, highest_score):
        self.stats.clear()
        self.menu.clear()
        self.menu.penup()
        self.menu.color("white")
        self.menu.goto(0, 0)
        self.menu.write(f"Game Over! Final Score: {score}, Highest Score: {highest_score}",
                        align="center", font=("Arial", 24, "bold"))
        self.menu.goto(0, -30)
        self.menu.write("Press 'q' to quit", align="center", font=("Arial", 16, "normal"))

    def update_in_game_stats(self, score, lives, level):
        self.show_in_game_stats(score, lives, level)




