# Day 5 - Looping Through Lists
# This program demonstrates how to iterate through lists and perform operations

#--------------------
# List Creation
#--------------------

# Create a list of fruits
fruits = ["Apple", "Peach", "Pear"]

#--------------------
# List Iteration
#--------------------

# Loop through each fruit in the list
for fruit in fruits:
    # Print the fruit name
    print(fruit)
    
    # Create and print a pie variety for each fruit
    print(fruit + " Pie")
    
    # Print the entire list for each iteration
    # This shows that we can access the original list inside the loop
    print(fruits)