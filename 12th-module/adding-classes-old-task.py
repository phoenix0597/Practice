# Добавляем родительский класс с методом __add__ в чтобы потом использования его в дочерних классах
class Element:
    def __add__(self, other):
        combined = type(self).__name__ + '+' + type(other).__name__
        class_name = combinations.get(combined, None)
        try:
            result_class = eval(class_name + '()')
        except (KeyError, NameError):
            result_class = None
        return result_class


# Обеспечиваем поддержку __str__ метода в дочерних классах
class Water(Element):
    def __str__(self):
        return "Вода"


class Air(Element):
    def __str__(self):
        return "Воздух"


class Fire(Element):
    def __str__(self):
        return "Огонь"


class Earth(Element):
    def __str__(self):
        return "Земля"


class Metal(Element):
    def __str__(self):
        return "Металл"


class Storm(Element):
    def __str__(self):
        return "Шторм"


class Steam(Element):
    def __str__(self):
        return "Пар"


class Mud(Element):
    def __str__(self):
        return "Грязь"


class Lightning(Element):
    def __str__(self):
        return "Молния"


class Dust(Element):
    def __str__(self):
        return "Пыль"


class Lava(Element):
    def __str__(self):
        return "Лава"


class Wing(Element):
    def __str__(self):
        return "Крыло"


class Shovel(Element):
    def __str__(self):
        return "Лопата"


class Oar(Element):
    def __str__(self):
        return "Весло"


class Plasma(Element):
    def __str__(self):
        return "Плазма"


# Функция для получения экземпляра по имени класса
def get_instance(name):
    return eval(name + '()')


# Функция тестирования всех комбинаций, помещенных в словаре combinations
def test_combinations(comb_dict):
    for combined, result_class_name in comb_dict.items():
        # Получаем имена классов из ключа и результат комбинации
        elem1_name, elem2_name = combined.split('+')
        elem1 = get_instance(elem1_name)
        elem2 = get_instance(elem2_name)
        
        # Выполняем комбинацию
        result = elem1 + elem2
        
        # Проверяем результат комбинации
        if result_class_name:
            expected_result = get_instance(result_class_name)
        else:
            expected_result = None
        
        # expected_result = get_instance(result_class_name) if result_class_name else None
        if result:
            result_str = result
        else:
            result_str = "None"
        
        # result_str = result if result != None else "None"
        
        test_res = 'Test: OK' if expected_result.__str__() == result.__str__() else 'Test: FAIL'
        # Выводим результат
        print(f'{elem1} + {elem2} = {result_str} - {test_res}')


# Словарь со всеми комбинациями и соответствующими им результатами
combinations = {
    'Water+Air': 'Storm',
    'Water+Fire': 'Steam',
    'Water+Earth': 'Mud',
    'Water+Metal': 'Oar',
    'Air+Water': 'Storm',
    'Air+Fire': 'Lightning',
    'Air+Earth': 'Dust',
    'Air+Metal': 'Wing',
    'Fire+Water': 'Steam',
    'Fire+Air': 'Lightning',
    'Fire+Earth': 'Lava',
    'Fire+Metal': 'Plasma',
    'Earth+Water': 'Mud',
    'Earth+Air': 'Dust',
    'Earth+Fire': 'Lava',
    'Earth+Metal': 'Shovel',
    'Metal+Air': 'Wing',
    'Metal+Fire': 'Plasma',
    'Metal+Earth': 'Shovel',
    'Metal+Water': 'Oar'
}

# Проведение тестов
test_combinations(combinations)
