import requests
import json


def get_starship_information(starship_to_search: str) -> dict:
    """
    Получает информацию о звездолете и его пилотах с использованием SWAPI (Star Wars API).
    Args:
        starship_to_search (str): Название звездолета для поиска, например "X-wing".
    Returns:
        dict: Информация о звездолете, включая его название, класс, максимальную скорость и список пилотов.
        Каждый пилот представлен словарем, содержащим информацию о его имени, росте, весе, родной планете
        и URL родной планеты.
    """
    # Запрос к API для получения списка звездолетов, удовлетворяющих искомому названию
    response = requests.get(f'https://swapi.dev/api/starships/?search={starship_to_search}')
    # print(response.text)
    starships = json.loads(response.text).get('results', [])
    
    for starship in starships:
        if starship['name'].lower() == starship_to_search.lower():
            # Найден нужный звездолет, получаем информацию о пилотах
            pilots_info = []
            for pilot_url in starship['pilots']:
                pilot_response = requests.get(pilot_url)
                pilot_data = json.loads(pilot_response.text)
                
                # Запрос информации о родной планете пилота
                homeworld_response = requests.get(pilot_data['homeworld'])
                homeworld_data = json.loads(homeworld_response.text)
                
                pilots_info.append({
                    'name': pilot_data['name'],
                    'height': pilot_data['height'],
                    'mass': pilot_data['mass'],
                    'homeworld': homeworld_data['name'],
                    'homeworld_url': pilot_data['homeworld']
                })
            
            # Сохраняем и возвращаем полученные данные о звездолете и пилотах
            starship_data = {
                'ship_name': starship['name'],
                'starship_class': starship['starship_class'],
                'max_atmosphering_speed': starship['max_atmosphering_speed'],
                'pilots': pilots_info
            }
            
            # Записываем данные в JSON-файл
            with open('starship_information.json', 'w') as json_file:
                json.dump(starship_data, json_file, indent=4)
            
            return starship_data
    
    return {}


# Пример использования
starship_name = 'X-wing'
starship_info = get_starship_information(starship_name)
print(json.dumps(starship_info, indent=4))

# Ищем звездолет по имени, используя Star Wars API.
# После нахождения соответствующего звездолета он извлекает информацию о каждом из пилотов и их родных планетах.
# Полученные данные выводятся на экран и сохраняются в JSON-файл с названием `starship_information.json`.
# Приведенный пример поиска информации выполнен для звездолета "X-wing".
