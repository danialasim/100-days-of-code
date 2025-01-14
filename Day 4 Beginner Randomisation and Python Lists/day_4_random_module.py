# Day 4 - Working with Python's Random Module
# This file demonstrates various ways to generate random numbers

#--------------------
# Module Imports
#--------------------

import random  # Python's built-in random number generator
import day_4_my_module  # Custom module with PI value

#--------------------
# Random Integers
#--------------------

# Generate random integer between 1 and 10 (inclusive)
random_integer = random.randint(1, 10)
print(random_integer)

# Using value from custom module
print(day_4_my_module.pi)  # Access PI from our custom module

#--------------------
# Random Floats
#--------------------

# Generate random float between 0 and 5
# random.random() generates between 0 and 1, multiply by 5 for desired range
random_float = random.random() * 5
print(random_float)

#--------------------
# Example Application
#--------------------

# Generate random love score between 1 and 100
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")