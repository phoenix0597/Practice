# Задача "Время создания"
# Условие задачи:
# - Классы
# - Объекты (инстансы) классов
#
# Выходные данные:
# - Дата и время в момент создания каждого объекта (в момент его инициализации в программе)
import functools
import time
from datetime import datetime, timezone
from typing import Callable


def createtime(cls):  # декорировать мы будем не функцию. а инстанс класса, поэтому передаем cls
    """ Декоратор класса. Выводит дату и время создания инстанса класса. """
    
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print(f'Время создания инстанса {cls.__name__}: {datetime.now(timezone.utc)}')
        # datetime.now(timezone.utc) - текущие дата и время во временной зоне UTC
        return instance
    
    return wrapper


def timer(func: Callable) -> Callable:
    """ Декоратор функции. Выводит время выполнения функции. """
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения функции {func.__name__}: {end - start}')
        return result
    
    return wrapper


def for_all_methods(decorator: Callable) -> Callable:
    """ Декоратор класса. Получает другой декоратор и применяет его ко всем методам класса. """
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method_name in cls.__dict__:
            if i_method_name.startswith('__') is False:
                setattr(cls, i_method_name, decorator(getattr(cls, i_method_name)))
        return cls
    return decorate


@createtime
@for_all_methods(timer)
class Functions:
    def __init__(self, max_num):
        self.max_num = max_num
    
    def squares_sum(self) -> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(self.max_num)])
        
        return result
    
    def cubes_sum(self, number: int) -> int:
        result = 0
        for _ in range(number):
            result += sum([i_num ** 3 for i_num in range(self.max_num)])
        
        return result


my_funcs_1 = Functions(max_num=1000)
time.sleep(1)
# my_funcs_2 = Functions(max_num=2000)
# time.sleep(2)
# my_funcs_3 = Functions(max_num=3000)
# Единственное отличие декоратора функции от декоратора класса - в качестве аргумента передается cls, а не func

my_funcs_1.squares_sum()
my_funcs_1.cubes_sum(number=2000)

# 1. Декораторы можно использовать для декорирования класса. В таком случае внутри декоратора будет использоваться
# вместо func стоит использовать cls
# 2. Обычно декоратор класса никак не будет затрагивать содержимое этого класса - он работает только с его инстансом.
# 3. Если мы хотим модифицировать поведение внутри класса, то понадобится декоратор с аргументом (кстати говоря,
# он не обязательно должен его принимать - можно оставить пустые скобки).
# 4. Для получения всех методов класса, включая магические, может использоваться функция dir(cls)
# 5. Чтобы с помощью имени взять метод класса в качестве объекта, используют функцию getattr(cls, i_method_name)
# 6. После декорирования метода необходимо заменить старый на новый. Для этого используется функция
# setattr(cls, i_method_name, decorated_method):
# setattr(cls, i_method_name, decorator(getattr(cls, i_method_name))), где decorator - декоратор метода, переданный
# в декоратор методов в качестве аргумента (def for_all_methods(decorator: Callable)).
