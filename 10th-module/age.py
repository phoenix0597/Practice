# Задача 2. Возраст
# Дан файл ages.txt, в котором построчно хранятся десять возрастов для каждого человека.
#
# Напишите программу, которая считывает файл, даёт имя для каждого возраста (можно просто использовать буквы алфавита)
# и выводит результат в новый файл result.txt в формате «имя — возраст».
# Программа должна обрабатывать следующие ошибки и выводить сообщение на экран:
#
# Попытка создания файла, который уже существует.
# На чтение ожидался файл, но это оказалась директория.
# Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).
# При желании воспользуйтесь подсказкой, чтобы найти подходящие имена ошибок.
import random
import string

characters = string.ascii_letters
unique_symbols = []
age_dict = {}
try:
    with open("age.txt", "r", encoding="utf-8") as age_file:
        count_ages, max_count = 0, len(age_file.readlines())
        for age in age_file:
            name = random.choice(characters).strip()
            if name in unique_symbols:
                continue
            count_ages += 1
            unique_symbols.append(name)
            age_dict[name] = int(age)
        print(*(f"{key}: {value}\n" for (key, value) in age_dict.items()))
        
except FileNotFoundError:
    print("Такого файла не существует!")
except (ValueError, TypeError):
    print("\nНеверный тип данных или некорректное значение!")
except Exception:
    print("Неизвестная ошибка!")
