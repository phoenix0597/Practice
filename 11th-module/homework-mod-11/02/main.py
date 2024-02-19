# Задача 2. Студенты
# Что нужно сделать.
# Реализуйте модель с именем Student, содержащую поля «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
# Затем создайте список из десяти студентов (данные о студентах можете придумать или запросить у пользователя)
# и отсортируйте список по возрастанию среднего балла. Выведите результат на экран.
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
# Сообщения о процессе получения результата осмысленны и понятны для пользователя.
# Переменные, функции и собственные методы классов имеют значащие имена, не a, b, c, d.
import random
from students import Student


def generate_names(surnames_lst: list, names_lst: list, comb_count: int) -> list:
    """
    Генерируем список уникальных вариантов ФИ в заданном количестве
    :param surnames_lst:
    :param names_lst:
    :param comb_count:
    :return:
    """
    if comb_count > len(surnames_lst) * len(names_lst):
        raise ValueError(
            f"Ошибка: {comb_count} превышает максимальное количество уникальных вариантов.\n"
            f"Необходимо увеличить количество исходных данных!")
    
    combinations = []
    while len(combinations) < comb_count:
        surname = random.choice(surnames_lst)
        name = random.choice(names_lst)
        combination = f"{surname} {name}"
        if combination not in combinations:
            combinations.append(combination)
    
    return combinations


def sort_students_by_score(students: list[Student]) -> list[Student]:
    """
    Получаем список студентов, отсортированных по средней оценке
    :param students:
    :return:
    """
    if len(students) == 0:
        raise ValueError('Список студентов пуст')
    return sorted(students, key=lambda student: student.average_score())


def create_students(count: int, surnames_list: list, names_list: list) -> list[Student]:
    """
    Генерируем список из заданного количества студентов с уникальными ФИ, случайными группами и оценками
    :param count:
    :param surnames_list:
    :param names_list:
    :return:
    """
    students_list = []
    try:
        students_fi_list = generate_names(surnames_list, names_list, count)
        for i in range(1, count + 1):
            name = students_fi_list[i - 1]
            group = random.randint(1, 5)
            score = [random.randint(1, 10) for _ in range(5)]
            student = Student(name, group, score)
            students_list.append(student)
    except ValueError as ex:
        print(ex)
    
    return students_list


# исходные данные для генерации случайных неповторяющихся ФИ
surnames = ['Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Смирнов', 'Колесов', 'Михайлов', 'Николаев', 'Белов', 'Орлов']
names = ['Иван', 'Петр', 'Сидор', 'Кузьма', 'Сергей', 'Коля', 'Михаил', 'Никита', 'Борис', 'Олег']
# surnames = []
# names = []

# создаем список студентов и сортируем его по средней оценке
try:
    stud_list = create_students(10, surnames, names)
    sorted_students = sort_students_by_score(stud_list)
except ValueError as e:
    print(e)
    exit()

# выводим результат
print("Список студентов по возрастанию среднего балла:")
for num, stud in enumerate(sorted_students, 1):
    print(f'\n{num}-й студент: ')
    stud.print_info()
