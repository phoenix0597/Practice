# Факториал числа.
# 5! = 1*2*3*4*5
# 5! = 5*4*3*2*1
# 5! = 5*4!
# Общая формула: n! = n*(n-1)!
# 4! = 4*3!
# 3! = 3*2!
# 2! = 2*1!
# 1! = 1
# найти факториал числа без использования циклов - с помощью рекурсии функции
def factorial(num):
	if num == 1:
		return 1
	else:
		return num * factorial(num - 1)


number = int(input('Enter number: '))
print(factorial(number).__format__(',.0f').replace(',', ' '))   # integer with ',' divisor of 3 digits

