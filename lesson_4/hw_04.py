# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

fil = "file_hw_4.txt"

def write_file(f, st):
    with open(f, "w") as data:
        data.write(st)

def rand():
    return random.randint(0,101)

def create_list(k):
    lst = [rand() for i in range(k + 1)]
    return lst  

def create_str(ar):
    lst = ar[::-1]
    text = ""
    if len(lst) < 1:
        text = "x = 0"
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                text += f"{lst[i]}x^{len(lst) - i - 1}"
                if lst[i+1] != 0:
                    text += " + "
            elif i == len(lst) - 2 and lst[i] != 0:
                text += f"{lst[i]}x"
                if lst[i+1] != 0:
                    text += " + "
            elif i == len(lst) - 1 and lst[i] != 0:
                text += f"{lst[i]} = 0"
            elif i == len(lst) - 1 and lst[i] == 0:
                text += " = 0"
    return text

k = int(input("Введите натуральную степень k = "))
ur = create_str(create_list(k))
print(f"Уравнение {ur} записано в файл {fil}")
write_file(fil, ur)
