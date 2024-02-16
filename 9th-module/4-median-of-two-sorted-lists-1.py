# Для нахождения медианы двух отсортированных массивов nums1 и nums2,
# мы можем воспользоваться бинарным поиском. Основная идея заключается в том,
# чтобы разделить оба массива таким образом, чтобы элементы слева от разделительного элемента
# были меньше или равны элементам справа от разделителя.
#
# Этот код реализует бинарный поиск для нахождения разделителя, который делит оба массива так,
# чтобы условие медианы было выполнено. Когда мы находим правильный разделитель,
# мы вычисляем медиану на основе элементов по обе стороны от разделителя.

def find_median_sorted_arrays(nums1, nums2):
    # """
    # :type nums1: List[int]
    # :type nums2: List[int]
    # :rtype: float
    # """
    # # Обеспечиваем, чтобы nums1 был меньшим массивом
    # if len(nums1) > len(nums2):
    #     nums1, nums2 = nums2, nums1
    #
    # x, y = len(nums1), len(nums2)
    # low, high = 0, x
    #
    # while low <= high:
    #     partition_x = (low + high) // 2
    #     partition_y = (x + y + 1) // 2 - partition_x
    #
    #     max_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
    #     min_x = float('inf') if partition_x == x else nums1[partition_x]
    #
    #     max_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
    #     min_y = float('inf') if partition_y == y else nums2[partition_y]
    #
    #     if max_x <= min_y and max_y <= min_x:
    #         if (x + y) % 2 == 0:
    #             return (max(max_x, max_y) + min(min_x, min_y)) / 2.0
    #         else:
    #             return max(max_x, max_y)
    #     elif max_x > min_y:
    #         high = partition_x - 1
    #     else:
    #         low = partition_x + 1
    
    total = sorted(nums1 + nums2)
    if len(total) % 2 == 0:
        return (total[len(total) // 2 - 1] + total[len(total) // 2]) / 2.0
    else:
        return total[len(total) // 2]


# Примеры использования
print(find_median_sorted_arrays([1, 3], [2]))  # Ожидаемый вывод: 2.0
print(find_median_sorted_arrays([1, 2], [3, 4]))  # Ожидаемый вывод: 2.5

# print(find_median_sorted_arrays([1, 3, 15], [2, 7, 11]))  # Ожидаемый вывод: 5.0
# print(find_median_sorted_arrays([1, 2], [3, 4]))  # Ожидаемый вывод: 2.5
