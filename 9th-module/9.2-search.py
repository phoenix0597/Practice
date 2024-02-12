# Задача Поиск.
# Входные данные:
# Путь к директории где ищем заданное имя файла
#
# Выходные данные
# Абсолютный путь к файлу
import os


def find_file(dir_to_search_in, file_name, verbose=True):
    if verbose:
        print('Переходим в каталог', dir_to_search_in)
    for i_elem in os.listdir(dir_to_search_in):
        path = os.path.join(dir_to_search_in, i_elem)
        if verbose:
            print('\t', 'Смотрим в', path)
        if file_name == i_elem:
            result = os.path.abspath(path)
            return result
        if os.path.isdir(path):
            if verbose:
                print('\tЭто каталог')
            result = find_file(path, file_name, verbose)
            if result:
                return result
    return None


# ---------- тесты ----------
def test(func):
    # curr_dir = os.getcwd()
    curr_dir = os.path.abspath(os.path.join('..', '..', 'Practice'))
    # print('Каталог для поиска:', curr_dir)
    tests_list = [
        (curr_dir, 'root_dir.py'),
        (curr_dir, '9.1-lesson-resume.md'),
        (curr_dir, 'test_none.py'),
        (curr_dir, 'dogs_scores.py'),
    ]
    
    test_results = dict()
    args = [i_elem for i_elem in tests_list]
    print('Тесты: ', args)
    
    for ind, (curr_dir, file_name) in enumerate(args):
        if func(curr_dir, file_name, verbose=False) == os.path.abspath(file_name):
            test_results['Тест #' + str(ind+1)] = 'OK'
        else:
            test_results['Тест #' + str(ind+1)] = 'FAIL'
    
    exit(0)
    
    # # тест #1
    # if func(*tests_list[0]) == os.path.abspath('root_dir.py'):
    #     test_results['Тест #1'] = 'OK'
    # else:
    #     test_results['Тест #1'] = 'FAIL'
    # # тест #2
    # if func(*tests_list[1]) == os.path.abspath('9.1-lesson-resume.md'):
    #     test_results['Тест #2'] = 'OK'
    # else:
    #     test_results['Тест #2'] = 'FAIL'
    # # тест #3
    # if func(*tests_list[2]) is None:
    #     test_results['Тест #3'] = 'OK'
    # else:
    #     test_results['Тест #3'] = 'FAIL'
    # # тест #4
    # if func(*tests_list[3]):
    #     test_results['Тест #4'] = 'OK'
    # else:
    #     test_results['Тест #4'] = 'FAIL'
    
    for test_num, test_result in test_results.items():
        print('  ', test_num, '-', test_result)

# ---------- запуск тестов ----------
print('Запуск тестов............')
test(find_file)
print('Тесты завершены...........')
