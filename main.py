#! python3
# To see how much PyInputPlus is doing for you,
# try re-creating the multiplication quiz project on your own without importing it.
# This program will prompt the user with 10 multiplication questions, ranging from 0 × 0 to 9 × 9.
# You’ll need to implement the following features:
#   If the user enters the correct answer,
#       the program displays “Correct!” for 1 second and moves on to the next question.
#   The user gets three tries to enter the correct answer
#       before the program moves on to the next question.
#   Eight seconds after first displaying the question,
#       the question is marked as incorrect even if the user enters the correct answer
#       after the 8-second limit.

import random
import time


# Function to handle each multiplication question
def ask_question():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    correct_answer = num1 * num2
    attempts = 0
    start_time = time.time()

    while attempts < 3:
        try:
            answer = int(input(f"What is {num1} x {num2}? "))
            elapsed_time = time.time() - start_time

            # Check for time limit of 8 seconds
            if elapsed_time > 8:
                print("Time's up! Moving to the next question.")
                return False

            if answer == correct_answer:
                print("Correct!")
                time.sleep(1)  # Wait for 1 second before moving to the next question
                return True
            else:
                attempts += 1
                print(f"Incorrect. {3 - attempts} attempt(s) left.")

        except ValueError:
            print("Please enter a valid number.")

    print(f"Out of attempts! The correct answer was {correct_answer}.")
    return False


# Main function for the quiz
def multiplication_quiz():
    print("Welcome to the multiplication quiz! You have 3 attempts and 8 seconds per question.")
    score = 0

    for _ in range(10):
        if ask_question():
            score += 1

    print(f"\nQuiz complete! Your score is {score}/10.")


# Start the quiz
multiplication_quiz()
