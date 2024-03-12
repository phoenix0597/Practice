from abc import ABC


class Figure(ABC):
    """
    Абстрактный базовый класс фигуры
    Args:
        pos_x (int): Координата x
        pos_y (int): Координата y
        length (int): Длина
        width (int): Ширина
    """
    
    def __init__(self, pos_x: int, pos_y: int, length: int, width: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width
    
    def move(self, new_pos_x: int, new_pos_y: int) -> None:
        self.pos_x = new_pos_x
        self.pos_y = new_pos_y


class ResizableMixin:  # Миксин
    """
    Миксин для изменения размеров фигуры
    В этом классе мы прописали нужный функционал для прямоугольника и квадрата, при этом (ЧТО САМОЕ ВАЖНОЕ),
    никак не вмешиваясь в структуру их наследования
    """
    
    def resize(self, new_length: int, new_width: int) -> None:
        self.length = new_length
        self.width = new_width


class Rectangle(Figure, ResizableMixin):
    """ Прямоугольник. Дочерний класс от Figure """
    pass


class Square(Figure, ResizableMixin):
    """ Квадрат. Дочерний класс от Figure """
    
    def __init__(self, pos_x: int, pos_y: int, size: int) -> None:
        super().__init__(pos_x, pos_y, size, size)


rect_1 = Rectangle(10, 20, 5, 6)
rect_2 = Rectangle(30, 40, 10, 11)
square_1 = Square(50, 60, 5)

# увеличим вдвое линейные размеры каждой из фигур
for figure in [rect_1, rect_2, square_1]:
    new_size_x = figure.length * 2
    new_size_y = figure.width * 2
    figure.resize(new_size_x, new_size_y)

# Миксины - это классы, которые используются в наследовании, но при этом остаются небольшими, чтобы избежать
# создания иерархий, сложных для понимания программистом.

for figure in [rect_1, rect_2, square_1]:
    print('Фигура: x = {0}, y = {1}, длина = {2}, ширина = {3} (класс {4})'.format(
        figure.pos_x, figure.pos_y, figure.length, figure.width, figure.__class__.__name__))
