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
class Potato:
    states = {0: "Отсутствует", 1: "Росток", 2: "Зеленая", 3: "Зрелая"}
    
    def __init__(self, index):
        self.index = index
        self.state = 0
    
    def grow(self):
        if self.state < 3:
            self.state += 1
            self.print_state()
    
    def is_ripe(self):
        if self.state == 3:
            return True
        return False
    
    def print_state(self):
        print("Картошка No{} - {}".format(self.index, self.states[self.state]))


class PotatoGarden:
    def __init__(self, count):  # count - количество посаженной картошки
        self.potatoes = [Potato(index) for index in range(1, count + 1)]
    
    def grow_all(self):
        print('Картошка подрастает:')
        for potato in self.potatoes:
            potato.grow()
    
    def print_state_all(self):
        for i_potato in self.potatoes:
            i_potato.print_state()
    
    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print("Картошка еще не созрела!\n")
        else:
            print("Вся картошка созрела. Можно собирать!\n")


# посадим в нашу грядку 5 клубней картошки
# my_garden = PotatoGarden(5)
# for _ in range(3):
#     my_garden.grow_all()
#     my_garden.are_all_ripe()

pot_1 = Potato(1)
pot_1.state = 3
pot_1.print_state()