# Paddle Class for Pong Game
# Handles paddle creation and movement

from turtle import Turtle

class Paddle(Turtle):
    """Class representing a paddle in the Pong game.
    Inherits from Turtle for graphics capabilities."""
    
    def __init__(self, position):
        """Initialize paddle with specific size and position.
        Args:
            position (tuple): Starting position (x, y) for the paddle"""
        super().__init__()
        self.shape("square")           # Set paddle shape
        self.color("white")            # Set paddle color
        self.shapesize(stretch_wid=5, stretch_len=1)  # Make paddle tall and thin
        self.penup()                   # Don't draw when moving
        self.goto(position)            # Move to starting position

    def go_up(self):
        """Move paddle up by 20 pixels."""
        new_y = self.ycor() + 20      # Calculate new y position
        self.goto(self.xcor(), new_y) # Move to new position

    def go_down(self):
        """Move paddle down by 20 pixels."""
        new_y = self.ycor() - 20      # Calculate new y position
        self.goto(self.xcor(), new_y) # Move to new position
