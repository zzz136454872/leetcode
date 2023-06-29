from collections import Counter
from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        c = list(Counter(nums).values())
        l = len(c)
        res = 0

        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                for k in range(j + 1, l):
                    res += c[i] * c[j] * c[k]

        return res


nums = [4, 4, 2, 4, 3]
nums = [1, 1, 1, 1, 1]
print(Solution().unequalTriplets(nums))
