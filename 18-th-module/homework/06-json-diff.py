# Задача 6. Поиск разницы между двумя JSON-файлами (пример из реального тестового задания
# на должность Python-разработчика уровня Junior)
# Что нужно сделать.
# Найдите различия между двумя JSON-файлами. Если различающиеся параметры входят в diff_list, выведите различие.
# Иными словами, вам нужно отловить изменение определённых параметров и вывести значение: что изменилось и на что.
# Набор ключей в обоих файлах идентичный, различаются лишь значения.
#
# Напишите программу, которая:
#
# загружает данные из двух предложенных JSON-файлов (находятся в репозитории);
# выполняет сравнение параметров, указанных в diff_list;
# формирует результат в виде словаря;
# записывает словарь в JSON-файл с названием result.json.
# Исходные данные
#
# Файлы:
#
# json_old.json,
# json_new.json.
# Список параметров для отслеживания (можно сформировать инпутом или ввести вручную):
#
# diff_list = [‘services’, ‘staff’, ‘datetime’]
#
# Формат итогового словаря с результатом:
#
# Словарь {параметр: новое_значение, ….}

# Пример
#
# Данные, загруженные из json_old.json:
# {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create', 'data': {'id': 11111111,
# 'company_id': 111111, 'services': [{'id': 9035445, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500,
# 'first_cost': 1500, 'amount': 1}], 'goods_transactions': [], 'staff': {'id': 1819441, 'name': 'Мастер'},
# 'client': {'id': 130345867, 'name': 'Клиент', 'phone': '79111111111', 'success_visits_count': 2,
# 'fail_visits_count': 0}, 'clients_count': 1, 'datetime': '2022-01-25T11:00:00+03:00',
# 'create_date': '2022-01-22T00:54:00+03:00', 'online': False, 'attendance': 0, 'confirmed': 1,
# 'seance_length': 3600, 'length': 3600, 'master_request': 1, 'visit_id': 346427049, 'created_user_id': 10573443,
# 'deleted': False, 'paid_full': 0, 'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '',
# 'date': '2022-01-22 10:00:00'}}
#
# Данные, загруженные из json_new.json:
# {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create', 'data': {'id': 11111111,
# 'company_id': 111111, 'services': [{'id': 22222225, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500,
# 'first_cost': 1500, 'amount': 1}], 'goods_transactions': [], 'staff': {'id': 1819441, 'name': 'Мастер'},
# 'client': {'id': 130345867, 'name': 'Клиент', 'phone': '79111111111', 'success_visits_count': 2,
# 'fail_visits_count': 0}, 'clients_count': 1, 'datetime': '2022-01-25T13:00:00+03:00',
# 'create_date': '2022-01-22T00:54:00+03:00', 'online': False, 'attendance': 2, 'confirmed': 1,
# 'seance_length': 3600, 'length': 3600, 'master_request': 1, 'visit_id': 346427049, 'created_user_id': 10573443,
# 'deleted': False, 'paid_full': 1, 'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '',
# 'date': '2022-01-22 10:00:00'}}
# diff_list = [‘services’, ‘staff’, ‘datetime’]
#
# Результат
#
# print(result)
# В консоли должно вывестись следующее сообщение:
#
# {'services': [{'id': 22222225, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500,
# 'amount': 1}], 'datetime': '2022-01-25T13:00:00+03:00'}
# Помимо вывода в консоль, должен быть сформирован JSON-файл с получившимся словарём (result.json).
#
# Обратите внимание: в result представлены не все изменившиеся поля, а лишь те, что объявлены в diff_list.


# Для решения этой задачи мы выполним следующие шаги:
#
# 1. Загрузим данные из JSON-файлов;
# 2. Сравним данные по ключам из `diff_list`;
# 3. Сформируем результат в виде словаря;
# 4. Запишем результат в файл `result.json`.
#
# Прежде всего, убедимся, что у вас есть два файла `json_old.json` и `json_new.json` в вашем рабочем каталоге.
# Для демонстрации работы программы у нас уже есть примеры содержимого этих файлов, как описано в задаче.
#
# ### Шаг 1: Загрузка данных
#
# Для начала напишем код для загрузки данных из файлов:
import json
from typing import List, Dict, Any


def load_json(filename: str) -> Dict[str, Any]:
    """
    Загружает данные из JSON-файла.
    :param filename: Имя файла для загрузки.
    :return: Словарь с данными из JSON.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# ### Шаг 2: Сравнение параметров
# Теперь, когда у нас есть функция для чтения данных, давайте реализуем функцию для сравнения параметров:
def find_differences(old_data: Dict[str, Any], new_data: Dict[str, Any], diff_list: List[str]) -> Dict[str, Any]:
    """
    Находит различия между двумя словарями по заданным ключам.
    :param old_data: Словарь со старыми данными.
    :param new_data: Словарь с новыми данными.
    :param diff_list: Список ключей для отслеживания изменений.
    :return: Словарь с различиями между данными.
    """
    differences = {}
    for key in diff_list:
        if old_data.get(key) != new_data.get(key):
            differences[key] = new_data[key]
    return differences


# ### Шаг 3: Формирование и запись результата
# Наконец, формируем наш итоговый результат и запишем его в файл `result.json`:
def write_to_json(data: Dict[str, Any], filename: str) -> None:
    """
    Записывает данные в JSON-файл.
    :param data: Словарь с данными для записи.
    :param filename: Имя целевого файла.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# Теперь объединим все шаги и выполним программу:
def main():
    # Задаем список ключей для отслеживания
    diff_list = ['services', 'staff', 'datetime']
    
    old_data = load_json('json_old.json')
    new_data = load_json('json_new.json')
    
    # Находим различия
    differences = find_differences(old_data['data'], new_data['data'], diff_list)
    
    # Выводим результат и записываем его в файл
    print(differences)
    write_to_json(differences, 'result.json')


if __name__ == "__main__":
    main()

# После запуска этой программы, она сравнит данные из файлов `json_old.json` и `json_new.json`,
# найдет изменения для параметров, указанных в `diff_list`, и выведет эти изменения в консоль,
# а также запишет их в файл `result.json`.
