# Import required modules and assets
from day_14_higher_Lower_art import logo, vs  # Import ASCII art for game visuals
from day_14_higher_lower_data import data     # Import game data (celebrities/brands)
import random  # For random selection of accounts
import os      # For clearing the screen

def get_random_account():
    """Get data from random account"""
    # Randomly select and return one account from the data list
    return random.choice(data)

def format_data(account):
    """Format account into printable format: name, description and country"""
    # Extract account details
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # Return formatted string for display
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    # Compare follower counts based on user's guess
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    # Display game logo
    print(logo)
    # Initialize score and game state
    score = 0
    game_should_continue = True
    # Get initial accounts for comparison
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        # Move B to A and get new B
        account_a = account_b
        account_b = get_random_account()

        # Ensure A and B are different accounts
        while account_a == account_b:
            account_b = get_random_account()

        # Display comparison
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Get user's guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        # Get follower counts
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        
        # Check if guess is correct
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Clear screen and show logo again
        os.system("cls")
        print(logo)
        
        # Handle game result
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

# Start the game
game()