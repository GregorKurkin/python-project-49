from random import choice


def not_prime(num_range=100):
    # 1. создает список составных чисел в диапазоне
    not_prime_list_ = []
    for i in range(4, num_range + 1):
        for c in range(2, (i // 2 + 1)):
            if i % c == 0:
                not_prime_list_.append(i)
                break
    return not_prime_list_


def num_divisor(numbers):
    # принимает список составных чисел
    # возвращает список кортежей (число, {делители})
    list_num_divisors = []
    for num in numbers:
        divisors = {i for i in range(2, (num // 2 + 1)) if num % i == 0}
        list_num_divisors.append((num, divisors))
    return list_num_divisors


def max_divisor_list(divisors_list):
    # принимает список пар
    # 3. находим пары чисел с общими делителями с помощью пересечения множеств.
    #    создаем список элементов ((пара чисел), максимальный общий делитель)
    pairs_max_divisor_list = []
    for index_ in range(len(divisors_list) - 1):
        for next_index in range(index_ + 1, len(divisors_list)):
            common_set = (divisors_list[index_][1]
                          & divisors_list[next_index][1])
            if common_set:
                pair_max_divisor = (
                    (divisors_list[index_][0],
                     divisors_list[next_index][0]), max(common_set))
                pairs_max_divisor_list.append(pair_max_divisor)
    return pairs_max_divisor_list


def game_task():
    task = 'Find the greatest common divisor of given numbers.'
    return task


def game_logik():
    numbers = not_prime()  # список составных чисел
    divisors_list = num_divisor(numbers)  # список из (число, {делители})
    pair, divisor = choice(max_divisor_list(divisors_list))
    a, b = pair
    question = f'Question: {a} {b}'
    func_result = str(divisor)
    return (question, func_result)
