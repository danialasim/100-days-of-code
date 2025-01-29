# Day 19 - Instances, State and Higher Order Functions

## Concepts Learned
1. **Higher Order Functions**
   - Functions as arguments
   - Event listeners
   - Callback functions
   - Function passing

2. **Instance State**
   - Object instances
   - State management
   - Multiple objects
   - Object coordination

3. **Event Handling**
   - Key events
   - Mouse events
   - Event binding
   - User input

4. **Projects**
   - Etch-A-Sketch
   - Turtle Race Game
   - Event Listeners Demo

## Code Structure
### 1. Event Handling
```python
def move_forward():
    turtle.forward(10)

screen.onkey(key="space", fun=move_forward)
screen.listen()
```

### 2. Multiple Instances
```python
all_turtles = []
for i in range(6):
    new_turtle = Turtle()
    all_turtles.append(new_turtle)
```

## Key Components
1. **Event Listeners**
   - Key bindings
   - Mouse events
   - Screen setup
   - Event loops

2. **Turtle Control**
   - Movement
   - Direction
   - State tracking
   - Screen bounds

3. **Game Logic**
   - Race conditions
   - Random movement
   - Winner detection
   - User betting

## Key Takeaways
- Functions as arguments
- Object state management
- Event-driven programming
- Multiple object control
- Game design basics

## Program Features
1. Keyboard control
2. Drawing capabilities
3. Race simulation
4. Betting system
5. Multiple turtles
6. Random movement

## Next Steps
- Add more game modes
- Implement scoring
- Add obstacles
- Create power-ups
- Save drawings
- Add multiplayer
