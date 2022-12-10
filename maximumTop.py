from typing import List


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            if k % 2 == 0:
                return nums[0]

            return -1

        if k <= 1:
            return nums[k]
        res = max(nums[:k - 1])

        if len(nums) > k:
            res = max(res, nums[k])

        return res


nums = [5, 2, 2, 4, 0, 6]
k = 4
nums = [2]
k = 1

nums = [18]
k = 3
nums = [99, 95, 68, 24, 18]
k = 69
print(Solution().maximumTop(nums, k))
