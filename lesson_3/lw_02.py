# Определить, присутствует ли в заданном списке строк, некоторое число

import random

def gen_string(ot, do):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(chars) for i in range(random.randint(ot, do)))

def gen_list(a, b, c):
    return [gen_string(a, b) for i in range(c)]

aa = 2 # минимальное количество элементов в стороке
bb = 7 # максимальное количество элементов в стороке
cc = 6 # количество строк в списке

lst = gen_list(aa, bb, cc)
print(lst)

number = input("Введите число для поиска: ")

flag = False
for i in lst:
    if number in i:
        flag = True
        break

if flag:
    print("Присутствует")
else:
    print("Не присутствует")