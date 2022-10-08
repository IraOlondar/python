# Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

def find_sequence(lst):
    out = []
    tmp = []
    j = 1
    while j < len(lst):
        i = j
        copy_lst = lst[:]
        while i < len(copy_lst) - 1:
            if copy_lst[i] < copy_lst[i + 1]: 
                tmp.append(copy_lst[i])
                i += 1
            else:
                copy_lst.pop(i + 1)
        j += 1
        if len(out) < len(tmp):
            out = tmp
        tmp = []

    if lst[-1] > out[-1]:
        out.append(lst[-1])
    
    if lst[0] < out[0]:
        out.insert(0, lst[0])

    return out

list = [1, 5, 2, 3, 4, 6, 1, 7]
print(list)
print(find_sequence(list))