while True:
    grats_template = input("Введите шаблон поздравления, "
                           "в шаблоне нужно использовать конструкцию "
                           "{name} и {age}: ")
    if '{name}' in grats_template and '{age}' in grats_template:
        break
    print("Шаблон поздравления должен содержать {name} и {age}!")

names_list = input("Введите список людей через запятую: ").split(', ')  # ['Tom', 'Bob', 'Sam']
ages_str = input("Введите список возрастов через пробел: ")  # 25 30 35

ages = [int(i_age) for i_age in ages_str.split()]

for i_man in range(len(names_list)):
    print(grats_template.format(name=names_list[i_man], age=ages[i_man]))

people = [
    ' '.join([names_list[i_man], str(ages[i_man])])
    for i_man in range(len(names_list))
]

people_str = ', '.join(people)
print("Именинники: ", people_str)