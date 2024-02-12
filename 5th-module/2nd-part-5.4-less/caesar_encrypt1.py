# Задача 8. Шифр Цезаря
# Что нужно сделать
# Юлий Цезарь использовал свой способ шифрования текста.
# Каждая буква заменялась на следующую по алфавиту через K позиций по кругу.
# Если взять русский алфавит и K = 3, то в слове, которое мы хотим зашифровать, буква А станет буквой Г,
# Б станет Д и так далее.
#
# Пользователь вводит сообщение, а также значение сдвига.
# Напишите программу, которая зашифрует это сообщение при помощи шифра Цезаря.
#
# Пример:
#
# Введите сообщение: это питон.
# Введите сдвиг: 3
# Зашифрованное сообщение: ахс тлхср.


def caesar_encrypt(char, shft):
	alfabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
	if char not in alfabet:  # если буква не из русского алфавита (или это символ) - не шифруем
		return char

	i_pos = alfabet.index(char)
	i_pos = (i_pos + shft) % 33  # сдвигаем, обеспечивая цикличность
	return alfabet[i_pos]


message = input("Введите сообщение: ").lower()
shift = int(input("Введите сдвиг: "))

encrypted_msg = [caesar_encrypt(char, shift) for char in message]
print("Зашифрованное сообщение: ", *encrypted_msg, sep='')
