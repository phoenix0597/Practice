class Solution(object):
    
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the complement values and their indices
        complements = {}

        # Iterate through the array
        for i, num in enumerate(nums):
            # Check if the complement value for the current number is in the dictionary
            if target - num in complements:
                # Return the indices of the two numbers
                return [complements[target - num], i]
            # Add the current number and its index to the dictionary
            complements[num] = i

        # If no solution is found, return an empty list
        return []


# Example usage:
sol = Solution()
print(sol.two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(sol.two_sum([3, 2, 4], 6))       # Output: [1, 2]
print(sol.two_sum([3, 3], 6))          # Output: [0, 1]
