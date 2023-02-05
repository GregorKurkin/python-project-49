from random import randint


def if_even(question_number):
    if question_number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def game_task():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    return task


def game_logik():
    question_number = randint(-1000, 1000)
    question = f'Question: {question_number}'
    func_result = if_even(question_number)
    return (question, func_result)
