import prompt
from random import randint


def progression_func(start=1, lenght=10, step=2):
    progression = []
    elem = start
    for _ in range(lenght):
        progression.append(str(elem))
        elem += step
    return progression


def game_task():
    task = 'What number is missing in the progression?'
    return task


def game_logik():
    lenght = randint(5, 15)
    start = randint(1, 25)
    step = randint(2, 10)
    hidden_index = randint(0, lenght - 1)
    progression = progression_func(start, lenght, step)
    hidden_elem = progression[hidden_index]
    progression[hidden_index] = '..'
    question = f"Question: {' '.join(progression)}"
    func_result = hidden_elem
    return (question, func_result)
