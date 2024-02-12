# Задача "Участники конференции"
# Входные данные:
# speakers.txt
# Строчка файла: Фамилия Имя возраст
#
# Выходные данные:
# Содержимое файла speakers.txt
# Петров Петр 25
# Степанова Лена 23
# Lannister Bob 32
# Jones Braun 22
#
import chardet


def detect_encoding(f_path):
    with open(f_path, 'rb') as f:
        rawdata = f.read()
        result = chardet.detect(rawdata)
        return result['encoding']


speakers = 'speakers.txt'
encoding = detect_encoding(speakers)
print(f"The file '{speakers}' is encoded in {encoding}")

with open(speakers, 'r', encoding=encoding) as file:
    file.seek(1)  # в скобках метода мы указываем позицию, с которой мы хотим начать чтение
    # data = file.readlines()  # возвращает список строк текста из файла
    data = file.read(14)  # возвращает первые 14 символов текста из файла в виде строки
    data_2 = file.read(19)  # возвращает следующие 2 символа текста из файла в виде строки
    print(data, data_2)
