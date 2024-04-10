phonebook_dict = {
	"Ваня": 88005555555,
	"Петя": 88001111111,
	"Лена": 88002222222,
}

name = input("Введите имя: ")
if name in phonebook_dict:
	print(phonebook_dict[name])
else:
	print("Ошибка: человек с именем {} не найден".format(name))