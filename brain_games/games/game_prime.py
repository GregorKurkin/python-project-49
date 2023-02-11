from random import randint


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


def game_logik():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    number = randint(MIN_NUMBER, MAX_NUMBER)
    func_result = (is_prime(number) and 'yes' or 'no')
    return (number, func_result)
