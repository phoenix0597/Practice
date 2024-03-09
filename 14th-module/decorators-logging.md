Декораторы в Python - это функции, которые принимают другую функцию в качестве аргумента, добавляют к ней некоторую функциональность и возвращают новую, модифицированную функцию. Они позволяют изменять поведение функции без изменения ее кода.

Декораторы часто используются для:

1. **Логирования**: Декоратор может добавить логирование вызовов функции, ее аргументов, возвращаемых значений и времени выполнения.

2. **Кэширования**: Декоратор может кэшировать результаты вызова функции, чтобы избежать повторных вычислений при последующих вызовах с теми же аргументами.

3. **Проверки прав доступа**: Декоратор может проверять права доступа пользователя перед вызовом функции.

4. **Синхронизации**: Декоратор может добавить синхронизацию при вызове функции для безопасного доступа к общим ресурсам.

5. **Измерения производительности**: Декоратор может измерять время выполнения функции.

Вот простой пример декоратора для логирования:

```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function returned: {result}")
        return result
    return wrapper

@log_decorator
def add_numbers(a, b):
    return a + b

result = add_numbers(2, 3)
# Вывод:
# Calling function: add_numbers
# Function returned: 5
```

В этом примере `log_decorator` - это функция-декоратор, которая принимает функцию `func` в качестве аргумента. Внутри декоратора определяется вспомогательная функция `wrapper`, которая выполняет логирование и вызывает исходную функцию `func`. Затем декоратор возвращает функцию `wrapper`.

Применение `@log_decorator` к функции `add_numbers` приводит к тому, что вызов `add_numbers(2, 3)` на самом деле вызывает функцию `wrapper` из декоратора, которая выполняет логирование и затем вызывает исходную функцию `add_numbers`.

Декораторы позволяют добавлять дополнительную функциональность к функциям без изменения их кода, что повышает модульность и расширяемость программы.

