import prompt
from random import randint
from brain_games.functions import is_prime


def game_prime():
    number = randint(1, 100)
    print(f"Question: {number}")
    func_result = is_prime(number)
    answer = prompt.string('Your answer: ')
    return (answer, func_result)
