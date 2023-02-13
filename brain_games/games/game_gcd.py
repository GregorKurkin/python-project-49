from random import randint


def generate_numbers():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    a = randint(MIN_NUMBER, MAX_NUMBER)
    b = randint(MIN_NUMBER, MAX_NUMBER)
    if a == b:
        while a == b:
            a = randint(MIN_NUMBER, MAX_NUMBER)
            b = randint(MIN_NUMBER, MAX_NUMBER)
    return a, b


def game_task():
    task = 'Find the greatest common divisor of given numbers.'
    return task


def find_nod(a, b):
    if b > a:
        a, b = b, a
    dividend = a
    divisor = b
    remainder = dividend % divisor
    while remainder != 0:
        dividend = divisor
        divisor = remainder
        remainder = dividend % divisor
    return divisor


def game_logik():
    a, b = generate_numbers()
    question = f'{a} {b}'
    func_result = str(find_nod(a, b))
    return (question, func_result)
