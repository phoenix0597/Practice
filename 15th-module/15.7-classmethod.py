class Pet:
    TOTAL_SOUNDS = 0
    
    def __init__(self):
        self.__legs = 4
        self.__has_tail = True
    
    def __str__(self):
        tail = "да" if self.__has_tail else "нет"
        return 'Всего ног {legs}\n Хвост присутствует - {has_tail}'.format(
            legs=self.__legs,
            has_tail=tail
        )


class Cat(Pet):
    @classmethod
    def sound(cls) -> None:  # cls - это объект, который содержит сам класс, а не экземпляр класса,
        cls.TOTAL_SOUNDS += 1  # а значит через него можно обращаться к чему угодно, что есть в самом классе
        print(cls.TOTAL_SOUNDS)
        print('Мяу')


class Dog(Pet):
    @classmethod
    def sound(cls) -> None:
        cls.TOTAL_SOUNDS += 1
        print(cls.TOTAL_SOUNDS)
        print('Гав')


Cat.sound()
Cat.sound()
cat = Cat()

cat.sound()
cat.sound()

# cls - это объект, который содержит сам класс, а не экземпляр класса,
# а значит через него можно обращаться к чему угодно, что есть в самом классе
# Таким образом, в основном, если метод класса никак не использует self, то надо помечать этот метод
# декоратором classmethod и заменять self на cls (и не удивляться ,если где-то будет использоваться staticmethod,
# просто не надо использовать его самим)

