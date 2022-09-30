# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def mult_list(lst):
    return [round(i % 1, 2) for i in lst if i % 1 != 0]

def gen_list(a, b, c):
    return [round(random.uniform(a, b), 2) for i in range(c)]

aa = 0 # минимальное число в стороке списка
bb = 99 # максимальное число в строке списка
cc = 10 # количество строк в списке

list = gen_list(aa, bb, cc)

new_lst = mult_list(list)
print(list, "=>", max(new_lst) - min(new_lst))