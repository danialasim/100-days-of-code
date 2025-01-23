# Day 13 - Debugging: How to Find and Fix Errors in Your Code

## Concepts Learned
1. **Types of Bugs**
   - Syntax Errors
   - Logical Errors
   - Runtime Errors
   - Off-by-One Errors
   - Type Errors

2. **Debugging Techniques**
   - Print Debugging
   - Using a Debugger
   - Reproducing Bugs
   - Playing Computer
   - Error Messages

3. **Common Python Errors**
   - IndexError
   - TypeError
   - ValueError
   - NameError
   - SyntaxError

4. **Project: Debugging Examples**
   - Range Function Issues
   - Random Number Bugs
   - Conditional Logic Errors
   - Type Conversion Problems
   - List Manipulation Bugs

## Code Examples Explained

### 1. Range Function Bug
```python
# Bug: range(1, 20) goes from 1 to 19, missing 20
def my_function():
    for i in range(1, 21):  # Fixed: Changed to include 20
        if i == 20:
            print("You got it")
```

### 2. Random Number Bug
```python
# Bug: randint(1, 6) with 0-based list indexing causes IndexError
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)  # Fixed: Changed range to match list indices
print(dice_imgs[dice_num])
```

### 3. Type Conversion Bug
```python
# Bug: Input returns string, comparison with number fails
age = int(input("How old are you?"))  # Fixed: Added int() conversion
if age > 18:
    print(f"You can drive at age {age}.")  # Fixed: Added f-string
```

## Key Takeaways
- Always read error messages carefully
- Use print statements strategically
- Test edge cases
- Check variable types
- Verify loop boundaries
- Use descriptive variable names
- Break down complex problems

## Debugging Steps
1. Identify the problem
2. Reproduce the bug
3. Evaluate the code
4. Fix the error
5. Test the solution
6. Document the fix

## Next Steps
- Learn to use a Python debugger
- Practice with more complex bugs
- Study common error patterns
- Create debugging checklists
- Learn logging techniques
- Explore automated testing
