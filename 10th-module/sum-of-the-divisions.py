def devide(num: int) -> float:
    return 10 / num


def sum_of_devided(left: int, right: int) -> float:
    div_sum = 0
    for i_num in range(left, right + 1):
        try:
            div_sum += devide(i_num)
            print(div_sum)
        except ZeroDivisionError:
            print("Деление на ноль невозможно!")
    return div_sum


total = 0
try:
    with open("numbers.txt", "r", encoding="utf-8") as numbers_file:
        for line in numbers_file:
            nums_lst = line.split()
            left_num = int(nums_lst[0])
            right_num = int(nums_lst[1])
            total += sum_of_devided(int(left_num), int(right_num))
        print(f"Общая сумма: {total}")
        
except FileNotFoundError:
    print("Такого файла не существует!")
except ValueError:
    print("Невозможно преобразовать строку в число!")
except ZeroDivisionError:
    print("Деление на ноль невозможно!")
except Exception:
    print("Неизвестная ошибка!")

answer_file = open("answer.txt", "w", encoding="utf-8")
try:
    answer_file.write(f"Общая сумма: {total}")
except Exception:
    print("Неизвестная ошибка!")
else:
    print("Результат записан в файл.")
finally:  # код, который записан в этом блоке ВЫПОЛНИТСЯ ВСЕГДА
    answer_file.close()