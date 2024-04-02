## Итоги 16 модуля
1. Если нам нужно быстро реализовать функцию в качестве контекст-менеджера, то для этого используется декоратор 
```@contextmanager``` из библиотеки ```contextlib```
2. Если нам нужно реализовать декоратор, принимающий аргументы, то для этого нам нужно реализовать просто 
еще один слой с функцией, которая будет принимать нужные аргументы и возвращать вложенный декоратор:
```python
def timer_with_presicion(precision: int):
    def timer_decorator(func):
        pass

```
3. Декораторы можно также использовать для классов. Обычно декоратор класса никак не будет затрагивать содержимое 
этого класса - он работает только с его инстансом.
4. Если мы хотим модифицировать поведение внутри класса, то для этого понадобится декоратор с аргументом, а также
функции dir(), getattr() и setattr():
```python
import functools


def for_all_methods(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                setattr(cls, i_method_name, decorator(getattr(cls, i_method_name)))
        return cls
    
    return decorate 
```

5. Декоратор также можно реализовать как отдельный класс, однако используется это крайне редко.
```
@CountCalls
```