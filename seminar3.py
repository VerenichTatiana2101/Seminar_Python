# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

"""
myList = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(myList)))
print(set(myList))
"""

# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

"""
myList = [1, 2, 3, 4, 5]
n = int(input("Введите количество сдвигов: ")) % len(myList)
for i in range(n):
    myList.insert(0, myList.pop())
print(myList)
"""

# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

"""
myList = [{"V" : "S001"}, {"V" : "S002"}, {"VI" : "S001"}, 
          {"VI" : "S005"}, {"VII" : "S005"}, 
          {"V" : "S009"}, {"VIII" : "S007"}]

result = []   #создаём пустой список
for item in myList:
    result.append(list(item.values())[0])  #list тип данных keys ключи, values значения
print(set(result))
"""




