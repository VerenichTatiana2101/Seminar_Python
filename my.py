# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

def input_array(size):
    array = []
    for i in range(size) :
        input_element1 = int(input(f'{i + 1} элемент массива: '))
        array.append(input_element1)
    return array

size1 = int(input('Введите количество элементов первого набора: '))
print(input_array(size1))
size2 = int(input('Введите количество элементов второго набора: '))
print(input_array(size2))

rez = []
for i in range(size1):
    for j in range(size2 -1):
        if i != j:
            rez.append(i)
print(rez)