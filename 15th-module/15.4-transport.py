from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
    
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def sound_the_horn(self):
        pass


class PlayMusicMixin:
    def play_music(self):
        print("Музыка играет в амфибии")


class Car(Transport):
    def move(self):
        print("Автомобиль едет")
    
    def sound_the_horn(self):
        print("Автомобиль сигналит")


class Ship(Transport):
    def move(self):
        print("Лодка плывет")
    
    def sound_the_horn(self):
        print("Лодка сигналит")


class Amphibious(Transport, PlayMusicMixin):
    
    def __init__(self, color, speed, move_like_ship):
        super().__init__(color, speed)
        self.move_like_ship = move_like_ship
    
    def move(self, move_like_ship=False):
        if move_like_ship:
            print("Амфибия плывет")
        else:
            print("Амфибия едет")
    
    def sound_the_horn(self):
        print("Амфибия сигналит")


# проверка работы

car = Car("red", 100)
car.move()
car.sound_the_horn()
print()
amphibious = Amphibious("blue", 200, True)
amphibious.move(True)
amphibious.sound_the_horn()
amphibious.play_music()
