"""
This script demonstrates various examples of list comprehension in Python.
It covers basic operations, string manipulation, range operations, and conditional filtering.
"""

# Increment each number in the list by 1 using list comprehension
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]  # [expression for item in iterable]
print(new_numbers)

# Create a list of letters from the string using list comprehension
name = "Danial"
letter_list = [letter for letter in name]  # Iterates over each character in the string
print(letter_list)

# Generate a list of numbers from 2 to 20 (multiplied by 2) using list comprehension
range_list = [num * 2 for num in range(1, 11)]  # Multiplies each number in the range by 2
print(range_list)

# Filter names with less than 5 characters using list comprehension
names = ["Danial", "Noura", "Amina", "Mohammed", "Ahmad", "Angela"]
short_names = [name for name in names if len(name) < 5]  # Adds name to the list if its length is less than 5
print(short_names)

# Convert names longer than 5 characters to uppercase using list comprehension
long_names = [name.upper() for name in names if len(name) > 5]  # Applies .upper() to names longer than 5 characters
print(long_names)
