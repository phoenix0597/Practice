from typing import List

users: List[str] = ['user1', 'user2', 'user30', 'user3', 'user22', 'user100']
sorted_users = sorted(users, key=lambda elem: int(elem[4:]))
print(sorted_users)


# lambda может также быть присвоена переменной
# хорошее использование (соответствует PEP8)
def f(a): return a + 10


print(f(5))

# ПЛОХОЕ ИСПОЛЬЗОВАНИЕ (не соответствует PEP8 - его следует избегать)
# 1. Использование оператора присвоения вместо def
f = lambda a: a * 2

# 2. Вызов исключения в lambda-выражении
def some_exception(ex): raise ex  # плохо
(lambda: some_exception(Exception('Какая-то ошибка')))()  # плохо

# 3. Написание в стиле Cryptonic style
(lambda _: list(map(lambda _: _ // 3, _)))([1, 2, 3, 4, 5])  # плохо, т.к. такой краткий код трудно читать
# [1, 2, 3, 4, 5]


# 4. Lambda, как метод класса
class Person:
    def __init__(self, name: str, age: int) -> None:
       pass
    
    name = property(lambda self: getattr(self._name),
                    lambda self, value: setattr(self, '._name', value))  # плохо


# Общие проблемы плохого использования lambda, которые не вяжутся с Pythonic-кодом:
# - каждый из них не следует руководству по стилю Python (PEP8)
# - код выглядит громоздким и трудночитаемым

print(f(5))
