import os


def process_files():
    # Пути к файлам
    path_group_1 = os.path.join(os.getcwd(), 'task', 'group_1.txt')
    path_group_2 = os.path.join(os.getcwd(), "task", "Additional_info", "group_2.txt")
    
    # Работаем с первой группой
    with open(path_group_1, 'r', encoding='utf-8') as file:
        group_1_scores = [int(line.split()[-1]) for line in file]
    
    # Работаем со второй группой
    with open(path_group_2, 'r', encoding='utf-8') as file:
        group_2_scores = [int(line.split()[-1]) for line in file]
    
    # Вычисляем сумму, разность и произведение
    sum_group_1 = sum(group_1_scores)
    diff_group_1 = max(group_1_scores) - min(group_1_scores)
    prod_group_2 = 1
    for score in group_2_scores:
        prod_group_2 *= score
    
    # Возвращаем результаты
    return sum_group_1, diff_group_1, prod_group_2


def test_process_files(func):
    # Предполагаемый результат
    exp_sum_group_1 = 60
    exp_diff_group_1 = 20
    exp_prod_group_2 = 10500  # 20 * 35 * 15

    # Получаем результаты выполнения функции
    results = func()
    
    # Проверяем каждое значение
    print("Проверяем результаты выполнения функции...")
    print("Сумма очков первой группы:",
          "OK" if results[0] == exp_sum_group_1 else "FAIL")
    print("Разность максимального и минимального количества очков первой группы:",
          "OK" if results[1] == exp_diff_group_1 else "FAIL")
    print("Произведение очков второй группы:",
          "OK" if results[2] == exp_prod_group_2 else "FAIL")
    
    # Проверяем, что все тесты прошли успешно
    if results[0] == exp_sum_group_1 and results[1] == exp_diff_group_1 and results[2] == exp_prod_group_2:
        print("Все тесты пройдены успешно!")
    else:
        print("Не все тесты пройдены успешно.")


# Вызываем тестовую функцию для проверки
test_process_files(process_files)
