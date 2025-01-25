# Day 15 - Coffee Machine Project

## Concepts Learned
1. **Local Development Setup**
   - IDE selection
   - Python installation
   - Environment setup
   - Project organization

2. **Data Structures**
   - Nested dictionaries
   - Resource management
   - Menu systems
   - Transaction handling

3. **Program Flow**
   - State management
   - User input processing
   - Resource checking
   - Transaction validation

4. **Project: Coffee Machine**
   - Drink menu system
   - Resource tracking
   - Coin processing
   - Change calculation
   - ASCII art interface

## Code Structure
### 1. Menu System
```python
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    # More drinks...
}
```

### 2. Resource Management
```python
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
```

## Key Functions
1. `is_resources_sufficient()`: Check ingredient availability
2. `process_coins()`: Handle money input
3. `make_coffee()`: Prepare the drink
4. `coffee_machine()`: Main program loop

## Key Takeaways
- Resource management is crucial
- Input validation improves reliability
- Clear user feedback is important
- Modular design helps maintenance
- State tracking simplifies logic

## Program Features
1. Multiple drink options
2. Resource tracking
3. Coin calculation
4. Change return
5. Profit tracking
6. Maintenance mode

## Next Steps
- Add more drink options
- Implement temperature selection
- Add milk alternatives
- Create drink customization
- Save machine state
- Add GUI interface
