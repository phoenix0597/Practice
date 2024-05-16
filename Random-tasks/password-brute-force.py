import zipfile
from typing import List
import logging

# Настройка логирования
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def get_password_list(frst_part_list: List[str], scnd_part_list: List[str]) -> list:
    """
    Генерирует список паролей из двух списков. Предназначен для генерации паролей, состоящих из двух частей.
    Каждый пароль является комбинацией из двух частей, где каждая часть является списком
    из возможных вариантов начала/конца пароля.
    Args:
        frst_part_list: список возможных вариантов начала пароля
        scnd_part_list: список возможных вариантов конца пароля
    """
    
    combinations = [f"{first_item}{second_item}" for first_item in frst_part_list for second_item in scnd_part_list]
    
    logging.info('Сгенерированы комбинации паролей.')
    # Для демонстрации может быть много, поэтому закомментировано:
    # logging.debug(f'Комбинации паролей: {combinations}')
    return combinations


def extract_file(passwd_list, path_to_arch_file):
    """
    Пытается разархивировать файл, используя пароли из списка pass_list.
    Выводит пароль, если он подошел для разархивирования.
    Args:
        passwd_list: список паролей, которые нужно проверить - подходят ли они для разархивирования
        path_to_arch_file: путь к архиву
    """
    
    logging.info(f'Начало процесса распаковки файла {path_to_arch_file}.')
    for password in passwd_list:
        try:
            with zipfile.ZipFile(path_to_arch_file, 'r') as zip_file:
                zip_file.extractall(pwd=password.encode())
                logging.info(f"Пароль найден: {password}")
                return
        except RuntimeError as e:
            logging.error(f"Ошибка runtime при попытке использовать пароль {password}: {e}")
            continue
        except zipfile.BadZipFile as e:
            logging.error(f"Некорректный формат zip-файла {path_to_arch_file}: {e}")
            continue
        except Exception as e:
            logging.error(f"Неожиданная ошибка при попытке использовать пароль {password}: {e}")
            continue
    
    # Если ни один из паролей не подошел
    logging.warning("Пароль не найден в списке.")


first_part_list = []  # Здесь задаются возможные варианты начала пароля
second_part_list = []  # Здесь задаются возможные варианты конца пароля

path_to_file = r"D:\Path\to\archive\file.zip"  # Путь к архиву

pass_list = get_password_list(first_part_list, second_part_list)

extract_file(pass_list, path_to_file)
