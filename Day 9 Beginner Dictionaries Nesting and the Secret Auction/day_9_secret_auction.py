# Day 9 - Secret Auction Program
# A program that runs a secret auction where bidders can't see each other's bids

#--------------------
# Imports
#--------------------

import os  # For clearing the screen
from day_9_secret_auction_art import logo  # Import ASCII art

#--------------------
# Helper Functions
#--------------------

def clear_screen():
    """Clear the console screen for better visibility."""
    os.system("cls")  # Use "clear" for Unix/Linux/MacOS

def find_highest_bidder(bidding_record):
    """
    Find the highest bidder from the bidding record.
    
    Args:
        bidding_record (dict): Dictionary containing bidder names and their bids
        
    Returns:
        None: Prints the winner and their bid amount
    """
    highest_bid = 0
    winner = ""
    
    # Loop through all bidders and their bids
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    # Announce the winner
    print(f"The winner is {winner} with a bid of ${highest_bid}")

#--------------------
# Main Program
#--------------------

# Display the auction logo
print(logo)

# Initialize auction data
bid = {}  # Dictionary to store bids
bidding_finished = False

# Main auction loop
while not bidding_finished:
    # Get bidder information
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    
    # Store the bid
    bid[name] = price
    
    # Check for more bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bid)
    elif should_continue == "yes":
        clear_screen()  # Clear screen for next bidder