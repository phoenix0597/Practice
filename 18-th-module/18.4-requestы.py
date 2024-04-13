import requests
import json

response = requests.get("https://swapi.dev/api/planets/3/")
json_data = json.loads(response.text)  # десериализация JSON (так мы в т.ч. избегаем любых проблем со спецзнаками)
# print(json_data)

json_data['name'] = "Kamino"
# print(json_data['name'])

with open("my_test.json", "w") as file:
    json.dump(json_data, file, indent=4)  # сериализация JSON

with open("my_test.json", "r") as file:
    json_data = json.load(file)  # десериализация JSON - load / dump - работа с файлами
    # load() - читает из файла, dump() - записывает в файл
    # load() лучше использовать после десериализации JSON

print(json_data)
