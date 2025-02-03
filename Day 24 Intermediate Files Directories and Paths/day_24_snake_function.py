# Snake Class for Snake Game
# Handles snake creation, movement, and growth mechanics

from turtle import Turtle

# Game Constants
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # Initial snake segments
MOVE_DISTANCE = 20                                # Movement step size

# Direction Constants (in degrees)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """Class representing the snake in the game.
    Manages snake segments, movement, and growth."""

    def __init__(self):
        """Initialize snake with starting segments."""
        self.segments = []           # List to store all segments
        self.create_snake()          # Create initial snake
        self.head = self.segments[0] # Reference to snake's head

    def create_snake(self):
        """Create initial snake body from STARTING_POSITION."""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """Create a new snake segment at specified position.
        Args:
            position (tuple): (x, y) coordinates for new segment"""
        new_square = Turtle("square")  # Create segment
        new_square.color("white")      # Set color
        new_square.penup()             # Don't draw while moving
        new_square.goto(position)      # Position segment
        self.segments.append(new_square)  # Add to segments list

    def reset(self):
        """Reset snake to initial state.
        Moves existing segments off screen and creates new snake."""
        # Move old segments off screen
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()        # Clear segment list
        self.create_snake()          # Create new snake
        self.head = self.segments[0] # Reset head reference

    def extend(self):
        """Add new segment to snake.
        Called when snake eats food."""
        # Add segment at position of last segment
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move snake forward by MOVE_DISTANCE.
        Each segment follows the one in front of it."""
        # Move segments from tail to head
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Get position of segment in front
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # Move current segment to that position
            self.segments[seg_num].goto(new_x, new_y)
        # Move head forward
        self.segments[0].forward(MOVE_DISTANCE)

    #--------------------
    # Direction Controls
    #--------------------
    # Each method checks current direction to prevent 180-degree turns

    def up(self):
        """Turn snake up if not moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turn snake down if not moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """Turn snake right if not moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """Turn snake left if not moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
