# Day 8 - Function Parameters & Caesar Cipher

## Concepts Learned
1. **Function Parameters**
   - Function definition
   - Positional arguments
   - Keyword arguments
   - Default parameters
   - Multiple parameters

2. **String Manipulation**
   - String indexing
   - String methods
   - Character handling
   - ASCII art

3. **List Operations**
   - List indexing
   - List methods
   - Modular arithmetic
   - Character shifting

4. **Project: Caesar Cipher**
   - Text encryption/decryption
   - Input validation
   - Program flow control
   - User interface design

## Code Examples Explained

### 1. Function Parameters (`day_8_function_with_input.py`)
```python
# Simple function without parameters
def greet():
    print("Hello")

# Function with one parameter
def greet_with_name(name):
    print(f"Hello {name}!")

# Function with multiple parameters
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}")
```

### 2. Caesar Cipher Implementation (`day_8_caesar_cipher.py`)
```python
def caesar(start_text, shift_amount, cipher_direction):
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
```

### 3. Program Flow Control
```python
# Main program loop
while not should_end:
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    
    caesar(text, shift, direction)
    
    restart = input("Type 'yes' to go again, 'no' to end:\n")
    if restart == "no":
        should_end = True
```

## Key Takeaways
- Functions make code reusable and organized
- Parameters allow functions to be flexible
- Input validation is crucial for user interaction
- Modular arithmetic helps handle circular shifts
- ASCII art enhances user experience
- While loops enable program repetition

## Next Steps
- Explore more complex encryption methods
- Add file input/output capabilities
- Implement error handling
- Create a graphical user interface
- Support multiple languages
- Add additional cipher algorithms
