# Задание 5. Пароль
# Что нужно сделать
# При регистрации на сайте, помимо логина, нужно придумать пароль.
# Этот пароль должен состоять минимум из восьми символов, содержать хотя бы одну большую букву и не менее трёх цифр.
# Тогда он будет считаться надёжным.
#
# Напишите программу, которая просит пользователя придумать пароль до тех пор, пока этот пароль не станет надёжным.
# Должна использоваться латиница.
#
# Пример
# Придумайте пароль: qwerty.
# Пароль ненадёжный. Попробуйте ещё раз.
#
# Придумайте пароль: qwerty12.
# Пароль ненадёжный. Попробуйте ещё раз.
#
# Придумайте пароль: qwerty123.
# Пароль ненадёжный. Попробуйте ещё раз.
#
# Придумайте пароль: qWErty123.
# Это надёжный пароль.
def is_password_strong(passwd):
	if len(passwd) < 8:
		return False
	if not any(char.isupper() for char in passwd):
		return False
	if not any(char.isdigit() for char in passwd):
		return False
	if len([char for char in passwd if char.isdigit()]) < 3:
		return False
	return True


def is_string_contains_cyrillic(s):
	return any(char.lower() in s for char in "абвгдеежзийклмнопрстуфхцчшщъыьэюя")


while True:
	password = input("Придумайте пароль: ")
	if is_string_contains_cyrillic(password):
		print("Пароль содержит кириллицу. Попробуйте ещё раз.")
		continue
	if is_password_strong(password):
		print("Это надёжный пароль.")
		break
	else:
		print("Пароль ненадёжный. Попробуйте ещё раз.")
