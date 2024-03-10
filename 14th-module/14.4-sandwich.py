from typing import Callable


def get_some_buns(func: Callable) -> Callable:
    """Декоратор для добавления хлеба к блюду."""
    
    def wrap_that_buns(*args, **kwargs):
        print('</---------\\>')
        func(*args, **kwargs)
        print('<\\______/>')
    
    return wrap_that_buns


def get_some_salad(func: Callable) -> Callable:
    """Декоратор для добавления ингредиентов к блюду."""
    
    def wrap_that_salad(*args, **kwargs):
        print('#помидоры#')
        func(*args, **kwargs)
        print('~салат~')
    
    return wrap_that_salad


@get_some_buns
@get_some_salad
def make_sandwich(ingredient: str):
    print(ingredient)


make_sandwich('~ветчина~')
