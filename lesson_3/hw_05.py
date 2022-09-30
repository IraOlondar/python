# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Пример: 
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи] (https://ru.wikipedia.org/wiki/Негафибоначчи)

def fibonacci(n):
    if n == 1 or n == 2:                       
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def nega_fibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    num1, num2 = 1, -1
    for i in range(2, n):
        num1, num2 = num2, num1 - num2
    return num2

list = [0]
number = int(input('Введите число: '))
for e in range(1, number + 1):
    list.append(fibonacci(e))
    list.insert(0, nega_fibonacci(e))
print(list)
