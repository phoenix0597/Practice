# Задача "Корабли"
# Условие задачи:
# Класс Грузовой корабль
# Атрибуты:
#   - модель
#   - заполненность (0)
# Методы:
#   - назвать модель
#   - идти по воде
#   - погрузить груз
#   - выгрузить груз

# Класс Военный корабль
# Атрибуты:
#   - модель
#   - оружие
# Методы:
#   - назвать модель
#   - идти по воде
#   - атаковать
#
# Выходные данные:
# Экземпляры классов
class Ship:
    def __init__(self, model):
        self.__model = model  # сделаем модель приватным атрибутом (все равно менять не нужно будет)
    
    def go(self):
        print('идем по воде')
    
    def __str__(self):
        return '\nМодель корабля: {model}'.format(
            model=self.__model
        )


class WarShip(Ship):
    def __init__(self, model, weapon):
        super().__init__(model)
        self.__weapon = weapon
    
    def attack(self):
        print('\nКорабль атакует с помощью оружия {weapon}'.format(
            weapon=self.__weapon
        )
        )
    
    def __str__(self):
        return super().__str__() + '\nОружие: {weapon}'.format(
            weapon=self.__weapon
        )


class CargoShip(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.tonnage_load = 0
    
    def load(self):
        if not self.tonnage_load:
            self.tonnage_load += 1
        print('Груз погружен.', 'Текущая загруженность:', self.tonnage_load)
    
    def unload(self):
        if self.tonnage_load > 0:
            self.tonnage_load -= 1
        print('Груз выгружен')
    
    def __str__(self):
        return super().__str__() + '\nТекущая загруженность: {tonnage_load}'.format(
            tonnage_load=self.tonnage_load
        )
    

warship = WarShip('Линейный корабль', 'зенитные пушки')
warship.go()
warship.attack()

cargoship = CargoShip('Танкер')
cargoship.go()
cargoship.load()
cargoship.unload()

print(warship)
print(cargoship)