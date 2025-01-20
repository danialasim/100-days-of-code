# Day 11 - Blackjack Game
# Implementation of the classic card game Blackjack (also known as 21)

#--------------------
# Imports
#--------------------

import os  # For clearing the screen
import random  # For card selection
from day_11_black_jack_art import logo  # Import ASCII art

#--------------------
# Game Functions
#--------------------

def deal_card():
    """
    Return a random card from the deck.
    
    Returns:
        int: Card value (11 for Ace, 10 for face cards, 2-10 for number cards)
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """
    Calculate the score of a hand of cards.
    
    Args:
        cards (list): List of card values
        
    Returns:
        int: Score of the hand (0 represents a Blackjack)
    """
    # Check for blackjack (ace + 10 = 21)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
        
    # Handle ace value (11 or 1)
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score, computer_score):
    """
    Compare scores and determine the winner.
    
    Args:
        user_score (int): Player's score
        computer_score (int): Computer's score
        
    Returns:
        str: Result message with appropriate emoji
    """
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
        
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    """
    Run a single game of Blackjack.
    Handles all game logic including dealing, scoring, and determining winner.
    """
    print(logo)
    
    # Initialize hands
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Player's turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        # Show current game state
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for game-ending conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask player for next move
            if input("Type 'y' to get another card, 'n' to pass: ") == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Show final results
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#--------------------
# Game Loop
#--------------------

# Keep playing until player chooses to stop
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("cls")  # Clear screen for new game
    play_game()