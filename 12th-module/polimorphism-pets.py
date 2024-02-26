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
    
    def walk(self):
        print('Гуляет')


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
    
    def walk(self):  # переопределяем метод родительского класса
        print('Плавает')  # способность к изменению функционала ,унаследованного от базового класса - ПОЛИМОРФИЗМ


cat = Cat()
dog = Dog()

print(cat)
cat.sound()

print(dog)
dog.sound()

frog = Frog()
print(frog)
frog.Sound()

cat.walk()
dog.walk()
frog.walk()

# Наследование - это механизм языка, позволяющий создавать новый класс на основе уже существующего класса.
# Используется для выделения общих атрибутов и методов объектов.

# Полифорфизм - принцип, предполагающий способность к изменению функционала, унаследованного от базового класса.
