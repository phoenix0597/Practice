input_word_as_list = list(input("Введите слово: "))
replace_num = int(input("Какую букву заменить: "))
replace_sym = input("На что заменить: ")

# заменить букву под заданным номером в списке
input_word_as_list[replace_num - 1] = replace_sym

# вывести элементы списка как строку
for sym in input_word_as_list:
	print(sym, end="")

