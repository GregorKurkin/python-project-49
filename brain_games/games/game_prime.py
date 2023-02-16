from random import randint


MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    if number <= 2:
        return True
    else:
        for num in range(2, number // 2 + 1):
            if number % num == 0:
                return False
        return True


def game_task():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return task


def game_quiz_and_answer():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    right_answer = (is_prime(number) and 'yes' or 'no')
    return (number, right_answer)
