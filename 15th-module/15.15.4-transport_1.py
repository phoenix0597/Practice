from abc import ABC, abstractmethod


class MusicalMixin:
    """
    Примесь, реализующая функционал проигрывания музыки.
    """
    
    def __init__(self):
        self.music_on = False
    
    def turn_music_on(self) -> None:
        """
        Включает проигрывание музыки.
        """
        self.music_on = True
        print("Музыка включена")
    
    def turn_music_off(self) -> None:
        """
        Выключает проигрывание музыки.
        """
        self.music_on = False
        print("Музыка выключена")


class Transport(ABC):
    """
    Абстрактный базовый класс для всех видов транспорта.
    """
    
    def __init__(self, color: str, speed: int):
        self.color = color
        self.speed = speed
    
    @abstractmethod
    def move(self) -> None:
        """
        Абстрактный метод для перемещения транспорта.
        """
        pass
    
    @abstractmethod
    def signal(self) -> None:
        """
        Абстрактный метод для подачи сигнала транспортом.
        """
        pass


class Car(Transport):
    """
    Класс для автомобилей, перемещающихся по земле.
    """
    
    def move(self) -> None:
        print(f"Автомобиль {self.color} цвета движется со скоростью {self.speed} км/ч по земле.")
    
    def signal(self) -> None:
        print("Би-би!")


class Boat(Transport):
    """
    Класс для лодок, перемещающихся по воде.
    """
    
    def move(self) -> None:
        print(f"Лодка {self.color} цвета движется со скоростью {self.speed} км/ч по воде.")
    
    def signal(self) -> None:
        print("Ту-ту!")


class Amphibian(Transport, MusicalMixin):
    """
    Класс для амфибий, перемещающихся по земле и воде, с возможностью проигрывания музыки.
    """
    
    def move(self) -> None:
        print(f"Амфибия {self.color} цвета движется со скоростью {self.speed} км/ч по земле и воде.")
    
    def signal(self) -> None:
        print("Ууу-ууу!")


# Пример использования
car = Car("красный", 100)
car.move()
car.signal()

boat = Boat("синий", 20)
boat.move()
boat.signal()

amphibian = Amphibian("зеленый", 50)
amphibian.move()
amphibian.signal()
amphibian.turn_music_on()
amphibian.turn_music_off()

# Автомобиль красный цвета движется со скоростью 100 км/ч по земле.
# Би-би!
# Лодка синий цвета движется со скоростью 20 км/ч по воде.
# Ту-ту!
# Амфибия зеленый цвета движется со скоростью 50 км/ч по земле и воде.
# Ууу-ууу!
# Музыка включена
# Музыка выключена
