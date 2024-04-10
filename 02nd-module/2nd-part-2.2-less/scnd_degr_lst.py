# Task "The second degree of list's elements" (2.1 Списки и их инициализация)
numbers_list = [1, 5, 2, -7, 6]

# append 5 elements to the list by input
for _ in range(1):
	try:
		new_num = int(input("Введите число: "))
	except ValueError:
		print("Вы ввели не число!")
		continue
	numbers_list.append(new_num)

# print the second degree of each element of the list
for number in numbers_list:
	print(number, "** 2 =", number ** 2)
