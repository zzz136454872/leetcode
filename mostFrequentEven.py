from collections import defaultdict
from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        mem = defaultdict(int)

        for num in nums:
            if num % 2 != 0:
                continue
            mem[num] += 1

        if len(mem) == 0:
            return -1
        r = max(mem.values())
        ks = sorted(list(mem.keys()))

        for k in ks:
            if mem[k] == r:
                return k

        return -1


nums = [0, 1, 2, 2, 4, 4, 1]
nums = [4, 4, 4, 9, 2, 4]
print(Solution().mostFrequentEven(nums))
