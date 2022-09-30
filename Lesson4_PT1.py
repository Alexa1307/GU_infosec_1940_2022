'''Реализовать скрипт, в котором должна быть предусмотрена
функция расчёта заработной платы сотрудника. Используйте
в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений
необходимо запускать скрипт с параметрами.
'''


# Вариант 1
def sal():
    try:
        time = float(input('Выработка в часах '))
        salary = int(input('Ставка в у.е. '))
        bonus = int(input('Премия в у.е. '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a number')


sal()


# Вариант 2
def simple_calc():
    x = float(input('Введите количество отработанных часов : '))
    y = float(input('Введите суммы оплаты труда за 1 час : '))
    c = float(input('Укажите размер премии - '))
    pay = x * y
    return pay + c


print(f'Размер заработной платы составил: {simple_calc()}')
