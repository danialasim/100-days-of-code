# Day 3 - Control Flow and Logical Operators

## Concepts Learned
1. **Conditional Statements**
   - if/elif/else statements
   - Nested if statements
   - Multiple if statements
   - Conditional operators (>, <, >=, <=, ==, !=)

2. **Logical Operators**
   - AND operator (and)
   - OR operator (or)
   - NOT operator (not)

3. **Code Blocks and Indentation**
   - Understanding Python indentation
   - Code block structure
   - Proper nesting of conditions

4. **Project: Treasure Island**
   - Complex conditional statements
   - Multiple choice adventure game
   - User input handling
   - ASCII art in Python

## Code Examples Explained

### 1. Rollercoaster Ticket System (`day_3_if_else_Conditional_Operators.py`)
```python
# Height check with nested age check and photo option
height = int(input("What is your height in cm? "))
if height >= 120:
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12
    
    # Additional photo option
    wants_photo = input("Do you want a photo? Y or N. ")
    if wants_photo == "Y":
        bill += 3
```

### 2. Treasure Island Game (`day_3_trasure_island.py`)
```python
# Adventure game with multiple paths
choice1 = input('Left or right? ').lower()
if choice1 == "left":
    choice2 = input('Swim or wait? ').lower()
    if choice2 == "wait":
        choice3 = input("Which door? Red/Yellow/Blue ").lower()
        if choice3 == "yellow":
            print("You Win!")
        else:
            print("Game Over")
```

## Key Takeaways
- Conditional statements control program flow
- Proper indentation is crucial in Python
- Logical operators combine conditions
- Input validation is important
- Complex programs can be built with nested conditions
- String comparisons are case-sensitive
- Lower() method helps handle user input consistently

## Next Steps
- Practice combining multiple conditions
- Explore more complex logical operations
- Build interactive programs with multiple paths
- Learn about switch/match statements (Python 3.10+)
- Study error handling with try/except
