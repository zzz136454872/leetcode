from collections import defaultdict
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mem = defaultdict(int)
        res = 0

        for num in nums:
            d = num - int(str(num)[::-1])
            res += mem[d]
            mem[d] += 1

        return res % (10**9 + 7)


nums = [42, 11, 1, 97]
nums = [13, 10, 35, 24, 76]
print(Solution().countNicePairs(nums))
