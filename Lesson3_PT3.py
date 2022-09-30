"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.
"""


# Вариант 1
def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg2 < arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


print(f'Result - '
      f'{my_func(int(input("Первое число ")), int(input("Второе число ")), int(input("Третье число ")))}')
# Хотел перенести строку - не получилось :(

# Вариант 2
a = (10, 1, 250)


def get_max(my_list):
    print(sum(sorted(list(my_list), reverse=True)[:2]))


get_max(a)


# Вариант 3

def my_func(*args):
    print('Сумма двух наибольших чисел - ', sum(args) - min(args))


my_func(int(input('Введите 1-е число:')), int(input('Введите 2-е число:')), int(input('Введите 3-е число:')))
