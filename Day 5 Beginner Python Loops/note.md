# Day 5 - Python Loops

## Concepts Learned
1. **For Loops**
   - Basic loop syntax
   - Looping through lists
   - Using range() function
   - Loop control statements

2. **Range Function**
   - Basic range usage
   - Step arguments
   - Negative stepping
   - Range with lists

3. **List Operations in Loops**
   - Iterating through lists
   - Modifying lists in loops
   - List methods (append, extend)
   - List comprehension basics

4. **Project: Password Generator**
   - Random character selection
   - String manipulation
   - List shuffling
   - Combining different character types

## Code Examples Explained

### 1. Basic For Loop with Range (`day_5_loops_range.py`)
```python
# Calculate sum of numbers from 1 to 100
total_number = 0
for number in range(1, 101):
    total_number += number
print(total_number)  # Output: 5050
```

### 2. Loops with Lists (`day_5_loops_with_lists.py`)
```python
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")  # String concatenation in loops
```

### 3. Password Generator (`day_5_password_generator.py`)
```python
# Easy Level - Sequential password
for char in range(nr_letters):
    password += random.choice(letters)

# Hard Level - Randomized password
password_list = []
for char in range(nr_letters):
    password_list.append(random.choice(letters))
random.shuffle(password_list)
```

## Key Takeaways
- For loops are essential for repetitive tasks
- range() function provides sequence of numbers
- Lists can be modified during iteration
- random.shuffle() randomizes list order
- String concatenation works in loops
- Password security through randomization

## Next Steps
- Explore while loops
- Study nested loops
- Learn about loop control statements (break, continue)
- Practice list comprehensions
- Implement more complex loop algorithms
- Study loop optimization techniques
