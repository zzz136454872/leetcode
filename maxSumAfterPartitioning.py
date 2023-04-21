from functools import cache
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache
        def dp(loc):
            if loc > len(arr):
                return -12345678999
            m = 0
            res = 0

            for i in range(k):
                if i + loc >= len(arr):
                    break
                m = max(arr[i + loc], m)
                res = max(res, (i + 1) * m + dp(loc + i + 1))

            return res

        return dp(0)


arr = [1, 15, 7, 9, 2, 5, 10]
# arr = [1,15,7,9]
k = 3

print(Solution().maxSumAfterPartitioning(arr, k))
