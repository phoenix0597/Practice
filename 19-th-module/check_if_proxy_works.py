import requests

# Параметры прокси-сервера
proxy = {
    'http': 'http://xtTMe2Ve:9tEWqdD1@46.232.26.187:64334',
    'https': 'http://xtTMe2Ve:9tEWqdD1@46.232.26.187:64334'
}

# URL сервиса для проверки IP-адреса
url = 'https://httpbin.org/ip'

try:
    # Запрос с использованием прокси-сервера
    response = requests.get(url, proxies=proxy)
    data = response.json()
    print(f'IP-адрес, который видит сайт через прокси: {data["origin"]}')
except requests.exceptions.RequestException as e:
    print(f"Ошибка при подключении через прокси: {e}")

# Проверка реального IP-адреса
try:
    # Прямой запрос без использования прокси-сервера
    response_direct = requests.get(url)
    data_direct = response_direct.json()
    print(f'Ваш реальный IP-адрес: {data_direct["origin"]}')
except requests.exceptions.RequestException as e:
    print(f"Ошибка при прямом подключении: {e}")
