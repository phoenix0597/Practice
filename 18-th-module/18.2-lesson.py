import re
text = 'AV - Analytics Vidhya AV'
# text = re.sub('AV', 'AV Analytics Vidhya', text, flags=re.I)
# print(text)
result = re.match('AV', text, flags=re.I)