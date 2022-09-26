# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def input_data():
    not_error = False
    while  not not_error:
        try:
            out_int = int(input(f"Введите натуральное число: ")) 
            not_error = True
        except ValueError:
            print("Введено не натуральное число!")

    return out_int
    

def composition_print(res):
    a = []
    composit = n = 1
    while n <= res:
        composit *= n
        a.append(composit)
        n += 1

    print(a)


composition_print(input_data())
