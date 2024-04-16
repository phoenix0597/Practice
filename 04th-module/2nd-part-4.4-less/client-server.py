nums = [x for x in range(1, 101) if x % 10 == 0]
# nums_copy = nums.copy()
nums_copy = nums[:] # с помощью среза мы можем брать нужный нам кусочек списка 
# (в данном случае - все элементы списка nums)
nums_copy[3] = 0

print(nums)
print("С помощью среза мы можем выбрать все элементы списка с 2 по 7 (включительно)")
print(nums[2:8])
# print(nums_copy[2:8])

print("С помощью среза мы можем заменять определенные элементы (с 0 по 2-й включительно)")
nums[:3] = [0, 0, 0]
print(nums)

print("С помощью среза мы можем заменить несколько элементов списка на 1 элемент, тем самым уменьшив список")
nums[:3] = [0]
print(nums)