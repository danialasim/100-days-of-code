# Import required modules
import turtle as t
import random

# Create and configure turtle
tim = t.Turtle()
t.colormode(255)  # Set colormode to accept RGB values (0-255)

# Function to generate random RGB color
def random_color():
    """Generate and return random RGB color tuple."""
    r = random.randint(0, 255)  # Random red value
    g = random.randint(0, 255)  # Random green value
    b = random.randint(0, 255)  # Random blue value
    return (r, g, b)

# Define possible directions (0=East, 90=North, 180=West, 270=South)
directions = [0, 90, 180, 270]

# Configure turtle appearance
tim.pensize(15)        # Set line thickness
tim.speed("fastest")   # Set maximum speed

# Perform random walk
for _ in range(200):
    tim.color(random_color())                    # Set random color
    tim.forward(30)                              # Move forward
    tim.setheading(random.choice(directions))    # Turn to random direction
