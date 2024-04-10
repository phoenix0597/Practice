def histogram(string):
	# создаем словарь для хранения частоты встречаемости букв
	letter_freq = {}
	for let in string:
		if let in letter_freq:
			letter_freq[let] += 1
		else:
			letter_freq[let] = 1
	return letter_freq


# запрашиваем у пользователя текст, который приводим к нижнему регистру
text_input = input("Введите текст: ").lower().strip()
hist = histogram(text_input)
print(sorted(hist))
print(hist)

# выводим на экран буквы в алфавитном порядке и их частоты встречаемости
for letter in sorted(hist.keys()):
	print(f"{letter}: {hist[letter]}")

print("Максимальная частота встречаемости: ", max(hist.values()))
