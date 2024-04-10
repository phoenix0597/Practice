# Задача 2. Сервер
# У вас есть данные о сервере, которые хранятся в виде вот такого словаря:
# server_data = {
#     "server": {
#         "host": "127.0.0.1",
#         "port": "10"
#     },
#     "configuration": {
#         "access": "true",
#         "login": "Ivan",
#         "password": "qwerty"
#     }
# }
#
# Напишите программу, которая выводит для пользователя эти данные так же красиво и понятно,
# как они представлены в словаре.
#
# Результат работы программы:
# server:
#     host: 127.0.0.1
#     port: 10
# configuration:
#     access: true
#     login: Ivan
#     password: qwerty


server_data = {
	"server": {
		"host": "127.0.0.1",
		"port": "10"
	},
	"configuration": {
		"access": "true",
		"login": "Ivan",
		"password": "qwerty"
	}
}

print('\n{server_data}\n'.format(server_data=server_data))

for key, value in server_data.items():
	print('{key}:'.format(key=key))
	for key2, value2 in value.items():
		print('\t{key2}: {value2}'.format(
			key2=key2,
			value2=value2
		))