# def from_string(cls, date_as_string):
#     year, month, day = map(int, date_as_string.split('-'))
#     date = cls(year, month, day)
from typing import List


my_nums: List[int] = [3, 1, 4, 1, 5, 9, 2, 6]
other_nums: List[int] = [2, 7, 1, 8, 2, 8, 1, 8, 9]

# сложим два списка
result: List[int] = list(map(lambda x, y: x + y, my_nums, other_nums))
print(result)

result1 = list(map(lambda x, y: 1, [1, 2], [2, 3, 4]))
print(result1)

# print([*result])

animals = ['cat', 'dog', 'cow']

# Нужно ['Cat', 'Dog', 'Cow']
# Вариант-1 (с помощью map, lambda)
print(list(map(lambda animal: animal.capitalize(), animals)))

# Вариант-2 (с помощью list comprehension)
print([animal.capitalize() for animal in animals])

# Как выбрать - что использовать в конкретном случае?
# 1. Функцию map удобно использовать, если нам не нужны сразу все значения (для т.н. ленивых вычислений)
# 2. Функция map ОБЫЧНО быстрее чем list comprehension, особенно, если вместо lambda использовать заранее объявленную
# функцию (но только, если выражение довольно короткое или простое, в противном случае list comprehension будет быстрее)

# result_even = list(filter(lambda x: x % 2 == 0, result))
result_even: List[int] = list(filter(lambda x: x % 2 == 0, result))
print(result_even)

result_2: List[int] = list(map(lambda num: num * 3, filter(lambda num: num % 2 == 0, my_nums)))
print(result_2)

# Такими конструкциями лучше не увлекаться, т.к. они очень быстро повышают сложность кода и дальнейшее его сопровождение
result_3: int = sum(map(lambda num: num * 3, filter(lambda num: num % 2, my_nums)))
print(result_3)

my_nums4 = [0, 1, 4, 1, 5, 9, 2, 6]
# В таком случае будут возвращаться только те значения, которые являются истинными
# (в данном случае, все, кроме 0, который будет преобразован в False) - т.е. [1, 4, 1, 5, 9, 2, 6]
result4: List[int] = list(filter(None, my_nums4))
print(result4)