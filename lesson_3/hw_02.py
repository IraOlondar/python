# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

def mult_list(lst):
    l = len(lst) // 2 + 1 if len(lst) % 2 != 0 else len(lst) // 2
    new_lst = [lst[i] * lst[len(lst) - i - 1] for i in range(l)]
    print(new_lst)

def gen_list(a, b, c):
    return [random.randint(a, b) for i in range(c)]

aa = 1 # минимальное число в стороке списка
bb = 9 # максимальное число в строке списка
cc = 10 # количество строк в списке

list = gen_list(aa, bb, cc)
print(list)
mult_list(list)
