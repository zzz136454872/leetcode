from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)

        while l <= r:
            m = (l + r) // 2
            tmp = 0

            for num in nums:
                tmp += (num - 1) // m

            if tmp <= maxOperations:
                r = m - 1
            else:
                l = m + 1

        return l


nums = [9]
maxOperations = 2
nums = [2, 4, 8, 2]
maxOperations = 4
nums = [7, 17]
maxOperations = 2
print(Solution().minimumSize(nums, maxOperations))
