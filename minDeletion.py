from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        d = 0
        prev = -1

        for i in range(len(nums)):
            if (i - d) % 2 == 1 and nums[i] == prev:
                d += 1
            else:
                prev = nums[i]

        if (len(nums) - d) % 2 == 1:
            d += 1

        return d


nums = [1, 1, 2, 3, 5]
nums = [1, 1, 2, 2, 3, 3]
print(Solution().minDeletion(nums))
