"""Создать текстовый файл (не программно), сохранить
в нём несколько строк, выполнить подсчёт строк и слов
в каждой строке."""

# Вариант 1

my_list = ['Привет\n', 'добрый\n', 'Python!\n']
with open("test_2.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("test_2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"Количество символов в строке: {letters}")
    print(f"Всего слов: {lines}")

# Вариант 2 (при подсчете учитыватся и \n :()

my_file = open('test_2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('test_2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('test_2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('test_2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()
