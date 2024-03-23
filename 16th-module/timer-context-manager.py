import time
from contextlib import contextmanager


# class Timer:
#
#     def __init__(self):
#         self.start = None
#         self.end = None
#         self.interval = None
#
#     def __enter__(self):
#         self.start = time.perf_counter()
#         return self
#
#     def __exit__(self, *args):
#         self.end = time.perf_counter()
#         self.interval = self.end - self.start

@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield
    except Exception as ex:
        print(ex)
    finally:
        end = time.perf_counter()
        print(end - start)


# Функция time.perf_counter() в Python - это высокоточная функция, которая возвращает время,
# прошедшее с момента последнего вызова time.perf_counter(). Она измеряет время с помощью высокоточного счетчика
# (обычно на основе аппаратного обеспечения), что делает ее более точной, чем time.time(),
# которая использует системные часы
# Возвращаемое значение:
# Число с плавающей запятой, представляющее время в секундах с момента последнего вызова time.perf_counter().
# Например:
# print(time.perf_counter())
# 376379.6699431
# print(time.perf_counter())
# 376386.9261088

with timer() as t1:
    print('Первая часть')
    val_1 = 100 * 100 ** 100000
    # еще какой-то код

with timer() as t2:
    print('Вторая часть')
    val_2 = 200 * 200 ** 200000
    # еще какой-то код

with timer() as t3:
    print('Третья часть')
    val_3 = 300 * 300 ** 300000
    # еще какой-то код
