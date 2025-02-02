# Player Class for Turtle Crossing Game
# Handles the player turtle's movement and position management

from turtle import Turtle

# Game Constants
STARTING_POSITION = (0, -280)  # Player starts at bottom center
MOVE_DISTANCE = 10            # Distance to move in each step
FINISH_LINE_Y = 280          # Y-coordinate of finish line


class Player(Turtle):
    """Class representing the player-controlled turtle.
    Inherits from Turtle class for basic movement and appearance."""

    def __init__(self):
        """Initialize player turtle with starting position and appearance."""
        super().__init__()
        self.shape("turtle")     # Set turtle shape
        self.penup()             # Don't draw while moving
        self.go_to_start()       # Position at start
        self.setheading(90)      # Face upward (90 degrees)

    def go_up(self):
        """Move the turtle forward by MOVE_DISTANCE."""
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        """Move the turtle backward by MOVE_DISTANCE."""
        self.backward(MOVE_DISTANCE)

    def go_to_start(self):
        """Reset turtle to starting position."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Check if turtle has reached the finish line.
        Returns:
            bool: True if turtle has crossed finish line, False otherwise."""
        return self.ycor() > FINISH_LINE_Y