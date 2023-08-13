from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s1 = 0
        s2 = 0
        res = 0

        for num in nums:
            s1 += num

            if s1 < 0:
                s1 = 0
            else:
                res = max(s1, res)
            s2 += num

            if s2 > 0:
                s2 = 0
            else:
                res = max(res, -s2)

        return res


nums = [1, -3, 2, 3, -4]
nums = [2, -5, 1, -4, 3, -2]
print(Solution().maxAbsoluteSum(nums))
