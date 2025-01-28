# Import turtle module with alias and random module
import turtle as t
import random

# Create turtle object
tim = t.Turtle()

# Define list of colors for random selection
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", 
          "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    """Draw a shape with specified number of sides."""
    # Calculate angle for turns based on number of sides
    angle = 360 / num_sides
    # Draw the shape
    for _ in range(num_sides):
        tim.forward(100)    # Move forward
        tim.right(angle)    # Turn right by calculated angle

# Draw shapes from triangle (3 sides) to decagon (10 sides)
for shape_side_n in range(3, 11):
    # Choose random color for each shape
    tim.color(random.choice(colours))
    # Draw shape with current number of sides
    draw_shape(shape_side_n)
