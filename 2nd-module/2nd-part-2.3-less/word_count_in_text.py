# count specific word in text
input_text = input("Введите текст: ")
word = input("Введите искомое слово: ")


def count_word_in_text(txt, wrd):
	return txt.lower().count(wrd.lower())


print(count_word_in_text(input_text, word))
