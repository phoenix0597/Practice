# Задача 2. Человек
# Реализуйте класс «Человек», который инициализируется именем (имя должно состоять только из букв) и возрастом
# (должен быть в диапазоне от 0 до 100), а внутри класса считается общее количество инициализированных объектов.
# Реализуйте сокрытие данных для всех атрибутов (как статических, так и динамических),
# а для изменения и получения данных объекта напишите специальные геттеры и сеттеры.
#
# При тестировании класса измените приватный атрибут (например, возраст) двумя способами:
# сеттером и «крайне не рекомендуемым», который был показан в уроке.
class Person:
    __count = 0
    
    def __init__(self, name, age):
        self.__name = ''
        self.__age = 0
        self.set_name(name)
        self.set_age(age)
        Person.__count += 1
    
    def set_age(self, age):
        if 0 <= age <= 100:
            self.__age = age
        else:
            raise ValueError("Invalid age value. Age should be between 0 and 100.")
    
    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            raise ValueError('Invalid name value. Name should contain only letters.')
    
    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name
    
    def __str__(self):
        return 'Имя: {}, Возраст: {}'.format(self.__name, self.__age)
    
    @staticmethod
    def get_count():
        return Person.__count


# Testing the class
misha = Person('Misha', 25)
misha.set_age(30)  # Using the safe setter
print('Misha age (safe setter):', misha.get_age())
print('Misha age (unsafe way):', misha._Person__age)  # крайне не рекомендуемый способ получения приватного свойства

tom = Person('Tom', 30)
print('Tom age:', tom.get_age())

print('Количество человек: ', misha.get_count())
