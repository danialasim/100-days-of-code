# Day 20 - Snake Game Part 1: Main Game
# This module implements the main game loop and controls

#--------------------
# Imports
#--------------------

from turtle import Screen
from day_20_snake_function import Snake
from day_21_snake_food import Food
from day_21_snake_scoreboard import ScoreBoard

#--------------------
# Screen Setup
#--------------------

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turn off automatic screen updates

#--------------------
# Game Objects
#--------------------

# Creating snake, food, and scoreboard objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

#--------------------
# Controls Setup
#--------------------

# Listening for keyboard events
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#--------------------
# Game State
#--------------------

# Variable to control game state
is_game_on = True

#--------------------
# Game Loop
#--------------------

def game_loop():
    """Main game loop handling movement, collisions, and scoring."""
    global is_game_on

    if is_game_on:
        # Move snake
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or 
            snake.head.ycor() > 280 or snake.head.ycor() < -280):
            is_game_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                is_game_on = False
                scoreboard.game_over()

        # Update screen and schedule next frame
        screen.update()
        screen.ontimer(game_loop, 100)  # 100ms delay between frames

#--------------------
# Start Game
#--------------------

# Start the game loop
game_loop()

# Keep window open until clicked
screen.exitonclick()
