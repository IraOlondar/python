# 5. Реализуйте алгоритм перемешивания списка.

import random

lst = [random.randint(10,100) for i in range(random.randint(15,20))]

print(f"Новый список => {lst}")

random.shuffle(lst)

print(f"Перемешанный список => {lst}")