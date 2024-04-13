# Входные данные:
# text = "AV is largest Analytics community of India"

# Выходные данные:
# Слова, начинающиеся на гласную букву: ['AV', 'is', 'Analytics', 'of', 'India']

import re

text = 'AV is largest Analytics community of India'
result = re.findall(r'\b[aeiou]\w+', text, flags=re.I)
print('Слова, начинающиеся на гласную букву:', result)
