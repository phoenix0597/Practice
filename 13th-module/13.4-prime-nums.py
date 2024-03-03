# Задача 3. Простые числа
# Реализуйте класс-итератор Primes, который принимает максимальное число N и выдаёт все простые числа от 1 до N.
#
# Основной код:
#
# prime_nums = Primes(50)
#
# for i_elem in prime_nums:
#
#     print(i_elem, end=' ')
#
# Ожидаемый результат кода:
#
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
class Primes:
    """
    Класс для генерации простых чисел в заданном диапазоне.
    Attributes:
        max_num (int): Верхний предел диапазона для генерации простых чисел
        num (int): Текущее число для проверки на простоту.
    """
    
    def __init__(self, max_num):
        """
        Инициализация класса с заданным максимальным числом.
        Args:
            max_num (int): Верхний предел для генерации простых чисел.
        """
        self.max_num = max_num
        self.num = 1
    
    def __iter__(self):
        """
        Возвращает итератор объекта.
        Returns:
            self: Возвращает себя как объект итератора.
        """
        return self
    
    @staticmethod
    def is_prime(n):
        """
        Статический метод для проверки числа на простоту.
        Args:
            n (int): Число для проверки на простоту.
        Returns:
            bool: True, если число простое. Иначе False.
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def __next__(self):
        """
        Возвращает следующее простое число в заданном диапазоне.
        Returns:
            int: Следующее простое число.
        Raises:
            StopIteration: Исключение, сигнализирующее о завершении итерации.
        """
        self.num += 1
        while self.num <= self.max_num:
            if self.is_prime(self.num):
                return self.num
            self.num += 1
        raise StopIteration


# Пример использования
# prime_nums = Primes(12)
# for i_elem in prime_nums:
#     print(i_elem, end=' ')
print(Primes.is_prime(17))
