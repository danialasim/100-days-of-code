# Example of Class Inheritance in Python
# Demonstrates how a child class can inherit and extend parent class functionality

class Animal:
    """Parent class representing basic animal attributes and behaviors."""
    def __init__(self):
        self.num_eyes = 2  # All animals have 2 eyes by default

    def breathe(self):
        """Basic breathing method for all animals."""
        print("Inhale, exhale.")

class Fish(Animal):  # Fish inherits from Animal
    """Child class representing specific fish attributes and behaviors."""
    def __init__(self):
        super().__init__()  # Initialize parent class attributes

    def breathe(self):
        """Override parent's breathe method but still use it."""
        super().breathe()  # Call parent's breathe method
        print("doing this underwater.")  # Add fish-specific behavior

    def swim(self):
        """Fish-specific method not present in parent class."""
        print("moving in water.")

# Create and test a Fish object
nemo = Fish()
nemo.breathe()  # Will print both parent and child breathe messages