class Person:
    """
    Человек
    Args:
        name (str): Имя
        age (int): Возраст
        
    Attributes:
        _name (str): Имя
        _age (int): Возраст (от 0 до 100, иначе генерируется исключение)
    """
    
    def __init__(self, name, age):
        self._name = name
        self.age = age
    
    def get_name(self):
        return self._name
    
    @property
    def age(self):
        """ Геттер. Возвращает возраст """
        return self._age  # одно нижнее подчеркивание вместо двух - такой атрибут может быть использован
        # в дочернем классе, но не желательно его использование в основном коде
    
    @age.setter
    def age(self, age):
        """ Сеттер. Устанавливает возраст """
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        if not (0 < age <= 100):
            raise ValueError("Возраст может быть только в пределах от 1 до 100")
        self.age = age


tom = Person('Tom', 30)

print(tom)
print(tom.age)
tom.age = 50
print(tom.age)
print(tom)
