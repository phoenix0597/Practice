# Задача 1. Свой for (ну почти)
# Дан любой итерируемый объект, например список из N чисел.
# Реализуйте функцию, которая эмулирует работу цикла for с помощью цикла while и проходит
# по всем элементам итерируемого объекта. Не забудьте про исключение «конца итерации».

def for_circle(iterable):
    iterator = iterable.__iter__()
    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            break


my_list = [1, 2, 3, 4, 5]
for_circle(my_list)
