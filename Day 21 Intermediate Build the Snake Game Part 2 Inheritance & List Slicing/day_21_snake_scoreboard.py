# Snake Game Scoreboard Class
# Handles score display and game over message

from turtle import Turtle

# Constants for text display
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    """Class for managing and displaying the game score.
    Inherits from Turtle to use turtle graphics for text display."""

    def __init__(self):
        """Initialize scoreboard with starting score and position."""
        super().__init__()  # Initialize parent Turtle class
        self.score = 0  # Initialize score
        self.color("white")  # Set text color
        self.penup()  # Don't draw when moving
        self.goto(0, 270)  # Position scoreboard at top
        self.hideturtle()  # Hide the turtle cursor
        self.update_scoreboard()  # Display initial score

    def update_scoreboard(self):
        """Display current score on screen."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Display game over message in center of screen."""
        self.goto(0, 0)  # Move to center
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increment score and update display."""
        self.score += 1  # Increase score
        self.clear()  # Clear previous score
        self.update_scoreboard()  # Display new score
