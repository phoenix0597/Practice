# Входные данные:
# 1) Словарь - структура сайта, 2) Искомый ключ
# Выходные данные:
# 1) Значение ключа (None, если ключа нет)

site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}


def find_tag(struct, key):
	if key in struct:
		return struct[key]
	else:
		for sub_struct in struct.values():
			if isinstance(sub_struct, dict):
				val = find_tag(sub_struct, key)
				if val is not None:
					return val
		return None


user_key = input('Какой ключ ищем? ')
value = find_tag(site, user_key)

if value is None:
	print('Такого ключа в структуре сайта нет')
else:
	print(value)
	