from random import randint


def game_rules():
    print('What number is missing in the progression?')


def create_progression():
    start_num = randint(1, 20)
    step = randint(1, 9)
    progression = [start_num + (i * step) for i in range(10)] 
    return progression


def game_logic():
    progression = create_progression()
    random_index = randint(0, len(progression) - 1)
    answer = progression[random_index]
    question = ' '.join(['..' if x == answer else str(x) for x in progression])
    return question, str(answer)
