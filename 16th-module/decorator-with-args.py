import functools
import time
from typing import Callable
from typing import Optional


# from typing import Optional


# При передаче аргумента в декоратор мы, по сути, поместили один декоратор в другой и добавили обработку
# значения аргумента
# def timer_with_precision(_func: Optional[Callable] = None, *, precision: int = 10) -> Callable:
def timer_with_precision(_func: Optional[Callable] = None, *, precision: int = 10) -> Callable:
    # ^^^ здесь _func действует как маркер, отмечающий - был ли декоратор вызван с аргументами или без них
    # это, в свою очередь, означает, что все аргументы декоратора должны передаваться, как именованные аргументы
    # синтаксис "*" указывает, что все остальные аргументы передаются исключительно по ключу
    
    def timer_decorator(func: Callable) -> Callable:
        """Декоратор-таймер для подсчета времени выполнения функции."""
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            started_at = time.time()
            result = func(*args, **kwargs)
            ended_at = time.time()
            run_time = round(ended_at - started_at, precision)  # пусть нам нужна разная точность для разных функций
            print(f"Функция {func.__name__} выполнялась {run_time} секунд")
            return result
        
        return wrapper
    
    return timer_decorator


@timer_with_precision()
def hard_func() -> list:
    """Функция, возвращающая список выражений чисел в заданном диапазоне."""
    return [x ** 640 for x in range(10)]


@timer_with_precision(precision=4)
def hard_func1() -> list:
    """Функция, возвращающая список выражений чисел в заданном диапазоне."""
    return [x ** 640 for x in range(20)]


print(hard_func())
print(hard_func1())

print(hard_func.__doc__)
print(hard_func.__name__)

print(hard_func.__dict__)
print(hard_func1.__dict__)
