# Задание 2. Самое длинное слово
# Что нужно сделать
# Пользователь вводит строку, содержащую пробелы. Найдите в ней самое длинное слово, выведите его и его длину.
# Если таких слов несколько, выведите первое.
#
# Пример 1.
# Введите строку: я есть строка.
# Самое длинное слово: «строка».
# Длина этого слова: 6 символов.
#
# Пример 2.
# Введите строку: а б.
# Самое длинное слово: «а».
# Длина этого слова: 1 символ.
#
# Пример 3.
# Введите строку: б.
# Самое длинное слово: «б».
# Длина этого слова: 1 символ.
print("Введите строку: ", end="")
input_string_list = input().split(" ")  # вводим строку, содержащую пробелы и преобразуем ее в список по разделителю " "
max_item = max(input_string_list, key=len)  # выбираем самое длинное слово из списка (1-е, если их несколько)
print("Самое длинное слово:", max_item)
print("Длина этого слова:", len(max_item), "символов.")
