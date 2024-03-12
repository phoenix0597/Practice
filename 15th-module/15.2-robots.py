from abc import ABC, abstractmethod


class Robot(ABC):
    """Абстрактный базовый класс для всех типов роботов."""
    
    def __init__(self, model: str):
        """
        Инициализирует экземпляр класса Robot.
        Args:
            model (str): Модель робота.
        """
        self.model = model
    
    def say_hello(self) -> None:
        """Выводит приветственное сообщение робота."""
        print(f"Я - Робот {self.model}")
    
    @abstractmethod
    def operate(self) -> None:
        """
        Абстрактный метод, реализующий основную функциональность робота.
        Должен быть переопределен в дочерних классах.
        """
        pass


class FlyingAbility(ABC):
    """Абстрактный класс, предоставляющий способность летать."""
    
    def __init__(self, height: float, speed: float):
        """
        Инициализирует экземпляр класса FlyingAbility.
        Args:
            height (float): Высота полета.
            speed (float): Скорость полета.
        """
        self.height = height
        self.speed = speed
    
    def take_off(self) -> None:
        """Выводит сообщение о взлете."""
        print("Взлетаю...")
    
    def fly(self) -> None:
        """Выводит сообщение о полете."""
        print(f"Лечу на высоте {self.height} м со скоростью {self.speed} м/с")
    
    def land(self) -> None:
        """Выводит сообщение о посадке."""
        print("Приземляюсь...")
    
    @abstractmethod
    def operate(self) -> None:
        """
        Абстрактный метод, реализующий основную функциональность летающего объекта.
        Должен быть переопределен в дочерних классах.
        """
        pass


class ReconDrone(Robot, FlyingAbility):
    """Класс разведывательного дрона, наследующий функциональность робота и летающего объекта."""
    
    def __init__(self, model: str, height: float, speed: float):
        """
        Инициализирует экземпляр класса ReconDrone.
        Args:
            model (str): Модель робота.
            height (float): Высота полета.
            speed (float): Скорость полета.
        """
        Robot.__init__(self, model)
        FlyingAbility.__init__(self, height, speed)
    
    def operate(self) -> None:
        """Реализует основную функциональность разведывательного дрона."""
        print("Веду разведку с воздуха")
        self.take_off()
        self.fly()
        self.land()


class WarDrone(Robot, FlyingAbility):
    """Класс военного дрона, наследующий функциональность робота и летающего объекта."""
    
    def __init__(self, model: str, height: float, speed: float, weapon: str):
        """
        Инициализирует экземпляр класса WarDrone.
        Args:
            model (str): Модель робота.
            height (float): Высота полета.
            speed (float): Скорость полета.
            weapon (str): Тип оружия.
        """
        Robot.__init__(self, model)
        FlyingAbility.__init__(self, height, speed)
        self.weapon = weapon
    
    def operate(self) -> None:
        """Реализует основную функциональность военного дрона."""
        print(f"Защищаю военный объект с воздуха с помощью {self.weapon}")
        self.take_off()
        self.fly()
        self.land()


# Проверка работы классов
recon_drone = ReconDrone("Разведчик-1000", 500, 100)
recon_drone.say_hello()  # Я - Робот Разведчик-1000
recon_drone.operate()  # Веду разведку с воздуха
print()

war_drone = WarDrone("Боевой дрон-2000", 1000, 200, "ракеты")
war_drone.say_hello()  # Я - Робот Боевой дрон-2000
war_drone.operate()  # Защищаю военный объект с воздуха с помощью ракеты

# Этот код реализует иерархию классов для различных типов роботов, включая разведывательный дрон и военный дрон.
# Базовый класс `Robot` определяет общие атрибуты и методы для всех роботов, такие как модель и приветственное сообщение
# Класс `FlyingAbility` предоставляет функциональность полета, включая взлет, полет и посадку.
#
# Классы `ReconDrone` и `WarDrone` наследуют функциональность от классов `Robot` и `FlyingAbility`,
# добавляя при этом свою специфическую реализацию метода `operate()`.
#
# Код также включает docstrings на русском языке, аннотации типов и проверку работы функций.
#
# Вывод:
#
# Я - Робот Разведчик-1000
# Веду разведку с воздуха
# Взлетаю...
# Лечу на высоте 500.0 м со скоростью 100.0 м/с.
# Приземляюсь...
#
# Я - Робот Боевик-2000.
# Защищаю военный объект с воздуха с помощью ракеты
# Взлетаю...
# Лечу на высоте 1000.0 м со скоростью 200.0 м/с.
# Приземляюсь...
