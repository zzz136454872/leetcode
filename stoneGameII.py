from functools import cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @cache
        def dp(m, p):
            s = 0

            for i in range(p, n):
                s += piles[i]

            if 2 * m >= n - p:
                return s

            res = 0

            for i in range(1, 2 * m + 1):
                res = max(res, s - dp(max(m, i), p + i))

            return res

        return dp(1, 0)


piles = [2, 7, 9, 4, 4]
piles = [1, 2, 3, 4, 5, 100]
print(Solution().stoneGameII(piles))
