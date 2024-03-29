Вот простой пример использования декоратора для измерения времени выполнения функции в Python:

```python
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнялась {execution_time:.6f} секунд")
        return result
    return wrapper

@timing_decorator
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(f"Факториал 5: {factorial(5)}")
print(f"Факториал 10: {factorial(10)}")
```

Вывод:
```
Функция factorial выполнялась 0.000002 секунд
Факториал 5: 120
Функция factorial выполнялась 0.000004 секунд
Факториал 10: 3628800
```

Разберем работу этого декоратора:

1. Функция `timing_decorator` принимает функцию `func` в качестве аргумента.
2. Внутри `timing_decorator` определяется вспомогательная функция `wrapper`.
3. В начале функции `wrapper` получается текущее время с помощью `time.time()` и сохраняется в переменной `start_time`.
4. Затем `wrapper` вызывает исходную функцию `func` с переданными аргументами, и ее результат сохраняется в переменной `result`.
5. После выполнения `func` снова получается текущее время с помощью `time.time()` и сохраняется в переменной `end_time`.
6. Вычисляется разница `end_time - start_time`, которая представляет время выполнения функции `func`, и сохраняется в переменной `execution_time`.
7. Выводится сообщение с именем функции `func` и временем ее выполнения `execution_time`.
8. Функция `wrapper` возвращает результат `result` исходной функции `func`.
9. Функция `timing_decorator` возвращает `wrapper`.
10. Декоратор `@timing_decorator` применяется к функции `factorial`.
11. При вызове `factorial(5)` и `factorial(10)` сначала вызывается `wrapper` из декоратора, который измеряет время выполнения функции `factorial` и выводит его на экран.

Этот декоратор измерения времени выполнения может быть полезен для отладки и оптимизации производительности программы. Он позволяет легко измерять время выполнения любой функции, не изменяя ее код.

Обратите внимание, что в этом примере используется функция `time.time()` из модуля `time` для получения текущего времени. Она возвращает количество секунд, прошедших с определенного момента времени (называемого "эпохой"). Разница между двумя значениями, полученными с помощью `time.time()`, дает время выполнения кода между этими двумя моментами.

Также стоит отметить, что для более точного измерения времени выполнения коротких функций может потребоваться использовать более точные таймеры, такие как `time.perf_counter()` или `time.process_time()`, которые имеют более высокое разрешение, чем `time.time()`.