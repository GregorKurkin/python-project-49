import prompt
from random import randint
from brain_games.functions import progression_func


def game_progression():
    lenght = randint(5, 15)
    start = randint(1, 25)
    step = randint(2, 10)
    hidden_index = randint(0, lenght - 1)
    progression = progression_func(start, lenght, step)
    hidden_elem = progression[hidden_index]
    progression[hidden_index] = '..'
    print(f"Question: {' '.join(progression)}")
    func_result = hidden_elem
    answer = prompt.string('Your answer: ')
    return (answer, func_result)
