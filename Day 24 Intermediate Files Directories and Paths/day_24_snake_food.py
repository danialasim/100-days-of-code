# Food Class for Snake Game
# Handles the creation and placement of food items that the snake can eat

from turtle import Turtle
import random


class Food(Turtle):
    """Class representing food in the snake game.
    Inherits from Turtle for appearance and movement capabilities."""

    def __init__(self):
        """Initialize food with specific appearance and position."""
        super().__init__()
        self.shape("circle")                           # Set food shape
        self.penup()                                  # Don't draw when moving
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make food smaller
        self.color("blue")                            # Set food color
        self.speed("fastest")                         # Fast movement
        self.refresh()                                # Position food randomly

    def refresh(self):
        """Move food to a new random position on the screen.
        Called when snake eats the food or game restarts."""
        # Generate random coordinates within game boundaries
        random_x = random.randint(-280, 280)  # Screen width constraints
        random_y = random.randint(-280, 280)  # Screen height constraints
        self.goto(random_x, random_y)         # Move food to new position
