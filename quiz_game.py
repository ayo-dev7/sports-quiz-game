class QuizGame:
    # Initialize the QuizGame with a question bank, question number, score, and flag
    def __init__(self, question_bank):
        self.question_bank = question_bank
        self.question_number = 0
        self.score = 0
        self.flag = True  # The flag to control the game state

    def questions_left(self):
        # Check if there are more questions left to answer
        if self.question_number < len(self.question_bank) and self.flag:
            return True
        else:
            print("End of quiz.")
            if not self.flag:
                print(f"Your final score is: {self.score}/{len(self.question_bank)}.")
            else:
                print(f"Your final score is: {self.score}/{self.question_number}.")
            return False

    def display_question(self):
        # Display questions and handle user input
        print("Enter 'end' at any point you want to exit the game.")
        while True:
            question = self.question_bank[self.question_number]
            self.question_number += 1
            your_answer = input(f"Q{self.question_number}. {question.text} "
                         f"Options: ({question.options}):")
            if your_answer.lower() == 'end':
                self.flag = False  # Set the flag to exit the game
                break  # Exit the loop when 'end' is entered
            elif your_answer in question.options:
                self.check_answer(your_answer, question.answer)
                break
            else:
                self.question_number -= 1
                print("Your answer is not in the list of options. Please try again.")

    def check_answer(self, your_answer, question_answer):
        # Check if the answer provided by the user is correct
        if your_answer.lower() == question_answer.lower():
            print("Correct answer")
            self.score += 1
        else:
            print("Incorrect answer")
        print(f"The correct answer is: {question_answer}.")
        print(f"The correct score is: {self.score}/{self.question_number}")
        print("\n")
