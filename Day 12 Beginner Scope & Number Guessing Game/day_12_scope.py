# Day 12 - Python Scope Examples
# This module demonstrates various scope concepts in Python

#--------------------
# Basic Scope Example
#--------------------

enemies = 1

def increase_enemies():
    """
    Demonstrates local vs global scope.
    Local variable shadows global variable.
    """
    enemies = 2  # Local variable
    print(f"enemies inside function: {enemies}")  # Prints 2

increase_enemies()
print(f"enemies outside function: {enemies}")  # Prints 1

#--------------------
# Local Scope
#--------------------

def drink_potion():
    """
    Demonstrates local scope.
    Variable only exists inside function.
    """
    potion_strength = 2  # Local variable
    print(potion_strength)

drink_potion()
# print(potion_strength)  # This would cause an error - variable not accessible

#--------------------
# Global Scope
#--------------------

player_health = 10  # Global variable

def new_drink_potion():
    """
    Demonstrates accessing global variable.
    No global keyword needed for reading.
    """
    potion_strength = 2  # Local variable
    print(player_health)  # Can access global variable

new_drink_potion()

#--------------------
# Block Scope
#--------------------

# Python has no block scope
if 3 > 2:
    a_variable = 10  # This is in global scope

# Example showing lack of block scope
game_level = 3

def create_enemy():
    """
    Demonstrates variable scope in blocks.
    Variables created in if blocks are function-scoped.
    """
    game_enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = game_enemies[0]
    print(new_enemy)  # Accessible because Python has no block scope

#--------------------
# Global Keyword
#--------------------

enemies = 1

def increase_enemies_global():
    """
    Demonstrates global keyword.
    Not recommended - can lead to bugs.
    """
    global enemies  # Tells Python to use global variable
    enemies += 1
    print(f"enemies inside function: {enemies}")

# Better approach using return
def increase_enemies_return():
    """
    Better approach using return value.
    Avoids global variable modification.
    """
    print(f"enemies inside function: {enemies}")
    return enemies + 1

increase_enemies_global()
print(f"enemies outside function: {enemies}")

increase_enemies_return()
print(f"enemies outside function: {enemies}")

#--------------------
# Global Constants
#--------------------

# Constants are typically named in UPPERCASE
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

def calculate():
    """
    Demonstrates using global constants.
    Constants are meant to be read-only.
    """
    print(PI)  # Accessing global constant

calculate()
