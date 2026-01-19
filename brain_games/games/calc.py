import random


def game_rules():
    print('What is the result of the expression?')


def game_logic():
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    match operator:
        case '+':
            question = f'{num_1} + {num_2}'
            answer = num_1 + num_2
        case '-':
            question = f'{num_1} - {num_2}'
            answer = num_1 - num_2
        case '*':
            question = f'{num_1} * {num_2}'
            answer = num_1 * num_2
    return question, str(answer)
