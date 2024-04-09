# Задача 3. Палиндром: возвращение
# Что нужно сделать.
# Есть множество встроенных и внешних библиотек для работы с данными в Python. С некоторыми из них вы уже работали.
# Например, с модулем collections, когда использовали специальный класс OrderedDict,
# с помощью которого делали упорядоченный словарь. В этой библиотеке есть и другие возможности, но их немного.
# Официальная документация: collections — Container datatypes.
#
# Используя модуль collections, реализуйте функцию can_be_poly, которая принимает на вход строку и проверяет,
# можно ли получить из неё палиндром.
#
# Пример кода:
#
# print(can_be_poly('abcba'))
# print(can_be_poly('abbbc'))
# Результат:
# True
# False
from collections import Counter
from typing import Dict


def can_be_poly(string: str) -> bool:
    """
    Проверяет, можно ли получить палиндром из заданной строки.
    Args:
        string (str): Входная строка.
    Returns:
        bool: True, если из строки можно получить палиндром, False в противном случае.
    """
    # Создаем словарь, где ключи - символы, а значения - их количество
    char_counts: Dict[str, int] = Counter(string)
    
    # Используем лямбда-функцию для проверки, что в словаре не более одного символа с нечетным количеством
    is_palindrome_possible: bool = sum(1 for count in char_counts.values() if count % 2 != 0) <= 1
    
    return is_palindrome_possible


# Примеры использования
print(can_be_poly('abcba'))  # True
print(can_be_poly('abbbc'))  # False
