# Условие задания "Итератор случайных чисел":
# Класс RandomNumbers:
# Атрибут limit: int - количество случайных чисел
#
# Выходные данные:
# Итерируемый объект класса
import random


class RandomNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.__counter = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__counter < self.limit:
            self.__counter += 1
            return random.randint(0, 10)
        else:
            raise StopIteration


my_iterator = RandomNumbers(limit=3)
for i_num in my_iterator:
    print(i_num)
