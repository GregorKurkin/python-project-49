import prompt
from random import randint, choice
from brain_games.functions import calc


def game_calc():
    a = randint(0, 10)
    b = randint(0, 10)
    operators = '+-*'
    used_operator = choice(operators)
    print(f'Question: {a} {used_operator} {b}')
    func_result = calc(a, used_operator, b)
    answer = int(prompt.string('Your answer: '))
    return (answer, func_result)
