# Day 16 - Object Oriented Programming (OOP)

## Concepts Learned
1. **Object-Oriented Programming Basics**
   - Classes and Objects
   - Attributes and Methods
   - Constructor (`__init__`)
   - Instance Variables
   - Class Variables and Constants
   - Docstrings
   - Method Parameters and Return Values

2. **Python Packages**
   - Using PyPI (Python Package Index)
   - Installing external packages
   - Working with PrettyTable
   - Using the Turtle module

3. **Coffee Machine Project (OOP Version)**
   - Class Design and Implementation
   - Object Interaction
   - Modular Programming
   - Code Organization
   - Resource Management
   - Payment Processing

## Code Files Explained

### 1. Basic OOP Concepts (`day_16_oop_attributes_&_methods.py`)
```python
# Demonstrates basic OOP concepts using Turtle graphics
from turtle import Turtle, Screen

timmy = Turtle()          # Object creation
timmy.shape("turtle")     # Method calls
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()      # Screen object
print(my_screen.canvheight)  # Accessing attributes
```

### 2. PyPI and PrettyTable (`day_16_pypi_prettytable.py`)
```python
# Using external package for formatted table output
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
```

### 3. Coffee Machine Classes

#### Menu System (`day_16_menu.py`)
```python
class MenuItem:
    # Blueprint for menu items with properties:
    # - name: drink name
    # - cost: drink price
    # - ingredients: dictionary of required ingredients

class Menu:
    # Manages menu items with methods:
    # - get_items(): returns available drinks
    # - find_drink(): searches for specific drink
```

#### Coffee Maker (`day_16_coffee_maker.py`)
```python
class CoffeeMaker:
    # Manages coffee machine resources:
    # - water, milk, coffee quantities
    # Methods:
    # - report(): shows resource levels
    # - is_resource_sufficient(): checks ingredients
    # - make_coffee(): prepares drink
```

#### Money Machine (`day_16_money_machine.py`)
```python
class MoneyMachine:
    # Handles payment processing:
    # - Coin values (quarters, dimes, nickles, pennies)
    # - Profit tracking
    # Methods:
    # - process_coins(): calculates inserted amount
    # - make_payment(): handles transactions
```

#### Main Program (`day_16_oop_coffee_main.py`)
```python
# Combines all classes for coffee machine operation:
# 1. Creates objects from each class
# 2. Handles user input and menu display
# 3. Coordinates between classes for orders
# 4. Manages machine state (on/off)
```

## Coffee Machine Project Structure

### Class Relationships:
1. **Main Program**
   - Creates and coordinates all objects
   - Handles user interface
   - Controls program flow

2. **Menu System**
   - MenuItem: Data structure for drinks
   - Menu: Collection and search functionality
   - Used by main program to display options

3. **CoffeeMaker**
   - Resource management
   - Coffee preparation
   - Status reporting

4. **MoneyMachine**
   - Payment processing
   - Change calculation
   - Profit tracking

### Data Flow:
1. User selects drink from Menu
2. CoffeeMaker checks resources
3. MoneyMachine processes payment
4. CoffeeMaker makes drink
5. Main program coordinates all steps

## Key Takeaways
- OOP helps organize complex programs
- Classes encapsulate related data and behavior
- Objects interact through well-defined methods
- Modular design improves maintainability
- External packages extend functionality
- Clear class responsibilities improve design

## Next Steps
- Explore inheritance and polymorphism
- Implement error handling
- Add data persistence (save state)
- Create GUI interface
- Add new drink customization
- Implement user accounts
- Add inventory management
- Create maintenance mode
