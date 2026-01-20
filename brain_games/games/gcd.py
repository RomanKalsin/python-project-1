from random import randint


def game_rules():
    print('Find the greatest common divisor of given numbers.')


def find_least_divider(num_1, num_2):
    return num_1 if num_2 == 0 else find_least_divider(num_2, num_1 % num_2)


def game_logic():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    question = f'{num_1} {num_2}'
    answer = find_least_divider(num_1, num_2)
    return question, str(answer)
