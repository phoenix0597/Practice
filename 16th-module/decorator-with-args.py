import functools
import time
from collections.abc import Callable


def timer(func: Callable) -> Callable:
    """Декоратор-таймер для подсчета времени выполнения функции."""
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        started_at = time.time()
        result = func()
        ended_at = time.time()
        run_time = round(ended_at - started_at, 4)
        print(f"Функция {func.__name__} выполнялась {run_time} секунд")
        return result
    
    return wrapper


@timer
def hard_func() -> list:
    """Функция, возвращающая список выражений чисел в заданном диапазоне."""
    return [x ** 2 ** x for x in range(22)]


print(hard_func)

print(hard_func.__doc__)
print(hard_func.__name__)
