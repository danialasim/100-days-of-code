# Day 3 - Rollercoaster Ticket System
# This program demonstrates conditional statements, nested if/else, and logical operators

#--------------------
# Initial Setup
#--------------------

print("Welcome to the rollercoaster!")
# Convert height input to integer for numerical comparison
height = int(input("What is you height in cm? "))

# Initialize ticket price
bill = 0

#--------------------
# Height Check
#--------------------

if height >= 120:  # Primary safety check
    print("You can ride the rollercoster!")
    
    #--------------------
    # Age-based Pricing
    #--------------------
    
    age = int(input("What is you age? "))
    if age < 12:  # Child ticket
        bill = 5
        print("Child tickets are 5$.")
    elif age <= 18:  # Youth ticket
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age < 55:  # Mid-life crisis discount
        print("Everything is going to be ok. Have a free ride on us!")
    else:  # Adult ticket
        bill = 12
        print("Adult tickets are $12.")
    
    #--------------------
    # Photo Option
    #--------------------
    
    # Ask if they want a photo and add to bill if yes
    wants_photo = input("Do you want a photo Taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3  # Add photo cost to ticket price
    
    # Display final bill
    print(f"Your Final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
