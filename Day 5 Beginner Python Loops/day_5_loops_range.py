# Day 5 - Using Range in Loops
# This program demonstrates the use of range() function to generate number sequences

#--------------------
# Sum Calculator
#--------------------

# Initialize sum variable
total_number = 0

# Loop through numbers 1 to 100 (inclusive)
for number in range(1, 101):  # range(1, 101) generates numbers from 1 to 100
    total_number += number    # Add each number to the running total

# Print final sum
print(total_number)  # Should output 5050 (sum of first 100 natural numbers)