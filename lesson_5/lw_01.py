# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

# -1 1 2 3 4 5 6 7 8 10 11 12 13 14 15 16

import random

def write_file(f, st):
    with open(f, "w") as data:
        data.write(st)

def read_file(f):
    with open(f, "r") as data:
        return data.readlines()

def find_number(ls):
    for i in ls:
        if i == 0: continue
        if ls[i] - 1 != ls[i - 1]:
            return ls[i] - 1

f = "lesson_5/file_lw_1.txt"
write_file(f, "-1 0 1 2 3 4 5 6 7 8 9 10 11 12 14 15 16")

lst = list(map(int, read_file(f)[0].split()))
print(find_number(lst))

