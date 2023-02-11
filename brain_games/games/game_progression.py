from random import randint


def progression_func(initial_term=1, number_of_terms=10, common_difference=2):
    progression = []
    elem = initial_term
    for _ in range(number_of_terms):
        progression.append(str(elem))
        elem += common_difference
    return progression


def game_task():
    task = 'What number is missing in the progression?'
    return task


def game_logik():
    number_of_terms = randint(5, 15)
    initial_term = randint(1, 25)
    common_difference = randint(2, 10)
    hidden_index = randint(0, number_of_terms - 1)
    progression = progression_func(initial_term, number_of_terms, common_difference)
    hidden_elem = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(progression)
    func_result = hidden_elem
    return (question, func_result)
