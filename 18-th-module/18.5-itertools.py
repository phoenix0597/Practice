# стандартная библиотека Python, которая содержит распространенные шаблоны итераторов
# (бесконечные счетчики, перебор различных комбинаций, итераторы среза и многое другое)
import itertools

colors = ['красный', 'синий', 'зеленый', 'желтый']

# получение всех возможных комбинаций этих 4-х цветов, без повторений, где порядок цветов будет важен
for color_combo in itertools.permutations(colors, 2):
    print(color_combo)

print('=' * 20)

# получение всех возможных комбинаций этих 4-х цветов, без повторений, где порядок цветов НЕ важен
for color_combo in itertools.combinations(colors, 2):
    print(color_combo)

print('=' * 20)
# с помощью метода cycle() можно создать бесконечный (кольцевой) итератор,
# итератор будет повторять элементы итерируемого объекта, но при этом будет возвращать итератор

my_cycle = itertools.cycle(['раз', 'два', 'три'])
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))

print('=' * 20)

# Таким образом, модуль itertools позволяет легко создавать бесконечные и конечные итераторы,
# а также комбинаторные генераторы.
# Инструменты itertools очень быстры и эффективные по памяти, а также часто используются в связке
# с другими инструментами и библиотеками

# Помимо вышеперечисленного в Python есть множество других бибиотек для работы с данными:
# - pandas
# - numpy
# - collections
# - itertools
# - datetime
# - decimal
# - matplotlib...
