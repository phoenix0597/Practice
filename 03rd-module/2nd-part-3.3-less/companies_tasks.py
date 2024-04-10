# 3.3. Вывести список всех задач, которые должен выполняться на всех компаниях.
def get_comp_tasks_signs_list(comp_amount):
	comp_names_list = []
	company_tasks_signs_list = []
	for i_comp in range(comp_amount):
		if i_comp == 0:
			comp_name = "main_company"
		else:
			comp_name = f"company_{i_comp}"

		comp_names_list.append(comp_name)
		signs = input(f"Укажите признаки выполнения всех имеющихся задач {comp_name} (1 - выполнена / 0 - нет): ")
		signs_list = list(signs)

		# check the correctness of input: should be only 1 or 0 in the sequence of signs
		i_signs = 0
		while i_signs < len(signs_list):
			if signs_list[i_signs] != "1" and signs_list[i_signs] != "0":
				print("Неправильный ввод. Повторите ввод.")
				signs = input(f"Укажите признаки выполнения всех имеющихся задач {comp_name} (1 - выполнена / 0 - нет): ")
				signs_list = list(signs)
			i_signs += 1

		company_tasks_signs_list.append(signs_list)
	return comp_names_list, company_tasks_signs_list


tot_comp_amount = int(input("Введите количество объединяемых компаний: "))
total_companies_tasks = get_comp_tasks_signs_list(tot_comp_amount)
tot_tasks_extended = []
for i in range(len(total_companies_tasks[1])):
	print(f"{total_companies_tasks[0][i]} = {total_companies_tasks[1][i]}")
	tot_tasks_extended.extend(total_companies_tasks[1][i])

print("\nОбщий список задач: ", tot_tasks_extended)
print("Количество невыполненных задач: ", tot_tasks_extended.count("0"))
