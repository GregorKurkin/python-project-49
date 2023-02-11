from random import randint, choice
import operator


def calc(a, used_operator, b):
    operators_dict = {'+': operator.add(a, b),
                      '-': operator.sub(a, b),
                      '*': operator.mul(a, b)}
    return operators_dict[used_operator]


def game_task():
    task = 'What is the result of the expression?'
    return task


def game_logik():
    a = randint(0, 10)
    b = randint(0, 10)
    operators = '+-*'
    used_operator = choice(operators)
    question = f'{a} {used_operator} {b}'
    func_result = str(calc(a, used_operator, b))
    return (question, func_result)
