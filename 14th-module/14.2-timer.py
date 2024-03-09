# Условие задачи:
# Написать декоратор для подсчета времени выполнения функции.
# Выходные данные:
# Среднее время выполнения функции в секундах.
import time
from typing import Callable, Any


def timer(func: Callable, *args: Any, **kwargs: Any) -> Any:
    """Функция-таймер для подсчета времени выполнения функции."""
    started_at = time.time()
    result = func(*args, **kwargs)
    ended_at = time.time()
    run_time = round(ended_at - started_at, 4)
    print('Время выполнения: {} секунд.'.format(run_time))
    
    return result


def squares_sum() -> int:
    """
    Для каждого числа от 0 до 100 создает список квадратов для i_num от 0 до 10000 и считает общую сумму этих квадратов.
    """
    number = 1000
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])
    
    return result


def cubes_sum(number: int) -> int:
    """
    Для каждого числа от 0 до number + 1 создает список кубов и суммирует их от 0 до 10000.
    """
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10000)])
    
    return result


my_result = timer(squares_sum)
print(my_result)

my_cubes_result = timer(cubes_sum, 1000)
print(my_cubes_result)
