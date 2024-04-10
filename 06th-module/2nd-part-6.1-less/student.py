# Пример ввода:
# Илья Иванов Москва МГУ 5 4 4 4 5
# Написать программу, которая из всей этой информации создаст словарь и выведет его на экран
student_str = input(
	"Введите информацию о студенте через пробел\n"
	"(имя, фамилия, город, место учебы, оценки): "
)

student_info = student_str.split()
student = dict()
student["Имя"] = student_info[0]
student["Фамилия"] = student_info[1]
student["Город"] = student_info[2]
student["Место учебы"] = student_info[3]
student["Оценки"] = []
for grade in student_info[4:]:
	student["Оценки"].append(int(grade))

print('\n', student, '\n')

for key in student:
	print(key, '-', student[key])
