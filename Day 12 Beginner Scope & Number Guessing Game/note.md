# Day 12 - Scope & Number Guessing Game

## Concepts Learned
1. **Python Scope**
   - Local scope
   - Global scope
   - Block scope (and its absence in Python)
   - Global constants
   - Namespace rules

2. **Variable Scope**
   - Function scope
   - Module scope
   - Global keyword
   - Best practices for scope usage

3. **Game Development**
   - Random number generation
   - Game state management
   - User input validation
   - Difficulty levels
   - Turn-based gameplay

4. **Project: Number Guessing Game**
   - Game rules implementation
   - Difficulty selection
   - Score tracking
   - User feedback
   - ASCII art interface

## Code Examples Explained

### 1. Scope Examples (`day_12_scope.py`)
```python
# Local Scope
def drink_potion():
    potion_strength = 2  # Only accessible inside function
    print(potion_strength)

# Global Scope
player_health = 10  # Accessible everywhere
def use_potion():
    print(player_health)  # Can access global variable
```

### 2. Number Guessing Game (`day_12_number_gassing_game.py`)
```python
# Game Configuration
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """Compare guess with answer and return remaining turns"""
    if guess > answer:
        return turns - 1
    elif guess < answer:
        return turns - 1
    else:
        return turns
```

## Key Takeaways
- Local variables are only accessible within their scope
- Global variables should be used sparingly
- Constants are typically in UPPERCASE
- Game logic benefits from clear scope separation
- User feedback improves game experience

## Next Steps
- Add high score tracking
- Implement different game modes
- Add hints system
- Create difficulty presets
- Add multiplayer mode
- Create GUI version
