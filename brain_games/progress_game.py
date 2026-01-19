import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def check_answer(game_rules, game_logic):
    game_rules()
    count = 0
    while count < 3:
        question, answer = game_logic()
        print(f'Question: {question}')
        user_ansver = prompt.string('Your answer: ')
        if answer != user_ansver:
            return False
        count += 1
    return True


def finish_game(result, user_name):
    if result:
        print(f"Congratulations, {user_name}!")
    elif not result:
        print(f"Let's try again, {user_name}!")
