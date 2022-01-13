from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m1 = 0
        l1 = -1
        m2 = 0

        for i in range(len(nums)):
            if nums[i] > m1:
                m1, m2 = nums[i], m1
                l1 = i
            elif nums[i] > m2:
                m2 = nums[i]

        if m1 >= 2 * m2:
            return l1

        return -1


nums = [3, 6, 1, 0]
nums = [1, 2, 3, 4]
nums = [1]
print(Solution().dominantIndex(nums))
