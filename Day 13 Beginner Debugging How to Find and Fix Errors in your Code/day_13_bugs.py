###########DEBUGGING#####################

# Day 13 - Debugging Examples
# This module demonstrates common programming bugs and their solutions

#--------------------
# Example 1: Range Function Bug
#--------------------

def my_function():
    """
    Demonstrates off-by-one error in range function.
    Bug: range(1, 20) only goes up to 19
    Fix: Use range(1, 21) to include 20
    """
    for i in range(1, 21):  # Fixed: Changed range to include 20
        if i == 20:
            print("You got it")

my_function()

#--------------------
# Example 2: Random Number Bug
#--------------------

from random import randint

# List of dice faces using Unicode characters
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]

# Generate random dice roll
dice_num = randint(0, 5)  # Fixed: Changed range to match list indices (0-5)
print(dice_imgs[dice_num])

#--------------------
# Example 3: Conditional Logic Bug
#--------------------

# Get birth year and determine generation
year = int(input("What's your year of birth? "))  # Fixed: Added space after ?
if year > 1980 and year < 1994:
    print("You are a millennial.")  # Fixed: Spelling of "millennial"
elif year >= 1994:
    print("You are a Gen Z.")
# Bug: Missing else clause for years <= 1980

#--------------------
# Example 4: Type Conversion Bug
#--------------------

# Check driving age
age = int(input("How old are you? "))  # Fixed: Added int() conversion
if age > 18:
    print(f"You can drive at age {age}.")  # Fixed: Added f-string formatting

#--------------------
# Example 5: Variable Assignment Bug
#--------------------

# Calculate total words in a book
pages = 0
word_per_page = 0

# Get user input
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))

# Calculate total
total_words = pages * word_per_page
print(total_words)

#--------------------
# Example 6: List Manipulation Bug
#--------------------

def mutate(a_list):
    """
    Doubles each number in the input list.
    Bug: Original had indentation error in append
    Fix: Properly indent the append statement
    
    Args:
        a_list (list): List of numbers to mutate
        
    Returns:
        None: Prints the mutated list
    """
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)  # Fixed: Proper indentation
    print(b_list)

# Test the function
mutate([1, 2, 3, 5, 8, 13])