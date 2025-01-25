# Import required classes from other modules
from day_16_coffee_maker import CoffeeMaker
from day_16_menu import Menu
from day_16_money_machine import MoneyMachine

# Create objects from each class
money_machine = MoneyMachine()    # Handles money operations
coffee_machine = CoffeeMaker()    # Handles coffee making operations
menu = Menu()                     # Manages the menu items

# Set initial machine state
is_on = True

# Print initial reports
coffee_machine.report()           # Show resource levels
money_machine.report()            # Show profit

# Main program loop
while is_on:
    # Get and display menu options
    options = menu.get_items()
    choices = input(f"What would you like? {options}: ")
    
    # Handle different user inputs
    if choices == "off":
        is_on = False                # Turn off the machine
    elif choices == "report":
        coffee_machine.report()      # Show resource levels
        money_machine.report()       # Show profit
    else:
        # Process drink order
        drink = menu.find_drink(choices)
        # Check resources and process payment
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
