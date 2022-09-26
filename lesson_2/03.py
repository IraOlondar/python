# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

def input_data():
    not_error = False
    while  not not_error:
        try:
            out_int = int(input(f"Введите натуральное число: ")) 
            not_error = True
        except ValueError:
            print("Введено не натуральное число!")

    return out_int
    

def summ_print(res):
    a = []
    summ = 0
    n = 1
    while n <= res:
        summ += round((1 + 1/n) ** n, 2)
        a.append(summ)
        n += 1

    print(a)
    print(f"Сумма равна: {summ}")


summ_print(input_data())
