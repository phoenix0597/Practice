# Задание 6. Сжатие
# Что нужно сделать
# Из-за того, что объём данных увеличился, понадобилось сжать эти данные, но так, чтобы не потерять важную информацию.
# Для этого было придумано специальное кодирование: s = 'aaaabbсaa' преобразуется в 'a4b2с1a2'.
# То есть группы одинаковых символов исходной строки заменяются на эти символы и количество их повторений в строке.
#
# Напишите программу, которая считывает строку, кодирует её, используя предложенный алгоритм,
# и выводит закодированную последовательность на экран. Код должен учитывать регистр символов.
#
# Пример
# Введите строку: aaAAbbсaaaA.
# Закодированная строка: a2A2b2с1a3A1.
# Write a code that converts the string like 'aaaabbсaa' into 'a4b2с1a2'
def compress_string(input_str):
	compressed_str = ""
	count = 1
	for i in range(len(input_str) - 1):
		if input_str[i] == input_str[i + 1]:
			count += 1
		else:
			compressed_str += input_str[i] + str(count)
			count = 1
			
	compressed_str += input_str[-1] + str(count)
	return compressed_str


input_string = input("Введите строку: ")
compressed_string = compress_string(input_string)
print("Закодированная строка:", compressed_string)
