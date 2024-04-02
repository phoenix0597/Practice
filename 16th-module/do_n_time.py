from typing import Callable


def repeat(n: int = 2) -> Callable:
    """
    Декоратор, который повторяет вызов функции задекорированной функции n раз.

    Args:
    - n (int): Количество повторений вызова функции.

    Returns:
    - Callable: Декорированная функция.
    """
    
    def decorator_repeat(func: Callable) -> Callable:
        def wrapped(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        
        return wrapped
    
    return decorator_repeat


@repeat(n=5)
def greeting(name: str) -> None:
    """Выводит приветствие."""
    print(f"Hello, {name}!")


# Пример использования
greeting("John")

# Пример использования
greeting("Jane")