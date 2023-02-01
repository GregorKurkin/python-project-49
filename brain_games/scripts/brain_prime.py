#!/usr/bin/env python3


import prompt
from brain_games.games.game_prime import game_prime


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    while counter != 3:
        answer, func_result = game_prime()
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
