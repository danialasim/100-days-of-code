# Day 17 - Question Model
# This module defines the Question class for the quiz game

class Question:
    """
    A class representing a quiz question.
    
    Attributes:
        text (str): The question text
        answer (str): The correct answer
    """
    
    def __init__(self, q_text, q_answer):
        """
        Initialize a new Question.
        
        Args:
            q_text (str): The question text
            q_answer (str): The correct answer
        """
        self.text = q_text
        self.answer = q_answer
