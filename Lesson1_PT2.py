"""2.1 Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк (пока без форматирования!!!)."""


s = int(input("Введите время в секундах: "))
hour = s // 3600
hour1 = s % 3600
min = hour1 // 60
sec = hour1 % 60
print(hour, ":", min, ":", sec)
# ========================================================================================================
# 2.2 С форматированием

s = int(input("Введите время в секундах: "))
hour = s // 3600
hour1 = s % 3600
min = hour1 // 60
sec = hour1 % 60
print("{}: {}: {}".format(hour, min, sec))
