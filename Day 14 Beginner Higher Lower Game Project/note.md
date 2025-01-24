# Day 14 - Higher Lower Game Project

## Concepts Learned
1. **Data Structures**
   - Dictionaries
   - Lists of dictionaries
   - Nested data structures
   - Data organization

2. **Game Logic**
   - Comparison operations
   - Score tracking
   - Random selection
   - Game state management

3. **User Interface**
   - Clear screen operations
   - ASCII art
   - User input handling
   - Game flow control

4. **Project: Higher Lower Game**
   - Social media comparison game
   - Follower count comparison
   - Score tracking
   - Continuous gameplay

## Code Structure
### 1. Data Module (`day_14_higher_lower_data.py`)
```python
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    # More entries...
]
```

### 2. Game Logic
```python
def check_answer(guess, a_followers, b_followers):
    """Check if user's guess is correct"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
```

## Key Takeaways
- Data organization is crucial
- Clean user interface improves experience
- Clear game rules are important
- Score tracking adds engagement
- Random selection adds variety

## Game Features
1. Random celebrity selection
2. Follower count comparison
3. Score tracking
4. Continuous play option
5. Clear screen between rounds
6. ASCII art interface

## Next Steps
- Add difficulty levels
- Include more celebrities
- Add categories (musicians, athletes, etc.)
- Save high scores
- Add multiplayer mode
- Create GUI version
