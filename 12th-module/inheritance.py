class Pet:
    legs = 4
    has_tail = True
    
    def __str__(self):
        tail = 'Да' if self.has_tail else 'Нет'
        return '{pet}:\nВсего ног: {legs}, Есть хвост: {has_tail}'.format(
            pet=self.__class__.__name__,
            legs=self.legs,
            has_tail=tail
        )


class Cat(Pet):
    
    def sound(self):
        print('Звук - Мяу')


class Dog(Pet):
    def sound(self):
        print('Звук - Гав')


class Frog(Pet):
    has_tail = False  # переопределяем атрибут has_tail родительского класса
    def Sound(self):
        print('Звук - Кряк')


cat_1 = Cat()
dog = Dog()

print(cat_1)
cat_1.sound()

print(dog)
dog.sound()

frog = Frog()
print(frog)
frog.Sound()

# Наследование - это механизм языка, позволяющий создавать новый класс на основе уже существующего класса.
# Используется для выделения общих атрибутов и методов объектов.
