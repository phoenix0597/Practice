from collections import Counter
from typing import Dict


def can_be_poly(string_to_check: str) -> bool:
    """
    Проверяет, может ли строка быть перестроена в палиндром.
    Args:
        string_to_check (str): Исходная строка.
    Returns:
        bool: True, если из строки можно сформировать палиндром, иначе False.

    Примеры использования:
    >>> can_be_poly('abcba')
    True
    >>> can_be_poly('abbbc')
    False
    """
    # Подсчет количества каждого символа в строке
    char_count: Dict[str, int] = Counter(string_to_check)
    
    # Подсчет количества символов, которые встречаются нечетное количество раз
    # Для создания палиндрома можно допустить не более одного символа с нечетным количеством
    odd_count: int = sum(map(lambda x: x % 2 == 1, char_count.values()))
    
    return odd_count <= 1


# Тестирование функции
if __name__ == "__main__":
    print(can_be_poly('abcba'))  # Должно вывести: True
    print(can_be_poly('abbbc'))  # Должно вывести: False
