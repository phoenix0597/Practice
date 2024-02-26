class DivisionError(Exception):
    """Исключение, возникающее при попытке поделить меньшее число на большее."""
    pass


def divide_numbers(first, second):
    """Делит первое число на второе, выдает исключение, если первое меньше второго."""
    if first < second:
        raise DivisionError("Первое число меньше второго - деление невозможно")
    
    return first / second


def main():
    """Основная функция для чтения файла, деления чисел и вывода результата."""
    try:
        with open("numbers.txt", "r") as file:
            for line in file:
                numbers = line.split()  # Предполагается, что числа в файле разделены пробелом
                if len(numbers) != 2:
                    continue  # Пропускаем строки, где не два числа
                
                try:
                    num1, num2 = map(int, numbers)
                    result = divide_numbers(num1, num2)
                    print(f"Результат деления {num1} на {num2}: {result:.2f}")
                except DivisionError as e:
                    print(f"Ошибка: {e} (числа {num1} и {num2})")
                except ValueError:
                    print("Ошибка: Невозможно преобразовать одно из чисел в целое.")
                except ZeroDivisionError:
                    print("Ошибка: Деление на ноль.")
    except FileNotFoundError:
        print("Ошибка: Файл numbers.txt не найден.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()
