import functools
import time
from typing import Callable


def slowdown(n_seconds: int) -> Callable:
    def slowdown_decorator(func: Callable) -> Callable:
        """Функция-декоратор, которая задерживает выполнение декорируемой функции на n_seconds секунд."""
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Callable:
            """Функция-обертка для декорируемой функции."""
            time.sleep(n_seconds)
            
            return func(*args, **kwargs)
        
        return wrapper
    
    return slowdown_decorator


@slowdown(n_seconds=7)
def slow_func(a: int, b: int) -> int:
    """Функция, которая складывает два целых числа."""
    return a + b


if __name__ == '__main__':
    print(slow_func(1, 2))
