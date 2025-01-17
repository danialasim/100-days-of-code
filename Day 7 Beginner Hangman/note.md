# Day 7 - Hangman Game

## Concepts Learned
1. **Module Organization**
   - Separating code into multiple files
   - Importing custom modules
   - Code organization best practices

2. **Game Logic**
   - Loop control with boolean flags
   - String manipulation
   - List operations
   - User input handling

3. **ASCII Art**
   - Multi-line strings
   - Raw strings (r-strings)
   - Visual game elements
   - Console display management

4. **Project Structure**
   - Main game logic (`day_7_hnagman.py`)
   - Word list module (`day_7_hangman_words.py`)
   - Art assets module (`day_7_hangman_art.py`)

## Code Examples Explained

### 1. Game Setup (`day_7_hnagman.py`)
```python
# Import required modules
from day_7_hangman_words import word_list
from day_7_hangman_art import logo, stages

# Initialize game
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
display = ["_" for _ in range(word_length)]
```

### 2. Game Logic
```python
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    # Check if letter was already guessed
    if guess in display:
        print(f"You already guessed {guess}")
        
    # Update display with correct guesses
    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess
```

### 3. ASCII Art Management (`day_7_hangman_art.py`)
```python
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', ...]  # Multiple stages for different lives

logo = r''' 
 _                                             
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
...
'''
```

## Key Takeaways
- Code organization improves maintainability
- Modular design makes code reusable
- ASCII art enhances user experience
- Game logic requires careful state management
- Input validation is crucial
- Clear user feedback improves gameplay

## Next Steps
- Add difficulty levels
- Implement score tracking
- Add word categories
- Create a word hint system
- Improve user interface
- Add multiplayer functionality
