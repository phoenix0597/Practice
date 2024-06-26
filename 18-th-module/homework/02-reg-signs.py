# Задача 2. Регистрационные знаки
# Что нужно сделать
# В России для транспорта применяются регистрационные знаки нескольких видов.
#
# Общее в них то, что они состоят из цифр и букв. Причём используются только 12 букв кириллицы,
# имеющих графические аналоги в латинском алфавите: А, В, Е, К, М, Н, О, Р, С, Т, У и Х.
#
# У частных легковых автомобилей номера — это буква, три цифры, две буквы, затем две или три цифры с кодом региона.
#
# У такси — две буквы, три цифры, затем две или три цифры с кодом региона.
#
# Напишите программу, которая в перечне номеров находит номера частных автомобилей и номера такси.
#
# Пример перечня:
#
# 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
#
#
# Результат:
# Список номеров частных автомобилей: ['А578ВЕ777', 'К901МН666']
# Список номеров такси: ['ОР233787', 'СТ46599']
import re

# Входные данные для номеров
letters = 'АВЕКМНОРСТУХ'
nums_example = """'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'"""

# Паттерны номеров
private_num_pattern = r'[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}'
taxi_num_pattern = r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}'

# Выполняем поиск номеров частных автомобилей, согласно паттерну
private_nums = re.findall(private_num_pattern, nums_example)
print('Список номеров частных автомобилей:', private_nums)

# Выполняем поиск номеров такси, согласно паттерну
taxi_nums = re.findall(taxi_num_pattern, nums_example)
print('Список номеров такси:', taxi_nums)