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


# def is_correct(answer, func_result):
#     test_result = (answer == 'yes' and func_result) or (
#         answer == 'no' and not func_result)
#     return test_result
