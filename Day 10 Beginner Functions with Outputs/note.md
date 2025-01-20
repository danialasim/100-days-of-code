# Day 10 - Functions with Outputs

## Concepts Learned
1. **Function Returns**
   - Return values vs print
   - Multiple returns
   - Early returns
   - Docstrings

2. **String Manipulation**
   - Title case
   - String methods
   - String formatting
   - Input validation

3. **Calculator Operations**
   - Basic arithmetic
   - Function dictionaries
   - Recursive functions
   - User input handling

4. **Project: Calculator**
   - Function-based design
   - Operation mapping
   - Continuous calculations
   - ASCII art interface

## Code Examples Explained

### 1. Functions with Outputs (`day_10_function_with_outputs.py`)
```python
# Print vs Return
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")  # Just prints

def new_format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Invalid input"  # Early return
    return f"{f_name.title()} {l_name.title()}"  # Returns value
```

### 2. Calculator Implementation (`day_10_calculator.py`)
```python
# Operation Functions
def add(n1, n2):
    return n1 + n2

# Operation Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Main Calculator Function
def calculator():
    num1 = float(input("First number: "))
    while should_continue:
        operation = input("Pick operation: ")
        num2 = float(input("Next number: "))
        function = operations[operation]
        answer = function(num1, num2)
```

## Key Takeaways
- Functions can return values or print them
- Early returns help with input validation
- Dictionaries can store functions
- Recursion enables continuous calculations
- ASCII art enhances user interface
- Code organization improves readability

## Next Steps
- Add memory function
- Support more operations
- Add decimal precision control
- Implement scientific notation
- Add unit conversion
- Create a GUI version
