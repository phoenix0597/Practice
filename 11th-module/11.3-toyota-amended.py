# Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
#
#
# Добавьте два метода класса:
#
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Проверьте работу этих методов.
class Toyota:
    color = "красный"
    price = 1000000
    max_speed = 200
    current_speed = 0
    
    def print_info(self):
        print('Цвет машины: {}\nЦена: {}\nМаксимальная скорость: {}\nТекущая скорость: {}'.format(
            self.color, self.price, self.max_speed, self.current_speed))
    
    def set_current_speed(self, speed):
        self.current_speed = speed
        print('Значение свойстве current_speed класса Toyota изменено на {}'.format(self.current_speed))


toyota1 = Toyota()
toyota1.set_current_speed(100)
toyota1.print_info()
