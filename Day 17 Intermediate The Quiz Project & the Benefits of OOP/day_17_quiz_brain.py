# Day 17 - Quiz Brain
# This module contains the QuizBrain class that manages the quiz game logic

class QuizBrain:
    """
    A class to manage quiz game logic.
    
    Attributes:
        question_number (int): Current question number
        question_list (list): List of Question objects
        score (int): Current user score
    """
    
    def __init__(self, q_list):
        """
        Initialize a new QuizBrain.
        
        Args:
            q_list (list): List of Question objects
        """
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        """
        Check if there are more questions.
        
        Returns:
            bool: True if more questions remain, False otherwise
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Present the next question to the user and process their answer.
        Gets user input and calls check_answer to validate.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        Check if the user's answer is correct.
        
        Args:
            user_answer (str): The user's answer
            correct_answer (str): The correct answer
            
        Updates the score and provides feedback to the user.
        """
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
