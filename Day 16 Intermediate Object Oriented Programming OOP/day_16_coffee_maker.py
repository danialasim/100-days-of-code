# CoffeeMaker class to handle coffee machine resources and coffee making operations
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        """Initialize machine resources (water, milk, coffee)"""
        self.resources = {
            "water": 300,    # Water in ml
            "milk": 200,     # Milk in ml
            "coffee": 100,   # Coffee in grams
        }

    def report(self):
        """Prints a report of all resources."""
        # Display current levels of all resources
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # Check if we have enough of each ingredient for the drink
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        # Update resource levels by subtracting used ingredients
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
