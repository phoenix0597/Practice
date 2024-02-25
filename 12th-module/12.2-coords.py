# Задача 1. Координаты точки
# В одной из практик предыдущего модуля была задача на реализацию класса «Точка».
# Модернизируйте класс по следующему условию: объект «Точка» на плоскости имеет координаты x и y;
# при создании новой точки могут передаваться пользовательские значения координат, по умолчанию x = 0, y = 0.
#
# Реализуйте класс, который будет представлять эту точку, и напишите следующие методы:
#
# Предоставление информации о точке (используйте магический метод str).
# Геттер и сеттер для x.
# Геттер и сеттер для y.
# Для сеттеров реализуйте проверку на корректность входных данных: координаты должны быть числом.
class Point:
    count = 0
    
    def __init__(self, x, y):
        self.__x = self.set_x(x)  # приватное свойство x
        self.__y = self.set_y(y)  # приватное свойство y
        Point.count += 1
    
    def __str__(self):
        return 'Координаты точки: ({}, {})'.format(self.__x, self.__y)
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    @staticmethod
    def check_value(value):
        if not isinstance(value, (int, float)):
            raise TypeError('Координаты должны быть числами')
        else:
            return value
    
    def set_x(self, x):
        value = self.check_value(x)
        if value:
            return value
    
    def set_y(self, y):
        value = self.check_value(y)
        if value:
            return value


p = Point(1, 2)
print(p)
print('Количество точек: ', Point.count)
