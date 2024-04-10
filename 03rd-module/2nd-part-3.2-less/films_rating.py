films = [
	'Крепкий орешек', 'Назад в будущее', 'Таксист',
	'Леон', 'Богемская рапсодия', 'Город грехов',
	'Мементо', 'Отступники', 'Деревня',
	'Проклятый остров', 'Начало', 'Матрица'
]

my_list = []

while True:
	print('\nВаш текущий рейтинг фильмов:', my_list)
	new_movie = input('Введите название фильма: ')

	if new_movie in films:
		command = input('\nВведите действие (добавить/удалить/вставить): ')
		if command == 'добавить' and new_movie not in my_list:
			my_list.append(new_movie)
		elif command == 'удалить':
			my_list.remove(new_movie)
		elif command == 'вставить':
			place = int(input('Введите место вставки: '))
			my_list.insert(place - 1, new_movie)
	else:
		print('Такого фильма нет на сайте.')

print(my_list)
