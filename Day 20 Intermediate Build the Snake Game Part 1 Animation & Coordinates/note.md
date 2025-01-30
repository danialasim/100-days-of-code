# Day 20 - Snake Game Part 1: Animation & Coordinates

## Concepts Learned
1. **Screen Setup and Animation**
   - Screen dimensions
   - Background color
   - Screen tracer
   - Screen update
   - Animation control

2. **Object-Oriented Programming**
   - Class creation
   - Object instances
   - Methods and attributes
   - Inheritance
   - Encapsulation

3. **Coordinate System**
   - X and Y coordinates
   - Movement vectors
   - Heading angles
   - Position tracking
   - Boundary detection

4. **Game Development Concepts**
   - Game loop
   - Event handling
   - Collision detection
   - State management
   - Score tracking

## Code Structure
### 1. Snake Class
```python
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
```

### 2. Game Loop
```python
while game_is_on:
    screen.update()
    snake.move()
    # Collision detection
    # Score updates
```

## Key Components
1. **Snake Class**
   - Segment management
   - Movement control
   - Direction handling
   - Growth mechanics

2. **Game Control**
   - Screen setup
   - Event binding
   - Game loop
   - State tracking

3. **Movement System**
   - Direction constants
   - Position updates
   - Segment following
   - Boundary checks

## Program Features
1. Snake movement
2. Keyboard control
3. Snake growth
4. Wall collision
5. Self collision
6. Score tracking

## Implementation Details
1. **Screen Setup**
   - 600x600 window
   - Black background
   - Title display
   - Animation control

2. **Snake Movement**
   - 20-pixel steps
   - 90-degree turns
   - Segment following
   - Direction constraints

3. **Game Logic**
   - Continuous movement
   - Collision checks
   - Score updates
   - Game over conditions

## Next Steps
1. Add food system
2. Implement scoring
3. Add sound effects
4. Create high score
5. Add difficulty levels
6. Create start menu
7. Add pause feature
8. Implement game restart
