class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxX = max(float('-inf'), nums1[partitionX - 1] if partitionX > 0 else float('-inf'))
            minX = min(float('inf'), nums1[partitionX] if partitionX < x else float('inf'))

            maxY = max(float('-inf'), nums2[partitionY - 1] if partitionY > 0 else float('-inf'))
            minY = min(float('inf'), nums2[partitionY] if partitionY < y else float('inf'))

            if maxX <= minY and maxY <= minX:
                if (x + y) % 2 == 0:
                    return (maxX + minY) / 2.0
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                high = partitionX - 1
            else:
                low = partitionX + 1

# Примеры использования
solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2]))  # Ожидаемый вывод: 2.0
print(solution.findMedianSortedArrays([1, 2], [3, 4]))  # Ожидаемый вывод: 2.5
