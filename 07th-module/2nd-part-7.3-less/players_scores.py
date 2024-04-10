scores = [54, 67, 48, 99, 27]
# функция enumerate генерирует кортежи, состоящие из индекса и значения элементов итерируемого объекта
# (в данном случае - списка)
# for i_player, i_score in enumerate(scores):
# 	print(i_player, i_score)
	
# syms_list = ['a', 'b', 'c']
# gen = enumerate(syms_list)
# print(gen)

syms_list = ['a', 'b', 'c']
my_dict = {11: syms_list, 24: syms_list[::-1]}
# for _, (key, value) in enumerate(my_dict.items()):
for ind, (key, value) in enumerate(my_dict.items()):
	print(ind, key, value)
