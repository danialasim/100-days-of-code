# Day 19 - Event Listeners Demo
# This module demonstrates basic event handling with turtle graphics

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
# Event Handlers
#--------------------

def move_forward():
    """Move turtle forward when space key is pressed."""
    tim.forward(10)

#--------------------
# Event Binding
#--------------------

# Start listening for events
screen.listen()

# Bind space key to move_forward function
screen.onkey(key="space", fun=move_forward)

#--------------------
# Exit
#--------------------

# Keep window open until clicked
screen.exitonclick()
