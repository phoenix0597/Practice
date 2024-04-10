numbers_list = [3, 7, 5]

while True:
	number = int(input('Новое число: '))
	numbers_list.append(number)
	print('Текущий список чисел:', numbers_list)

	for i in numbers_list:
		print(i ** 2, i ** 3, i ** 4)

	print()
