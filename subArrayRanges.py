from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        out = 0

        for i in range(len(nums) - 1):
            m1 = nums[i]
            m2 = nums[i]

            for j in range(i + 1, len(nums)):
                m1 = max(m1, nums[j])
                m2 = min(m2, nums[j])
                out += m1 - m2

        return out


nums = [1, 2, 3]
nums = [1, 3, 3]
print(Solution().subArrayRanges(nums))
