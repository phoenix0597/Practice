class Employee:
    def __init__(self, name, age, salary, position):  # конструктор класса
        print('\nСоздание нового сотрудника...')
        self.name = name  # здесь определили атрибуты самого объекта, т.е. с какими свойствами он инициализируется
        self.age = age    # (такие атрибуты называются динамическими, т.е. именованными аргументами)
        self.salary = salary
        self.position = position
    
    def print_info(self):
        print('Имя: {}\nВозраст: {}\nЗарплата: {}\nДолжность: {}'.format(
            self.name, self.age, self.salary, self.position))


emp_1 = Employee('Иван', 25, 3000, 'разработчик')
emp_1.print_info()

emp_2 = Employee('Петр', 30, 2000, 'менеджер')
emp_2.print_info()
