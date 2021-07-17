from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        out = nums[0]

        for num in nums:
            s += num
            out = max(out, s)

            if s < 0:
                s = 0

        return out


sl = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(sl.maxSubArray(nums))
