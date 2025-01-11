# Day 2 - Mathematical Operations in Python
# This file demonstrates basic math operations and their order of precedence

#--------------------
# Basic Operations
#--------------------

3 + 5  # Addition
7 - 4  # Subtraction
3 * 2  # Multiplication
6 / 3  # Division (always returns float)
2**3   # Exponentiation (2 to the power of 3)

#--------------------
# Order of Operations
#--------------------

# PEMDAS Rule in Mathematics:
# P - Parentheses ()
# E - Exponents **
# M - Multiplication *
# D - Division /
# A - Addition +
# S - Subtraction -

# Python's Order of Operations:
# 1. Parentheses ()
# 2. Exponents **
# 3. Multiplication and Division (*, /) - Left to right
# 4. Addition and Subtraction (+, -) - Left to right

# Example calculations
print(3 * 3 + 3 / 3 - 3)  # Will follow order of operations
print((3 * 3) + (3 / 3) - 3)  # Same calculation with explicit parentheses