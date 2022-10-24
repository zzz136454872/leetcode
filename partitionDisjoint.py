from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        rmax = [0] * len(nums)
        tmp = 1234567

        for i in range(len(nums) - 1, 0, -1):
            tmp = min(tmp, nums[i])
            rmax[i - 1] = tmp

        tmp = -1

        for i in range(len(nums)):
            tmp = max(nums[i], tmp)

            if rmax[i] >= tmp:
                return i + 1

        return -1


nums = [5, 0, 3, 8, 6]
nums = [1, 1, 1, 0, 6, 12]
print(Solution().partitionDisjoint(nums))
