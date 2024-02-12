langs = ['Python', 'Java', 'JS',  'SQL']
user_langs = input('После какого языка вставить С++: ')
i_user_langs = langs.index(user_langs)

langs.insert(i_user_langs + 1, 'C++')

print("Новый рейтинг языков: ", langs)

