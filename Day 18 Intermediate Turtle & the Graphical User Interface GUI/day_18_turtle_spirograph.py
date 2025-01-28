# Import required modules
import turtle as t
import random

# Create and configure turtle
tim = t.Turtle()
t.colormode(255)  # Set colormode to accept RGB values

# Function to generate random RGB color
def random_color():
    """Generate and return random RGB color tuple."""
    r = random.randint(0, 255)  # Random red value
    g = random.randint(0, 255)  # Random green value
    b = random.randint(0, 255)  # Random blue value
    return (r, g, b)

# Set maximum drawing speed
tim.speed("fastest")

def draw_spirograph(size_of_gap):
    """Draw spirograph pattern with specified gap size between circles."""
    # Calculate number of circles needed for full 360° pattern
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())    # Set random color
        tim.circle(100)              # Draw circle
        # Turn by gap size for next circle
        tim.setheading(tim.heading() + size_of_gap)

# Create spirograph with 5-degree gaps
draw_spirograph(5)

# Create screen and set it to close on click
screen = t.Screen()
screen.exitonclick()
