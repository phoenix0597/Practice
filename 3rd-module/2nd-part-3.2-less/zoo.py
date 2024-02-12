zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
zoo_rus = ['лев', 'кенгуру', 'слон', 'обезьяна']
print("\nЗоопарк: ", zoo)
new_animal = input('\nКакое животное вы хотите добавить (in english)? ')
new_animal_rus = input(f'\nВведите русское название {new_animal}: ')

if new_animal != '' and new_animal not in zoo:
	cage_num = int(
		input(f'В какую клетку поместить животное {new_animal_rus.capitalize()} (целое число от 1 до 5)? ')
	)
	if 0 < cage_num <= len(zoo):
		zoo.insert(cage_num - 1, new_animal)
		zoo_rus.insert(cage_num - 1, {new_animal_rus})
		print("Зоопарк: ", zoo)
	else:
		print("Такой клетки нет")

num = input(
	"Про скольких животных вы хотите узнать информацию (номер клетки, в которой оно находится)? "
)
if 0 < int(num) <= len(zoo):
	for i in range(1, int(num) + 1):
		print("Назовите животное (in english): ", end="")
		animal = input()
		if animal in zoo:
			print(f"{zoo_rus[zoo.index(animal)].capitalize()} сидит в клетке {zoo.index(animal) + 1}")
		else:
			print("Такого животного нет в зоопарке")
else:
	print("Столько животных в зоопарке нет")
