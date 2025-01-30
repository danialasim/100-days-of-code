# Day 20 - Snake Game Part 1: Snake Class
# This module defines the Snake class and its behavior

#--------------------
# Imports
#--------------------

from turtle import Turtle

#--------------------
# Constants
#--------------------

# Initial snake segment positions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# Movement settings
MOVE_DISTANCE = 20

# Direction angles
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#--------------------
# Snake Class
#--------------------

class Snake:
    """Class representing the snake in the game."""
    
    def __init__(self):
        """Initialize the snake with three segments."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the initial snake body."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake at the given position."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Extend snake by adding a new segment."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward by one step."""
        # Move each segment to the position of the segment in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Move the head forward
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Change direction to up if not moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change direction to down if not moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change direction to left if not moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change direction to right if not moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
