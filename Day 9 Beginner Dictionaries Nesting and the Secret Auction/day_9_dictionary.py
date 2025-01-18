# Day 9 - Python Dictionaries
# This file demonstrates basic dictionary operations in Python

#--------------------
# Dictionary Creation
#--------------------

# Create a dictionary with initial key-value pairs
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

#--------------------
# Basic Operations
#--------------------

# Retrieve a value using its key
print(programming_dictionary["Bug"])

# Add a new key-value pair
programming_dictionary["Loop"] = "The action of doing something again and again"

# Display the entire dictionary
print(programming_dictionary)

#--------------------
# Dictionary Management
#--------------------

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary (commented out for demonstration)
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an existing key's value
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

#--------------------
# Dictionary Iteration
#--------------------

# Loop through all key-value pairs
for key in programming_dictionary:
    print(f"Key: {key}")
    print(f"Value: {programming_dictionary[key]}\n")