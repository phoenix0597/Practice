# Задача 3. May the force be with you
# Что нужно сделать
# Фанаты «Звёздных войн» (Star Wars) написали API по своей любимой вселенной. Ссылка на документацию: Documentation.
#
# Внимательно изучите документацию этого API и напишите программу, которая выводит на экран (и в JSON-файл)
# информацию о пилотах легендарного истребителя X-wing.
#
# Информация о корабле должна содержать следующие пункты:
#
# название,
# максимальная скорость,
# класс,
# список пилотов.
# Внутри списка о каждом пилоте должна быть следующая информация:
#
# имя,
# рост,
# вес,
# родная планета,
# ссылка на информацию о родной планете.

import requests
import json

url = 'https://swapi.dev/api/starships/12/'

req = requests.get(url)
data = json.loads(req.text)

print(json.dumps(data, indent=4))

pilots = []
for pilot in data['pilots']:
    req_2 = requests.get(pilot)
    data_2 = json.loads(req_2.text)
    pilots.append({
        'name': data_2['name'],
        'height': data_2['height'],
        'mass': data_2['mass'],
        'homeworld': data_2['homeworld'],
    })

data['pilots'] = pilots

with open('x-wing.json', 'w') as file:
    json.dump(data, file, indent=4)
