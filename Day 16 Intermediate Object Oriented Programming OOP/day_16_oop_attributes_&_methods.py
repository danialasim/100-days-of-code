# Import required classes from the turtle module
from turtle import Turtle, Screen

# Create a new Turtle object instance named 'timmy'
timmy = Turtle()

# Print the object reference
print(timmy)

# Use object methods to modify the turtle's properties
timmy.shape("turtle")  # Change shape to turtle
timmy.color("coral")   # Set color to coral
timmy.forward(100)     # Move forward 100 units

# Create a new Screen object instance
my_screen = Screen()

# Access object attribute to get canvas height
print(my_screen.canvheight)

# Use method to keep window open until clicked
my_screen.exitonclick()