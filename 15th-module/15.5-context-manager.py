import time


class Timer:
    def __init__(self) -> None:
        print('Время работы кода:')
        self.start = None
    
    def __enter__(self) -> 'Timer':
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        print("=", time.time() - self.start, "секунд")
        # if exc_type is TypeError:
        #     return True  # с помощью return True мы "пропускаем ошибку мимо" и идем дальше по нашему коду
        # также здесь можно использовать и блоки try / except для обработки ошибок
        return True     # или просто return True, что будет означать, что мы в любом случае игнорируем ошибку
        # и выполняем код дальше


with Timer() as t1:
    print('Первая часть')
    val_1 = 100 * 100 ** 100000
    val_1 += 'str'
    # еще какой-то код

with Timer() as t2:
    print('Вторая часть')
    val_2 = 200 * 200 ** 200000
    # еще какой-то код

with Timer() as t3:
    print('Третья часть')
    val_3 = 300 * 300 ** 300000
    # еще какой-то код
