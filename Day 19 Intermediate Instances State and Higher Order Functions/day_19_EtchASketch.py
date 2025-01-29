# Day 19 - Etch-A-Sketch
# This module implements an Etch-A-Sketch drawing program using turtle graphics

#--------------------
# Imports
#--------------------

from turtle import Turtle, Screen

#--------------------
# Setup
#--------------------

# Create turtle and screen
tim = Turtle()
screen = Screen()

#--------------------
# Control Functions
#--------------------

def move_forward():
    """Move turtle forward (W key)."""
    tim.forward(10)

def move_backward():
    """Move turtle backward (S key)."""
    tim.backward(10)

def turn_right():
    """Turn turtle right (D key)."""
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def turn_left():
    """Turn turtle left (A key)."""
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear():
    """Clear screen and reset turtle (C key)."""
    tim.clear()          # Clear the drawing
    tim.penup()          # Lift pen
    tim.home()           # Return to center
    tim.pendown()        # Lower pen

#--------------------
# Key Bindings
#--------------------

# Start listening for events
screen.listen()

# Bind movement keys (WASD controls)
screen.onkey(move_forward, "w")   # Forward
screen.onkey(move_backward, "s")  # Backward
screen.onkey(turn_left, "a")      # Left
screen.onkey(turn_right, "d")     # Right

# Bind clear function
screen.onkey(clear, "c")

#--------------------
# Exit
#--------------------

# Keep window open until clicked
screen.exitonclick()