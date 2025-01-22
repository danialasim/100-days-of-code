# Day 12 - Number Guessing Game
# A game where the player tries to guess a random number between 1 and 100

#--------------------
# Imports
#--------------------

from random import randint  # For generating random numbers
from day_12_number_guessing_art import logo  # Import ASCII art

#--------------------
# Game Configuration
#--------------------

# Constants for difficulty levels
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#--------------------
# Game Functions
#--------------------

def check_answer(guess, answer, turns):
    """
    Check if the guess matches the answer and return remaining turns.
    
    Args:
        guess (int): Player's guessed number
        answer (int): The correct number
        turns (int): Number of turns remaining
        
    Returns:
        int: Updated number of turns remaining
    """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return turns

def set_difficulty():
    """
    Set game difficulty based on user input.
    
    Returns:
        int: Number of turns based on difficulty (10 for easy, 5 for hard)
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    """
    Main game function.
    Handles game setup, player turns, and win/lose conditions.
    """
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate random answer
    answer = randint(1, 100)
    
    # Set up game difficulty
    turns = set_difficulty()
    
    # Main game loop
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        
        # Get player's guess
        guess = int(input("Make a guess: "))
        
        # Check guess and update turns
        turns = check_answer(guess, answer, turns)
        
        # Check for game over conditions
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

#--------------------
# Start Game
#--------------------

game()  # Start the game
