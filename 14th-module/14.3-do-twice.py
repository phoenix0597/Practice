from typing import Callable
from functools import wraps


def do_twice(func: Callable) -> Callable:
    """Декоратор, который вызывает функцию func дважды."""
    
    @wraps(func)
    def wrapped(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    
    return wrapped


@do_twice
def greeting(name: str) -> None:
    print("Hello, {name}!".format(name=name))


greeting("John")
print(greeting.__name__)