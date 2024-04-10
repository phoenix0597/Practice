while True:
    grats_template = input("Введите шаблон поздравления, "
                           "в шаблоне нужно использовать конструкцию {name}: ")
    if '{name}' in grats_template:
        break
    print("Шаблон поздравления должен содержать {name}.")

print("Введите список имен (заканчивается на end): ")
names_list = []
while True:
    name = input()
    if name == 'end':
        break
    names_list.append(name)

for i_name in names_list:
    print(grats_template.format(name=i_name))