from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a, b = 0, 0

        for num in nums:
            a, b = max(b + num, a), max(b, a - num)

        return a


nums = [4, 2, 5, 3]
nums = [5, 6, 7, 8]
nums = [6, 2, 1, 2, 4, 5]
print(Solution().maxAlternatingSum(nums))
