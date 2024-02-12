def try_to_change_values(some_list, num):
	for index, value in enumerate(some_list):
		some_list[index] += 10
	num += 10


my_list = [1, 2, 3]
number = 100

print(my_list, number)
try_to_change_values(my_list, number)
print(my_list, number)
