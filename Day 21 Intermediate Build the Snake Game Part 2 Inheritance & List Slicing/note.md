# Day 21 - Snake Game Part 2: Inheritance & List Slicing

## Key Concepts

### 1. Class Inheritance
Demonstrated in `day_21_class_inheritance.py`:
```python
class Animal:
    def __init__(self):
        self.num_eyes = 2

class Fish(Animal):  # Fish inherits from Animal
    def __init__(self):
        super().__init__()  # Call parent's init
```

Key points:
- Child class inherits attributes and methods from parent
- `super().__init__()` calls parent's initialization
- Methods can be overridden in child class
- Child can add new methods

### 2. List Slicing
Shown in `day_21_slicing.py`:
```python
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_keys[2:5])  # Prints: ["c", "d", "e"]
print(piano_keys[2:])   # From index 2 to end
print(piano_keys[:5])   # From start to index 4
print(piano_keys[::2])  # Every second item
```

### 3. Snake Game Enhancements

#### Food Class (`day_21_snake_food.py`)
- Inherits from Turtle
- Creates food at random positions
- Handles collision detection with snake

#### Scoreboard Class (`day_21_snake_scoreboard.py`)
- Inherits from Turtle
- Displays and updates score
- Shows game over message
- Uses constants for alignment and font

## Game Components

### 1. Snake Class (from Day 20)
- Handles snake movement and growth
- Manages snake segments
- Controls direction changes
- Prevents reverse movement

### 2. Food Class
```python
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.refresh()  # Place food randomly
```

### 3. Scoreboard Class
```python
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.update_scoreboard()
```

## Game Mechanics

### 1. Collision Detection
- With food: Distance < 15 pixels
- With walls: x/y coordinate > 280 or < -280
- With tail: Distance < 10 pixels with any segment

### 2. Score System
- Score increases when food is eaten
- Score displayed at top of screen
- Game over shown when collision occurs

### 3. Movement
- Continuous movement in current direction
- Direction changes through arrow keys
- Snake grows when eating food
- Tail follows head's path

## Code Structure

### Main Game Loop
1. Move snake
2. Check food collision
3. Check wall collision
4. Check tail collision
5. Update screen
6. Repeat

### Class Hierarchy
```
Turtle (built-in)
├── Snake
├── Food
└── Scoreboard
```

## Key Takeaways
1. Inheritance reduces code duplication
2. List slicing provides powerful data manipulation
3. Class structure improves code organization
4. Collision detection using distance calculation
5. Game loop timing affects difficulty

## Next Steps
1. Add high score system
2. Implement difficulty levels
3. Add sound effects
4. Create start menu
5. Add pause functionality
6. Implement boundary wrapping
7. Add power-ups
8. Create level system
