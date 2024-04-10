# input number of elements in list
count = int(input("Введите количество элементов в списке: "))

# input elements of list
num_list = []
for _ in range(count):
	element = input("Введите элемент списка: ")
	num_list.append(element)

# input the multiplicity number
multiplicity = int(input("\nВведите делитель: "))
print()

# find indexes numbers that are multiples of the given one, print them and evaluate the sum of indexes
multiples_indexes = []
sum_multiples = 0
index_sum = 0
for i in range(count):
	number = int(num_list[i])
	if number % multiplicity == 0:
		print(f"Индекс числа {number}: {i}")
		index_sum += i

print("\nСумма индексов:", index_sum)
