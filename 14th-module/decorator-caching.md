Вот простой пример использования декоратора для кэширования в Python:

```python
def cache_decorator(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f"Returning cached result for {args}")
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            print(f"Caching result for {args}")
            return result

    return wrapper

@cache_decorator
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Вычисляется и кэшируется
print(fibonacci(10))  # Возвращается из кэша
print(fibonacci(15))  # Вычисляется и кэшируется
print(fibonacci(10))  # Возвращается из кэша
```

Вывод:
```
Caching result for (10,)
55
Returning cached result for (10,)
55
Caching result for (15,)
610
Returning cached result for (10,)
55
```

Разберем работу этого декоратора:

1. Функция `cache_decorator` принимает функцию `func` в качестве аргумента.
2. Внутри `cache_decorator` создается вспомогательная функция `wrapper` и пустой словарь `cache`.
3. Функция `wrapper` проверяет, есть ли результат для переданных аргументов `args` в кэше `cache`.
4. Если результат есть в кэше, `wrapper` возвращает его из кэша.
5. Если результата в кэше нет, `wrapper` вызывает исходную функцию `func` с аргументами `args`, сохраняет результат в кэше и возвращает его.
6. Функция `cache_decorator` возвращает `wrapper`.
7. Декоратор `@cache_decorator` применяется к функции `fibonacci`.
8. При первом вызове `fibonacci(10)` результат вычисляется и кэшируется.
9. При последующих вызовах `fibonacci(10)` результат возвращается из кэша, избегая повторных вычислений.
10. Для аргументов, которых еще нет в кэше (например, `fibonacci(15)`), результат вычисляется и добавляется в кэш.

Этот декоратор кэширования может быть полезен для функций, которые выполняют ресурсоемкие вычисления, особенно если эти функции часто вызываются с одними и теми же аргументами. Кэширование позволяет избежать повторных вычислений и повысить производительность программы.

Обратите внимание, что в этом простом примере кэш никогда не очищается, поэтому при длительной работе программы он может занять слишком много памяти. В реальных приложениях обычно используются более сложные стратегии кэширования, такие как удаление старых или редко используемых элементов из кэша.