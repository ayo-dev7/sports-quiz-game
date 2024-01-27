from question_model import Question
from data import question_data
import random
from quiz_game import QuizGame

# Initialize an empty list to store Question objects
question_list = []

# Iterate through the question data and create Question objects
for item in question_data:
    q = item["question"]  # Extract the question text
    a = item["correct_answer"]  # Extract the correct answer
    o = item["incorrect_answers"]  # Extract the incorrect answer options
    o.append(item["correct_answer"])  # Add the correct answer to the options
    random.shuffle(o)  # Shuffle the options randomly
    question_list.append(Question(q, o, a))  # Create a Question object and add it to the list

# Create a QuizGame object with the list of questions
quiz = QuizGame(question_list)

# Start the quiz loop
while quiz.questions_left():
    quiz.display_question()  # Display questions and handle user input

