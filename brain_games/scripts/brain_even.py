import random

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'
        

def brain_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        num = random.randint(1, 100)
        print(f'Question: {num}')
        user_ansver = prompt.string('Your answer: ')
        if is_even(num) != user_ansver:
            return False
        count += 1
    return True


def finish_game(result, user_name):
    if result:
        print(f"Congratulations, {user_name}!")
    elif not result:
        print(f"Let's try again, {user_name}!")


def main():
    user_name = welcome_user()
    result = brain_even()
    finish_game(result, user_name)


if __name__ == '__main__':
    main()
