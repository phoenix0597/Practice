# Дан немного изменённый текст скороговорки:
#
# How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,
#
# Напишите программу, которая выводит список из всех упоминаний подстроки \wwood+?,
#
# Ожидаемый результат:
# Список всех упоминаний шаблона: ['\\wwood+?,', '\\wwood+?,']

import re

text = r'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,'
pattern = re.compile(r'\\wwood\+\?,')
result = pattern.findall(text)
print('Список всех упоминаний шаблона:', result)
