# Day 15 - Coffee Machine
# Implementation of a virtual coffee machine with drink menu, resource management, and coin processing

#--------------------
# Imports
#--------------------

from day_15_coffee_machiene_art import logo  # Import ASCII art
import os  # For clearing the screen

#--------------------
# Menu Configuration
#--------------------

# Dictionary containing drink recipes and costs
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

#--------------------
# Machine State
#--------------------

# Track machine's profit
profit = 0

# Track available resources
resources = {
    "water": 300,  # ml
    "milk": 200,   # ml
    "coffee": 100, # g
}

#--------------------
# Helper Functions
#--------------------

def is_resources_sufficient(order_ingredients):
    """
    Check if there are sufficient resources for the drink.
    
    Args:
        order_ingredients (dict): Required ingredients for the drink
        
    Returns:
        bool: True if enough resources, False otherwise
    """
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough

def process_coins():
    """
    Process inserted coins and calculate total.
    
    Returns:
        float: Total money inserted
    """
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """
    Check if payment is sufficient and handle change.
    
    Args:
        money_received (float): Money inserted by user
        drink_cost (float): Cost of the drink
        
    Returns:
        bool: True if payment successful, False otherwise
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """
    Make the coffee by deducting resources.
    
    Args:
        drink_name (str): Name of the drink
        order_ingredients (dict): Required ingredients
    """
    for item, quantity in order_ingredients.items():
        resources[item] -= quantity
    print(f"Here is your {drink_name} ☕️. Enjoy!")

#--------------------
# Main Function
#--------------------

def coffee_machine():
    """Main function to run the coffee machine."""
    is_on = True
    while is_on:
        print(logo)
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        
        # Handle special commands
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        else:
            # Process drink order
            drink = MENU.get(choice)
            if drink and is_resources_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        
        # Clear screen for next order
        if is_on:
            input("\nPress Enter to continue...")
            os.system("cls")

# Start the coffee machine
coffee_machine()
