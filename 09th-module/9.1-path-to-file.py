# Задача "Путь к файлу"
# Входные данные:
# Папка и имя файла
# path = docs/{folder}/{file}
#
# Выходные данные
# Относительный путь к файлу
import os


folder_name = 'project'
file_name = 'my_file.txt'

path = 'docs/{folder_name}/{file_name}'.format(
    folder_name=folder_name,
    file_name=file_name,
)
print(path)

# создает строку-путь, "собираемую" методом join() класса path модуля os
# (соединяет с помощью правильных для данной ОС слэшей) строки, переданные в метод в качестве параметров
rel_path = os.path.join('docs', folder_name, file_name)
print(rel_path)

# метод abspath создает абсолютный путь к строке-файлу/папке/пути для данной операционной системы,
# так, если бы данные файл/папка лежала бы в папке, в которой запускается скрипт
abs_path = os.path.abspath(file_name)
print(abs_path)

# считать папку folder_name, находящейся на уровень выше и вывести абсолютный путь к ней
prev_dir = os.path.abspath(os.path.join('..', folder_name))
print(prev_dir)

# считать папку folder_name, находящейся в корневой папке и вывести абсолютный путь к ней
prev_dir = os.path.abspath(os.path.join(os.path.sep, folder_name))
print(prev_dir)

