# Day 2 - Number Manipulation and F-Strings in Python
# This file shows various ways to manipulate numbers and format strings

#--------------------
# Number Rounding
#--------------------

# Round a number to 2 decimal places
print(round(8 / 3, 2))  # Output: 2.67

# Floor division (// operator)
print(type(8 // 3))  # Output: <class 'int'> (removes decimal)
print(type(8 / 3))   # Output: <class 'float'> (keeps decimal)

#--------------------
# Variables for F-String Demo
#--------------------

score = 0
height = 1.8
isWinning = True

# Increment score using shorthand operator
score += 1  # Same as: score = score + 1

#--------------------
# F-String Examples
#--------------------

# F-strings allow embedding expressions inside string literals
# They make it easy to combine different data types in one string
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
