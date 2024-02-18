# Задача 1. Машина 3
# Вам предстоит снова немного видоизменить класс Toyota из прошлого урока. На всякий случай вот описание класса.
#
# Четыре атрибута:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Два метода:
#
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Теперь все четыре атрибута должны инициализироваться при создании экземпляра класса (то есть передаваться в init).
# Реализуйте такое изменение класса.
class Toyota:
    def __init__(self, color, price, max_speed, current_speed):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed

    def print_info(self):
        print('Цвет машины: {}\nЦена: {}\nМаксимальная скорость: {}\nТекущая скорость: {}'.format(
            self.color, self.price, self.max_speed, self.current_speed))

    def set_current_speed(self, speed):
        self.current_speed = speed
        print('Значение свойстве current_speed класса Toyota изменено на {}\n'.format(self.current_speed))


toyota_1 = Toyota('красный', 1000000, 200, 0)
print('Первоначальные значения атрибутов экземпляра класса Toyota:')
toyota_1.print_info()
toyota_1.set_current_speed(100)
print('Значения атрибутов экземпляра класса Toyota после изменения:')
toyota_1.print_info()
