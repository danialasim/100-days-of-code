# Day 10 - Calculator Program
# A calculator that can perform basic arithmetic operations

#--------------------
# Imports
#--------------------

from day_10_calculator_art import logo

#--------------------
# Operation Functions
#--------------------

def add(n1, n2):
    """Add two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Subtract n2 from n1."""
    return n1 - n2

def multiply(n1, n2):
    """Multiply two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Divide n1 by n2."""
    return n1 / n2

# Dictionary mapping operation symbols to their functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#--------------------
# Calculator Function
#--------------------

def calculator():
    """
    Run the calculator program.
    Allows continuous calculations with the result of previous operation.
    """
    # Display calculator logo
    print(logo)
    
    # Get the first number
    num1 = float(input("What's the first number?: "))

    # Display available operations
    for symbol in operations:
        print(symbol)

    # Main calculation loop
    should_continue = True
    while should_continue:
        # Get operation and second number
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))

        # Perform calculation
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        # Display result
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Check if user wants to continue with result
        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to start new: ") == "y":
            num1 = answer  # Use previous answer as first number
        else:
            should_continue = False
            calculator()  # Start fresh calculation

# Start the calculator
calculator()