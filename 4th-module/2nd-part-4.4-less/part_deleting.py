# Задача 3. Удаление части
# Дан список из N чисел, а также числа А и В (можно сгенерировать случайно, при этом А < B). Напишите программу,
# которая удаляет элементы списка с индексами от А до В. Не используйте дополнительные переменные и методы списков.
import random


def get_borders():
	left_ind = random.randint(0, 8)
	right_ind = random.randint(0, 9)
	while left_ind >= right_ind:
		right_ind = random.randint(0, 9)
	return [left_ind, right_ind]


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
borders = get_borders()
left_index, right_index = borders[0], borders[1]
print("Левый индекс: ", left_index)
print("Правый индекс: ", right_index)

num_list[left_index:right_index+1] = []  
print(num_list)
