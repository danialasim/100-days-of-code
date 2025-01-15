# Day 5 - Password Generator Project
# This program creates secure passwords with a mix of letters, numbers, and symbols

#--------------------
# Character Sets
#--------------------

import random

# Define available characters for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#--------------------
# User Input
#--------------------

print("Welcome to the PyPassword Generator!")
# Get desired number of each character type
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#--------------------
# Easy Level Password
#--------------------
# Characters are added in sequence: letters, then symbols, then numbers

password = ""
# Add requested number of letters
for char in range(1, nr_letters + 1):
    password += random.choice(letters)

# Add requested number of symbols
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

# Add requested number of numbers
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(f"Your password is {password}")

#--------------------
# Hard Level Password
#--------------------
# Characters are added in random order

# Create a list to store password characters
password_list = []

# Add requested number of letters
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

# Add requested number of symbols
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

# Add requested number of numbers
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

# Randomize the order of characters
random.shuffle(password_list)

# Convert list back to string
new_password = ""
for char in password_list:
    new_password += char
print(f"Your password is {new_password}")
