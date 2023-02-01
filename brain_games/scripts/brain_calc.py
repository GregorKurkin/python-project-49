#!/usr/bin/env python3


import prompt
from brain_games.games.game_calc import game_calc


def main():  # brain_calc.py
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    # start game
    # print('Answer "yes" if the number is even, otherwise answer "no".')
    print('What is the result of the expression?')
    counter = 0
    while counter != 3:
        answer, func_result = game_calc()
        if answer != str(func_result):
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{func_result}'. \nLet's try again, {name}!")
            break
        else:
            print('Correct!')
            counter += 1
    if counter == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
