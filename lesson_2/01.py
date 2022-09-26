# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def input_data():
    not_error = False
    while  not not_error:
        out_int = input(f"Введите натуральное число: ")
        try:
            int(out_int) 
            not_error = True
        except ValueError:
            print("Введено не натуральное число!")

    return out_int
    

def summ_int(number):
    summ = 0
    for item in number:
        summ += int(item)
    return summ


def result_print(res):
    print(f"Сумма числа равна {res}")


result_print(summ_int(input_data()))
