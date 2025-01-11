# Day 2 - Type Conversion (Type Casting) in Python
# This file demonstrates how to convert between different data types

# Get the length of user's name (returns an integer)
num_char = len(input("What is your name?"))

# Type Conversion Example 1: Integer to String
# We need to convert num_char to string to concatenate with other strings
new_num_char = str(num_char)  # Convert integer to string
print("Your name has " + new_num_char + " charaters.")

# Type Checking
# The type() function shows the data type of a variable
print(type(num_char))  # Will show <class 'int'>

# Type Conversion Example 2: String to Float
# Converting string "100.5" to float and adding to integer 70
print(70 + float("100.5"))  # Output: 170.5

# Type Conversion Example 3: Integer to String
# Converting numbers to strings for concatenation
print(str(70) + str(100))  # Output: "70100" (as a string)