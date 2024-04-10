# функция добавляет заданное число к каждому элементу последовательности
def add_num(seq, num):
	seq = list(seq)
	for i in range(len(seq)):
		seq[i] += num
	return seq


origin_tuple = (3, 1, 4, 1, 5)
changed_list = add_num(origin_tuple, 5)
print(origin_tuple)
print(changed_list)
