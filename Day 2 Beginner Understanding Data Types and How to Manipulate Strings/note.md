# Day 2 - Understanding Data Types and String Manipulation

## Concepts Learned
1. **Data Types**
   - String (str)
   - Integer (int)
   - Float (float)
   - Boolean (bool)
   - Type conversion/casting

2. **Mathematical Operations**
   - Basic operations (+, -, *, /)
   - PEMDAS rule in Python
   - Exponents (**)
   - Integer division (//)
   - Modulo (%)

3. **Number Manipulation**
   - Round function
   - Floor division
   - F-strings
   - Number formatting

4. **Project: Tip Calculator**
   - Input handling
   - Type conversion
   - Mathematical operations
   - Formatting output

## Code Examples Explained

### 1. Data Types (`day_2_data_types.py`)
```python
# String subscripting
print("Hello"[0])  # Outputs: H

# Integer handling
print(123 + 345)  # Simple addition
num = 123_456_789  # Using underscore for readability

# Float
pi = 3.14159  # Decimal numbers
```

### 2. Type Conversion (`day_2-data_type_conversion.py`)
```python
# Converting between types
num_char = len(input("What is your name?"))
new_num_char = str(num_char)  # Convert int to string
print("Your name has " + new_num_char + " characters.")

# Type checking
print(type(num_char))  # Check variable type
```

### 3. Number Manipulation (`day_2_f_string_num_manuplation.py`)
```python
# Rounding numbers
print(round(8 / 3, 2))  # Round to 2 decimal places

# Floor division
print(8 // 3)  # Integer division

# F-strings
score = 0
height = 1.8
isWinning = True
print(f"Score: {score}, Height: {height}, Winning: {isWinning}")
```

### 4. Tip Calculator (`day_2_tip_calculator.py`)
```python
# Final project combining all concepts
bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_percentage = tip / 100
total_tip = bill * tip_percentage
total_bill = bill + total_tip
bill_per_person = round(total_bill / people, 2)

print(f"Each person should pay ${bill_per_person}")
```

## Key Takeaways
- Different data types serve different purposes
- Type conversion is essential for handling user input
- Mathematical operations follow PEMDAS rule
- F-strings make string formatting easy
- Proper number formatting is important for financial calculations

## Next Steps
- Practice type conversion with different data types
- Explore more mathematical operations
- Learn about string methods and formatting
- Work with more complex calculations
