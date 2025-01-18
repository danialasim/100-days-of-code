# Day 8 - Function Parameters
# This file demonstrates different ways to create and use functions with parameters

#--------------------
# Simple Function
#--------------------

# Function without parameters
def greet():
    print("Hello")
    print("Welcome to the programming word.")
    print("My name is Danial")

# Call the simple function
greet()

#--------------------
# Function with Input
#--------------------

# Function that takes a single parameter
def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How do you do {name}")

# Call function with one argument
greet_with_name("Angela")

#--------------------
# Multiple Parameters
#--------------------

# Function that takes two parameters
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}")

# Call function with keyword arguments
# This makes the code more readable and order doesn't matter
greet_with(name="Danial Asim", location="Gujranwala")
