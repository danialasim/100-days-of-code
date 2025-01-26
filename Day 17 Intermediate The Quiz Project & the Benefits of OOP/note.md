# Day 17 - Quiz Project & OOP Benefits

## Concepts Learned
1. **Object-Oriented Programming**
   - Classes and Objects
   - Constructors
   - Attributes
   - Methods
   - Encapsulation

2. **Class Design**
   - Class attributes
   - Instance methods
   - Constructor parameters
   - Object initialization
   - Method parameters

3. **Project Structure**
   - Module organization
   - Data separation
   - Model-View separation
   - Business logic

4. **Project: Quiz Game**
   - Question model
   - Quiz brain logic
   - Data management
   - Score tracking
   - User interaction

## Code Structure
### 1. Question Model (`day_17_question_model.py`)
```python
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

### 2. Quiz Brain (`day_17_quiz_brain.py`)
```python
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
```

## Key Components
1. **Question Class**
   - Stores question text
   - Stores correct answer
   - Simple data model

2. **QuizBrain Class**
   - Manages quiz state
   - Tracks score
   - Handles user input
   - Validates answers

3. **Data Module**
   - Stores question bank
   - Easy to modify/extend
   - Separation of concerns

## Key Takeaways
- OOP improves code organization
- Classes encapsulate related data
- Methods provide behavior
- Separation of concerns
- Modular design

## Program Features
1. Multiple questions
2. Score tracking
3. Input validation
4. Progress tracking
5. Final score display
6. Clean interface

## Next Steps
- Add categories
- Add difficulty levels
- Add time limits
- Save high scores
- Add multiplayer
- Create GUI version
