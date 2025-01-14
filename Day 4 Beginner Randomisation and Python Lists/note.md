# Day 4 - Randomisation and Python Lists

## Concepts Learned
1. **Random Module**
   - Importing modules
   - Random integer generation
   - Random float generation
   - Creating custom modules

2. **Python Lists**
   - List creation and indexing
   - List modification
   - List methods (append, extend)
   - Negative indexing
   - List length

3. **Nested Lists**
   - Creating lists within lists
   - Accessing nested list elements
   - 2D lists
   - List organization

4. **Project: Rock Paper Scissors Game**
   - User input handling
   - Random choice generation
   - Game logic implementation
   - ASCII art in Python
   - Conditional statements with lists

## Code Examples Explained

### 1. Random Module Usage (`day_4_random_module.py`)
```python
import random
import day_4_my_module

# Generate random integer between 1 and 10
random_integer = random.randint(1, 10)

# Generate random float between 0 and 5
random_float = random.random() * 5

# Custom module usage
print(day_4_my_module.pi)
```

### 2. Lists Manipulation (`day_4_lists.py`)
```python
states_of_america = ["Delaware", "Pennsylvania", ...]

# Modifying list elements
states_of_america[1] = "Pencilvania"

# Getting last element
index_list = len(states_of_america)
print(states_of_america[index_list - 1])
```

### 3. Nested Lists (`day_4_nested_lists.py`)
```python
fruits = ["Strawberries", "Nectarines", "Apples"]
vegetables = ["Spinach", "Kale", "Tomatoes"]
# Combining lists
new_dirty_dozen = [fruits, vegetables]
```

### 4. Rock Paper Scissors Game (`day_4_rock_paper_game.py`)
```python
game_images = [rock, paper, scissors]
user_choice = int(input("Choose (0/1/2): "))
computer_choice = random.randint(0, 2)

# Game logic
if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
```

## Key Takeaways
- Random module is essential for games and simulations
- Lists are fundamental data structures in Python
- List indexing starts at 0
- Lists can contain any type of data
- Nested lists create complex data structures
- Input validation is crucial for user interactions

## Next Steps
- Explore more list methods
- Practice nested list operations
- Learn about list comprehensions
- Study other Python data structures
- Build more complex games with randomization
