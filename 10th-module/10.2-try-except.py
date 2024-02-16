num_sum = 0
nums_count = 0
try:
    with open("numbers.txt") as numbers_file:
        for line in numbers_file:
            nums_count += 1
            num_sum += int(line)
        print(f"Среднее арифметическое: {num_sum / nums_count}")
except FileNotFoundError:
    print("Такого файла не существует!")
except ValueError:
    print("Невозможно преобразовать строку в число!")