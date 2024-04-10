# task/group_1.txt
# Бобровский Игорь 10
# Дронов Александр 20
# Жуков Виктор 30

# task/Additional_info/group_2.txt
# Павленков Геннадий 20
# Щербаков Владимир 35
# Marley Bob 15
# sym_count.txt - количество символов в каждой строчке
import os


def read_scores(file_path):
    """
    Функция для чтения очков из файла.
    Параметры:
        file_path (str): Путь к файлу с очками.
    Возвращает:
        list: Список очков.
    """
    scores = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(' ')
            if parts:  # Если строка не пустая
                try:
                    score_count = int(parts[-1])  # Предполагаем, что очки находятся в последнем столбце
                    scores.append(score_count)
                except ValueError:
                    continue  # В случае ошибки преобразования пропускаем некорректную строку
    return scores


def count_syms_in_lines(file_path):
    """
    Функция для подсчета количества символов в каждой строчке из файла.
    Параметры:
        file_path (str): Путь к файлу с очками.
    Возвращает:
        list: Список количества символов в каждой строчке.
    """
    syms_count = []
    with open(file_path, 'r', encoding='utf-8') as inp_file:
        for i_line in inp_file:
            syms_count.append(len(i_line))
    return syms_count


# Пути к файлам
path_group_1 = os.path.join(os.getcwd(), 'task', 'group_1.txt')
path_group_2 = os.path.join(os.getcwd(), "task", "Additional_info", "group_2.txt")
path_to_speakers = os.path.join(os.getcwd(), "speakers.txt")

# Чтение очков групп
scores_group_1 = read_scores(path_group_1)
scores_group_2 = read_scores(path_group_2)

# Вычисление суммы, разности и произведения очков
sum_group_1 = sum(scores_group_1)
difference_group_1 = max(scores_group_1) - min(scores_group_1)  # Разность между максимальным и минимальным значением
product_group_2 = 1
for score in scores_group_2:
    product_group_2 *= score
   
    
# Запись в файл sym_count.txt количества символов в каждой строчке файла
# (числа списка, возвращаемого функцией count_syms_in_lines)
def write_file(file_path, syms_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        for count in syms_list:
            print(str(count))
            file.write(str(count) + '\n')


# Вывод результатов
print("Сумма очков первой группы:", sum_group_1)
print("Разность очков первой группы (между максимальным и минимальным значениями):", difference_group_1)
print("Произведение очков второй группы:", product_group_2)

syms_count_1 = count_syms_in_lines(path_to_speakers)
print("Количество символов в каждой строчке первого файла:", syms_count_1)
new_file_path = os.path.join(os.getcwd(), "sym_count.txt")
write_file(new_file_path, syms_count_1)