from collections import defaultdict
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        mem = defaultdict(int)

        for num in nums:
            if num > 0:
                mem[num] |= 1
            else:
                mem[-num] |= 2
        a = sorted([k for k in mem if mem[k] == 3])

        if len(a) == 0:
            return -1

        return a[-1]


nums = [-1, 2, -3, 3]
nums = [-1, 10, 6, 7, -7, 1]
nums = [-10, 8, 6, 7, -2, -3]
print(Solution().findMaxK(nums))
