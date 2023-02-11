from random import randint


def is_even(question_number):
    return question_number % 2 == 0


def game_task():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    return task


def game_logik():
    MIN_NUMBER = 0
    MAX_NUMBER = 1000
    question = randint(MIN_NUMBER, MAX_NUMBER)
    func_result = (is_even(question) and 'yes' or 'no')
    return (question, func_result)
