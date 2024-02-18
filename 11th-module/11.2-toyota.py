# Напишите класс Toyota, состоящий из четырёх статических атрибутов:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200.
import random


class Toyota:
    color = "red"
    price = 1000000
    max_speed = 200
    current_speed = 0


toyota1 = Toyota()
toyota1.current_speed = random.randint(0, 200)

toyota2 = Toyota()
toyota2.current_speed = random.randint(0, 200)

toyota3 = Toyota()
toyota3.current_speed = random.randint(0, 200)

print('Текущая скорость первого автомобиля: {} км/ч: '.format(toyota1.current_speed))
print('Текущая скорость второго автомобиля: {} км/ч: '.format(toyota2.current_speed))
print('Текущая скорость третьего автомобиля: {} км/ч: '.format(toyota3.current_speed))