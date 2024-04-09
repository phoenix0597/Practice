# Задача 1. Новые списки
# Что нужно сделать
# Даны три списка:
#
# floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
# names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
# numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
# Напишите код, который создаёт три новых списка. Вот их содержимое:
#
# Каждое число из списка floats возводится в третью степень и округляется до трёх знаков после запятой.
# Из списка names берутся только имена минимум из пяти букв.
# Из списка numbers берётся произведение всех чисел.
from typing import List
from functools import reduce

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

floats_1: List[float] = list(map(lambda x: round(x ** 3, 4), floats))
names_1: List[str] = list(filter(lambda x: len(x) >= 5, names))
numbers_1: int = reduce(lambda x, y: x * y, numbers)

print(floats_1, names_1, numbers_1, sep="\n")
