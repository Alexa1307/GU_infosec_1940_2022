"""Реализовать формирование списка, используя
функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000
(включая границы). Нужно получить результат
вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""

# Вариант 1

from functools import reduce


def my_func(el_p, el):
    return el_p * el


print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка '
      f'{reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

# Вариант 2 (покороче)

# from functools import reduce
#
# my_list = [el for el in range(100, 1001) if el % 2 == 0]
#
#
# def my_func(prev_el, el):
#     return prev_el * el
#
#
# print(reduce(my_func, my_list))
