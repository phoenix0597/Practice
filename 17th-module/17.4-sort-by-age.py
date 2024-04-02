# Задача 2. Сортировка
# Таблица базы данных состоит из строк, в которых хранится информация о каждом человеке:
# его имя, возраст и остальные данные.
# Вас попросили реализовать для этой базы сортировку по возрасту (по убыванию и по возрастанию).
#
# Реализуйте класс Person с соответствующей инициализацией, а также сеттерами и геттерами.
# Затем создайте список из хотя бы трёх людей и отсортируйте их. Для сортировки используйте лямбда-функцию.
class Person:
    """
    Представляет человека с именем и возрастом.

    Атрибуты:
        name (str): имя человека.
        age (int): возраст человека.
    """
    
    def __init__(self, name: str, age: int) -> None:
        """
        Инициализирует объект человека с заданными именем и возрастом.

        Параметры:
            name (str): имя человека.
            age (int): возраст человека.
        """
        
        self._name = name
        self._age = age
    
    @property
    def name(self) -> str:
        """Возвращает имя человека."""
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
        """Устанавливает имя человека."""
        self._name = name
    
    @property
    def age(self) -> int:
        """Возвращает возраст человека."""
        return self._age
    
    @age.setter
    def age(self, age: int) -> None:
        """Устанавливает возраст человека."""
        if age <= 0:
            raise ValueError('Возраст должен быть больше нуля.')
        self._age = age
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Возвращает:
            str: Строка с именем и возрастом человека.
        """
        return f"{self.name}, возраст {self.age}"


people = [
    Person('Иван', 25),
    Person('Петр', 30),
    Person('Сергей', 20)
]

sorted_persons_by_age_asc = sorted(people, key=lambda person: person.age)
sorted_persons_by_age_desc = sorted(people, key=lambda person: person.age, reverse=True)

print('Sorted by age asc:\n' + '-' * 20)
print(*sorted_persons_by_age_asc, sep='; ')
print()
print('Sorted by age desc:\n' + '-' * 20)
print(*sorted_persons_by_age_desc, sep='; ')
