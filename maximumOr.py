from typing import List


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        m = 2**k
        res = 0
        n = len(nums)
        suf = [0] * n

        for i in range(len(nums) - 1, 0, -1):
            suf[i - 1] = suf[i] | nums[i]
        pre = 0

        for i in range(len(nums)):
            res = max(res, pre | nums[i] * m | suf[i])
            pre |= nums[i]

        return res


nums = [12, 9]
k = 1
nums = [8, 1, 2]
k = 2
print(Solution().maximumOr(nums, k))
