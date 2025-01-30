# Day 20 - Snake Game (Pygame Version)
# This module implements the Snake game using Pygame instead of Turtle graphics

#--------------------
# Imports
#--------------------

import pygame
import random

#--------------------
# Initialize Pygame
#--------------------

pygame.init()

#--------------------
# Constants
#--------------------

# Colors (RGB values)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Game settings
BLOCK_SIZE = 20

#--------------------
# Game Setup
#--------------------

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Initialize clock for controlling game speed
clock = pygame.time.Clock()

#--------------------
# Helper Functions
#--------------------

def draw_snake(snake_list):
    """Draw the snake on the screen."""
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def message(msg, color):
    """Display a message on the screen."""
    font = pygame.font.SysFont(None, 50)
    text = font.render(msg, True, color)
    screen.blit(text, [WIDTH // 6, HEIGHT // 3])

def get_difficulty():
    """Get difficulty level from user input."""
    screen.fill(BLACK)
    message("Select Difficulty: \n 1-Easy, \n2-Medium, 3-Hard", WHITE)
    pygame.display.update()

    difficulty = None
    while difficulty not in [1, 2, 3]:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = 1
                elif event.key == pygame.K_2:
                    difficulty = 2
                elif event.key == pygame.K_3:
                    difficulty = 3
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    return difficulty

#--------------------
# Main Game Loop
#--------------------

def game_loop():
    """Main game loop handling game logic and events."""
    # Set game speed based on difficulty
    difficulty = get_difficulty()
    speed = {1: 10, 2: 15, 3: 20}[difficulty]

    # Game state
    game_over = False
    game_close = False

    # Snake initial position
    x1 = WIDTH // 2
    y1 = HEIGHT // 2
    x1_change = 0
    y1_change = 0

    # Snake properties
    snake_list = []
    length_of_snake = 1

    # Food initial position
    foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    # Main game loop
    while not game_over:
        # Game over screen
        while game_close:
            screen.fill(BLACK)
            message("Game Over! Press Q-Quit or C-Play Again", WHITE)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        # Check wall collision
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change

        # Draw game elements
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        
        # Update snake body
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check self collision
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw snake and update display
        draw_snake(snake_list)
        pygame.display.update()

        # Check food collision
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1

        # Control game speed
        clock.tick(speed)

    # Quit game
    pygame.quit()
    quit()

#--------------------
# Start Game
#--------------------

game_loop()