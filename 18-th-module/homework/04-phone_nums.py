# Задача 4. Телефонные номера
# Что нужно сделать
# В одной организации перед записью телефонного номера в базу данных его проверяют на соответствие следующим критериям:
#
# Длина номера — ровно десять знаков.
# Номер начинается с цифры 8 или 9.
# Остальные знаки — только цифры.
# На вход в программу подаётся список номеров (можно взять готовый или запросить у пользователя).
# Реализуйте код, который проверяет каждый номер из списка на соответствие критериям и выводит на экран
# соответствующие сообщения.
#
# Пример списка:
# ['9999999999', '999999-999', '99999x9999']
#
#
#
# Результат:
# первый номер: всё в порядке
# второй номер: не подходит
# третий номер: не подходит
import re
from typing import List


def validate_phone_numbers(phone_numbers: List[str]) -> None:
    """
    Проверяет список телефонных номеров на соответствие заданным критериям с помощью регулярного выражения:
    длина номера ровно 10 знаков, номер начинается с цифры 8 или 9, остальные знаки только цифры. Выводит
    результат проверки для каждого номера.

    :param phone_numbers: список телефонных номеров для проверки
    """
    pattern = re.compile(r'^[89]\d{9}$')
    
    for i, phone in enumerate(phone_numbers, start=1):
        if pattern.match(phone):
            print(f"{i}-й номер: всё в порядке")
        else:
            print(f"{i}-й номер: не подходит")


if __name__ == '__main__':
    # Пример списка телефонных номеров
    phone_numbers_example = ['9999999999', '999999-999', '99999x9999']
    
    # Запуск программы для проверки списка
    validate_phone_numbers(phone_numbers_example)
