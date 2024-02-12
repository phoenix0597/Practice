# 1) программа ищет в заданной папке и вложенных в нее папках файл с заданным именем
# 2) программа создает файл history.txt в папке, где находится запускаемый скрипт и записывает в него
# все полные пути к искомым файлам
import os


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
    for root, _, files in os.walk(path):
        for i_file in files:
            if i_file == name and "Module" in root:
                files_list.append(os.path.join(root, i_file))
                
    return files_list


path = os.path.abspath(os.path.join('..', '..', '..', 'Python_Basic'))
f_name = "main.py"
print(f"\nПереходим в папку {path}...\n")
found_files = file_search(path, f_name)
with open("history.txt", "a") as file:
    for file_path in found_files:
        file.write(file_path + "\n")
        print(file_path)

