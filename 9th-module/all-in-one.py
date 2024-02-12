import os


def find_py_files_in_module_dirs(root_folder, module_prefix='Module'):
    scripts = {}
    for root, dirs, files in os.walk(root_folder):
        for dir_name in dirs:
            if dir_name.startswith(module_prefix):
                module_path = os.path.join(root, dir_name)
                for inner_root, _, inner_files in os.walk(module_path):
                    for file_name in inner_files:
                        if file_name.endswith('.py'):
                            script_path = os.path.join(inner_root, file_name)
                            module_key = os.path.relpath(inner_root, root_folder)
                            if module_key not in scripts:
                                scripts[module_key] = []
                            scripts[module_key].append(script_path)
    return scripts


def write_scripts_to_file(script_paths_by_module, output_file='scripts.txt', delimiter='*' * 40):
    with open(output_file, 'w', encoding='utf-8') as f:
        for module_name, script_paths in script_paths_by_module.items():
            f.write(f"Скрипты, расположенные в папке {module_name}:\n\n")
            for script_path in script_paths:
                with open(script_path, 'r', encoding='utf-8') as script_file:
                    f.write(script_file.read())
                    f.write('\n' + delimiter + '\n')


# Задаем корневую директорию для поиска
root_dir = os.path.abspath(os.path.join('..', '..', os.curdir))
print('\nНачальная директория:', root_dir)

# Теперь вызываем функции:
module_script_paths = find_py_files_in_module_dirs(root_dir)
write_scripts_to_file(module_script_paths)
