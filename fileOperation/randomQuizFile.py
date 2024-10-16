# Here is what the program does:
#   Creates 35 different quizzes
#   Creates 50 multiple-choice questions for each quiz, in random order
#   Provides the correct answer and three random wrong answers for each question, in random order
#   Writes the quizzes to 35 text files
#   Writes the answer keys to 35 text files
# This means the code will need to do the following:
#   Store the states and their capitals in a dictionary
#   Call open(), write(), and close() for the quiz and answer key text files
#   Use random.shuffle() to randomize the order of the questions and multiple-choice options

#! python3
# randomQuizFile.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random
import os
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
    'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
    'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
    'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
    'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
    'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# Generate 35 quiz files.
num_quizzes = 35
num_questions = 50
os.makedirs('quizzes', exist_ok = True)
os.makedirs('answers', exist_ok = True)
for quizNum in range(1, num_quizzes + 1):
    # TODO: Create the quiz and answer key files
    quiz_filename = f'quizzes/capitalsquiz{quizNum}.txt'
    answer_key_filename = f'answers/capitalsquiz_answers{quizNum}.txt'
    with open(quiz_filename, 'w') as quizFile, open(answer_key_filename, 'w') as answerKeyFile:
        # TODO: Write out the head for the quiz.
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write((' ' * 20) + f'State Capitals Quiz (Form {quizNum})')
        quizFile.write('\n\n')
        # TODO: Shuffle the order of the states.
        states = list(capitals.keys())
        random.shuffle(states)
        # TODO: Loop through all 50 states, making a question for each.
        for questionNum in range(num_questions):
            state = states[questionNum]
            correctAnswer = capitals[state]
            wrongAnswers = list(capitals.values())
            wrongAnswers.remove(correctAnswer)
            wrongAnswers = random.sample(wrongAnswers, 3)
            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)
            # TODO: Write the question and answer options to the quiz file.
            quizFile.write(f'{questionNum + 1}. What is the capital of {state}?\n')
            for i in range(4):
                quizFile.write(f"\t{'ABCD'[i]}. { answerOptions[i]}\n")
            quizFile.write('\n')
            # TODO: Write the answer key to a file.
            correct_option = 'ABCD'[answerOptions.index(correctAnswer)]
            answerKeyFile.write(f"{questionNum + 1}. {correct_option}\n")
