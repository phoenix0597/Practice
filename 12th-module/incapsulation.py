# Инкапсуляция - механизм языка, позволяющий объединить данные и методы работы с ними в один объект и скрыть
# детали их реализации от пользователя.
# Encapsulation - a language mechanism that allows bundling data and methods that operate on that data into one object
# and hide the implementation details from the user.
class Person:
    __count = 0
    
    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)  # в этом случае при инициализации объекта с неправильным возрастом возникнет ошибка
        Person.__count += 1
    
    def __str__(self):
        return 'Имя: {}, Возраст: {}'.format(self.__name, self.__age)
    
    def get_count(self):  # такой метод в питоне называется getter (получает значение скрытого атрибута)
        return self.__count
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):  # такой метод в питоне называется setter (устанавливает значение скрытого атрибута)
        """
        Если нужно проверять присваиваемое полю значение на корректность, то такую проверку необходимо делать
        внутри setter-метода, который получает данные для присвоения полю, а само поле должно быть закрыто для изменения
        извне. В этом случае ему невозможно будет присвоить недопустимое значение.
        :param age:
        :return:
        """
        if age in range(1, 150):
            self.__age = age
        else:
            raise ValueError('Недопустимый возраст')


misha = Person('Misha', 25)
tom = Person('Tom', 30)
print(misha)
print(tom)
print('Количество человек: ', tom.get_count())
new_age = 80
misha.set_age(new_age)
print(misha)
print('возраст Миши', misha.get_age())
# Приватные значения атрибутов можно изменять и получать только при помощи геттеров и сеттеров
# Это позволяет защитить данные от случайных изменений
