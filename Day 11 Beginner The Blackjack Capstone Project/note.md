# Day 11 - Blackjack Capstone Project

## Concepts Learned
1. **Game Logic**
   - Card dealing
   - Score calculation
   - Game state management
   - Win/lose conditions

2. **Functions and Returns**
   - Function composition
   - Return values
   - Early returns
   - Conditional logic

3. **List Operations**
   - List manipulation
   - Random selection
   - List comprehension
   - Score tracking

4. **Project: Blackjack**
   - Game rules implementation
   - Player interaction
   - Computer AI
   - ASCII art interface

## Code Examples Explained

### 1. Card Dealing (`day_11_black_jack.py`)
```python
def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
```

### 2. Score Calculation
```python
def calculate_score(cards):
    """Calculate score from a list of cards."""
    # Check for blackjack (0)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
        
    # Handle ace (11/1)
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)
```

### 3. Game Logic
```python
def play_game():
    # Initial setup
    user_cards = []
    computer_cards = []
    
    # Deal initial cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    # Game loop
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
```

## Key Takeaways
- Complex game logic requires careful planning
- Functions should have single responsibilities
- Early returns simplify code flow
- User experience is important
- ASCII art enhances presentation
- Error handling is crucial

## Next Steps
- Add betting system
- Support multiple players
- Add card counting
- Implement split hands
- Add save/load game
- Create GUI version
