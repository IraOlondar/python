# 4. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в списке positions - создайте этот список 
# Пример: positions = [1, 3, 6]

import random

def input_int(text):
    not_error = False
    print(text)
    while  not not_error:
        try:
            out_int = int(input(f"Введите натуральное число: ")) 
            not_error = True
        except ValueError:
            print("Введено не натуральное число!")

    return out_int

def gen_position(numbers):
    data = []
    for i in range(numbers):
        data.append(random.randrange(0, 2 * numbers))

    return data

def input_data(number):
    return [i for i in range( - number, number + 1)]

def composition_print(d, a):
    res = 1
    for i in range(len(d)):
        res *= a[d[i]]
    print(f"Результат равен: {res}")

nam = gen_position(input_int("Количество позиций"))
ar = input_data(input_int("Список"))
print(f"Позиции => {nam}")
print(f"Список => {ar}")
composition_print(nam, ar)
