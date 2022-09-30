"""
Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


# Вариант 1
def get_dif(*args):
    if args[1] != 0:
        print('Результат деления - ', args[0] / args[1])
    else:
        print('На ноль делить нельзя !')


get_dif(int(input('Введите 1-е целое число:')), int(input('Введите 2-е целое число:')))


# Вариант 2


def get_div(first_namb, second_namb):
    try:
        result = first_namb / second_namb
        return result
    except ZeroDivisionError:
        return "На '0' делить нельзя!"


try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print('Результат деления - ', get_div(a, b))
except ValueError:
    print("Вводите только число!")


# Вариант 3


def get_div():
    try:
        arg1 = int(input("Введите первое число: "))
        arg2 = int(input("Введите второе число: "))
        res = arg1 / arg2
    except ValueError:
        return "Вводите только число!"
    except ZeroDivisionError:
        return "На '0' делить нельзя!"
    return res


print('Результат деления - ', get_div())
