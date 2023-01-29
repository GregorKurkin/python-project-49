def if_even(question_number):
    return question_number % 2 == 0


def is_correct(answer, func_result):
    test_result = (answer == 'yes' and func_result) or (
        answer == 'no' and not func_result)
    return test_result
