def count_word_in_text(txt, wrd):
	return txt.lower().count(wrd.lower())


# count specific word in text
input_text = input("Введите текст: ")
for i in range(3):
	print("Введите", i + 1, "слово: ", end="")
	word = input()
	print(count_word_in_text(input_text, word))
