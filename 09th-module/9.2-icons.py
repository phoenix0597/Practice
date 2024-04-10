# Задача 1. Иконки
# Андрей для себя хочет сделать экспериментальный сайт, где будет красиво отображаться
# вся структура его диска: папки одними иконками, файлы — другими.
# Поэтому ему нужен код, который поможет определить, какой тип иконки вставить.
#
# Напишите программу, которая по заданному абсолютному пути определяет, на что указывает этот путь
# (на директорию, файл, или же путь является ссылкой), и выведите соответствующее сообщение.
# Если путь указывает на файл, то также выведите его размер (сколько он весит в байтах).
# Обеспечьте контроль ввода: проверка пути на существование.
#
# Подсказка: для вывода размера файла поищите соответствующий метод.
#
# Пример 1:
# Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
# Это файл
# Размер файла: 605 байт
#
# Пример 2:
# Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
# Указанного пути не существует
import os

input_path = input('Введите путь: ')


def is_link_dir_file(path):
    if os.path.exists(path):
        if os.path.islink(path):
            print('Это ссылка')
        if os.path.isdir(path):
            print('Это папка')
        elif os.path.isfile(path):
            size = os.path.getsize(path)
            print(f'Это файл\nРазмер файла: {size} байт')
        else:
            print('Это не ссылка')
    else:
        print('Указанного пути не существует')


# Testing
test_data = [
    ('C:\\Users\\Roman\\PycharmProjects\\Skillbox\\Module17\\lesson2.py', 'Это файл\nРазмер файла: 605 байт'),
    ('C:\\Users\\Roman\\PycharmProjects\\Skillbox\\Module17\\lesson2.py', 'Указанного пути не существует')
]

# Testing function
def test(func, path):
    print(func(path))


is_link_dir_file(input_path)