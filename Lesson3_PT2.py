"""
2. Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Осуществить вывод данных
о пользователе одной строкой.
"""


# Вариант 1

def my_func(**kwargs):
    return kwargs


print(my_func(first_name='Petrov',
              last_name='Alex',
              year_of_birth=1963,
              city='Moscow',
              email='alex@rambler',
              hone='+903-123-45-67'))


# Вариант 2
# Определяем функцию


def info_user(first_name, last_name, year_of_birth, city, email, phone):
    print(f'{first_name} {last_name} {year_of_birth} года рождения, '
          f'проживает в городе {city}, Email: {email}, тел: {phone}')
    # print(" " + first_name + " " + last_name + " " + year_of_birth +
    # " года рождения "  "проживает в городе " + city + " Email: " +
    # email + " тел: " + phone + '.')


# Вызываем функцию
info_user(first_name="Иван", last_name="Иванов",
          year_of_birth="1963", city="Москва",
          email="alex@rambler", phone="+903-123-45-67")


# Вариант 3

def personal_data(**pd):
    for k in pd:
        print(pd[k], end=' ')


personal_data(name='Ivan',
              first_name='Ivanov',
              born=2000, city='Moscow',
              e_mail='ivan_ivanov@mail.ru',
              phone='+7-900-1234567')
