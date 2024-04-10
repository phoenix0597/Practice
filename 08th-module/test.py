import copy
# import pprint


# функция принимает ключ и значение словаря, находит в значении ключа определенную подстроку и заменяет его на заданную
def replace_value(key_to_change, val_to_change: str, new_val: str, site_struct: dict):
    if key_to_change in site_struct:
        site_struct[key_to_change] = site_struct[key_to_change].replace(val_to_change, new_val)
    else:
        for val in site_struct.values():
            if isinstance(val, dict):
                replace_value(key_to_change, val_to_change, new_val, val)
                

def copy_site(site_templ):
    return copy.deepcopy(site_templ)


def get_product_name():
    prod_name = input('\nВведите название продукта для нового сайта: ')
    return prod_name


def create_new_site(keys_to_modify, site_templ):
    # создаем шаблон нового сайта путем глубокого копирования словаря-шаблона
    new_site = copy_site(site_templ)
    for i_key, i_val, new_val in keys_to_modify:
        replace_value(i_key, i_val, new_val, new_site)
    return new_site


# функция для печати словаря в человекоудобном виде (многострочном, с отступами)
def print_dict(dictionary, indent=0):
    for i_key, i_val in dictionary.items():
        print(' ' * indent, end='')
        print(f"'{i_key}': ", end='')
        if isinstance(i_val, dict):
            print('{')
            print_dict(i_val, indent + 4)
            print(' ' * indent, end='')
            print('}')
        else:
            print(f"'{i_val}'")


# словарь-шаблон для создания новых сайтов
site_template = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

sites_num = int(input('Сколько сайтов: '))
# новые сайты поместим в словарь сайтов, ключами которого будут названия продуктов, а значениями - словари новых сайтов
sites_dict = {}
for i in range(sites_num):
    product_name = get_product_name()
    
    # Ключи и значения, которые необходимо заменить в словаре-шаблоне
    keys_to_change = [
        ('title', 'телефон', product_name),
        ('h2', 'iphone', product_name)
    ]
    
    # создаем словарь нового сайта
    next_site = create_new_site(keys_to_change, site_template)
    
    # добавляем новый сайт в словарь сайтов
    sites_dict[product_name] = next_site
    
    # после добавления нового сайта в словарь сайтов, печатаем все активные сайты
    print('\nСписок активных сайтов:')
    for ind, (i_prod, i_site) in enumerate(sites_dict.items()):
        print(f'{ind + 1}) Сайт для {i_prod}: ')
        print('site = {')
        print_dict(i_site, 4)
        print('}')
        # pprint.pprint(i_site)
