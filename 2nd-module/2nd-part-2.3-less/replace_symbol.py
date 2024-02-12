# input word, input symbol to replace number,
# input symbol to paste instead of replaced symbol,
# get new word with replaced symbol
def replace_symbol(input_word, sym_num_to_replace, sym_to_paste):
	new_word = ""
	for i in range(len(input_word)):
		if i + 1 == sym_num_to_replace:
			new_word += sym_to_paste
		else:
			new_word += input_word[i]
	return new_word


word = input("Введите слово: ")
symbol_num_to_replace = int(input("Введите номер символа для замены: "))
symbol_to_paste = input("Введите заменяющий символ: ")


replaced_word = replace_symbol(word, symbol_num_to_replace, symbol_to_paste)
print("Новое слово: ", replaced_word)



