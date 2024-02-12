# Используя функцию поиска файла из предыдущего урока, реализуйте программу,
# которая находит внутри указанного пути все файлы с искомым названием
# и выводит на экран текст одного из них (выбор можно сгенерировать случайно).
#
# Подсказка: можно использовать, например, список для сохранения найденного пути.
import os
import random


def file_search(path, name):
    """
    Функция поиска файла в указанном пути.
    Параметры:
        path (str): Путь к папке.
        name (str): Название искомого файла.
    Возвращает:
        str: Путь к искомому файла.
    """
    files_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == name:
                files_list.append(os.path.join(root, file))
                
    return files_list


found_files = file_search("C:\\Users\\phoen\\PycharmProjects\\Python_Basic", "main.py")

random_num = random.randint(0, len(found_files) - 1)
print(f"{len(found_files)} files found:\n")
[print(i_file) for i_file in found_files]
print("\nRandom file:", str(found_files[random_num]))
