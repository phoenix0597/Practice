import requests
import json

# Получение данных о корабле X-wing
xwing_url = "https://swapi.dev/api/starships/12/"
response = requests.get(xwing_url)
xwing_data = response.json()

# Извлечение данных о пилотах
pilots_data = []
for pilot_url in xwing_data["pilots"]:
    response = requests.get(pilot_url)
    pilot_data = response.json()
    pilots_data.append({
        "name": pilot_data["name"],
        "height": pilot_data["height"],
        "mass": pilot_data["mass"],
        "homeworld": pilot_data["homeworld"],
        "homeworld_url": pilot_data["homeworld_url"]
    })

# Формирование данных о корабле
xwing_info = {
    "ship_name": xwing_data["name"],
    "starship_class": xwing_data["starship_class"],
    "max_atmosphering_speed": xwing_data["max_atmosphering_speed"],
    "pilots": pilots_data
}

# Вывод информации в консоль
print(xwing_info)

# Запись информации в JSON-файл
with open("xwing_info.json", "w") as f:
    json.dump(xwing_info, f, indent=4)
