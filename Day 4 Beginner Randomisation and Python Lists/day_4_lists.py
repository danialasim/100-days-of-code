# Day 4 - Working with Python Lists
# This file demonstrates list creation, modification, and basic operations

#--------------------
# List Creation
#--------------------

# Create a list of all US states
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", 
                    "Connecticut", "Massachusetts", "Maryland", "South Carolina", 
                    "New Hampshire", "Virginia", "New York", "North Carolina", 
                    "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", 
                    "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", 
                    "Maine", "Missouri", "Arkansas", "Michigan", "Florida", 
                    "Texas", "Iowa", "Wisconsin", "California", "Minnesota", 
                    "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", 
                    "Colorado", "North Dakota", "South Dakota", "Montana", 
                    "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", 
                    "New Mexico", "Arizona", "Alaska", "Hawaii"]

#--------------------
# List Modification
#--------------------

# Example of modifying a list element (commented out to preserve original list)
# states_of_america[1] = "Pencilvania"

# Example of extending a list (commented out to preserve original list)
# states_of_america.extend(["Angela land", "Jack Bauer Land"])

#--------------------
# List Operations
#--------------------

# Get the length of the list
index_list = len(states_of_america)

# Print the last element using list length
# Subtract 1 because list indices start at 0
print(states_of_america[index_list - 1])  # Output: Hawaii
