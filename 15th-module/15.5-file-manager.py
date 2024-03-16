# class File:
#     def __init__(self, file_name, mode='w', encoding='utf-8'):
#         self.file = open(file_name, mode, encoding)
#
#     def __enter__(self) -> 'File':
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# with File('file.txt', 'w', 'utf-8') as file:
#     file.write('Всем привет!')


class File:
    """
    Контекстный менеджер для работы с файлами.
    Принимает на вход имя файла и режим чтения/записи, открывает файл в начале работы
    и закрывает в конце.
    Пример использования:
        with File('example.txt', 'w', 'utf-8') as file:
            file.write('Всем привет!')
    """
    
    def __init__(self, filename: str, mode: str, encoding: str = 'utf-8'):
        """
        Инициализирует объект File.
        Args:
            filename (str): Имя файла.
            mode (str): Режим чтения/записи файла.
        """
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None
    
    def __enter__(self) -> 'File':
        """
        Открывает файл и возвращает файловый объект.
        Returns:
            file: Открытый файловый объект.
        """
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        """
        Закрывает файл после выхода из контекстного менеджера.
        Args:
            exc_type: Тип исключения, если оно было вызвано
            exc_value: Значение исключения, если оно было вызвано
            traceback: Трассировка стека, если исключение было вызвано.
        """
        self.file.close()


# Пример использования
if __name__ == "__main__":
    with File('example.txt', 'w', 'utf-8') as file:
        file.write('Всем привет!')
    
    with File('example.txt', 'r', 'utf-8') as file:
        content = file.read()
        print(content)  # Выведет: Всем привет!

# Этот код реализует класс `File`, который является контекстным менеджером для работы с файлами.
# Он принимает на вход имя файла и режим чтения/записи, открывает файл в начале работы с помощью метода `__enter__`
# и закрывает файл в конце с помощью метода `__exit__`.
#
# В методе `__init__` происходит инициализация объекта `File` с заданными именем файла и режимом чтения/записи.
# Метод `__enter__` открывает файл и возвращает файловый объект. Метод `__exit__` закрывает файл
# после выхода из контекстного менеджера.
#
# В коде также добавлены docstrings на русском языке для описания класса и его методов. Кроме того,
# использованы аннотации типов для параметров и возвращаемых значений.
#
# В конце кода приведен пример использования класса `File`. Сначала открывается файл `example.txt` в режиме записи, и в
# него записывается строка "Всем привет!". Затем файл открывается в режиме чтения, и его содержимое выводится на экран.
#
# При запуске этого кода в консоли будет выведено:
#
# Всем привет!
