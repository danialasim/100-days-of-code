# Day 8 - Caesar Cipher
# A program that implements the Caesar Cipher encryption/decryption technique

#--------------------
# Imports and Setup
#--------------------

from day_8_caesar_cipher_art import logo

# Create alphabet list with duplicates for easy wrapping
# The list is duplicated to handle positive shifts without using modulo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#--------------------
# Cipher Function
#--------------------

def caesar(start_text, shift_amount, cipher_direction):
    """
    Encrypts or decrypts text using the Caesar Cipher technique.
    
    Args:
        start_text (str): The text to encrypt/decrypt
        shift_amount (int): Number of positions to shift each letter
        cipher_direction (str): Either 'encode' or 'decode'
    """
    end_text = ""
    # Reverse shift direction for decoding
    if cipher_direction == "decode":
        shift_amount *= -1
    
    # Process each character in the text
    for char in start_text:
        if char in alphabet:
            # Find the character's position and shift it
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            # Keep non-alphabet characters unchanged
            end_text += char
            
    print(f"Here's the {cipher_direction}d result: {end_text}")

#--------------------
# Main Program
#--------------------

# Display the program logo
print(logo)

# Main program loop
should_end = False
while not should_end:
    # Get user inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    # Handle large shift numbers using modulo
    # This ensures shift stays within alphabet range (0-25)
    shift = shift % 26
    
    # Process the text
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    # Ask if user wants to continue
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
