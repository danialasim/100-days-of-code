# Import required modules
import turtle as turtle_module
import random

# Configure turtle graphics
turtle_module.colormode(255)  # Set color mode to accept RGB values

# Create and configure turtle
tim = turtle_module.Turtle()
tim.speed("fastest")     # Set maximum speed
tim.penup()             # Lift pen up (don't draw lines)
tim.hideturtle()        # Hide turtle cursor

# Color palette extracted from Hirst painting image
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241),
              (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
              (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

# Position turtle at starting point
tim.setheading(225)     # Point towards starting position
tim.forward(300)        # Move to starting position
tim.setheading(0)       # Reset heading to east

# Set number of dots to create
number_of_dots = 100

# Create dot painting
for dot_count in range(1, number_of_dots + 1):
    # Draw dot with random color from palette
    tim.dot(20, random.choice(color_list))
    tim.forward(50)     # Move forward for next dot

    # Move to next row after every 10 dots
    if dot_count % 10 == 0:
        tim.setheading(90)    # Turn north
        tim.forward(50)       # Move up
        tim.setheading(180)   # Turn west
        tim.forward(500)      # Move to start of next row
        tim.setheading(0)     # Turn east for next row

# Create screen and set it to close on click
screen = turtle_module.Screen()
screen.exitonclick()