# 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше
# предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно
# сделать оптимизацию кода по памяти, по скорости.

import timeit

start2 = timeit.timeit()
src2 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
for i in range(len(src2) - 1):
    if src2[i] < src2[i + 1]:
        result.append(src2[i + 1])
print(result, timeit.timeit() - start2)

start1 = timeit.timeit()
src1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [i for j, i in zip(src1, src1[1:]) if i > j]
print(result, timeit.timeit() - start1)



