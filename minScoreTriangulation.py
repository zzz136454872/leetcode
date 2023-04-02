from functools import cache
from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def find(a, b):
            if b - a == 1:
                return 0

            if b - a == 2:
                return values[a] * values[a + 1] * values[a + 2]
            res = 123456789
            tmp = values[a] * values[b]

            for i in range(a + 1, b):
                res = min(tmp * values[i] + find(a, i) + find(i, b), res)

            return res

        return find(0, len(values) - 1)


values = [1, 2, 3]
values = [3, 7, 4, 5]
values = [1, 3, 1, 4, 1, 5]
print(Solution().minScoreTriangulation(values))
