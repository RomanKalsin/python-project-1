from random import randint


def game_rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(num):
    if num < 2:
        return 'no'
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 'no'        
    return 'yes'


def game_logic():
    num = randint(1, 101)
    question = str(num)
    answer = is_prime(num)
    return question, answer