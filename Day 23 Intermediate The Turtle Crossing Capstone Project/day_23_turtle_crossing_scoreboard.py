# Scoreboard Class for Turtle Crossing Game
# Handles level tracking and game over display

from turtle import Turtle

# Display settings
FONT = ("Courier", 24, "normal")  # Font for level display
GAME_OVER_FONT = ("Arial", 32, "normal")  # Font for game over message


class Scoreboard(Turtle):
    """Class to manage game scoring and level display.
    Inherits from Turtle for text display capabilities."""

    def __init__(self):
        """Initialize scoreboard with starting level and position."""
        super().__init__()
        self.level = 1            # Start at level 1
        self.hideturtle()         # Hide turtle cursor
        self.penup()              # Don't draw when moving
        self.goto(-280, 250)      # Position in top-left corner
        self.update_scoreboard()   # Display initial level

    def update_scoreboard(self):
        """Clear and redraw the current level."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increment level and update display."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display game over message in center of screen."""
        self.goto(0, 0)  # Center of screen
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)
