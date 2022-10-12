# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import shuffle

# CANDIES = 2021
CANDIES = 117
CANDIES_LIMIT = 28


def bot_run(candies: int) -> int:
    if candies <= CANDIES_LIMIT:  # забрать остаток
        result = candies
    else:
        result = CANDIES_LIMIT
        # для победы - нечётное
        cnt_step = candies // CANDIES_LIMIT
        if candies % CANDIES_LIMIT > 0:
            cnt_step += 1

        if cnt_step % 2 == 0:  # проигрываем
            if candies - CANDIES_LIMIT < CANDIES_LIMIT:
                result = candies - (CANDIES_LIMIT - 1)
    return result


rest_candies = CANDIES

players = ["human", 'bot' if int(input('Играть с  bot 1 - yes, 0 - no? ')) else 'person']
shuffle(players)

active_player = players[0]
print(f'1 игрок - {players[0]}, 2 игрок - {players[1]}')

while rest_candies > 0:
    print(f'\n{rest_candies} конфет на столе, ты можешь взять [1 .. {CANDIES_LIMIT}]')
    print(f"Игрок {active_player} ходит")

    if active_player == "bot":
        get_candies = bot_run(rest_candies)
        print(f'Бот взял {get_candies} конфет')
    else:
        get_candies = int(input(f'Сколько конфет ты хочешь взять {active_player}: '))

    # проверка выигрыша
    if get_candies not in range(1, CANDIES_LIMIT + 1):
        print('Неверный ход!')
    else:
        rest_candies -= get_candies
        if rest_candies > 0:
            if "bot" in players:
                active_player = "human" if active_player == "bot" else "bot"
            else:
                active_player = "human" if active_player == "person" else "person"
        else:
            print(f'Игрок {active_player} победил!')
