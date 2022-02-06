from collections import defaultdict
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        mem = defaultdict(int)

        for num in nums:
            mem[num] += 1
        out = 0

        for k in mem.keys():
            if mem[k] == 1:
                out += k

        return out


nums = [1, 2, 3, 2]
nums = [1, 1, 1, 1, 1]
nums = [1, 2, 3, 4, 5]
print(Solution().sumOfUnique(nums))
