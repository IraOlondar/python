# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
#  является ли этот день выходным.

def is_weekend(num_dey):
    if 1 <= num_dey <= 7:
        if num_dey > 5:
            return "да"
        else:
            return "нет"
    return "ошибка ввода"


in_data = input ("введите день недели: ")
print(is_weekend(int(in_data)))