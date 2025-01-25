# Classes for managing coffee menu items and menu functionality

class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        """Initialize menu item with its properties"""
        self.name = name        # Name of the drink
        self.cost = cost        # Cost of the drink
        self.ingredients = {    # Dictionary of required ingredients
            "water": water,     # Water in ml
            "milk": milk,       # Milk in ml
            "coffee": coffee    # Coffee in grams
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        """Initialize menu with predefined drinks"""
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        # Create string of all available drink names
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        # Search for drink in menu and return if found
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
