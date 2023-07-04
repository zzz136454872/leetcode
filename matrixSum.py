from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        nums = [sorted(arr) for arr in nums]

        return sum([
            max([nums[i][j] for i in range(len(nums))])
            for j in range(len(nums[0]))
        ])


nums = [[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]
nums = [[1]]
print(Solution().matrixSum(nums))
