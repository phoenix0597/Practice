from typing import Callable, Dict

PLUGINS: Dict[str, Callable] = dict()


def register(func: Callable) -> Callable:
    """Декоратор для регистрации плагина."""
    
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name: str) -> str:
    return "Hello, {name}!".format(name=name)


@register
def say_bye(name: str) -> str:
    return "Bye, {name}!".format(name=name)


for name, func in PLUGINS.items():
    print("{name} - {func}".format(name=name, func=func))


# print(PLUGINS)
#
# print(say_hello("John"))
