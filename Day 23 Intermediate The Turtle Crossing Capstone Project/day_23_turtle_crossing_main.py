# Turtle Crossing Game - Main Implementation
# A game where the player must guide a turtle across a busy road
# while avoiding randomly generated cars.

import time
from turtle import Screen
from day_23_turtle_crossing_player import Player
from day_23_car_manager import CarManager
from day_23_turtle_crossing_scoreboard import Scoreboard

#--------------------
# Game Setup
#--------------------

# Configure game screen
screen = Screen()
screen.setup(width=600, height=600)  # Set window size
screen.tracer(0)  # Turn off automatic updates

# Create game objects
player = Player()           # Create player turtle
car_manager = CarManager()  # Create car manager
scoreboard = Scoreboard()   # Create scoreboard

#--------------------
# Movement Control
#--------------------

# Movement state flags
is_up_key_held = False     # Track Up key state
is_down_key_held = False   # Track Down key state

def start_moving_up():
    """Set flag when Up key is pressed."""
    global is_up_key_held
    is_up_key_held = True

def stop_moving_up():
    """Reset flag when Up key is released."""
    global is_up_key_held
    is_up_key_held = False

def start_moving_down():
    """Set flag when Down key is pressed."""
    global is_down_key_held
    is_down_key_held = True

def stop_moving_down():
    """Reset flag when Down key is released."""
    global is_down_key_held
    is_down_key_held = False

#--------------------
# Keyboard Setup
#--------------------

# Configure keyboard controls
screen.listen()
# Up key controls
screen.onkeypress(start_moving_up, "Up")      # Key press handler
screen.onkeyrelease(stop_moving_up, "Up")     # Key release handler
# Down key controls
screen.onkeypress(start_moving_down, "Down")  # Key press handler
screen.onkeyrelease(stop_moving_down, "Down") # Key release handler

#--------------------
# Main Game Loop
#--------------------

game_is_on = True
while game_is_on:
    time.sleep(0.1)        # Control game speed
    screen.update()        # Update screen manually

    # Car management
    car_manager.create_car()  # Try to create new car
    car_manager.move_cars()   # Move all cars

    # Handle continuous movement based on key state
    if is_up_key_held:
        player.go_up()
    if is_down_key_held:
        player.go_down()

    # Collision detection with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # Check if player hits any car
            game_is_on = False         # End game
            scoreboard.game_over()     # Show game over message

    # Level completion check
    if player.is_at_finish_line():
        player.go_to_start()          # Reset player position
        car_manager.level_up()        # Increase difficulty
        scoreboard.increase_level()   # Update level display

# Wait for click to close game window
screen.exitonclick()
