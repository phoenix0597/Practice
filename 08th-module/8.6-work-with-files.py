# Задача. Работа с файлами.
# Входные данные:
# Функция, в которую передается:
# Вопрос
# Сообщение о неверном вводе
# Количество попыток
#
# Выходные данные:
# Если "да" - вернуть 1; если "нет" - вернуть 0.
# "Осталось попыток" и "Неверный ввод"

def ask_user(question, complaint="Неверный ввод. Пожалуйста, введите 'да' или 'нет'", retries=4):
	while True:
		answer = input(question).lower()
		if answer == "да":
			return 1

		elif answer == "нет":
			return 0

		retries -= 1
		if retries == 0:
			print("Количество попыток исчерпано.")
			break

		print(complaint)
		print("Осталось попыток:", retries)


ask_user("Вы действительно хотите выйти? ")
ask_user("Удалить файл? ")
ask_user("Записать файл? ")