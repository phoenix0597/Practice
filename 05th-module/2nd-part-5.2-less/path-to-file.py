user_name = input("Введите пользователя: ")
file_name = input("Введите имя файла: ")

path = f"C:\\Users\\{user_name}\\Desktop\\{file_name}.txt"
path_1 = "C:\\Users\\{0}\\Desktop\\{1}.txt".format(
	user_name,
	file_name
)

path_2 = "C:/Users/{user}/Desktop/{file}.txt".format(
	user=user_name,
	file=file_name
)

print(path)
