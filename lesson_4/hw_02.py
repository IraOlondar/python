# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

num = int(input("Введите число: "))
i = 2
lst = []
in_mun = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {in_mun}: {lst}")