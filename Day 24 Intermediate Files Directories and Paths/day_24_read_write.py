# File Operations Example
# Demonstrates basic file reading and writing operations in Python

#--------------------
# Reading from a file
#--------------------

# Using 'with' context manager for automatic file closing
# with open("day_24_my_file.txt") as file:
#     contents = file.read()      # Read entire file content
#     print(contents)             # Display file contents

#--------------------
# Writing to a file
#--------------------

# Open file in append mode ('a')
# Other modes: 'r' (read), 'w' (write), 'r+' (read & write)
with open("day_24_my_file.txt", mode="a") as file:
    file.write("\nNew text. ")  # Append new text with newline
