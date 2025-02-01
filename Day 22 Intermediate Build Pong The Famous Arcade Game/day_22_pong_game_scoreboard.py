# Scoreboard Class for Pong Game
# Handles score display and updates

from turtle import Turtle

# Constants for text display
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    """Class representing the scoreboard in the Pong game.
    Inherits from Turtle for text display capabilities."""

    def __init__(self):
        """Initialize scoreboard with starting scores and display settings."""
        super().__init__()
        self.color("white")        # Set text color
        self.penup()               # Don't draw when moving
        self.hideturtle()          # Hide the turtle cursor
        
        # Initialize scores
        self.l_score = 0          # Left player score
        self.r_score = 0          # Right player score
        self.update_score()       # Display initial scores

    def update_score(self):
        """Clear and redraw both scores on the screen."""
        self.clear()              # Clear previous scores
        
        # Draw left player score
        self.goto(-100, 200)      # Position for left score
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        
        # Draw right player score
        self.goto(100, 200)       # Position for right score
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        """Increment left player's score and update display."""
        self.l_score += 1         # Increase score
        self.update_score()       # Redraw scores

    def r_point(self):
        """Increment right player's score and update display."""
        self.r_score += 1         # Increase score
        self.update_score()       # Redraw scores
