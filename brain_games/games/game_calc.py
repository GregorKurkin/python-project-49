from random import randint, choice
import operator


MIN_NUMBER = 0
MAX_NUMBER = 15


def calc(a, used_operator, b):
    operators_dict = {'+': operator.add(a, b),
                      '-': operator.sub(a, b),
                      '*': operator.mul(a, b)}
    return operators_dict[used_operator]


def game_task():
    task = 'What is the result of the expression?'
    return task


def game_quiz_and_answer():
    a = randint(MIN_NUMBER, MAX_NUMBER)
    b = randint(MIN_NUMBER, MAX_NUMBER)
    operators = '+-*'
    used_operator = choice(operators)
    question = f'{a} {used_operator} {b}'
    right_answer = str(calc(a, used_operator, b))
    return (question, right_answer)
