import random


def game_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'
        

def game_logic():
    num = random.randint(1, 100)
    question = str(num)
    answer = is_even(num)
    return question, answer
