# Задача 3. Поиск элемента
# Когда мы работаем с большой многоуровневой структурой, нам нередко необходимо пройтись по ней и найти нужный элемент.
# Для этого в программировании используются специальные алгоритмы поиска.
#
# Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт значение этого ключа на экран.
# В качестве примера можно использовать такой словарь:
#
# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
# Пример 1:
# Искомый ключ: h2
# Значение: Здесь будет мой заголовок
#
# Пример 2:
# Искомый ключ: abc
# Такого ключа в структуре сайта нет.

site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}


def find_element(struct, key):
	if key in struct:
		return struct[key]
	else:
		for sub_struct in struct.values():
			if isinstance(sub_struct, dict):
				val = find_element(sub_struct, key)
				if val:  # if val is not None:
					return val
		return None


user_key = input('Какой ключ ищем? ')
value = find_element(site, user_key)
print(value)