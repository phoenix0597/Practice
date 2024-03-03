# Задача 2. Случайная сумма
# Алексею по работе необходимо обрабатывать огромные массивы данных из миллионов элементов.
# Каждый новый элемент — это сумма случайного вещественного числа от 0 до 1 и предыдущего элемента
# (первый элемент — просто случайное вещественное число от 0 до 1). Алексею нельзя хранить в памяти весь этот список,
# а со значениями работать как-то надо.
#
# Помогите Алексею, реализуйте такой класс-итератор и проверьте его работу.
# Также сделайте, чтобы при каждом новом вызове итератора в цикле значения считались заново.
#
# Пример работы программы:
#
# Кол-во элементов: 5
# Элементы итератора:
# 0.74
# 1.13
# 1.95
# 2.2
# 2.55
#
# Новое кол-во элементов: 6
# Элементы итератора:
# 0.79
# 1.58
# 2.55
# 2.81
# 3.06
# 3.34
import random


class RandomSumIterator:
    def __init__(self, num):
        self.number = num  # Количество элементов для генерации
        self.count = 0  # Счетчик текущего количества сгенерированных элементов
    
    def __iter__(self):
        self.count = 0  # Сброс счетчика перед новой итерацией
        self.current_sum = 0.0  # Сброс текущей суммы
        return self
    
    def __next__(self):
        if self.count < self.number:
            self.count += 1
            self.current_sum += random.random()  # Генерация и добавление к текущей сумме случайного числа
            return self.current_sum
        else:
            raise StopIteration


# Тестирование класса
n_elements = int(input("Кол-во элементов: "))
iterator = RandomSumIterator(n_elements)
print("\nЭлементы итератора:")
for value in iterator:
    print(round(value, 2))

# Используем итератор заново с новым значением элементов
new_n_elements = int(input("\nНовое кол-во элементов: "))
iterator = RandomSumIterator(new_n_elements)  # Создаем новый экземпляр с новым кол-вом элементов
print("\nЭлементы итератора:")
for value in iterator:
    print(round(value, 2))