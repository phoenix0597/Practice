from typing import List


class Person:
    """Базовый класс Человек"""
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def shout(self) -> None:
        print('Я - человек. Меня зовут {name}.'.format(name=self.name))


class Employee(Person):
    """Класс сотрудник. Дочерний класс от Person."""
    
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.__salary = 20000
    
    def get_salary(self) -> int:
        return self.__salary
    
    def shout(self) -> None:
        print('Я - сотрудник. Меня зовут {name}.'.format(name=self.name))


class Parent(Person):
    """Класс родитель. Дочерний класс от Person."""
    
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.__children = ['John', 'Tom', 'Jane']
    
    def get_children(self) -> List:
        return self.__children
    
    # def shout(self) -> None:
    #     print('Я - родитель. Меня зовут {name}.'.format(name=self.name))


class Citizen(Parent, Employee):
    """Житель. Является и родителем и сотрудником."""
    
    # def shout(self) -> None:
    #     print('Я - житель. Меня зовут {name}.'.format(name=self.name))
    
    pass


my_citizen = Citizen('John', 25)
print(my_citizen.get_salary())
print(my_citizen.get_children())

my_citizen.shout()

# MRO - Method Resolution Order (порядок разрешения метода) - решает проблему алмаза
print(my_citizen.__class__.mro())
print(my_citizen.__class__.__mro__)

# Стоит ли вообще использовать множественное наследование? Это один из самых спорных вопросов ООП
# Плюс: позволяет сокращать затраты на разработку класса и избегать повторного использования кода
# Минус: повышает сложность модификации системы классов. Увеличивает связь между классами, а значит,
# изменения в базовом классе могут повлечь серьезные проблемы в дочерних.
# Возникает ПРОБЛЕМА АЛМАЗА, когда мы переопределяем один и тот же метод в разных классах (особенно эта проблема
# касается магических методов, в частности, метода __init__(). Из-за этого ухудшается понимание и чистота кода
# ИТОГО: обычно не используют, но есть ситуации, когда это необходимо
