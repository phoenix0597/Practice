import py7zr
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
            with py7zr.SevenZipFile(path_to_arch_file, mode='r', password=password) as zip_file:
                zip_file.extractall()
                logging.info(f"Пароль найден: {password}")
                return
        except py7zr.exceptions.Bad7zFile as e:
            logging.error(f"Некорректный формат 7z-файла {path_to_arch_file} или неправильный пароль: {e}")
            continue
        except py7zr.exceptions.PasswordRequired as e:  # Использование более общего исключения для py7zr
            logging.error(f"Ошибка 7z при попытке использовать пароль {password}: {e}")
            continue
        except Exception as e:
            logging.error(f"Неожиданная ошибка при попытке использовать пароль {password}: {e}")
            continue
    
    logging.warning("Пароль не найден в списке.")


first_part_list = []  # Здесь задаются возможные варианты начала пароля
second_part_list = []  # Здесь задаются возможные варианты конца пароля

path_to_file = r"D:\Path\to\archive\file.7z"  # Путь к архиву

pass_list = get_password_list(first_part_list, second_part_list)

extract_file(pass_list, path_to_file)
