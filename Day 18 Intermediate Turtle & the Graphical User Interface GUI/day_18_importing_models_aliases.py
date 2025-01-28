# Different ways to import modules in Python

# Method 1: Import entire module
# import turtle
# tim = turtle.Turtle()

# Method 2: Import specific classes
# from turtle import Turtle
# tim = Turtle()
# tom = Turtle()
# terry = Turtle()

# Method 3: Import everything (not recommended)
# from turtle import *
# from random import *

# Method 4: Import with alias (recommended for long module names)
# import turtle as t
# tim = t.Turtle()

# Example using external module
import heroes  # Third-party module for generating hero names
print(heroes.gen())  # Generate and print random hero name
