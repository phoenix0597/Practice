# Дана строка S и номер позиции символа в строке.
# Напишите программу, которая выводит соседей этого символа и сообщение о количестве таких же символов
# среди этих соседей: их нет, есть ровно один или есть два таких же.
# Пример 1:
# Введите строку: abbc
# Номер символа: 3
#
# Символ слева: b
# Символ справа: c
#
# Есть ровно один такой же символ.

# Пример 2:
# Введите строку: abсd
# Номер символа: 3
#
#
# Символ слева: b
# Символ справа: d
#
# Таких же символов нет.

input_word = input("Введите строку: ")
input_sym_num = int(input("Номер символа: "))


def find_sym(inp_word, inp_sym_num):
	input_word_as_list = list(inp_word)
	same_sym_count = 0
	left_sym = input_word_as_list[inp_sym_num - 2]
	right_sym = input_word_as_list[inp_sym_num]
	if left_sym == input_word_as_list[inp_sym_num - 1]:
		same_sym_count += 1
	if right_sym == input_word_as_list[inp_sym_num - 1]:
		same_sym_count += 1

	return left_sym, right_sym, same_sym_count


l_sym = find_sym(input_word, input_sym_num)[0]
r_sym = find_sym(input_word, input_sym_num)[1]
same_sym = find_sym(input_word, input_sym_num)[2]

if same_sym == 2:
	mess_about_count = "Есть два таких же символа"
elif same_sym == 1:
	mess_about_count = "Есть ровно один такой же символ."
else:
	mess_about_count = "Таких же символов нет."


print(f"Символ слева: {l_sym}")
print(f"Символ справа: {r_sym}\n")
print(mess_about_count)
