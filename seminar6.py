from CustomFuncs import *

# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:
# 7
# 3 1 3 4 2 4 12
# Вывод:
# Ввод:
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12

"""
size1 = int(input('Введите количество элементов первого набора: '))
arr_1 = input_array(size1)
size2 = int(input('Введите количество элементов второго набора: '))
arr_2 = input_array(size2)

print(arr_1)
print(arr_2)
print(absence_elements(arr_1, arr_2))
"""

# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: 
# 1 2 3 2 3
# Вывод:
# 2

"""
# вариант1
size = int(input('Введите количество элементов первого набора: '))
arr = input_array(size)

print(arr)
print(counting_couples(arr))

# вариант2
# size = int(input('Введите количество элементов первого набора: '))
# arr = input_array(size)
result = pairs_count(arr)
print(result)
"""

# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:           Вывод:
# 300             220 284

"""
k = int(input("Введите число: "))
result = sum_of_dividers(k)

print(result)
print(frendly_numbers())
"""