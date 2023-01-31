import prompt
from random import randint
from brain_games.functions import if_even


def game_even():
    question_number = randint(-1000, 1000)
    print(f'Question: {question_number}')
    answer = prompt.string('Your answer: ')
    func_result = if_even(question_number)
    return (answer, func_result)
