from random import randint


MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_numbers():
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


def find_gcd(a, b):
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


def game_quiz_and_answer():
    a, b = generate_numbers()
    question = f'{a} {b}'
    right_answer = str(find_gcd(a, b))
    return (question, right_answer)
