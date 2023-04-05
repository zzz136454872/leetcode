from functools import cache
from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        @cache
        def find(b, e, p):
            if p == 1:
                if b == e:
                    return 0

                return find(b, e, k) + sum(stones[b:e + 1])

            return min(
                find(b, m, 1) + find(m + 1, e, p - 1)
                for m in range(b, e, k - 1))

        if (len(stones) - 1) % (k - 1) != 0:
            return -1

        return find(0, len(stones) - 1, 1)


stones = [3, 2, 4, 1]
K = 2
stones = [3, 2, 4, 1]
K = 3
stones = [3, 5, 1, 2, 6]
K = 3

stones = [
    16, 43, 87, 30, 4, 98, 12, 30, 47, 45, 32, 4, 64, 14, 24, 84, 86, 51, 11,
    22, 4
]
K = 2
print(Solution().mergeStones(stones, K))
