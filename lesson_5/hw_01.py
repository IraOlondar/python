# Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#  a) Добавьте игру против бота
#  b) Подумайте как наделить бота "интеллектом"

import random
from time import sleep

def player(n, p):
    if p == "1":
        player_1 = input('\nКак тебя зовут?: ')
        player_2 = "Бот"
        player = player_1
    elif p == "2":
        player_1 = input('\nКак тебя зовут?: ')
        player_2 = input('\nА твоего соперника?: ')
        x = random.randint(1, 2)
        m = 3
        i = 1
        while i <= m:
            print("\nХодить первым будет...")
            sleep(1)
            i += 1
        if x == 1:
            player = player_1
        else:
            player = player_2
        print(f"\nХодить первым будет {player}")
    
    s = 0
    err = 0
    print(f"\nВсего конфет: {n}. Начнем игру")
    while n - s > 28:
        try:
            if player == "Бот":
                if 86 <= n - s <= 112:
                    number = n - s - 85
                elif 58 <= n - s <= 84:
                    number = n - s - 57
                elif 30 <= n - s <= 56:
                    number = n - s - 29
                else:
                    number = random.randint(1,28)
            else:
                number = int(input(f"\n{player} возьми от 1 до 28 конфет: "))
            if number <= 28:
                s += number
                err = 0
                print(f"\n{player} взял: {number}, сталось: {n - s}")
                player = player_2 if player == player_1 else player_1
            else:
                err += 1
                if err > 1:
                    print("\nДа хватит уже умничать! Вводи от 1 до 28")
                else:
                    print("\nНужно ввести именно от 1 до 28. Попробуй еще раз")       
        except ValueError:
            print("\nВведено не число!\nПопробуй еше раз")
    print(f"\n{player} выйграл!")


p = input(f"Выбери тип игры 1 - игра с ботом, 2 - два игрока: ")

# 321 вместо 2021 для уменьшения времени игры
player(321, p)