# Day 17 - Quiz Game Main
# This is the main module that runs the quiz game

#--------------------
# Imports
#--------------------

from day_17_data import question_data        # Import question bank
from day_17_question_model import Question   # Import Question class
from day_17_quiz_brain import QuizBrain     # Import QuizBrain class

#--------------------
# Setup
#--------------------

# Create question bank from data
question_bank = []
for question in question_data:
    # Extract question and answer from data
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # Create Question object and add to bank
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create quiz instance
quiz = QuizBrain(question_bank)

#--------------------
# Game Loop
#--------------------

# Continue asking questions while available
while quiz.still_has_question():
    quiz.next_question()

# Display final score
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
