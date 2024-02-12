# Задача "Проекты"
# Входные данные:
# Список проектов ['Skillbox', 'My_project']
# Выходные данные:
# Абсолютные пути к содержимому проектов
#
# Содержимое проекта My_project:
# something - dir
# data.txt
# my_database.db
# script.py
import os


def print_dirs(projects_dir):
    print('\nСодержимое проекта', projects_dir)
    if os.path.exists(projects_dir):
        print('\t', os.listdir(projects_dir))
        for i_file in os.listdir(projects_dir):
            path = os.path.join(projects_dir, i_file)
            print('\t', path)
        print('\t Всего файлов и папок:', len(os.listdir(projects_dir)))
    else:
        print('\nКаталога проекта', projects_dir, 'не существует')
        # print('\n\t Каталога проекта не существует')
        
    
project_list = ['Prod', 'Practice', 'Module21']
for i_project in project_list:
    path_to_project = os.path.abspath(os.path.join('..', '..', i_project))
    print_dirs(path_to_project)
