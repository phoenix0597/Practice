# Задача 2. Возраст
#
# Дан файл ages.txt, в котором построчно хранятся десять возрастов для каждого человека.
#
# Напишите программу, которая считывает файл, даёт имя для каждого возраста (можно просто использовать буквы алфавита)
# и выводит результат в новый файл result.txt в формате «имя — возраст». Программа должна обрабатывать следующие ошибки
# и выводить сообщение на экран:
#
# Попытка создания файла, который уже существует.
# На чтение ожидался файл, но это оказалась директория.
# Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).
# При желании воспользуйтесь подсказкой, чтобы найти подходящие имена ошибок.
#

file_ages = None
file_result = None

try:
    file_ages = open("ages.txt", "r", encoding="utf8")
    file_result = open("result.txt", "x", encoding="utf8")
    # режим 'x' - это эксклюзивное создание, бросается исключение FileExistsError, если файл уже существует.
# названия исключений можно группировать в кортежи
except (FileNotFoundError, FileExistsError, PermissionError, IsADirectoryError) as exc:
    print("Поймано исключение: ", exc, type(exc))

if file_result and file_ages:
    names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    count = 0
    for line in file_ages:
        try:
            clear_line = line.rstrip()
            # на всякий случай пытаемся преобразить данные в int, но не сохраняем это в переменную, т.к. записывать нам
            int(clear_line)
            # в файл придётся именно строку
            file_result.write(names[count] + " - " + clear_line)
            count += 1
        except (ValueError, TypeError) as exc:
            print("Поймано исключение: ", exc, type(exc))
    
    file_ages.close()
    file_result.close()
    