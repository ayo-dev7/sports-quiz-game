class Question:
    # Initialize our Question object with attributes
    def __init__(self, text, options, answer):
        # Assign the question text, answer options, and correct answer to instance variables
        self.text = text  # The text of the question
        self.options = options  # A list of answer options
        self.answer = answer  # The correct answer to the question

