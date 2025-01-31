# Snake Game Food Class
# Handles the creation and placement of food in the game

from turtle import Turtle
import random

class Food(Turtle):
    """Class representing the food in the snake game.
    Inherits from Turtle to use turtle graphics functionality."""

    def __init__(self):
        """Initialize food with specific appearance and behavior."""
        super().__init__()  # Initialize parent Turtle class
        self.shape("circle")  # Set food shape
        self.penup()  # Don't draw lines when moving
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make food smaller
        self.color("blue")  # Set food color
        self.speed("fastest")  # Set maximum movement speed
        self.refresh()  # Place food in initial position

    def refresh(self):
        """Move food to a random position on the screen.
        Keeps food within game boundaries (-280 to 280)."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
