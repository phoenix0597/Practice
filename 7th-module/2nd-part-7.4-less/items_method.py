# Перебор ключей и значений в словаре. Метод items()
scores_dict = {
	'Миша': 54,
	'Ваня': 67,
	'Лена': 48
}

for key, value in scores_dict.items():
	print(key, value)