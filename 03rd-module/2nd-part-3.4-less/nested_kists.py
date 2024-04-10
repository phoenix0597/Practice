# список, элементы которого являются списками
# например, вложенные списки состоят из слова и цифры,
# означающей количество раз, которые это слово встречается в тексте
words_count_list = [['', 0], ['', 0], ['', 0]]

for i_num in range(3):
	print("Введите", i_num + 1, "-е слово:", end=" ")
	words_count_list[i_num][0] = input()

text_word = input("Слово из текста: ")
while text_word != "end":
	for i_num in range(3):
		if text_word == words_count_list[i_num][0]:
			words_count_list[i_num][1] += 1
	text_word = input("Слово из текста: ")

print("Подсчет слов в тексте: ")
for index in range(3):
	print("Слово", words_count_list[index][0], "встречается", words_count_list[index][1], "раз")