# Car Manager for Turtle Crossing Game
# Handles car creation, movement, and speed management

import random
from turtle import Turtle

# Game Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]  # Available car colors
STARTING_MOVE_DISTANCE = 5    # Initial car speed
MOVE_INCREMENT = 10          # Speed increase per level


class CarManager:
    """Class to manage all cars in the game.
    Handles car creation, movement, and difficulty progression."""

    def __init__(self):
        """Initialize car manager with empty car list and starting speed."""
        self.all_cars = []                    # List to store all active cars
        self.car_speed = STARTING_MOVE_DISTANCE  # Current movement speed

    def create_car(self):
        """Create a new car with random chance.
        Cars are created with 1/6 probability each time this is called
        to prevent overcrowding."""
        random_chance = random.randint(1, 6)
        if random_chance == 1:  # Create car only if random number is 1
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Make car rectangular
            new_car.penup()                                  # Don't draw while moving
            new_car.color(random.choice(COLORS))            # Random car color
            
            # Position car on right side at random height
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            
            self.all_cars.append(new_car)  # Add to active cars list

    def move_cars(self):
        """Move all cars from right to left at current speed."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Increase car speed when player completes a level."""
        self.car_speed += MOVE_INCREMENT