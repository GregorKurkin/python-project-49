#!/usr/bin/env python3


import prompt
from brain_games.games.game_gcd import game_gcd


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    while counter != 3:
        answer, func_result = game_gcd()
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
