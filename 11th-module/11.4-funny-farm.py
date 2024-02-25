# Задача "Весёлая ферма".
# Условие задачи:
# Два класса: Картошка и Грядка
# Класс Картошка, атрибуты: номер, стадия зрелости
# Класс Картошка методы: информация о зрелости, рост
#
# Класс Грядка, атрибуты: список картошки (которая на ней растет)
# Класс Грядка методы: информация о зрелости всей картошки, рост всей грядки
#
# Выходные данные: пример работы грядки
# import garden
from garden import PotatoGarden

# посадим в нашу грядку 5 клубней картошки
my_garden = PotatoGarden(5)
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()

# pot_1 = garden.Potato(1)
# pot_1.state = 3
# pot_1.print_state()