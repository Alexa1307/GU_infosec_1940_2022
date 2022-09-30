"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна,
лето, осень).
Напишите решения через list и через dict.
"""

lst = ['зима', 'весна', 'лето', 'осень']
d = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month = int(input("Введите месяц по номеру "))
if month == 12 or month == 1 or month == 2:
    print(d.get(1))
    print(lst[0])
elif 3 <= month <= 5:
    print(d.get(2))
    print(lst[1])
elif 6 <= month <= 8:
    print(d.get(3))
    print(lst[2])
elif 9 <= month <= 11:
    print(d.get(4))
    print(lst[3])
else:
    print("Такого месяца не бывает")
