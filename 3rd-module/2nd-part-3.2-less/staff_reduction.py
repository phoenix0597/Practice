# Задача 2. Сокращения
# В одной компании наступили «тёмные времена», и сотрудников стали сокращать.
# Зарплаты сотрудников хранятся в списке из N этих самых зарплат.
# Зарплаты уже уволенных сотрудников обозначаются в списке числом 0.
#
# Напишите программу, которая запрашивает у пользователя количество сотрудников и их зарплаты,
# затем удаляет все элементы списка со значением 0 и выводит в консоль,
# сколько сотрудников осталось, а также их зарплаты.
# Дополнительный список использовать нельзя.
def staff_hiring():
	salaries_list = []
	num_employees = int(input("Введите количество сотрудников: "))

	for i in range(num_employees):
		salary = int(input(f"Введите заработную плату сотрудника {i + 1}: "))
		salaries_list.append(salary)
	return salaries_list


def staff_reduction(salaries_list):
	for staff_sal in salaries_list:
		if staff_sal == 0:
			salaries_list.remove(staff_sal)
	print(f"Осталось сотрудников {len(salaries_list)}.\nЗарплаты: {salaries_list}")


salaries = staff_hiring()
staff_reduction(salaries)
