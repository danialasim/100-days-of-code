# Day 4 - Rock Paper Scissors Game
# A classic game implemented in Python using random choices and ASCII art

#--------------------
# ASCII Art
#--------------------

# Rock ASCII art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper ASCII art
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# Scissors ASCII art
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#--------------------
# Game Logic
#--------------------

import random

# Store game images in a list for easy access
game_images = [rock, paper, scissors]

# Get user's choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Input validation
if user_choice >= 3 or user_choice < 0:
    print("You type an invalid number, You Lose!")
else:
    # Display user's choice
    print(game_images[user_choice])
    
    # Generate and display computer's choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    #--------------------
    # Determine Winner
    #--------------------
    
    # Rock beats Scissors
    if user_choice == 0 and computer_choice == 2:
        print("You wins!")
    # Rock beats Scissors (computer wins)
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    # Higher number wins (Paper beats Rock, Scissors beats Paper)
    elif user_choice > computer_choice:
        print("You wins!")
    # Higher number wins (computer)
    elif computer_choice > user_choice:
        print("You lose!")
    # Same choice = draw
    elif computer_choice == user_choice:
        print("Its a draw!")