# even_nums_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0 else x ** 3]
#
# print("Список квадратов четных чисел:", even_nums_squares, "\n")

nums_squares_and_cubes = [(x ** 2 if x % 2 != 0 else x ** 3) for x in range(10)]
print("Список квадратов нечетных чисел и кубов четных:", nums_squares_and_cubes)
