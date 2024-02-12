# Задача 2. Степень числа
# На одном из форумов, посвящённых программированию, пользователь выложил такой код для расчёта степени числа
# без использования циклов, ** и функции math.pow():
#
# def power(a, n):
#     return a * power(a, n)
#
# float_num = float(input('Введите вещественное число: '))
# int_num = int(input('Введите степень числа: '))
# print(float_num, '**', int_num, '=', power(float_num, int_num))
#
# Другие пользователи отметили, что это решение нерабочее и в нём есть ошибки.
# Исправьте это решение, не используя циклы, возведение в степень через ** и функцию math.pow()

# a ** n = a * a * a * ... * a
# a ** 1 = a
# a ** 0 = 1

def power(a, n):
    if n == 1:
        return a
    else:
        return a * power(a, n - 1)


float_num = float(input('Введите вещественное число: '))
int_num = int(input('Введите степень числа: '))
print(float_num, '**', int_num, '=', power(float_num, int_num))