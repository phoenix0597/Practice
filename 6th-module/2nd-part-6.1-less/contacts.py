# Задача 3. Контакты
# Энтузиаст Степан, купив новый телефон, решил написать для него свою собственную операционную систему.
# И, конечно же, первое, что он захотел в ней реализовать, — это телефонная книга.
#
# Напишите программу, которая запрашивает у пользователя имя контакта и номер телефона,
# добавляет их в словарь и выводит на экран текущий словарь контактов.
# Запрос на добавление идёт бесконечно (но можно задать своё условие для завершения программы).
# Обеспечьте контроль ввода: если это имя уже есть в словаре, то выведите соответствующее сообщение.
#
# Пример:
# Текущие контакты на телефоне:
# <Пусто>
# Введите имя: Иван
# Введите номер телефона: 100200300
#
# Текущие контакты на телефоне:
# Иван  100200300
#
# Введите имя: Лена
# Введите номер телефона: 8005555522
#
# Текущие контакты на телефоне:
# Иван  100200300
# Лена  8005555522
#
# Введите имя: Иван
# Ошибка: такое имя уже существует.
def print_contacts(phonebook):
	print("\nТекущие контакты на телефоне:\n", end='')
	if len(phonebook) == 0:
		contacts = '<Пусто>'
		print(contacts)
	else:
		for key in phonebook:
			contacts = key + '  ' + phonebook[key]
			print(contacts)
	return


def add_contact(phonebook):
	while True:
		print_contacts(phonebook)
		name = input("Введите имя (для завершения введите 'стоп'): ")
		if name in phonebook:
			print("Ошибка: такое имя уже существует.")
			continue
		elif name == 'стоп':
			break
		else:
			phone = input("Введите номер телефона: ")
			phonebook[name] = phone
	return


phonebook_dict = {}
add_contact(phonebook_dict)
