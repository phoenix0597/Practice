## Выводы по модулю 15 ###
1. При множественном наследовании возникает т.н. проблема алмаза.
В Python она разрешается с помощью установленного порядка разрешения методов - Method resolution order (MRO).
Алгоритм, который при этом используетсая, называется:
**C3 superclass linearization (MRO)**

2. Обычно множественное наследование стараются не использовать, но иногда оно нужно, чтобы прописать какой-то функционал
и при этом не нарушать общую структуру наследования. Для этого используются примеси:
```Python
class ResizableMixin: # класс-примесь
    pass
```
3. Класс, который описывает общий функционал для наследников и не подразумевает создание инстансов,
называется абстрактным. Такой класс должен наследоваться от абстрактного класса ABC из модуля abc. 
```Python
from abc import ABC
class Figure(ABC): # абстрактный класс
    pass
```
4. Любой класс можно превратить в контекстный менеджер, чтобы затем использовать его в конструкции with ... as ...
Для этого в классе нужно определить магшические методы __enter__ и __exit__

```Python
def __enter__(self):
    pass
def __exit__(self, exc_type, exc_val, exc_tb):
    pass
```
5. При написании геттеров и сеттеров используют декораторы @property (для геттера) и @age.setter (для сеттера):
```Python
@property
def age(self):
    return self.__age
```
```Python
@age.setter
def name(self, value):
    self.age = value
```
Это позволяет в основном коде удобно работать с приватными атрибутами класса.

6. Методы, в которых нет обращения к атбрибутам или другим методам, всегда оборачиваются в специальный декоратор
@classmethod (в некоторых местах еще используют уже устаревающий @staticmethod)