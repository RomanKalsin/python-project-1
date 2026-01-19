from brain_games import welcome_user, check_answer, finish_game
from brain_games.games.brain_even import game_rules, game_logic


def main():
    user_name = welcome_user()
    result = check_answer(game_rules, game_logic)
    finish_game(result, user_name)


if __name__ == '__main__':
    main()
