"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить
на своем месте.
Для заполнения списка элементов необходимо использовать
функцию input().
"""
# Вариант 1
my_list = input("Введите элементы списка через пробел: ").split()
my_list[:-1:2], my_list[1::2] = my_list[1::2], my_list[:-1:2]
print(my_list)
# Вариант 2
el_count = int(input("Задайте количество элементов списка "))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Введите значение списка "))
    i += 1
for a in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)
