# Задача 2. Логирование
# Возможно, вы замечали, что некоторые программы не просто выдают ошибку и закрываются,
# но и записывают эту ошибку в файл. Таким образом проще сформировать отчёт об ошибках, а значит,
# программисту будет проще их исправить. Это называется логированием ошибок.
#
# Дан файл words.txt, в котором построчно записаны слова. Необходимо определить количество слов,
# из которых можно получить палиндром (привет предыдущим модулям). Если в строке встречается число,
# то программа выдаёт ошибку ValueError и записывает эту ошибку в файл errors.log
def string_contains_number(string):
    for char in string:
        if char.isdigit():
            return True
    return False


try:
    with open('words.txt', 'r', encoding='utf-8') as file:
        count = 0
        for ind, line in enumerate(file):
            line = line.rstrip('\n')
            if string_contains_number(line):
                raise ValueError
            if line == line[::-1]:
                count += 1
        print(count)
except FileNotFoundError:
    print('File not found')
except ValueError:
    with open('errors.log', 'a', encoding='utf-8') as file:
        file.write(f'String #{ind + 1} ("{line}") contains number\n')
        print(f'\nString #{ind + 1} ("{line}") contains number. Added to errors.log')
finally:
    print('File \'words.txt\' contains', count, 'palindromes.')
