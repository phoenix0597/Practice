names = ['John', 'Corey', 'Adam']
ages = [45, 40, 35]

# zip - переводится как "упаковать", в скобках функции - итерируемые объекты, которые нужно упаковать в один
people = zip(names, ages)
print(list(people))

people_2 = zip(names, ages)
print(dict(people_2))

# функцию zip можно использовать в представлениях словарей (равно как и списков)
people_3 = {
	i_name: i_age + 10
	for i_name, i_age in zip(names, ages)
}

print(people_3)