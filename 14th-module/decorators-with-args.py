from typing import Any


def benchmark(iters: int) -> Any:
    """Декоратор для подсчета времени выполнения функции."""
    def actual_decorator(func: Any) -> Any:
        """Функция декоратора."""
        import time
        
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Внутренняя функция декоратора."""
            total = 0
            for i in range(iters):
                start = time.time()
                return_value: object = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total / iters))
            return return_value
        
        return wrapper
    
    return actual_decorator


@benchmark(iters=10)
def fetch_webpage(url: str) -> str:
    """Получить содержимое веб-страницы."""
    import requests
    web_page = requests.get(url)
    return web_page.text


webpage = fetch_webpage('https://google.com')
print(webpage)
