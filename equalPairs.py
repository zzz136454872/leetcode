from collections import Counter
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = Counter([tuple(g) for g in grid])
        cols = Counter(
            [tuple([grid[i][j] for i in range(n)]) for j in range(n)])
        res = 0

        for c, v in cols.items():
            res += v * rows.get(c, 0)

        return res


grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
print(Solution().equalPairs(grid))
