# Day 2 - Tip Calculator Project
# This program calculates how much each person should pay when splitting a bill,
# including a tip percentage

#--------------------
# Get User Input
#--------------------

# Welcome message
print("Welcome to the tip calculator.")

# Get the bill amount (as float for decimal values)
bill = float(input("What was the total bill? $ "))

# Get the tip percentage (as integer)
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Get number of people (as integer)
people = int(input("How many people to split the bill? "))

#--------------------
# Calculate Amounts
#--------------------

# Convert tip percentage to decimal (e.g., 15 becomes 0.15)
tip_as_percentage = tip / 100

# Calculate the tip amount
total_tip_ammount = bill * tip_as_percentage

# Calculate total bill including tip
total_bill = bill + total_tip_ammount

# Calculate amount per person and round to 2 decimal places
bill_per_person = round(total_bill / people, 2)

# Format the final amount to always show 2 decimal places
# This ensures amounts like $12.50 don't show as $12.5
final_ammount = "{:.2f}".format(bill_per_person)

#--------------------
# Display Result
#--------------------

# Show the amount each person should pay
print(f"Each Person should pay ${final_ammount}")