# Задача 2. Непонятно!
# Друг никак не может понять эту тему с изменяемыми и неизменяемыми типами, ссылками, объектами и их id.
# Видя, как он мучается, вы решили помочь ему и объяснить эту тему наглядно.
#
# Пользователь вводит любой объект. Напишите программу, которая выводит на экран тип введённых данных,
# информацию о его изменяемости, а также id этого объекта.
#
# Помните, что через input можно получить только строку, что бы вы ни вводили.
# В данном случае ввод можно выполнить вручную, просто вписав нужный объект в переменную,
# без использования функции input.
#
#
# Пример 1:
# Введите данные: привет
# Тип данных: str (строка)
# Неизменяемый (immutable)
# Id объекта: 1705156583984
#
# Пример 2:
# Введите данные: {‘a’: 10, ‘b’: 20}
# Тип данных: dict (словарь)
# Изменяемый (mutable)
# Id объекта: 1705205308536


def check_type(arg):
    arg_type = type(arg).__name__
    if isinstance(arg, (list, dict, set)):
        arg_kind = "изменяемый"
    else:
        arg_kind = "неизменяемый"
    print(f"\nИнформация об объекте {arg}:\n\tТип: {arg_type}, Вид: {arg_kind}\n\tId: {id(arg)}")


check_type(42)
check_type(3.14)
check_type("hello")
check_type((1, 2, 3))
check_type(True)
check_type([1, 2, 3])
check_type({"key": "value"})
check_type({1, 2, 3})
