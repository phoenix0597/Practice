# Задача 7. Список списков
# Что нужно сделать
# Дан многомерный список:
#
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# Напишите код, который «раскрывает» все вложенные списки, то есть оставляет только внешний список.
# Для решения используйте только list comprehensions.
#
# Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# nice_list = [1, 2, 3, 4, 5, 6]
# output = [digit for digit in nice_list]
# print(output)

# nice_list = [[1, 2], [3, 4], [5, 6]]
# # output = [digit for digit in each_list for each_list in nice_list]
# output = [digit for each_list in nice_list for digit in each_list]
# print(output)

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
output = [digit for each_list in nice_list for each_list_2 in each_list for digit in each_list_2]
print(output)