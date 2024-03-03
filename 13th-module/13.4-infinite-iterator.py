# Задача 1. Бесконечный итератор.
# Реализуйте итератор-счётчик, который не принимает никаких атрибутов и имеет только один статический атрибут — счётчик.
# Итератор увеличивает счётчик и возвращает предыдущее значение. У вас должен получиться бесконечный итератор.
#
# То есть при вызове такого кода в основной программе
#
# my_iter = СountIterator()
#
# for i_elem in my_iter:
#
#     print(i_elem)
#
# значения будут выдаваться бесконечно.
class СountIterator:
    def __init__(self):
        self.counter = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.counter += 1
        return self.counter


my_iter = СountIterator()

for i_elem in my_iter:
    print(i_elem)
