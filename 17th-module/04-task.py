# Задача.
# Напишите функцию, которая принимает строку и возвращает количество уникальных символов в строке.
# Уникальными считаются буквы, которые повторяются только один раз
# (например строка «аа» будет содержать 0 уникальных букв).
# Используйте для выполнения задачи lambda-функции и map и/или filter.
# Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного регистра должны считаться одинаковыми.
#
# Пример:
# message = "Today is a beautiful day! The sun is shining and the birds are singing."
# unique_count = count_unique_characters(message)
# print("Количество уникальных символов в строке:", unique_count)
# Вывод:
# количество уникальных символов в строке — 5.
def count_unique_characters(mess):
    """
    Эта функция принимает строку и возвращает количество уникальных символов в строке,
    не учитывая регистр. Уникальные символы - это те, которые появляются ровно один раз.
    Args:
        mess (str): Входная строка.
    Returns:
        int: Количество уникальных символов во входной строке.
    """
    mess_lower = mess.lower()
    unique_chars_list = list(filter(lambda x: mess_lower.count(x) == 1, set(mess_lower)))
    return len(unique_chars_list)


message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
