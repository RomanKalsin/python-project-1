from brain_games import check_answer, finish_game, welcome_user
from brain_games.games.prime import game_logic, game_rules


def main():
    user_name = welcome_user()
    result = check_answer(game_rules, game_logic)
    finish_game(result, user_name)


if __name__ == '__main__':
    main()
