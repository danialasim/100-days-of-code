# Day 7 - Hangman Game
# A classic word guessing game with visual feedback

#--------------------
# Imports
#--------------------

import os  # For clearing the screen
import random  # For selecting random words
from day_7_hangman_words import word_list  # Import the word list
from day_7_hangman_art import logo, stages  # Import game art

#--------------------
# Game Setup
#--------------------

# Select a random word and get its length
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initialize game state
end_of_game = False
lives = 6  # Player starts with 6 lives

# Display game logo
print(logo)

# Debug information (can be commented out in production)
print(f'Pssst, the solution is {chosen_word}.')

# Create display list with blanks for each letter
display = []
for _ in range(word_length):
    display += "_"

#--------------------
# Game Loop
#--------------------

while not end_of_game:
    # Get player's guess and convert to lowercase
    guess = input("Guess a letter: ").lower()
    
    # Clear the screen for better visibility
    os.system('cls')

    # Check if letter was already guessed
    if guess in display:
        print(f"You already guessed {guess}")

    # Check each position in the word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Handle incorrect guesses
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Display current game state
    print(f"{' '.join(display)}")  # Show word with guessed letters

    # Check for win condition
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Display current hangman stage
    print(stages[lives])