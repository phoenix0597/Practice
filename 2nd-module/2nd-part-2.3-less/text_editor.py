# Пользователь вводит строку S.
# Напишите программу, которая заменяет в строке все двоеточия (:) на точки с запятой (;).
# Также подсчитайте количество замен и выведите ответ на экран (и новую строку тоже).
# Для решения используйте list
# Пример:
# Введите строку: гвозди:шурупы:гайки
# Исправленная строка: гвозди;шурупы;гайки
# Кол-во замен: 2


text = input("Введите строку: ")
# text = "гвозди:шурупы:гайки:гвозди:шурупы:гайки"


def change_string(txt, substr1, substr2):
	sym_list = list(txt)
	count = 0
	for i in range(len(sym_list)):
		if sym_list[i] == substr1:
			sym_list[i] = substr2
			count += 1

	changed_text = ''.join(sym_list)
	return changed_text, count


new_text = change_string(text, ":", ";")[0]
repl_count = change_string(text, ":", ";")[1]
print("Исправленная строка: ", new_text)
print("Кол-во замен: ", repl_count)
