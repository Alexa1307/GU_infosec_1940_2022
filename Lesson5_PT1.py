"""Создать программный файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать
пустая строка."""

# Вариант 1
my_f = open('test.txt', 'w')
line = input('Введите текст: ')
while line:
    my_f.writelines(line)
    line = input('Введите текст: ')
    if not line:
        break
my_f.close()
my_f = open('test.txt', 'r')
content = my_f.readlines()
print(content)

# Вариант 2
my_list = []
while True:
    line = input("Введите текст: ")
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line
        my_list.append(newline)

    with open("test_1.txt", "w") as file_obj:
        file_obj.writelines(my_list)
