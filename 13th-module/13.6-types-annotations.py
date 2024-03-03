from collections.abc import Iterable


class Person:
    def __init__(self, name: str, age: int, friends: list) -> None:
        self.__name = name
        self.__age = age
        self.__friends = friends
    
    def __str__(self) -> str:
        return f"Имя: {self.__name},\nВозраст: {self.get_age()},\nДрузья: {self.__friends}"
    
    def set_age(self, age: int) -> None:
        self.__age = age
    
    def get_age(self) -> int:
        return self.__age


def fibonacci(number: int) -> Iterable[int]:
    cur_val, next_val = 0, 1
    for _ in range(number):
        yield cur_val
        cur_val, next_val = next_val, cur_val + next_val


ivan = Person("Иван", 20, ["Петя", "Вася"])
print(ivan)
