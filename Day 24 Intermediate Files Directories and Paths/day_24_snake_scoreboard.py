# Scoreboard Class for Snake Game
# Handles score tracking, display, and high score persistence

from turtle import Turtle

# Display Constants
ALIGNMENT = "center"                # Text alignment
FONT = ("Courier", 24, "normal")   # Text font settings


class Scoreboard(Turtle):
    """Class for managing and displaying game score.
    Inherits from Turtle for text display capabilities."""

    def __init__(self):
        """Initialize scoreboard with score and high score."""
        super().__init__()
        self.score = 0              # Current game score

        # Load high score from file
        try:
            with open("day_24_my_file.txt") as data:
                self.high_score = int(data.read().strip())
        except (ValueError, FileNotFoundError):
            # Set default if file doesn't exist or has invalid data
            self.high_score = 0

        # Configure scoreboard appearance
        self.color("white")         # Set text color
        self.penup()                # Don't draw when moving
        self.goto(0, 270)           # Position at top of screen
        self.hideturtle()           # Hide turtle cursor
        self.update_scoreboard()    # Display initial score

    def update_scoreboard(self):
        """Clear and redraw the scoreboard with current scores."""
        self.clear()                # Remove previous text
        # Write current and high scores
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                  align=ALIGNMENT, font=FONT)

    def reset(self):
        """Reset game score and update high score if necessary."""
        # Update high score if current score is higher
        if self.score > self.high_score:
            self.high_score = self.score
            # Save new high score to file
            with open("day_24_my_file.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0              # Reset current score
        self.update_scoreboard()    # Update display

    def increase_score(self):
        """Increment score by 1 and update display."""
        self.score += 1             # Increase score
        self.update_scoreboard()    # Update display
