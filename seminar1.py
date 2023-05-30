# Задача №1. Общее обсуждение
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2
"""
n = int(input('Введите расстояние, которое проезжает авто за день: '))
m = int(input('Введите длинну маршрута: '))
res = (n + m - 1) // n
print(res)
"""

# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

"""
a = int(input('Введите количество учеников в первом классе: '))
b = int(input('Введите количество учеников в втором классе: '))
c = int(input('Введите количество учеников в третьем классе: '))
n = 2
# res = (a + n - 1) // n + (b + n - 1) // n + (c + n - 1) // n
res = (a + 1) // n + (b + 1) // n + (c + 1) // n
# ну n у нас все время 2, потом делаем -1. так почему бы сразу не писать +1
print(res)
"""

# Задача №5. Решение в группах
# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

"""
i = int(input('Введите номер вагона от головы поезда: '))
j = int(input('Введите порядковый номер поезда: '))
if i != j:
    print(i + j - 1)
else:
    print('Информации недостаточно')
"""

# Задача №7. Общее обсуждение
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

n = int(input('Введите год: '))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('Yes')
else:
    print('No')