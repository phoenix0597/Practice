input_word_as_list = list(input("Введите слово: "))
replace_num = int(input("Какую букву заменить: "))
replace_sym = input("На что заменить: ")

# заменить букву под заданным номером в списке
input_word_as_list[replace_num - 1] = replace_sym

# перевести список в строку
input_word_as_string = ''.join(input_word_as_list)

print(f"Новое слово: {input_word_as_string}")
