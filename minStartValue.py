from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s = 0
        m = 0

        for num in nums:
            s += num
            m = min(m, s)

        return max(1, -m + 1)


nums = [-3, 2, -3, 4, 2]
nums = [1, 2]
nums = [1, -2, -3]
print(Solution().minStartValue(nums))
