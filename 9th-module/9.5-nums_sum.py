# Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке.
# Напишите программу, которая выводит их сумму в выходной файл answer.txt.
#
# Пример:
# Содержимое файла numbers.txt:
# 1
# 2
# 3
# 4
# 10
#
# Содержимое файла answer.txt
# 20
# Context from Code Snippet Practice\9th-module\9.5-nums_sum.py
with open('numbers.txt', 'r') as file:
    numbers = [int(line) for line in file]
print('\nСодержимое файла numbers.txt:')
with open('numbers.txt', 'r') as file_1:
    content_1 = file_1.read()
    print(content_1)

with open('answer.txt', 'w') as file_2:
    file_2.write(str(sum(numbers)))

print('\nСодержимое файла answer.txt:')
with open('answer.txt', 'r') as file_2:
    content_2 = file_2.read()
    print(content_2)
    