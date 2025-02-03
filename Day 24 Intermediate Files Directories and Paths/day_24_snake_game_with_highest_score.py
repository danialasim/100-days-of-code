# Snake Game - Main Implementation
# Manages game flow, collision detection, and user input handling

import time
from turtle import Screen
from day_24_snake_function import Snake
from day_24_snake_food import Food
from day_24_snake_scoreboard import Scoreboard

#--------------------
# Game State Variables
#--------------------
game_is_on = True          # Controls main game loop
waiting_for_input = False  # Tracks if waiting for restart/quit input

def start_game():
    """Initialize and start a new game session."""
    global snake, food, scoreboard, game_is_on, waiting_for_input

    # Configure game window
    screen.clear()                     # Clear previous game
    screen.bgcolor("black")            # Set background color
    screen.setup(width=600, height=600)  # Set window size
    screen.title("My Snake Game")      # Set window title
    screen.tracer(0)                   # Turn off animation updates

    # Initialize game objects
    snake = Snake()        # Create snake
    food = Food()         # Create food
    scoreboard = Scoreboard()  # Create scoreboard

    # Set up keyboard controls
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # Reset game state
    game_is_on = True
    waiting_for_input = False

    #--------------------
    # Main Game Loop
    #--------------------
    while game_is_on:
        screen.update()    # Update screen
        snake.move()       # Move snake

        #--------------------
        # Collision Detection
        #--------------------

        # Food collision
        if snake.head.distance(food) < 15:
            food.refresh()           # Move food
            snake.extend()           # Grow snake
            scoreboard.increase_score()  # Update score

        # Wall collision
        if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or 
            snake.head.ycor() > 280 or snake.head.ycor() < -280):
            game_over()

        # Self collision (tail)
        for segment in snake.segments:
            if segment == snake.head:
                pass  # Skip head segment
            elif snake.head.distance(segment) < 10:
                game_over()

        time.sleep(0.1)  # Control game speed

def game_over():
    """Handle game over state and display options."""
    global game_is_on, waiting_for_input
    game_is_on = False
    scoreboard.reset()     # Update high score if needed

    # Display game over message and options
    scoreboard.goto(0, 0)
    scoreboard.write(f"Game Over!\nPress 'C' to play again\nPress 'Q' to quit", 
                    align="center", font=("Courier", 24, "normal"))
    
    waiting_for_input = True
    handle_user_input()    # Set up input handlers

def quit_game():
    """Close the game window."""
    global game_is_on
    game_is_on = False
    screen.bye()          # Close window

def restart_game():
    """Reset game state and start new game."""
    global waiting_for_input
    waiting_for_input = False
    start_game()

def handle_user_input():
    """Set up key bindings for game over options."""
    global game_is_on, waiting_for_input
    if waiting_for_input:
        screen.onkeypress(restart_game, "c")  # 'C' to restart
        screen.onkeypress(quit_game, "q")     # 'Q' to quit
        screen.listen()

#--------------------
# Game Initialization
#--------------------
screen = Screen()          # Create game window
start_game()              # Start first game
screen.mainloop()         # Start event loop
