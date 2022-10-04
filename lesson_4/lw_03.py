# 3. Задайте два числа. Напишите программу, которая найдёт 
# НОК (наименьшее общее кратное) этих двух чисел.

def input_num():
    arr = []
    for i in range(2):
        not_nul = False
        while not not_nul:
            try:
                number = int(input(f"Ведите число {i + 1}: "))
                not_nul = True
                arr.append(number)          
            except ValueError:
                print("Введено не число!")
    return arr

def check_nok(ar):
    i = ar[0] + 1
    if ar[0] <= ar[1]:
        i = ar[1] + 1
    while True:
        if i % ar[0] == 0 and i % ar[1] == 0:
            return f"НОК чисел {ar[0]} и {ar[1]} равно: {i}"
        i += 1 

print(check_nok(input_num()))

