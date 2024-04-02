import functools
from typing import Callable


def logging(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Вызов функции {func.__name__}')
        return func(*args, **kwargs)
    
    return wrapper


def for_all_methods(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                setattr(cls, i_method_name, decorator(getattr(cls, i_method_name)))
        return cls
    
    return decorate


# @logging
@for_all_methods(logging)
class MyClass:
    def method_1(self) -> None:
        print('method_1')
    
    def method_2(self) -> None:
        print('method_2')
    
    def method_3(self) -> None:
        print('method_3')


mc = MyClass()
mc.method_1()
mc.method_2()
mc.method_3()
