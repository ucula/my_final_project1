import turtle


class Interface:
    """
    A class used for storing in game UI/stats and looks
    """
    def __init__(self):
        turtle.speed(0)
        self.border = turtle.Turtle(visible=False)  # Make a turtle for each method
        self.menu = turtle.Turtle(visible=False)  # Make a turtle for each method
        self.stats = turtle.Turtle(visible=False)  # Make a turtle for each method

    def draw_border(self, width=800, height=600):
        # Create a border for the game with width/height of 800x600
        self.border.penup()
        self.border.color("white")
        self.border.pensize(5)
        self.border.goto(-width // 2, -height // 2)
        self.border.pendown()
        for _ in range(2):
            self.border.forward(width)
            self.border.left(90)
            self.border.forward(height)
            self.border.left(90)

    def show_menu(self):
        # Shows a welcome message and tells the user the method to continue
        self.menu.hideturtle()
        self.menu.penup()
        self.menu.color("white")
        self.menu.goto(0, 100)
        self.menu.write("Welcome to Brick Breaker Game!", align="center", font=("Arial", 24, "bold"))
        self.menu.goto(0, 50)
        self.menu.write("Press Space to start!", align="center", font=("Arial", 16, "normal"))

    def update_stats(self, score=0, lives=3, level=1):
        # Shows all player stats at the top left corner of screen
        self.stats.hideturtle()
        self.stats.clear()
        self.stats.penup()
        self.stats.color("white")
        self.stats.goto(-400, 320)
        self.stats.write(f"Score: {score}  Lives: {lives}  Level: {level}", font=("Arial", 16, "bold"))

    def game_over(self, score, highest):
        """
        Show a message about player's current score highest score
        also shows options to quit the game or retry
        """
        self.stats.hideturtle()
        self.menu.hideturtle()
        self.menu.penup()
        self.menu.color("white")
        self.menu.goto(0, 0)
        self.menu.write(f"Game Over! Final Score: {score}, Highest Score: {highest}",
                        align="center", font=("Arial", 24, "bold"))
        self.menu.goto(0, -30)
        self.menu.write("Press 'R' to restart", align="center", font=("Arial", 16, "normal"))
        self.menu.goto(0, -60)
        self.menu.write("Press 'Q' to quit", align="center", font=("Arial", 16, "normal"))