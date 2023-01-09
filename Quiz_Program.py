# Quiz Game
import random
from questions import questions

"""create a dictionary in separate file or at top of 
   this program and name it 'questions' the key value
   pairs of 'question': 'answer'"""


marks = {'Correct': 0, 'Incorrect': 0}

"""You can change number to choose the number of questions
   you want selected from your questions dictionary"""
NUMBER = 5


def main():
    print("\nWelcome to my computer quiz!\n")

    playing = ''
    while playing not in ['yes', 'y', 'no', 'n']:
        playing = input('Would you like to play?: ')
        playing = playing.lower()

    if playing in ['yes', 'y']:
        print('Okay lets play!')
    else:
        print('no problem, bye!')
        quit()
    get_questions()
    items = marks.items()
    for item in items:
        print(f"Total {item[0]}", f"Total {item[1]}")
    score = (marks['Correct'] / (marks['Correct'] + marks['Incorrect'])) * 100
    print(f'Your score is: {score}%')


def get_questions(number=NUMBER):
    """randomly chooses 'number' questions from questions
       list and asks them"""
    while number > 0:
        if len(questions) == 0:
            break
        included_questions_list = {}
        included_keys = random.choices(list(questions.keys()), k=1)
        for key in included_keys:
            included_questions_list[key] = questions[key]
            questions.pop(key)
        for q, a in included_questions_list.items():
            q = q.lower()
            a = a.lower()
            ask_question(q, a)
            number -= 1


def ask_question(question, answer):
    """asks a question and checks the user answer
       against the correct answer"""

    get_answer = input(question)
    get_answer = get_answer.lower()
    if get_answer == answer:
        print('Correct!\n')
        marks['Correct'] += 1
    else:
        print('Incorrect!\n')
        marks['Incorrect'] += 1


main()
