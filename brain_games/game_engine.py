import prompt


def game_engine(module):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(module.game_task())
    counter = 0
    while counter != 3:
        question, func_result = module.game_logik()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer != func_result:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{func_result}'. \nLet's try again, {name}!")
            break
        else:
            print('Correct!')
            counter += 1
    if counter == 3:
        print(f'Congratulations, {name}!')