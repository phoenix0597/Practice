import requests
import json


def fetch_starship_info(starship_id):
    starship_url = f"https://swapi.dev/api/starships/{starship_id}/"
    response = requests.get(starship_url)
    starship_data = response.json()
    
    x_wing_info = {
        "ship_name": starship_data["name"],
        "starship_class": starship_data["starship_class"],
        "max_atmosphering_speed": starship_data["max_atmosphering_speed"],
        "pilots": []
    }
    
    for pilot_url in starship_data["pilots"]:
        pilot_data = requests.get(pilot_url).json()
        pilot_info = {
            "name": pilot_data["name"],
            "height": pilot_data["height"],
            "mass": pilot_data["mass"],
            "homeworld": requests.get(pilot_data["homeworld"]).json()["name"],
            "homeworld_url": pilot_data["homeworld"]
        }
        x_wing_info["pilots"].append(pilot_info)
    
    return x_wing_info


x_wing_info = fetch_starship_info(12)
print(json.dumps(x_wing_info, indent=4))

# Сохраняем информацию в файл
with open("x_wing_info.json", "w") as file:
    json.dump(x_wing_info, file, indent=4)

# Программа выполняет следующие шаги:
# 1. Запрашивает данные о корабле X-wing, используя его ID (12).
# 2. Перебирает URL пилотов этого корабля, выполняя запросы для получения информации о каждом пилоте
# и его родной планете.
# 3. Формирует структурированные данные о корабле и его пилотах.
# 4. Выводит полученные данные в консоль и сохраняет их в JSON-файл.
