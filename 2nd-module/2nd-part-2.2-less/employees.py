pass_id_list = []

# how many employees we have?
number_of_employees = int(input("Количество сотрудников в офисе: "))

# fill list with IDs
for _ in range(number_of_employees):
    pass_id_list.append(int(input("ID сотрудника: ")))

# number of employees
num_employees = len(pass_id_list)


# check if ID is in the list
def check_id_in_list(id_list, emp_id):
    if emp_id in id_list:
        print("Сотрудник на месте")
    else:
        print("Сотрудник не работает!")


# input ID
id_to_check = int(input("Какой ID ищем? "))


check_id_in_list(pass_id_list, id_to_check)
