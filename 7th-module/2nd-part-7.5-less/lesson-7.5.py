# кортежи - неизменяемые списки, как ключи в словарях (на языке базы данных)
phonebook = {
	('Петров', 'Ваня'): '703-493-1834',
	('Егоров', 'Ваня'): '857-384-1234',
	('Ульянов', 'Петя'): '484-584-2923',
	('Сидорова', 'Лена'): '484-584-2923'
}

print(phonebook)

phonebook[('Сидорова', 'Алена')] = '109090'

print(phonebook)
print()

# получим фамилии,имена и телефоны людей, фамилия которых - 'Сидорова'
for key, value in phonebook.items():
	if 'Сидорова' in key:
		print(key, value)
print()

for i_person, i_phone in phonebook.items():
	if 'Сидорова' in i_person:
		print(' '.join(i_person), '-', i_phone)

# решение с помощью ID и словарей
# phonebook_1 = {
# 	1: {'surname': 'Петров', 'name': 'Ваня', 'phone': '703-493-1834'},
# 	2: {'surname': 'Егоров', 'name': 'Ваня', 'phone': '857-384-1234'},
# 	3: {'surname': 'Ульянов', 'name': 'Петя', 'phone': '484-584-2923'},
# 	4: {'surname': 'Сидорова', 'name': 'Лена', 'phone': '484-584-2923'}
# }
#
# print(phonebook_1)
