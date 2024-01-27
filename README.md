# Sports Quiz Game

Welcome to the Sports Quiz Game repository! This project allows you to create and play a fun and interactive quiz game focused on sports-related questions. Players can test their knowledge of sports by answering multiple-choice questions.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Game Mechanics](#game-mechanics)
- [Contributing](#contributing)

## Introduction

The Sports Quiz Game is a Python-based project that allows users to play a quiz game focused on sports-related questions. It includes a set of sports-related questions with multiple-choice answers. The game presents questions one at a time and provides feedback on whether the answers are correct or incorrect.

## Project Structure

The project is structured as follows:

- `question_model.py`: Defines the Question class, which represents a single quiz question with its text, answer options, and correct answer.
- `data.py`: Contains the question data in a list of dictionaries. Each dictionary includes the question text, correct answer, and incorrect answer options.
- `quiz_game.py`: Defines the QuizGame class, which manages the game's logic, including question selection, user input, and scoring.
- `main.py`: The main script to run the sports quiz game.
- `README.md`: The documentation file you are currently reading.

## Getting Started

To get started with the Sports Quiz Game, follow the steps below.

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository to your local machine using the following command:

   ```shell
   git clone https://github.com/yourusername/sports-quiz-game.git
2. Navigate to the project directory:
    
    ```shell
    cd sports-quiz-game
3. Run the game by executing the main.py script:
    
    ```shell
    python main.py

## Usage
Once you've launched the game, you can start playing immediately. Answer each question to the best of your knowledge, and the game will provide feedback on whether your answer is correct or not. The game keeps track of your score and displays it at the end.

### Game Mechanics
The game mechanics are as follows:
- You will be presented with a series of sports-related questions.
- For each question, you can choose one of the provided answer options.
- If your answer is correct, you will receive a "Correct answer" message.
- If your answer is incorrect, you will receive an "Incorrect answer" message along with the correct answer.
- Your total score will be displayed at the end of the game.

![Screenshot 1](/sports-screenshot.png)

## Contributing
Contributions to the Sports Quiz Game project are welcome! If you have ideas for improvements or new features, please create a pull request. For major changes, please open an issue first to discuss your ideas.

Enjoy playing the Sports Quiz Game, and have fun testing your sports knowledge! If you encounter any issues or have suggestions for improvement, please feel free to contribute or report issues.
