#!/usr/bin/env python3


import prompt
from random import randint
from brain_games.logic import if_even, is_correct


def main():  # brain_games.py
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter != 3:
        question_number = randint(-1000, 1000)
        print(f'Question: {question_number}')
        answer = prompt.string('Your answer: ')
        if_even_result = if_even(question_number)
        correct_answer = (if_even_result and 'yes' or 'no')
        if is_correct(answer, if_even_result):
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'. \nLet's try again, {name}!")
            break
    if counter == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
