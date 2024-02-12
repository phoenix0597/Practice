# Задача 6.5 "Журнал посещений"
# Условие задачи: Список словарей (посетители - id, имя)
# Выходные данные: Дублирующие элементы списка удаляются. Остается список уникальных словарей. Уникальность определяется
# только по id.
data = [
	{"id": 10, "user": "Bob"},
	{"id": 11, "user": "Misha"},
	{"id": 12, "user": "Anton"},
	{"id": 10, "user": "Bob"},
	{"id": 11, "user": "Misha"}
]

unique_visitors = {i_dict["id"]: i_dict for i_dict in data}
unique_visitors_list = list(unique_visitors.values())
print(unique_visitors_list)
