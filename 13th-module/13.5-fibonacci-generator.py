def fibonacci(number):
    cur_val, next_val = 0, 1
    for _ in range(number):
        yield cur_val  # yield - выдать значение, произвести
        # (похож на return, с той разницей, что он как бы "замораживает" выполнение функции, а не завершает ее работу)
        cur_val, next_val = next_val, cur_val + next_val
        # мы можем прямо в генераторе выполнять проверку достижения генератором заданного числа
        if cur_val > 10 ** 6:
            return  # return - в данном случае аналогичен операции raise StopIteration


def square(nums):
    for i_nuber in nums:
        yield i_number ** 2


fib_seq = fibonacci(number=1000000000000000)
for i_number in fib_seq:
    print(i_number, end=" ")
print('\n')

# здесь мы как бы посчитали генератор от генератора
print(sum(square(fibonacci(5000))))

print()
# генераторные выражения (как list comprehension, только в круглых скобках) - более простой способ создания генераторов
# с помощью синтаксического сахара
cubes_gen = (num ** 3 for num in range(10))
for i_num in cubes_gen:
    print(i_num, end=" ")


