# Создайте программу для игры в "Крестики-нолики".

import os

def in_data(lst, t):
    exit = False
    while not exit:
        move = input(f"Куда поставим '{t}'? -> ")
        try:
            move = int(move)
        except:
            print("Еще раз!")
            continue
        if 1 <= move <= 9:
            if(str(lst[move - 1]) not in "XO"):
                exit = True
                lst[move - 1] = t
            else:
                print('Ячейка занята')
        else:
            print('Таких ячеек нет')

def print_lst(lst):
    os.system("cls")
    print("-" * 13)
    for i in range(3):
        print(f"| {lst[0 + i * 3]} | {lst[1 + i * 3]} | {lst[2 + i * 3]} |")
        print('-' * 13)

def is_winner(lst):
    win_list = [[0,1,2],[3,4,5],
               [6,7,8],[0,3,6],
               [1,4,7],[2,5,8],
               [0,4,8],[2,4,6]]
    for i in win_list:
        if lst[i[0]] == lst[i[1]] == lst[i[2]]:
            return lst[i[0]]
    return False

def play():
    count = 0
    lst = list(range(1,10))
    while True:
        print_lst(lst)
        player = "X" if count % 2 == 0 else "O"
        in_data(lst, player)
        count += 1
        if count > 4:
            win = is_winner(lst)
            if win:
                print(f"Победа {win}!")
                break
            if count == 9:
                print("Ничья!")
        print_lst(lst)

play()