from random import randint


MIN_NUMBER = 5
MAX_NUMBER = 15
MIN_TERM = 1
MAX_TERM = 25
MIN_DIFFERENCE = 2
MAX_DIFFERENCE = 10


def list_to_string(list_):
    list_of_strings = list(map(str, list_))
    # list_of_strings = [str(i) for i in list_]
    return ' '.join(list_of_strings)


def progression_func(initial_term=1, number_of_terms=10, common_difference=2):
    progression = []
    elem = initial_term
    for _ in range(number_of_terms):
        # progression.append(str(elem))
        progression.append(elem)
        elem += common_difference
    return progression


def game_task():
    task = 'What number is missing in the progression?'
    return task


def game_quiz_and_answer():
    number_of_terms = randint(MIN_NUMBER, MAX_NUMBER)
    initial_term = randint(MIN_TERM, MAX_TERM)
    common_difference = randint(MIN_DIFFERENCE, MAX_DIFFERENCE)
    hidden_index = randint(0, number_of_terms - 1)
    progression = progression_func(
        initial_term, number_of_terms, common_difference)
    hidden_elem = progression[hidden_index]
    progression[hidden_index] = '..'
    question = list_to_string(progression)
    right_answer = str(hidden_elem)
    return question, right_answer
