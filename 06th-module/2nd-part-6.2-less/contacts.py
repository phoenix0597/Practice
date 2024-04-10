# Дано:  два словаря, содержащие информацию о контактах: имя и телефон.
# Нужно их объединить в один словарь, где ключ - имя, значение - список телефонов
first_phonebook = {
	'Ваня': '123456789',
	'Петя': '987654321',
	'Алиса': '123456789'
}

second_phonebook = {
	'Игорь': '987654321',
	'Петя': '123456789',
	'Алена': '123456789'
}

# при объединении двух словарей и совпадении ключей необходимо оставить значения из второго словаря
first_phonebook.update(second_phonebook)

first_phonebook['Гоша'] = first_phonebook.pop('Игорь')
print(first_phonebook.get('Степан', 'Такого нет'))

# print(first_phonebook)

# при объединении двух словарей и совпадении ключей необходимо оставить значения из второго словаря
# merged_phonebook = first_phonebook | second_phonebook
# print("merged_dict_1 = first_phonebook | second_phonebook:\n", merged_phonebook)
print("first_dict.update(second_dict):\n", first_phonebook)
