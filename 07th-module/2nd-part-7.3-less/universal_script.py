# Задача 3. Универсальная программа
# Один заказчик попросил нас написать небольшой скрипт для своих криптографических нужд.
# При этом он заранее предупредил, что скрипт должен уметь работать с любым итерируемым типом данных.
#
# Напишите функцию, которая возвращает список из элементов итерируемого объекта (кортежа, строки, списка, словаря),
# у которых индекс чётный.
#
# Пример 1:
# Допустим, есть такая строка: 'О Дивный Новый мир!'
# Результат: ['О', 'Д', 'в', 'ы', ' ', 'о', 'ы', ' ', 'и', '!']
#
# Пример 2:
# Допустим, есть такой список: [100, 200, 300, 'буква', 0, 2, 'а']
# Результат: [100, 300, 0, 'а']
#
# Примечание: для проверки типа можно использовать функцию
# isinstance(<элемент>, <тип данных>), которая возвращает True, если элемент принадлежит к этому типу данных,
# и возвращает False в противном случае.

import random
import time


def get_even_elements(data):
	# если data не является словарем
	if not isinstance(data, dict):
		return [elem for ind, elem in enumerate(data) if ind % 2 == 0]
	# если data является словарем
	else:
		return [f'{key}: {value}' for ind, (key, value) in enumerate(data.items()) if ind % 2 == 0]


	
my_string = 'О Дивный Новый мир!'
my_list = [100, 200, 300, 'буква', 0, 2, 'а']
my_tuple = ('a', 1, 2, 3.4, 'b')
my_dict = {1: 'a', 2: 'b', 3: 'c'}

# создаем кортеж из вышеприведенных переменных
input_tuple = (my_string, my_list, my_tuple, my_dict)


input_enter = ''
while input_enter != 'exit':
	input_enter = input("Введите 'exit' для выхода или нажмите Enter для выбора случайного типа данных: ")
	if input_enter == 'exit':
		print("Всего доброго!")
		break
	else:
		# случайным образом выбираем элемент из кортежа input_tuple
		random_element = input_tuple[random.randint(0, len(input_tuple) - 1)]
		# проверяем тип выбранного элемента и в зависимости от полученного типа формируем сообщение о нем
		if isinstance(random_element, str):
			print("Допустим есть такая строка: ", random_element)
		elif isinstance(random_element, list):
			print("Допустим есть такой список: ", random_element)
		elif isinstance(random_element, tuple):
			print("Допустим есть такой кортеж: ", random_element)
		elif isinstance(random_element, dict):
			print("Допустим есть такой словарь: ", random_element)
	
	print("Результат (элементы с чётными индексами): ", get_even_elements(random_element))
	time.sleep(3)
	print()

