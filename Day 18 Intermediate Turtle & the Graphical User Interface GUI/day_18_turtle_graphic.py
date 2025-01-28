# Import required classes from turtle module
from turtle import Turtle, Screen

# Create first turtle object and customize it
tim = Turtle()
tim.shape("turtle")  # Change shape to turtle icon
tim.color("green")   # Set color to green

# Draw a square
for _ in range(4):
    tim.forward(100)  # Move forward 100 units
    tim.right(90)     # Turn right 90 degrees
tim.color("blue")     # Change color to blue

# Create second turtle object
tom = Turtle()

# Draw a dashed line
for _ in range(15):
    tom.forward(10)   # Draw line for 10 units
    tom.penup()       # Lift pen (stop drawing)
    tom.forward(10)   # Move without drawing
    tom.pendown()     # Put pen down (start drawing)

# Create screen and set it to close on click
screen = Screen()
screen.exitonclick()
