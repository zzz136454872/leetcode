from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        m1 = nums[:4]
        m2 = nums[-4:]

        return min(m2[0] - m1[0], m2[1] - m1[1], m2[2] - m1[2], m2[3] - m1[3])


nums = [5, 3, 2, 4]
nums = [1, 5, 0, 10, 14]
nums = [6, 6, 0, 1, 1, 4, 6]
nums = [1, 5, 6, 14, 15]
print(Solution().minDifference(nums))
