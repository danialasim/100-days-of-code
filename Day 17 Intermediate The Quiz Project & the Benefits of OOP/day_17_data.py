# Day 17 - Quiz Data
# This module contains the question bank for the quiz game

#--------------------
# Question Bank
#--------------------

# List of dictionaries containing questions and answers
# Each question has:
# - type: Question type (boolean)
# - difficulty: Question difficulty level
# - category: Question category
# - question: The actual question text
# - correct_answer: The correct answer
# - incorrect_answers: List of wrong answers

question_data = [
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "RAM stands for Random Access Memory.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "The Nvidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "The Windows ME operating system was released in the year 2000.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "Linus Torvalds created Linux and Git.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "The logo for Snapchat is a Bell.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "Ada Lovelace is often considered the first computer programmer.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    }
]

# Data structure:
# - All questions are boolean (True/False)
# - All questions are computer science related
# - All questions are easy difficulty
# - Each question has one correct and one incorrect answer

# Usage:
# 1. Import this module in the main game
# 2. Use question_data to create Question objects
# 3. Build question bank for QuizBrain
