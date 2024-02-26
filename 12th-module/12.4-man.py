class Person:
    __count = 0
    
    def __init__(self, name, age):
        self.__age = None
        self.__name = name
        self.set_age(age)
        Person.__count += 1
    
    def __str__(self):
        return 'Имя: {}, Возраст: {}'.format(self.__name, self.__age)
    
    @staticmethod
    def get_count():
        return Person.__count
    
    def set_age(self, age):
        if 0 <= age <= 100:
            self.__age = age
        else:
            raise ValueError("Недопустимый возраст (должен быть в диапазоне от 0 до 100).")
    
    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name


class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.__university = university
    
    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (info, 'Студент, учится в университете: {}'.format(self.__university))
        )
        return info


class Employee(Person):
    def __init__(self, name, age, company, salary):
        super().__init__(name, age)
        self.__company = company
        self.__salary = salary
    
    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (info, 'Компания: {}, зарплата: {}'.format(self.__company, self.__salary))
        )
        return info


student = Student(name='Миша', age=25, university='ФизТех')  # явное лучше, чем неявное!
print(student)

# хорошим тоном является - при создании объекта с помощью именованных параметров указывать, что конкретно мы передаём
employee = Employee(name='Вася', age=30, company='Google', salary=10000)
print(employee)

# Использование более 7 параметров является плохим тоном! Это показывает, что метод или функция плохо спроектированы
