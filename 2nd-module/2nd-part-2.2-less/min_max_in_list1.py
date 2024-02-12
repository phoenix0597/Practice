# find max and min in list
nums_list = []

N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)

max_val = min_val = nums_list[0]

for i in range(N):

    if max_val < nums_list[i]:
        max_val = nums_list[i]

    if min_val > nums_list[i]:
        min_val = nums_list[i]

print('Максимальное число в списке:', max_val)

print('Минимальное число в списке:', min_val)
