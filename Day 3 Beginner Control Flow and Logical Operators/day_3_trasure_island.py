# Day 3 - Treasure Island Game
# A text-based adventure game demonstrating nested if/else statements
# and complex program flow

#--------------------
# Game Introduction
#--------------------

# Display ASCII art treasure map
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Welcome message
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#--------------------
# Game Logic
#--------------------

# First choice - crossroad
# Convert input to lowercase to handle any capitalization
choise1 = input('You\'re at a cross road. Where does you want to go? Type "left" or "right" ').lower()

if choise1 == "left":
    # Second choice - lake
    choise2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" for a boat. Type "swim" to swim across.\n').lower()
    
    if choise2 == "wait":
        # Third choice - doors
        choise3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and blue. Which colour do you chose?\n").lower()
        
        # Final outcomes based on door choice
        if choise3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choise3 == "yellow":
            print("You found the treasure! You Win!")
        elif choise3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")