# Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел

from time import time
t = time()
print(f'Случайное число от 0 до 99 = {int((t - int(t)) * 1000)}')
