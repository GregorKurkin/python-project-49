import prompt


NUMBER_OF_ROUNDS = 3


def execute(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.game_task())
    counter = 0
    while counter != NUMBER_OF_ROUNDS:
        question, right_answer = game.game_quiz_and_answer()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        if answer != right_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{right_answer}'. \nLet's try again, {name}!")
            break
        else:
            print('Correct!')
            counter += 1
    if counter == NUMBER_OF_ROUNDS:
        print(f'Congratulations, {name}!')
