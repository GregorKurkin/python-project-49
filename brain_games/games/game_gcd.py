import prompt
from random import choice
from brain_games.functions import not_prime, num_divisor, max_divisor_list


def game_gcd():
    numbers = not_prime()  # список составных чисел
    divisors_list = num_divisor(numbers)  # список из (число, {делители})
    pair, divisor = choice(max_divisor_list(divisors_list))
    a, b = pair
    print(f'Question: {a} {b}')
    func_result = divisor
    answer = prompt.string('Your answer: ')
    return (answer, func_result)
