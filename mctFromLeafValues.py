from functools import cache
from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        BIG = 1234567890

        @cache
        def dp(l, r):
            if l >= r:
                return BIG

            if r == l + 1:
                return 0
            res = BIG

            for i in range(l + 1, r):
                res = min(res,
                          max(arr[l:i]) * max(arr[i:r]) + dp(l, i) + dp(i, r))

            return res

        return dp(0, len(arr))


arr = [6, 2, 4]
arr = [4, 11]
print(Solution().mctFromLeafValues(arr))
