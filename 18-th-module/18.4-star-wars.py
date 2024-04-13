# Задача 1. Звёздные войны
# Повторите пример парсинга, разобранный в уроке: перейдите на сайт с API, посвящённый вселенной Star Wars.
#
# После этого сгенерируйте реквест-ссылку на данные о человеке под номером 3 (people/3/).
#
# Затем напишите программу, которая парсит данные об этом человеке, изменяет его имя на ваше собственное
# и сохраняет результат в виде JSON-файла.
#
# Дополнительно: обратите внимание на значение ключа homeworld — там также хранится ссылка.
# В том же коде спарсите эту ссылку и посмотрите, что там.
#
# Примечание: API тоже пишут люди, а значит, время от времени его могут как-то менять и усовершенствовать,
# поэтому будьте внимательны: может быть, ссылка уже хранится в другом ключе.
import requests
import json
import re


def is_url(string):
    url_pattern = \
        r'^(https?://)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$'
    return bool(re.match(url_pattern, string))


req = requests.get('https://swapi.dev/api/people/3/')
data = json.loads(req.text)
print(data)

data['name'] = 'R10-D10'
with open('my_test.json', 'w') as file:
    json.dump(data, file, indent=4)

if is_url(data['homeworld']):
    req_2 = requests.get(data['homeworld'])
    data_2 = json.loads(req_2.text)
    print(data_2)
else:
    print('No homeworld')
