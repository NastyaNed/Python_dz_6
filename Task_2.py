# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

listn = [random.randint(-10, 10) for i in range(12)]
print(listn)
start = int(input('Введите начало диапозона: '))
end = int(input('Введите конец диапозона: '))

list_i = []
for i in range(len(listn)):
    if start <= listn[i] <= end:
        list_i.append(i)
print(list_i)