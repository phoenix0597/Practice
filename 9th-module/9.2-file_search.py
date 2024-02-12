import os


# вариант 1
def find_files(directory, filename):
    # Walk возвращает кортежи с root (текущая директория), dirs (поддиректории) и files (файлы)
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Проверяем, встречается ли имя файла в текущем списке файлов
            if file == filename:
                # Выводим абсолютный путь к файлу
                print(os.path.join(root, file))


# вариант 2
def find_files_1(dir_name, file_name):
    for i_elem in os.listdir(dir_name):
        if i_elem == file_name:
            print(os.path.join(dir_name, i_elem))
        else:
            if os.path.isdir(os.path.join(dir_name, i_elem)):
                find_files_1(os.path.join(dir_name, i_elem), file_name)


# Пример использования функции
directory_to_search = "C:\\Users\\phoen\\PycharmProjects\\Python_Basic"
file_to_find = "main.py"
# Вызов функции
# find_files(directory_to_search, file_to_find)
find_files_1(directory_to_search, file_to_find)
