#!/usr/bin/env python3


import prompt
from brain_games.games.game_progression import game_progression


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    counter = 0
    while counter != 3:
        answer, func_result = game_progression()
        if answer != func_result:
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
