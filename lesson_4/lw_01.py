# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

import random

def max_list(lst):
    return max([int(n) for n in lst.split(" ")])

def min_list(lst):
    return min([int(n) for n in lst.split(" ")])

def gen_list(a, b, c):
    return " ".join([str(random.randint(a, b)) for i in range(c)])

aa = 1 # минимальное число в стороке списка
bb = 99 # максимальное число в строке списка
cc = 20 # количество строк в списке

list = gen_list(aa, bb, cc)
print(list)
print(f"Min: {min_list(list)}; Max: {max_list(list)}")
