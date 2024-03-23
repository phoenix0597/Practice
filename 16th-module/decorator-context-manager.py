from contextlib import contextmanager
from typing import Generator  # или from collections.abc import Iterator


@contextmanager  # декоратор, который добавляет в декорируемую функцию (функцию-генератор!) методы __enter__ и __exit__
def next_num(num: int) -> Generator[int, None, None]:  # или Iterator[int]
    print('Входим в функцию')
    try:
        yield num + 1  # декорируемая функция должна возвращать генератор, поэтому заменим return на yield
    except ZeroDivisionError as e:
        print('Обнаружена ошибка:', e)
    finally:
        print('Здесь код выполнится в любом случае')
    print('Выход из функции')


with next_num(-1) as next_num:
    print('Следующее число = {}'.format(next_num))
    print(10 / next_num)

# Если функцию-генератор обернуть в декоратор @contextmanager, то вместо итератора вернется менеджер контекста,
# с уже определенными методами __enter__ и __exit__, где код до yield будет выполняться так, будто он был реализован
# методе __enter__, а код после yield будет выполняться так, будто он был реализован методе __exit__
