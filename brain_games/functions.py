import operator


def if_even(question_number):
    if question_number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def calc(a, used_operator, b):
    operators_dict = {'+': operator.add(a, b),
                      '-': operator.sub(a, b),
                      '*': operator.mul(a, b)}
    return operators_dict[used_operator]


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


def progression_func(start=1, lenght=10, step=2):
    progression = []
    elem = start
    for _ in range(lenght):
        progression.append(str(elem))
        elem += step
    return progression


def is_prime(number):
    if number != 1:
        for num in range(2, number // 2 + 1):
            if number % num == 0:
                return 'no'
        return 'yes'
    else:
        return 'yes'
