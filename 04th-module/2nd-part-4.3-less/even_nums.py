# Задача 1. Список чётных чисел
# Пользователь вводит два числа: А и В. Реализуйте код, который генерирует список из чётных чисел в диапазоне от А до B.
# Используйте list comprehensions (как и в следующих задачах).
from_num = int(input("A: "))
to_num = int(input("B: "))
even_nums = [x for x in range(from_num, to_num + 1) if x % 2 == 0]
print(even_nums)