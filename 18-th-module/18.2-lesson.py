import re

text = 'AV - Analytics Vidhya AV'
# text = re.sub('AV', 'AV Analytics Vidhya', text, flags=re.I)
# print(text)
result = re.match(r'AV', text, flags=re.I)  # поиск в начале строки по шаблону
print('Поиск в начале строки по шаблону:', result)
print(result.group(0))
print(result.span(0))
print(result.start())
print(result.end())

result = re.match(r'Analytics', text)
print('Поиск в начале строки по шаблону:', result)

print('=' * 50)

# r в начале подстроки поиска означает, что мы используем сырую строку (raw string)
# и не будем экранировать все специальные символы

result = re.match(r'A\w+', text)
print('Поиск по шаблону "A\\w+" (r в начале подстроки поиска):', result)

# Чтобы найти нужную подстроку можно использовать методы findall и search

result = re.findall(r'AV', text, flags=re.I)  # поиск в строке по шаблону
print('Поиск всех подстрок по шаблону "AV" с помощью findall:', result)

result = re.search(r'AV', text, flags=re.I)  # поиск в строке по шаблону
print('Поиск первой подстроки по шаблону "AV" с помощью search:', result.group(0))
# print(result.group())

print('=' * 50)

# Замена подстроки на другую
text_2 = 'AV is largwst Analytics community in India. India!'
result = re.sub(r'India', 'the world', text_2)
print(result)

print('=' * 50)

# Собираем регулярное выражение в объект, который, в свою очередь, можно использовать для поиска в разных текстах,
# не переписывая его заново
pattern = re.compile(r'AV', flags=re.I)
result = pattern.findall(text)
print('Поиск первой подстроки по шаблону "AV" с помощью search и созданного объекта:', result)

result_2 = pattern.findall(text_2)
print('Поиск первой подстроки по шаблону "AV" с помощью search и созданного объекта:', result_2)
