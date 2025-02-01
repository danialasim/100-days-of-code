# Ball Class for Pong Game
# Handles ball movement and collision responses

from turtle import Turtle

class Ball(Turtle):
    """Class representing the ball in the Pong game.
    Inherits from Turtle for graphics capabilities."""

    def __init__(self):
        """Initialize ball with starting position and movement properties."""
        super().__init__()
        self.shape("circle")       # Set ball shape
        self.color("white")        # Set ball color
        self.penup()               # Don't draw when moving
        self.goto(0, 0)           # Start at center
        
        # Movement properties
        self.dx = 0.1             # Delta x for movement calculation
        self.dy = 0.1             # Delta y for movement calculation
        self.x_move = 10          # X movement distance per step
        self.y_move = 10          # Y movement distance per step
        self.move_speed = 0.1     # Initial movement speed

    def move(self):
        """Move the ball based on current direction and speed."""
        new_x = self.xcor() + self.x_move  # Calculate new x position
        new_y = self.ycor() + self.y_move  # Calculate new y position
        self.goto(new_x, new_y)            # Move to new position

    def bounce_y(self):
        """Reverse the ball's vertical direction (for wall collisions)."""
        self.y_move *= -1  # Reverse y direction

    def bounce_x(self):
        """Reverse the ball's horizontal direction and increase speed (for paddle collisions)."""
        self.x_move *= -1                # Reverse x direction
        self.move_speed *= 0.9           # Increase speed by reducing delay

    def reset_position(self):
        """Reset ball to center after a point is scored."""
        self.goto(0, 0)                  # Return to center
        self.move_speed = 0.1            # Reset speed
        self.bounce_x()                  # Change direction