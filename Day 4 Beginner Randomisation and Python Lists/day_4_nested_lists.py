# Day 4 - Working with Nested Lists
# This file demonstrates how to create and work with lists within lists

#--------------------
# Single List Example
#--------------------

# Create a list of fruits and vegetables (known as the "dirty dozen")
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", 
               "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", 
               "Celery", "Potatoes"]

#--------------------
# Separate Lists
#--------------------

# Split items into separate fruits and vegetables lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", 
          "Peaches", "Charries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

#--------------------
# Nested List
#--------------------

# Create a nested list by combining fruits and vegetables lists
# This creates a 2D list where each element is itself a list
new_dirty_dozen = [fruits, vegetables]

# Now new_dirty_dozen[0] gives fruits list
# and new_dirty_dozen[1] gives vegetables list