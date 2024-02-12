# Задача 1. Заказ
# После того, как человек сделал заказ в интернет-магазине, ему на почту приходит оповещение
# с его именем и номером заказа.
# Напишите программу, которая получает на вход имя и код заказа, а затем выводит на экран соответствующее сообщение.
# Для решения используйте строковый метод format.
#
# Пример:
# Имя: Иван
# Номер заказа: 10948
#
# Здравствуйте, Иван! Ваш номер заказа: 10948. Приятного дня!

buyers_name = input("Имя: ")
order = input("Номер заказа: ")
print("Здравствуйте, {name}! Ваш номер заказа: {order}. Приятного дня!".format(
	name=buyers_name,
	order=order)
)