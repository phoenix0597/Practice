# Задача 3. Неправильный код
# Дан код, в котором должно происходить следующее: изначально есть кортеж из пяти чисел.
# Затем вызывается функция, которая получает на вход кортеж чисел, генерирует случайный индекс и случайное значение,
# а затем по этим индексу и значению меняет сам кортеж. Функция должна возвращать кортеж и случайное значение.
#
# В основном коде функция используется два раза, и на экран два раза выводится новый кортеж и случайное значение.
# Причём второй раз выводится сумма первого случайного значения и второго.
#
# Однако код, который вам дали, оказался нерабочим. Исправьте его в соответствии с описанием.
#
# import random
#
# def change(nums):
#     index = random.randint(0, 5)
#     value = random.randint(100, 1000)
#     nums[index] = value
#     return nums, value
#
# my_nums = 1, 2, 3, 4, 5
# new_nums, rand_val = change(my_nums)
# print(new_nums, rand_val)
# new_nums = change(new_nums)
# rand_val += change(new_nums)
# print(new_nums, rand_val)

import random


def change(nums):
	nums_list = list(nums)
	index = random.randint(0, 4)
	value = random.randint(100, 1000)
	nums_list[index] = value
	nums_1 = tuple(nums_list)
	return nums_1, value


my_nums = 1, 2, 3, 4, 5
print("\nИсходный кортеж:", my_nums)
new_nums_1, rand_val_1 = change(my_nums)
print("Новый кортеж:", new_nums_1)

new_nums_2, rand_val_2 = change(my_nums)
rand_val_3 = rand_val_2 + rand_val_1
print("\nВторой новый кортеж:", new_nums_2)
print(f"Сумма 1-го и 2-го случайных значения ({rand_val_2} + {rand_val_1}):", rand_val_3)
