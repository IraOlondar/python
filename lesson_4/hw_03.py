# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import random

def mult_list(lst):
    new_lst = []
    [new_lst.append(i) for i in lst if i not in new_lst]
    return new_lst

def gen_list(a, b, c):
    return [random.randint(a, b) for i in range(c)]

aa = 1 # минимальное число в стороке списка
bb = 20 # максимальное число в строке списка
cc = 25 # количество строк в списке

list = gen_list(aa, bb, cc)
print(list)
print(mult_list(list))
