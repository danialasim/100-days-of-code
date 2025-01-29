# Day 19 - Turtle Race Game
# This module implements a turtle racing game with betting

#--------------------
# Imports
#--------------------

import random
from turtle import Turtle, Screen

#--------------------
# Setup
#--------------------

# Game state
is_race_on = False

# Screen setup
screen = Screen()
screen.setup(width=500, height=400)

# Get user's bet
user_bet = screen.textinput(
    title="Make your bet.",
    prompt="Which turtle will win the race? Enter a color: "
)

# Turtle colors
colors = ["red", "yellow", "orange", "green", "blue", "purple"]
all_turtles = []

#--------------------
# Create Turtles
#--------------------

# Create and position turtles
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    # Position turtles at starting line
    new_turtle.goto(x=-230, y=-100 + (turtle_index * 40))
    all_turtles.append(new_turtle)

#--------------------
# Race Logic
#--------------------

# Start race if bet was made
if user_bet:
    is_race_on = True

# Main race loop
while is_race_on:
    # Move each turtle
    for turtle in all_turtles:
        # Check for winner
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            # Announce results
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        
        # Move turtle random distance
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

#--------------------
# Exit
#--------------------

# Keep window open until clicked
screen.exitonclick()