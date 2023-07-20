from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        m = max(nums)

        if m <= 0:
            return m
        s = 0
        res1 = 0
        t = 0
        res2 = 0

        for i in range(len(nums)):
            s += nums[i]
            t += nums[i]

            if s < 0:
                s = 0
            res1 = max(res1, s)

            if t > 0:
                t = 0
            res2 = min(res2, t)

        return max(res1, sum(nums) - res2)


nums = [1, -2, 3, -2]
nums = [5, -3, 5]
nums = [3, -2, 2, -3]
nums = [-3, -2, -3]
print(Solution().maxSubarraySumCircular(nums))
