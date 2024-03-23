import os
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def in_dir(path: str) -> Iterator[None]:
    """
    Контекст-менеджер для временного изменения текущей рабочей директории.

    :param path: Путь новой директории, куда необходимо перейти.
    :return: None
    """
    original_dir = os.getcwd()
    try:
        # Переход в новую директорию
        os.chdir(path)
        yield
    except FileNotFoundError:
        print(f"Директория {path} не найдена.")
    finally:
        # Возврат в исходную директорию
        os.chdir(original_dir)


# Пример использования
if __name__ == "__main__":
    print(f"Текущая директория до смены: {os.getcwd()}")
    try:
        with in_dir("C:\\"):
            print(f"Новая текущая директория: {os.getcwd()}")
            print(os.listdir())
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print(f"Текущая директория после смены: {os.getcwd()}")
