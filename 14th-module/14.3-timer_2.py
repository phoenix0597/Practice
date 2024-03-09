import time
from typing import Callable, Any


def logging(func: Callable) -> Callable:
    """Декоратор для подсчета времени выполнения функции."""
    
    def wrapper(*args, **kwargs) -> Any:
        print('\nВызов функции {func}\t'
              'Позиционные аргументы: {args}\t'
              'Именованные аргументы: {kwargs}'.format(
            func=func.__name__,
            args=args,
            kwargs=kwargs
        ))
        result = func(*args, **kwargs)
        print('Функция успешно выполнилась')
        return result
    
    return wrapper


def timer(func: Callable) -> Callable:
    """Декоратор, логирующий работу кода."""
    
    def wrapper(*args, **kwargs) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = round(end - start, 2)
        print(f'Функция {func.__name__} выполнялась {duration} секунд')
        return result
    
    return wrapper


@logging
@timer
def hard_func():
    return [x ** 2 ** x for x in range(22)]


hard_func()
