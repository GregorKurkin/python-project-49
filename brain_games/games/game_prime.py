from random import randint


def is_prime(number):
    if number != 1:
        for num in range(2, number // 2 + 1):
            if number % num == 0:
                return 'no'
        return 'yes'
    else:
        return 'yes'


def game_task():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return task


def game_logik():
    number = randint(1, 100)
    # question = f"Question: {number}"
    func_result = is_prime(number)
    return (number, func_result)
