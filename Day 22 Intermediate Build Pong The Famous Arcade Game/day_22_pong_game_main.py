# Pong Game - Main Implementation (Turtle Graphics Version)
# This file contains the main game logic, including:
# - Game initialization and setup
# - Game loop and state management
# - Paddle movement and AI control
# - Collision detection and scoring
# - Sound effects and user interface

from turtle import Turtle, Screen
from day_22_pong_game_scoreboard import Scoreboard
from day_22_pong_game_ball import Ball
from day_22_pong_game_paddle import Paddle
import time
import random
import pygame  # Import pygame for sound effects

#--------------------
# Game Setup
#--------------------

# Initialize Pygame mixer for sound effects
pygame.mixer.init()

# Load sound files for game events
paddle_hit_sound = pygame.mixer.Sound("your_sound_file.wav")
miss_sound = pygame.mixer.Sound("your_miss_sound_file.wav")

# Global state variables
game_is_on = True          # Controls the main game loop
waiting_for_input = False  # Controls post-game input state

#--------------------
# Game Functions
#--------------------

def start_game():
    """Initialize and start a new game session."""
    global r_paddle, l_paddle, ball, scoreboard, game_is_on, waiting_for_input

    # Reset and configure the game screen
    screen.clear()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong Game")
    screen.tracer(0)  # Turn off automatic updates for smooth animation

    # Create game objects
    r_paddle = Paddle((350, 0))    # Right paddle (player)
    l_paddle = Paddle((-350, 0))   # Left paddle (AI)
    ball = Ball()                  # Game ball
    scoreboard = Scoreboard()      # Score display

    # Initialize paddle movement flags
    global r_paddle_up, r_paddle_down
    r_paddle_up = False
    r_paddle_down = False

    # Configure keyboard controls
    setup_key_bindings()

    # Reset game state
    game_is_on = True
    waiting_for_input = False

    # Main game loop
    while game_is_on:
        time.sleep(ball.move_speed)  # Control game speed
        screen.update()              # Update screen manually
        ball.move()                  # Move the ball

        # Handle paddle movements
        move_r_paddle()              # Move player paddle
        move_l_paddle()              # Move AI paddle

        # Wall collision detection
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Paddle collision detection
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
           (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()
            paddle_hit_sound.play()  # Play hit sound effect

        # Score points when ball passes paddles
        if ball.xcor() > 380:  # Right side (player misses)
            ball.reset_position()
            scoreboard.l_point()
            miss_sound.play()

        if ball.xcor() < -380:  # Left side (AI misses)
            ball.reset_position()
            scoreboard.r_point()
            miss_sound.play()

        # Check if someone won
        if check_winner():
            break

def quit_game():
    """Close the game window and end the program."""
    global game_is_on
    game_is_on = False
    screen.bye()

def restart_game():
    """Reset the game state and start a new game."""
    global waiting_for_input
    waiting_for_input = False
    start_game()

def handle_user_input():
    """Set up key bindings for post-game options."""
    global game_is_on, waiting_for_input
    if waiting_for_input:
        screen.onkeypress(restart_game, "c")  # 'C' to continue
        screen.onkeypress(quit_game, "q")     # 'Q' to quit
        screen.listen()

#--------------------
# Paddle Control Functions
#--------------------

def r_paddle_go_up_start():
    """Start moving the right paddle up."""
    global r_paddle_up
    r_paddle_up = True

def r_paddle_go_up_stop():
    """Stop moving the right paddle up."""
    global r_paddle_up
    r_paddle_up = False

def r_paddle_go_down_start():
    """Start moving the right paddle down."""
    global r_paddle_down
    r_paddle_down = True

def r_paddle_go_down_stop():
    """Stop moving the right paddle down."""
    global r_paddle_down
    r_paddle_down = False

def move_r_paddle():
    """Move the right paddle based on keyboard input with boundary checking."""
    if r_paddle_up and r_paddle.ycor() < 250:
        r_paddle.go_up()
    if r_paddle_down and r_paddle.ycor() > -250:
        r_paddle.go_down()

def move_l_paddle():
    """
    Control the AI paddle movement with some intelligence and randomness.
    Includes a threshold to prevent jittery movement and random misses
    to make the game more interesting.
    """
    # Move only if the ball is significantly far from paddle center
    if abs(ball.ycor() - l_paddle.ycor()) > 40:
        if ball.ycor() > l_paddle.ycor() and l_paddle.ycor() < 250:
            l_paddle.go_up()
        elif ball.ycor() < l_paddle.ycor() and l_paddle.ycor() > -250:
            l_paddle.go_down()

    # Add randomness to make AI beatable
    miss_chance = random.randint(1, 100)
    if miss_chance <= 10:  # 10% chance to move in wrong direction
        if ball.ycor() > l_paddle.ycor() > -250:
            l_paddle.go_down()
        elif ball.ycor() < l_paddle.ycor() < 250:
            l_paddle.go_up()

#--------------------
# Game State Management
#--------------------

# Set winning condition
WINNING_SCORE = 10

def check_winner():
    """
    Check if either player has reached the winning score.
    Display appropriate message and handle end-game state.
    """
    global waiting_for_input
    if scoreboard.l_score == WINNING_SCORE:
        screen.clear()
        screen.bgcolor("black")
        screen.title("Pong Game")
        scoreboard.goto(0, 0)
        scoreboard.write("AI Wins!\nPress 'C' to play again\nPress 'Q' to quit",
                        align="center", font=("Courier", 24, "normal"))
        waiting_for_input = True
        handle_user_input()
        return True
    elif scoreboard.r_score == WINNING_SCORE:
        screen.clear()
        screen.bgcolor("black")
        screen.title("Pong Game")
        scoreboard.goto(0, 0)
        scoreboard.write("You Win!\nPress 'C' to play again\nPress 'Q' to quit",
                        align="center", font=("Courier", 24, "normal"))
        waiting_for_input = True
        handle_user_input()
        return True
    return False

def setup_key_bindings():
    """Configure keyboard controls for the game."""
    screen.listen()
    # Set up continuous paddle movement
    screen.onkeypress(r_paddle_go_up_start, "Up")
    screen.onkeyrelease(r_paddle_go_up_stop, "Up")
    screen.onkeypress(r_paddle_go_down_start, "Down")
    screen.onkeyrelease(r_paddle_go_down_stop, "Down")

#--------------------
# Game Initialization
#--------------------

# Initialize the game screen
screen = Screen()
setup_key_bindings()
start_game()
screen.mainloop()  # Start the game event loop
